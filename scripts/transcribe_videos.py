#!/usr/bin/env python3
"""
Batch-transcribe a folder of videos with the Gemini API.

What it does
------------
For every video in --input-dir it will:
  1. Upload the file to Gemini (File API; handles files up to 2 GB).
  2. Wait for Gemini to finish processing the video.
  3. Ask the model for a timestamped, speaker-labeled transcript.
  4. Save the transcript as a .md file next to the video (in --output-dir).
  5. Skip any video whose transcript already exists, so re-runs are safe.

Setup (one time)
----------------
  1. Get a free Gemini API key: https://aistudio.google.com/apikey
  2. Install the SDK:           pip install google-genai
  3. Set your key:
        Windows (PowerShell):  $env:GEMINI_API_KEY="your_key_here"
        Windows (cmd):         set GEMINI_API_KEY=your_key_here
        macOS/Linux:           export GEMINI_API_KEY="your_key_here"

Usage
-----
  python transcribe_videos.py --input-dir "C:\\path\\to\\videos"
  python transcribe_videos.py --input-dir ./videos --output-dir ./transcripts --model gemini-2.5-pro

Notes
-----
  * gemini-2.5-flash is fast + cheap and great for transcription (default).
    Use gemini-2.5-pro for tougher audio (heavy background noise, crosstalk).
  * Gemini transcribes English best. Very noisy phone clips may be imperfect.
  * Uploaded files are auto-deleted from Gemini after each video by default
    (--keep-uploads to leave them).
"""

import argparse
import os
import sys
import time
from pathlib import Path

VIDEO_EXTS = {".mp4", ".mov", ".m4v", ".avi", ".mkv", ".webm", ".mpeg", ".mpg", ".3gp"}

PROMPT = (
    "Transcribe the spoken audio in this video verbatim. "
    "Insert a timestamp in [mm:ss] format roughly every 15 seconds and at every "
    "speaker change. If there is more than one speaker, label them (Speaker 1, "
    "Speaker 2, etc.). Do not summarize, add commentary, or describe visuals — "
    "output the transcript text only. If there is no discernible speech, output "
    "exactly: [No speech detected]."
)


def log(msg: str) -> None:
    print(msg, flush=True)


def wait_until_active(client, file_obj, timeout_s: int = 900, poll_s: int = 5):
    """Poll an uploaded file until it's ACTIVE (ready) or raise on failure/timeout."""
    name = file_obj.name
    waited = 0
    while file_obj.state.name == "PROCESSING":
        if waited >= timeout_s:
            raise TimeoutError(f"Processing timed out after {timeout_s}s")
        time.sleep(poll_s)
        waited += poll_s
        file_obj = client.files.get(name=name)
    if file_obj.state.name != "ACTIVE":
        raise RuntimeError(f"File ended in state {file_obj.state.name}")
    return file_obj


def transcribe_one(client, model: str, video_path: Path, keep_uploads: bool) -> str:
    log(f"  uploading ({video_path.stat().st_size / 1e6:.1f} MB)...")
    uploaded = client.files.upload(file=str(video_path))
    try:
        log("  waiting for Gemini to process the video...")
        uploaded = wait_until_active(client, uploaded)
        log("  transcribing...")
        resp = client.models.generate_content(
            model=model,
            contents=[uploaded, PROMPT],
        )
        return resp.text or "[No transcript returned]"
    finally:
        if not keep_uploads:
            try:
                client.files.delete(name=uploaded.name)
            except Exception:
                pass


def main() -> int:
    ap = argparse.ArgumentParser(description="Batch-transcribe videos with Gemini.")
    ap.add_argument("--input-dir", required=True, help="Folder containing the videos.")
    ap.add_argument("--output-dir", default=None,
                    help="Where to write transcripts (default: same as input dir).")
    ap.add_argument("--model", default="gemini-2.5-flash",
                    help="Gemini model (default: gemini-2.5-flash).")
    ap.add_argument("--keep-uploads", action="store_true",
                    help="Don't delete uploaded files from Gemini after transcribing.")
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        log("ERROR: set GEMINI_API_KEY (see setup notes at top of this file).")
        return 1

    try:
        from google import genai
    except ImportError:
        log("ERROR: SDK not installed. Run:  pip install google-genai")
        return 1

    in_dir = Path(args.input_dir).expanduser()
    if not in_dir.is_dir():
        log(f"ERROR: input dir not found: {in_dir}")
        return 1
    out_dir = Path(args.output_dir).expanduser() if args.output_dir else in_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    videos = sorted(p for p in in_dir.iterdir()
                    if p.is_file() and p.suffix.lower() in VIDEO_EXTS)
    if not videos:
        log(f"No videos found in {in_dir}")
        return 0

    client = genai.Client(api_key=api_key)
    log(f"Found {len(videos)} video(s). Model: {args.model}\n")

    done = skipped = failed = 0
    for i, video in enumerate(videos, 1):
        out_file = out_dir / f"{video.stem}.md"
        log(f"[{i}/{len(videos)}] {video.name}")
        if out_file.exists():
            log("  already transcribed — skipping.")
            skipped += 1
            continue
        try:
            transcript = transcribe_one(client, args.model, video, args.keep_uploads)
            header = f"# Transcript: {video.name}\n\n"
            out_file.write_text(header + transcript.strip() + "\n", encoding="utf-8")
            log(f"  saved -> {out_file.name}")
            done += 1
        except Exception as e:
            log(f"  FAILED: {e}")
            failed += 1

    log(f"\nDone. {done} transcribed, {skipped} skipped, {failed} failed.")
    log(f"Transcripts in: {out_dir}")
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
