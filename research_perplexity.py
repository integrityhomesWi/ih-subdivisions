#!/usr/bin/env python3
"""
Subdivision research — Perplexity Sonar leg.

Runs the Kenzie SOP v2 deep-research prompt against Perplexity's Sonar API
for one subdivision and writes the raw output to disk.

This is one of three research legs. Claude Code's native web search handles
the Claude leg; OpenAI handles the ChatGPT leg once that key is set up.
Outputs are kept separate so a questionable claim can be traced to its source.

Usage:
    python research_perplexity.py "Ardent Glen" "Verona"
    python research_perplexity.py "Ardent Glen" "Verona" --model sonar-deep-research
    python research_perplexity.py --batch waunakee_batch.txt

Requires:
    PERPLEXITY_API_KEY environment variable
    pip install requests
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import date
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Missing dependency. Run: pip install requests")

API_URL = "https://api.perplexity.ai/chat/completions"
OUTPUT_DIR = Path("research")

# sonar-pro is the default: multi-source synthesis at reasonable cost.
# sonar is cheaper but thinner. sonar-deep-research is far more thorough
# and far more expensive — reserve it for high-priority subdivisions.
DEFAULT_MODEL = "sonar-pro"


PROMPT_TEMPLATE = """You are helping Wisconsin real estate agent John Reuter build the most complete and useful online neighborhood guide for:

SUBDIVISION: {subdivision}
CITY: {city}, Wisconsin

The goal is to establish John as the genuine neighborhood expert. This is not a generic subdivision description, sales pitch, or rewritten builder page. Research the neighborhood deeply enough to answer the questions that current residents, prospective buyers, sellers, and relocating families would actually ask.

RESEARCH REQUIREMENTS

Research before writing. Use multiple sources, prioritizing:
1. Municipal plats, planning documents, meeting packets and park plans
2. Recorded covenants, HOA documents and management information
3. Official school-district attendance maps
4. Builder and developer documents
5. Municipal park, trail and development maps
6. Current maps and local business information
7. Reputable local reporting and neighborhood sources

Do not rely primarily on the developer's marketing language.

Do NOT use Redfin, Zillow, Trulia, or similar consumer real-estate sites as a source for sold-price data, median/average sale price, or days-on-market figures. Those numbers come from John's own MLS (SCWMLS) export, which is supplied separately. Leave those fields marked "pending MLS data from John" rather than substituting a public-site estimate. Public real estate sites may be used only for non-market facts (e.g., confirming a builder name, a floor plan name, or an HOA management contact).

VERIFY, DO NOT GUESS

For every important fact:
* Confirm it through a reliable source whenever possible.
* Distinguish verified facts from reasonable conclusions.
* Say "not confident" when information cannot be reliably confirmed.
* Identify conflicting information instead of choosing one version silently.
* Do not present proposed amenities as completed amenities.
* Do not apply an HOA fee from one housing section to the entire neighborhood.
* Do not guarantee school assignments without checking the official attendance boundary.
* Date all prices, fees, development plans and other information that may change.
* Do not claim to live in the neighborhood or invent personal experiences.

DEPTH REQUIRED

Research and report on all of the following:

1. DEVELOPMENT HISTORY - original developer/builders; when planning/infrastructure/construction began; development phases and additions with dates; which phases are complete/active/approved/proposed; expected future expansion; original land use if documented.

2. EXACT LOCATION AND BOUNDARIES - what part of the city/village; exact roads, cross streets, physical boundaries; every confirmed street within the subdivision; major entrances/connections; whether phases have different access points; relationship to downtown and neighboring subdivisions; note uncertain boundaries due to active expansion.

3. SCHOOL ASSIGNMENTS - school district; assigned elementary/intermediate/middle/high schools; verify using addresses from different sections; note any attendance boundary crossings; grades served and approximate distance; advise address-level verification.

