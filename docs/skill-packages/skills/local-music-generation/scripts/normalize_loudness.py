#!/usr/bin/env python3
"""Normalize audio to a target LUFS and true-peak limit using ffmpeg/loudnorm.
Supports optional two-pass for higher accuracy.
Usage:
  python normalize_loudness.py input.wav output.wav [--lufs -14] [--tp -1.0] [--two-pass]
"""

import argparse
import json
import re
import subprocess
import sys
import os
import tempfile

def run(cmd, capture=True):
    print("Running:", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=capture, text=True)
    if result.returncode != 0:
        print(result.stderr if capture else "", file=sys.stderr)
        sys.exit(result.returncode)
    return result.stdout if capture else ""

def parse_loudnorm_json(stderr_or_stdout):
    # ffmpeg loudnorm prints JSON on stderr typically
    match = re.search(r"\{[^{}]*\"input_i\".*?\}", stderr_or_stdout, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        return None

def main():
    parser = argparse.ArgumentParser(description="Loudness normalize audio")
    parser.add_argument("input", help="Input audio file")
    parser.add_argument("output", help="Output audio file")
    parser.add_argument("--lufs", type=float, default=-14.0, help="Target integrated LUFS")
    parser.add_argument("--tp", type=float, default=-1.0, help="True peak limit (dBTP)")
    parser.add_argument("--two-pass", action="store_true", help="Use two-pass loudnorm for accuracy")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Input not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    if not args.two_pass:
        # Fast single-pass
        filter_complex = f"loudnorm=I={args.lufs}:TP={args.tp}:LRA=11"
        cmd = ["ffmpeg", "-y", "-i", args.input, "-af", filter_complex, args.output]
        run(cmd)
        print(f"Normalized (1-pass) {args.input} -> {args.output} (target {args.lufs} LUFS, TP {args.tp})")
        return

    # Two-pass
    measure_cmd = [
        "ffmpeg", "-i", args.input,
        "-af", f"loudnorm=I={args.lufs}:TP={args.tp}:print_format=json",
        "-f", "null", "-"
    ]
    # Capture both stdout and stderr
    result = subprocess.run(measure_cmd, capture_output=True, text=True)
    raw = result.stderr + result.stdout
    measured = parse_loudnorm_json(raw)
    if not measured:
        print("Two-pass measure failed; falling back to single-pass", file=sys.stderr)
        filter_complex = f"loudnorm=I={args.lufs}:TP={args.tp}:LRA=11"
        cmd = ["ffmpeg", "-y", "-i", args.input, "-af", filter_complex, args.output]
        run(cmd)
        print(f"Normalized (1-pass fallback) {args.input} -> {args.output}")
        return

    # Apply measured values
    i = measured.get("input_i", args.lufs)
    tp = measured.get("input_tp", args.tp)
    lra = measured.get("input_lra", 11)
    thresh = measured.get("input_thresh", -70)
    offset = measured.get("target_offset", 0)

    filter_complex = (
        f"loudnorm=I={args.lufs}:TP={args.tp}:LRA=11:"
        f"measured_I={i}:measured_TP={tp}:measured_LRA={lra}:"
        f"measured_thresh={thresh}:offset={offset}:linear=true"
    )
    cmd = ["ffmpeg", "-y", "-i", args.input, "-af", filter_complex, args.output]
    run(cmd)
    print(f"Normalized (2-pass) {args.input} -> {args.output} (target {args.lufs} LUFS, TP {args.tp})")
    print(f"Measured: I={i} TP={tp} LRA={lra}")

if __name__ == "__main__":
    main()
