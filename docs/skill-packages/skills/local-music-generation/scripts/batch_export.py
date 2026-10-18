#!/usr/bin/env python3
"""Batch export multiple audio files to a target loudness and format.
Usage: python batch_export.py --input-dir /path/to/audio --output-dir /path/to/out --lufs -14 --tp -1.0
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

def normalize_one(infile, outfile, lufs, tp):
    filter_complex = f"loudnorm=I={lufs}:TP={tp}:LRA=11"
    cmd = [
        "ffmpeg", "-y", "-i", str(infile),
        "-af", filter_complex,
        str(outfile)
    ]
    print("Processing:", infile.name)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        return False
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--lufs", type=float, default=-14.0)
    parser.add_argument("--tp", type=float, default=-1.0)
    parser.add_argument("--ext", default=".wav", help="Output extension")
    args = parser.parse_args()

    in_dir = Path(args.input_dir)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    files = list(in_dir.glob("*.wav")) + list(in_dir.glob("*.mp3")) + list(in_dir.glob("*.flac"))
    if not files:
        print("No audio files found", file=sys.stderr)
        sys.exit(1)

    ok = 0
    for f in files:
        out = out_dir / (f.stem + args.ext)
        if normalize_one(f, out, args.lufs, args.tp):
            ok += 1

    print(f"Completed {ok}/{len(files)} files → {out_dir}")

if __name__ == "__main__":
    main()