4. HOUSING PRODUCT TYPES (no sold-price stats) - break into single-family, cottage-style, twin/duplex/townhome/condo, apartments/senior housing, custom vs. production. For each: architectural styles, typical year built, typical sq ft, bed/bath ranges, lot-size range, garage configs, common builder floor plans, current new-construction starting prices (builder-quoted, dated). Do NOT report median/average sold price or days-on-market - mark those "pending MLS data from John" for every housing type. Do not substitute builder starting prices for actual sold data.

5. HOA, COVENANTS AND COSTS - HOA's full legal name; management company/contact; which properties fall under which association; current dues (dated by year); what dues include; separate fees for twin homes/condos if applicable; architectural-control requirements; restrictions on fences, sheds, rentals, parking, landscaping, pets, exterior changes; known special assessments or developer-controlled period. Show separately by housing type if fees/rules differ.

6. AMENITIES AND OPEN SPACE - divide into completed/available now, under construction, approved but not completed, proposed/uncertain. Cover parks, playgrounds, trails/sidewalks, conservancy/natural areas, ponds/stormwater, athletic facilities, dog parks, pools, clubhouses, gathering spaces, municipal trail connections, nearby public parks. Note ownership/maintenance of major amenities when known.

7. NEARBY CONVENIENCES - realistic driving/walking times to grocery, coffee, restaurants, gas, pharmacy/healthcare, library, schools, parks, downtown, major highways, Madison employment centers, Dane County Regional Airport. Name specific businesses - never "shopping and dining are nearby."

8. RESIDENT-LEVEL KNOWLEDGE - walking routes/trail connections, traffic patterns and primary exits, ongoing construction, snow-removal/private-maintenance arrangements, community events, noise/traffic considerations, access to schools/parks, postal address vs. municipal jurisdiction, trash/recycling/municipal services, questions residents commonly ask, details useful when selling in the subdivision.

9. BENEFITS AND POSSIBLE DRAWBACKS - what residents are likely to value, with specific evidence, not promotional adjectives. Also legitimate considerations: active construction, smaller lots, HOA restrictions, limited private amenities, traffic, distance from services, future development uncertainty, differing fee structures. Keep factual and fair - credibility, not "everything is perfect."

10. COMPARISON WITH NEARBY SUBDIVISIONS - compare against 3-5 most relevant nearby subdivisions on location, home age, price range (builder-quoted only, dated), lot sizes, housing variety, HOA structure, parks/pools/trails, downtown proximity, schools, buyer fit. Identify 2-3 genuinely distinctive qualities - avoid vague claims like "strong sense of community" unless supported.

REQUIRED OUTPUT - organize into these sections:
A. Expert Summary
B. Verified Quick-Facts Table
C. Development and Phase History
D. Location, Streets and Boundaries
E. Schools
F. Homes and Housing Products (builder prices only - sold data marked "pending MLS data from John")
G. HOA and Restrictions
H. Parks, Trails and Amenities
I. Nearby Conveniences with Distances
J. What Residents Value
K. Possible Considerations
L. Comparison With Nearby Subdivisions
M. Frequently Asked Questions
N. "Only a Local Would Know" Content Ideas (at least 10 specific questions/observations to investigate in person, use in videos, or ask residents about)
O. Missing Information John Should Verify (every MLS/sold-data field left pending)
P. Sources with direct links

QUALITY CHECK BEFORE ANSWERING - confirm that:
* The answer couldn't simply have the subdivision name swapped for another neighborhood's.
* It contains specific streets, dates, schools, housing data, fees, destinations.
* Completed vs. proposed amenities are separated.
* Different housing products/fee structures are separated.
* No sold-price/median-price/days-on-market figures came from Redfin/Zillow/Trulia - marked pending MLS data instead.
* Claims are supported by direct sources.
* Unknown information is labeled "not confident."
* The result helps John answer follow-up questions rather than merely advertise the neighborhood.

If public information is insufficient, don't pad with generic language - give verified findings plus a precise list of records/people/field observations needed to finish the file."""


