#!/usr/bin/env python3
"""
Subdivision research — OpenAI leg.

Mirrors research_perplexity.py's shape exactly (same CLI surface, same
auto-chained conveniences leg, same file-header conventions) but calls
OpenAI's Responses API with the built-in web_search tool instead of
Perplexity's Sonar API. Reuses the same prompt templates from
research_perplexity.py verbatim — one prompt, three interchangeable legs.

Usage:
    python research_openai.py "Ardent Glen" "Verona"
    python research_openai.py "Ardent Glen" "Verona" --model gpt-4.1
    python research_openai.py --batch waunakee_batch.txt

Each run does BOTH legs automatically: the full brief, then the narrow
conveniences leg anchored to the streets confirmed in section D. Add
--skip-conveniences to run only the full brief.

Requires:
    OPENAI_API_KEY environment variable
    pip install requests
"""

import argparse
import os
import sys
import time
from datetime import date
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Missing dependency. Run: pip install requests")

try:
    from research_perplexity import (
        PROMPT_TEMPLATE,
        CONVENIENCES_PROMPT_TEMPLATE,
        slugify,
        extract_streets_context,
    )
except ImportError:
    sys.exit(
        "Couldn't import from research_perplexity.py — make sure it's in the "
        "same folder as this script (it holds the shared prompt templates)."
    )

API_URL = "https://api.openai.com/v1/responses"
OUTPUT_DIR = Path("research")

# gpt-4.1 is the default: solid web_search grounding at reasonable cost.
# Swap via --model if your account has access to something better suited
# to long research tasks — check your OpenAI account's available models,
# this default may need updating as the model lineup changes.
DEFAULT_MODEL = "gpt-4.1"

SYSTEM_INSTRUCTIONS = (
    "You are a meticulous local-research analyst. You verify claims against "
    "primary sources, you clearly label anything you cannot confirm, and you "
    "never fabricate specifics to fill a gap. Use the web_search tool "
    "extensively — multiple distinct searches, not just one — before writing "
    "your answer."
)


def call_api(prompt: str, model: str, api_key: str, timeout: int = 300) -> dict:
    """Send a prompt to OpenAI's Responses API with web_search enabled."""
    payload = {
        "model": model,
        "instructions": SYSTEM_INSTRUCTIONS,
        "input": prompt,
        "tools": [{"type": "web_search"}],
    }

    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=timeout,
    )

    if response.status_code == 401:
        raise RuntimeError("401 Unauthorized — check OPENAI_API_KEY is valid.")
    if response.status_code == 402:
        raise RuntimeError("402 Payment Required — OpenAI billing/credit issue.")
    if response.status_code == 429:
        raise RuntimeError("429 Rate limited — wait and retry.")
    if response.status_code == 400:
        raise RuntimeError(f"400 Bad Request — check --model is valid for your "
                            f"account and supports the web_search tool. Response: "
                            f"{response.text[:500]}")
    response.raise_for_status()

    return response.json()


def extract_text_and_citations(data: dict) -> tuple:
    """Pull the assistant's final text and any URL citations out of a
    Responses API payload. Layout: data["output"] is a list of items; the
    one with type == "message" holds content items of type "output_text",
    each with a "text" field and an "annotations" list containing
    url_citation entries."""
    text_parts = []
    citations = []
    seen_urls = set()

    for item in data.get("output", []):
        if item.get("type") != "message":
            continue
        for content in item.get("content", []):
            if content.get("type") != "output_text":
                continue
            text_parts.append(content.get("text", ""))
            for ann in content.get("annotations", []):
                if ann.get("type") == "url_citation":
                    url = ann.get("url")
                    if url and url not in seen_urls:
                        seen_urls.add(url)
                        citations.append({"url": url, "title": ann.get("title", url)})

    return "\n\n".join(text_parts), citations


def research(subdivision: str, city: str, model: str, api_key: str,
             timeout: int = 300) -> dict:
    """Send the full research prompt to OpenAI. Returns the raw response."""
    prompt = PROMPT_TEMPLATE.format(subdivision=subdivision, city=city)
    return call_api(prompt, model, api_key, timeout)


def research_conveniences(subdivision: str, city: str, streets: str, model: str,
                           api_key: str, timeout: int = 300) -> dict:
    """Send the narrow, streets-anchored conveniences prompt. Returns the raw response."""
    prompt = CONVENIENCES_PROMPT_TEMPLATE.format(
        subdivision=subdivision, city=city, streets=streets)
    return call_api(prompt, model, api_key, timeout)


