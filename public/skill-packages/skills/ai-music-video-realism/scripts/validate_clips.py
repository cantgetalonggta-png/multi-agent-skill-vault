#!/usr/bin/env python3
"""Probe a folder of video clips with ffprobe."""
import argparse, json, subprocess, sys
from pathlib import Path

def probe(path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,bit_rate:stream=width,height,avg_frame_rate,codec_type",
        "-of", "json", str(path),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        return {"file": str(path), "error": r.stderr.strip()}
    data = json.loads(r.stdout or "{}")
    fmt = data.get("format", {})
    streams = data.get("streams", [])
    v = next((s for s in streams if s.get("codec_type") == "video"), {})
    a = next((s for s in streams if s.get("codec_type") == "audio"), {})
    return {
        "file": path.name,
        "duration": float(fmt.get("duration") or 0),
        "width": v.get("width"),
        "height": v.get("height"),
        "fps": v.get("avg_frame_rate"),
        "has_audio": bool(a),
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("folder")
    args = p.parse_args()
    folder = Path(args.folder)
    files = sorted([f for f in folder.iterdir() if f.suffix.lower() in {".mp4", ".mov", ".webm", ".mkv"}])
    if not files:
        print("no video files")
        sys.exit(1)
    for f in files:
        print(probe(f))

if __name__ == "__main__":
    main()