def slugify(name: str) -> str:
    """Lowercase, hyphenated, no punctuation — matches the URL slug convention."""
    slug = name.lower().strip()
    slug = re.sub(r"['’]", "", slug)       # drop apostrophes entirely
    slug = re.sub(r"[^a-z0-9]+", "-", slug)      # everything else becomes a hyphen
    return slug.strip("-")


def research(subdivision: str, city: str, model: str, api_key: str,
             timeout: int = 300) -> dict:
    """Send the research prompt to Perplexity. Returns the parsed response."""
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a meticulous local-research analyst. You verify claims "
                    "against primary sources, you clearly label anything you cannot "
                    "confirm, and you never fabricate specifics to fill a gap."
                ),
            },
            {"role": "user", "content": PROMPT_TEMPLATE.format(
                subdivision=subdivision, city=city)},
        ],
        "temperature": 0.2,
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
        raise RuntimeError("401 Unauthorized — check PERPLEXITY_API_KEY is valid.")
    if response.status_code == 402:
        raise RuntimeError("402 Payment Required — Perplexity credit balance is empty.")
    if response.status_code == 429:
        raise RuntimeError("429 Rate limited — wait and retry.")
    response.raise_for_status()

    return response.json()


def write_output(subdivision: str, city: str, model: str, data: dict) -> Path:
    """Write the raw research to research/<slug>-raw-perplexity.md."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / f"{slugify(subdivision)}-raw-perplexity.md"

    content = data["choices"][0]["message"]["content"]
    citations = data.get("citations", [])
    usage = data.get("usage", {})

    lines = [
        f"# {subdivision} — {city}, WI",
        "",
        "**Research leg:** Perplexity  ",
        f"**Model:** {model}  ",
        f"**Retrieved:** {date.today().isoformat()}  ",
        f"**Tokens:** {usage.get('total_tokens', 'n/a')}",
        "",
        "> Raw single-source output. Not a finished brief — merge with the Claude and "
        "ChatGPT legs per the union rules (keep all unique findings, flag only genuine "
        "conflicts). Sold-price and DOM figures here should read as pending; real numbers "
        "come from the SCWMLS export.",
        "",
        "---",
        "",
        content,
    ]

    if citations:
        lines += ["", "---", "", "## Citations (Perplexity)", ""]
        lines += [f"{i}. {url}" for i, url in enumerate(citations, 1)]

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def run_one(subdivision: str, city: str, model: str, api_key: str) -> bool:
    print(f"  {subdivision} ({city})... ", end="", flush=True)
    try:
        data = research(subdivision, city, model, api_key)
        path = write_output(subdivision, city, model, data)
        tokens = data.get("usage", {}).get("total_tokens", 0)
        print(f"ok — {path} ({tokens:,} tokens)")
        return True
    except Exception as exc:
        print(f"FAILED — {exc}")
        return False


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the Perplexity leg of subdivision research.")
    parser.add_argument("subdivision", nargs="?", help='e.g. "Ardent Glen"')
    parser.add_argument("city", nargs="?", help='e.g. "Verona"')
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"sonar | sonar-pro | sonar-deep-research (default: {DEFAULT_MODEL})")
    parser.add_argument("--batch", metavar="FILE",
                        help="Text file with one 'Subdivision|City' pair per line")
    args = parser.parse_args()

    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        sys.exit("PERPLEXITY_API_KEY is not set. Set it as an environment variable.")
    if api_key.startswith("pplx-your-key"):
        sys.exit("PERPLEXITY_API_KEY still holds the placeholder value.")

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

    print(f"\nPerplexity research — {len(pairs)} subdivision(s), model={args.model}\n")

    succeeded = 0
    for i, (sub, city) in enumerate(pairs):
        if run_one(sub, city, args.model, api_key):
            succeeded += 1
        if i < len(pairs) - 1:
            time.sleep(2)   # be polite to the API between calls

    failed = len(pairs) - succeeded
    print(f"\nDone. {succeeded} succeeded, {failed} failed.")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
