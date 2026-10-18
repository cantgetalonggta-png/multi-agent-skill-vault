#!/usr/bin/env python3
"""Quick media inspection using ffprobe.
Usage: python inspect_media.py file.mp4
"""

import argparse
import subprocess
import sys
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size,bit_rate:stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels",
        "-of", "json", args.input
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)

if __name__ == "__main__":
    main()