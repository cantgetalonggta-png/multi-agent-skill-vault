#!/usr/bin/env python3
"""Generate a simple text report for one or more audio files.
Usage: python generate_report.py file1.wav file2.mp3 --out report.txt
"""

import argparse
import subprocess
import os
from pathlib import Path

def probe(path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,bit_rate,size:stream=codec_name,sample_rate,channels",
        "-of", "default=noprint_wrappers=1", str(path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else "probe failed"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    parser.add_argument("--out", default="audio_report.txt")
    args = parser.parse_args()

    lines = ["Audio Analysis Report", "=" * 40, ""]
    for f in args.files:
        p = Path(f)
        lines.append(f"File: {p.name}")
        lines.append(f"Path: {p}")
        if p.exists():
            lines.append(probe(p))
        else:
            lines.append("FILE NOT FOUND")
        lines.append("-" * 40)

    report = "\n".join(lines)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(report)
    print(report)
    print(f"\nReport written to {args.out}")

if __name__ == "__main__":
    main()