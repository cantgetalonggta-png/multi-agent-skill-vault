#!/usr/bin/env python3
"""Print a simple bar/shot grid for a music video."""
import argparse

def main():
    p = argparse.ArgumentParser(description="MV shot grid from duration + BPM")
    p.add_argument("--duration", type=float, required=True, help="Song length in seconds")
    p.add_argument("--bpm", type=float, default=100.0)
    p.add_argument("--clip", type=float, default=6.0, help="Target clip length seconds")
    args = p.parse_args()
    beat = 60.0 / args.bpm
    bar = beat * 4
    print(f"duration={args.duration:.2f}s bpm={args.bpm} beat={beat:.3f}s bar={bar:.3f}s")
    t = 0.0
    i = 1
    while t < args.duration - 0.01:
        end = min(args.duration, t + args.clip)
        bars = (end - t) / bar
        print(f"shot {i:02d}  {t:6.2f} -> {end:6.2f}  (~{bars:.1f} bars)")
        t = end
        i += 1

if __name__ == "__main__":
    main()