def write_output(subdivision: str, city: str, model: str, data: dict) -> Path:
    """Write the raw research to research/<slug>-raw-chatgpt.md."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / f"{slugify(subdivision)}-raw-chatgpt.md"

    content, citations = extract_text_and_citations(data)
    usage = data.get("usage", {})

    lines = [
        f"# {subdivision} — {city}, WI",
        "",
        "**Research leg:** OpenAI (web_search)  ",
        f"**Model:** {model}  ",
        f"**Retrieved:** {date.today().isoformat()}  ",
        f"**Tokens:** {usage.get('total_tokens', 'n/a')}",
        "",
        "> Raw single-source output. Not a finished brief — merge with the "
        "Perplexity and Claude legs per the union rules (keep all unique "
        "findings, flag only genuine conflicts). Sold-price and DOM figures "
        "here should read as pending; real numbers come from the SCWMLS export.",
        "",
        "---",
        "",
        content,
    ]

    if citations:
        lines += ["", "---", "", "## Citations (OpenAI)", ""]
        lines += [f"{i}. [{c['title']}]({c['url']})" for i, c in enumerate(citations, 1)]

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_conveniences_output(subdivision: str, city: str, streets: str,
                               model: str, data: dict) -> Path:
    """Write the raw conveniences leg to research/<slug>-conveniences-chatgpt.md."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / f"{slugify(subdivision)}-conveniences-chatgpt.md"

    content, citations = extract_text_and_citations(data)
    usage = data.get("usage", {})

    lines = [
        f"# {subdivision} — {city}, WI — Nearby Conveniences",
        "",
        "**Research leg:** OpenAI (web_search, conveniences follow-up)  ",
        f"**Model:** {model}  ",
        f"**Retrieved:** {date.today().isoformat()}  ",
        f"**Anchored streets:** {streets}  ",
        f"**Tokens:** {usage.get('total_tokens', 'n/a')}",
        "",
        "> Patches section I of the main raw-chatgpt brief for this "
        "subdivision. Merge in; don't publish standalone. Re-check "
        "name-collision discards before use.",
        "",
        "---",
        "",
        content,
    ]

    if citations:
        lines += ["", "---", "", "## Citations (OpenAI)", ""]
        lines += [f"{i}. [{c['title']}]({c['url']})" for i, c in enumerate(citations, 1)]

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def run_conveniences(subdivision: str, city: str, streets: str, model: str, api_key: str) -> bool:
    print(f"  {subdivision} ({city}) conveniences... ", end="", flush=True)
    try:
        data = research_conveniences(subdivision, city, streets, model, api_key)
        path = write_conveniences_output(subdivision, city, streets, model, data)
        tokens = data.get("usage", {}).get("total_tokens", 0)
        print(f"ok — {path} ({tokens:,} tokens)")
        return True
    except Exception as exc:
        print(f"FAILED — {exc}")
        return False


def run_one(subdivision: str, city: str, model: str, api_key: str,
            skip_conveniences: bool = False) -> bool:
    print(f"  {subdivision} ({city})... ", end="", flush=True)
    try:
        data = research(subdivision, city, model, api_key)
        path = write_output(subdivision, city, model, data)
        tokens = data.get("usage", {}).get("total_tokens", 0)
        print(f"ok — {path} ({tokens:,} tokens)")
    except Exception as exc:
        print(f"FAILED — {exc}")
        return False

    if skip_conveniences:
        return True

    content, _ = extract_text_and_citations(data)
    streets = extract_streets_context(content)
    if not streets:
        print(f"  {subdivision} ({city}) conveniences... SKIPPED — couldn't find a "
              f"section D (streets) in the brief to anchor the query. Run manually with "
              f"--conveniences --streets \"...\" once you've read the brief.")
        return True

    return run_conveniences(subdivision, city, streets, model, api_key)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the OpenAI leg of subdivision research.")
    parser.add_argument("subdivision", nargs="?", help='e.g. "Ardent Glen"')
    parser.add_argument("city", nargs="?", help='e.g. "Verona"')
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"OpenAI model with web_search tool support "
                             f"(default: {DEFAULT_MODEL})")
    parser.add_argument("--batch", metavar="FILE",
                        help="Text file with one 'Subdivision|City' pair per line")
    parser.add_argument("--conveniences", action="store_true",
                        help="Re-run ONLY the narrow, streets-anchored nearby-conveniences leg "
                             "by hand (e.g. to retry with corrected streets), skipping the full "
                             "brief. Requires --streets. Not supported with --batch. Normally "
                             "you don't need this flag — a plain run does both legs already.")
    parser.add_argument("--streets", metavar="\"Street A, Street B, ...\"",
                        help="Confirmed streets to anchor a manual --conveniences re-run.")
    parser.add_argument("--skip-conveniences", action="store_true",
                        help="Run only the full brief; don't auto-chain the conveniences leg.")
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.exit("OPENAI_API_KEY is not set. Set it as an environment variable.")

    if args.conveniences:
        if args.batch:
            parser.error("--conveniences is not supported with --batch — run it per subdivision.")
        if not (args.subdivision and args.city):
            parser.error("Provide a subdivision and city with --conveniences.")
        if not args.streets:
            parser.error("--conveniences requires --streets \"Street A, Street B, ...\" "
                          "(pull these from the confirmed streets in the main brief).")
        print(f"\nOpenAI conveniences leg — {args.subdivision} ({args.city}), "
              f"model={args.model}\n")
        ok = run_conveniences(args.subdivision, args.city, args.streets, args.model, api_key)
        sys.exit(0 if ok else 1)

    if args.batch:
        pairs = []
        for line in Path(args.batch).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "|" not in line:
                print(f"  skipping malformed line: {line}")
                continue
            sub, city = (part.strip() for part in line.split("|", 1))
            pairs.append((sub, city))
    elif args.subdivision and args.city:
        pairs = [(args.subdivision, args.city)]
    else:
        parser.error("Provide a subdivision and city, or use --batch FILE.")

    leg_note = " (brief only, --skip-conveniences)" if args.skip_conveniences else " (brief + conveniences)"
    print(f"\nOpenAI research — {len(pairs)} subdivision(s), model={args.model}{leg_note}\n")

    succeeded = 0
    for i, (sub, city) in enumerate(pairs):
        if run_one(sub, city, args.model, api_key, skip_conveniences=args.skip_conveniences):
            succeeded += 1
        if i < len(pairs) - 1:
            time.sleep(2)   # be polite to the API between calls

    failed = len(pairs) - succeeded
    print(f"\nDone. {succeeded} succeeded, {failed} failed.")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
