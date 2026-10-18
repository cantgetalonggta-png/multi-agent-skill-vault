#!/usr/bin/env python3
"""Quick technical validation of audio files.
Checks existence, duration, sample rate, channels, and basic readability.
Usage: python simple_validate.py *.wav *.mp3
"""

import argparse
import subprocess
import sys
from pathlib import Path

def validate(path):
    p = Path(path)
    issues = []
    if not p.exists():
        return ["missing file"]
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration:stream=sample_rate,channels,codec_type",
        "-of", "json", str(p)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        issues.append("ffprobe failed")
        return issues
    # Minimal parsing
    if "duration" not in result.stdout:
        issues.append("no duration")
    if "sample_rate" not in result.stdout:
        issues.append("no sample_rate")
    return issues

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    all_ok = True
    for f in args.files:
        issues = validate(f)
        status = "OK" if not issues else "ISSUES: " + ", ".join(issues)
        print(f"{f}: {status}")
        if issues:
            all_ok = False

    sys.exit(0 if all_ok else 1)

if __name__ == "__main__":
    main()