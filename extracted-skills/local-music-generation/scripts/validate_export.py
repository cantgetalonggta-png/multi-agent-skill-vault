#!/usr/bin/env python3
"""Validate an exported audio file for common platform requirements.
Usage: python validate_export.py file.wav [--target spotify]
"""

import argparse
import subprocess
import os
import sys

def probe(path):
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "a:0",
        "-show_entries", "stream=sample_rate,channels,bits_per_raw_sample,codec_name:format=duration",
        "-of", "json", path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        return None
    return result.stdout

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--target", default="generic", choices=["spotify", "youtube", "tiktok", "generic"])
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Missing file: {args.input}", file=sys.stderr)
        sys.exit(1)

    info = probe(args.input)
    print(f"Validating {args.input} for target={args.target}")
    if info:
        print(info)
    else:
        print("Could not probe file. Ensure ffprobe is available.")
    print("Manual check still required for measured LUFS and true peak.")

if __name__ == "__main__":
    main()