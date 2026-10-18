---
name: local-music-generation
description: Local GPU music production skill for generating full songs, instrumentals, covers, section edits, vocal mastering, and loudness-normalized exports from text prompts or existing stems. Use when the user asks to make music, generate a song, create a beat, produce vocals, cover a track, repaint a section, apply vocal chains, remaster, export for streaming platforms, or build a music library. Triggers include music generation, song creation, ACE-Step, local music studio, lyrics-driven tracks, vocal mastering, remaster, and audio export workflows.
---

# Local Music Generation

## Overview

Turn descriptive text prompts into finished tracks using local GPU-accelerated models (primarily ACE-Step 1.5 style pipelines). Supports full songs with sung lyrics, instrumentals, style covers, section-level edits (repaint), quality presets, loudness normalization, and library management. All generation happens locally; no cloud per-song fees.

## Core Workflow

1. Clarify the request: genre/style, mood, length (seconds or bars), vocals vs instrumental, language of lyrics, reference tracks or constraints.
2. Plan structure if needed: intro / verse / chorus / bridge / outro, BPM, key, instrumentation.
3. Select quality preset (see references/quality-presets.md).
4. Generate the track.
5. Optionally analyze (BPM, key, loudness), enhance, or repaint specific sections.
6. Export in the required format and loudness target.
7. Catalog into the library with metadata and optional rating.

## Generation Commands and Patterns

- Full song with lyrics: "Make a [genre] song about [topic], [length], with [vocal style]"
- Instrumental: "Create an instrumental [style] piece, [BPM], [mood]"
- Cover / style transfer: "Make a rock cover of this song" or provide audio + new style
- Section edit (repaint): "Fix the chorus, make it more energetic" or "Replace the bridge with a quieter piano section"
- Random / surprise: "Surprise me with a [optional constraint]"
- Export: "Export for Spotify / YouTube / TikTok / Instagram" (applies platform loudness and format norms)

Always confirm before long high-quality generations (max preset can take several minutes) or when external API keys or large model downloads would be required.

## Quality Presets

Use the presets defined in `references/quality-presets.md`. Default to `standard` unless the user requests higher fidelity or speed is critical.

## Advanced Lyrics and Structure Planning

When the request involves vocals or a full song:

1. Extract or invent a clear theme, emotional arc, and narrative beats.
2. Propose a structure map before generation (e.g. Intro 8 bars → Verse 16 → Pre-Chorus 8 → Chorus 16 → Verse 16 → Chorus 16 → Bridge 8 → Final Chorus 16 → Outro).
3. Write or refine lyrics section-by-section, matching syllable stress to expected rhythm and BPM.
4. Specify vocal delivery (intimate whisper, powerful belt, stacked harmonies, ad-libs, gender, accent, language).
5. Note any call-and-response, doubles, or layered vocal textures desired.
6. Confirm the structure and key lyric lines with the user before committing to a long generation.

See `references/lyrics-structure-planning.md` for templates and examples.

## LoRA-style Custom Style Notes

For consistent artist or genre emulation across multiple tracks:

- Maintain a short "style card" per custom style: instrumentation palette, drum character, harmonic language, vocal production signature, mix references, forbidden elements.
- When the user provides reference tracks, extract and record 3–7 distinctive traits.
- Apply the style card on subsequent generations and covers.
- For true LoRA / fine-tune workflows (when the underlying model supports them), document training data requirements, rank, learning rate ranges, and evaluation criteria in `references/lora-custom-styles.md`.
- Always version style cards so older generations remain reproducible.

## Vocal Mastering and Effects Chains

Common vocal treatment chains (apply after generation or on provided stems):

- Clean intimate: gentle de-ess → subtle compression → short plate or room → light saturation → level to –14 to –16 LUFS integrated for the full mix.
- Radio polish: tighter compression + upward compression → presence EQ (3–5 kHz) → controlled de-ess → stereo width on doubles → limiter.
- Club / wet: longer reverb or delay throws, sidechain to kick if present, more aggressive saturation, wider stereo image.
- Warm plate / soul: dark plate reverb, gentle tape-style saturation, rounded low-mids, soft high shelf.

Always work non-destructively. Keep dry vocal available. Measure before/after loudness and true peak. See `references/vocal-mastering-chains.md
- `references/ai-vocal-mastering-era.md` — hybrid AI-era vocal mastering skills and standards`.

## Architecture Notes

See `references/architecture.md` for the high-level pipeline (prompt → structure planning → model inference → post-processing → library).

## Tooling and Environment

- Prefer local GPU (NVIDIA 8 GB+ VRAM recommended; 4 GB minimum for turbo modes).
- Required supporting tools when available: FFmpeg for format conversion and loudness, Python environment with the music model stack.
- For analysis and enhancement steps, call scripts in `scripts/` when present.

## Library Management

Maintain a simple local library of generated tracks with:
- Filename / title
- Style tags
- Duration
- BPM / key (if analyzed)
- User rating
- Generation parameters (for reproducibility)


## Remaster & Export Folder Convention

When processing existing stems or masters (e.g. from a Google Drive project folder):
1. Keep originals untouched.
2. Produce normalized variants with clear prefixes:
   - `ORIGINAL_*` — source files
   - `NORMALIZED_<LUFS>_*` — single-file targeted loudness
   - `BATCH_-14LUFS_*` (or other target) — bulk platform-ready WAVs
3. Place all versions in a single deliverable folder (e.g. `remastered_exports/`) with a `MANIFEST.txt`.
4. Prefer `--two-pass` on normalize_loudness.py for final masters.
5. Document the chain used (intimate / radio / club / warm-plate) in the MANIFEST or processing notes.

See the project `remastered_exports/` folder for a complete real-task example using the V3 masters + stripped vocals.

## Safety and Confirmation

- Ask for confirmation before any irreversible file overwrites, large model downloads, or credential use.
- Generated audio is user-owned; do not claim copyrights or redistribute models.
- Keep generations on-topic to the user's request; do not inject unrelated content.

## References

- `references/quality-presets.md` — speed/quality trade-offs and recommended use cases
- `references/process-checklist.md` — step-by-step production checklist
- `references/example-prompts.md` — high-signal example prompts and expected outputs
- `references/architecture.md` — pipeline and component overview
- `references/export-targets.md` — platform loudness and format guidelines
- `references/lyrics-structure-planning.md` — advanced structure maps and lyric workflows
- `references/lora-custom-styles.md` — style cards and LoRA-style custom notes
- `references/vocal-mastering-chains.md
- `references/ai-vocal-mastering-era.md` — hybrid AI-era vocal mastering skills and standards` — effects chains and vocal treatment recipes

## Scripts

- `scripts/normalize_loudness.py` — apply target LUFS and true-peak limits (optional `--two-pass`)
- `scripts/analyze_track.py` — extract duration/format (BPM/key best-effort when libs available)
- `scripts/validate_export.py` — check format, sample rate, channels, loudness
- `scripts/batch_export.py` — process multiple files to platform targets
- `scripts/generate_report.py` — produce a simple analysis report for a track or folder
- `scripts/simple_validate.py` — quick technical validation of audio files

Load the relevant reference files when the user asks for details, quality choices, or export settings. Keep the main instructions concise.