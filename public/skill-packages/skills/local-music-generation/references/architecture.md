# Architecture Overview

High-level pipeline for local music generation (inspired by ACE-Step 1.5 style systems and Claude Code skill wrappers):

1. **Prompt Intake & Planning**
   - User natural-language request
   - Optional structure planning (lyrics, sections, BPM, key)
   - Quality preset selection

2. **Model Inference**
   - Local GPU model (text-to-music or lyrics-conditioned)
   - Supports full generation, style transfer/cover, and section-level repaint
   - Multiple quality/speed modes trading compute for fidelity

3. **Post-Processing**
   - Format conversion (via FFmpeg)
   - Loudness normalization (LUFS + true peak)
   - Optional denoising, stem separation, enhancement

4. **Analysis**
   - BPM, key, duration, loudness metrics
   - Waveform and spectral checks when available

5. **Library & Metadata**
   - Local storage of audio + sidecar metadata
   - Tags, ratings, generation parameters for reproducibility

6. **Export Targets**
   - Platform-specific loudness and container settings (Spotify, YouTube, TikTok, etc.)

Components can be invoked independently (e.g., analyze an existing file, normalize only, or repaint one section of a previous generation).

The skill orchestrates these stages and calls helper scripts for deterministic steps.