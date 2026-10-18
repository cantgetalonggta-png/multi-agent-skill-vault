# AI Audio-Visual Sync and Video Effects

## Three different "sync" problems
Do not collapse these. Each needs a different tool.

1. Lip / viseme sync — mouth shape vs speech or sung lyric.
2. Beat / structure sync — cuts, camera hits, and energy vs tempo, downbeats, drops.
3. Event / foley sync — a visual event lands on an SFX or lyric word (glass smash, door, breath).

Native one-pass AV models (Veo / Kling / Seedance / HappyHorse / Wan) generate picture and sound together. Useful for dialogue shorts. For a finished music master, treat native audio as disposable and replace with the approved track.

## Lip-sync stack (2026)
- Generation-time: Kling Omni, Seedance 2, Wan InfiniteTalk-class workflows. Face the camera. Slow phrases only.
- Post / dub: Wav2Lip lineage, MuseTalk, LatentSync, SayAnything, OmniEdit, LipDub 2.0, sync.labs productions, Prime Video localization stack.
- Measure with LSE-C / LMD / SyncNet-style offset, not eyeballing alone.
- Failures: profile shots, occlusion, fast syllables, model music fighting the master, >100ms drift.
- Fix order: delay compensation → shorter phrase → cutaway on the downbeat → dedicated lip editor. Do not stretch the clip.

Classic research backbone: SyncNet (two-stream AV correspondence), Wav2Lip (sync expert loss), AV-HuBERT features, DiVAS (variable fps/sr transformers). Use them as QC, not as the only generator.

## Beat-sync / audio-reactive stack
Pipeline:
1. Analyze — BPM, beat grid, onsets, RMS, spectral flux, section labels (intro/verse/chorus/drop).
2. Demix when possible — kick, snare, bass, vocals, music as separate control streams (MTV-style multi-stream control).
3. Map features → picture
   - kick / downbeat → cut, camera hit, flash, zoom pulse
   - bass envelope → scale, warp, color weight
   - snare / clap → color snap, insert
   - vocal onset → performer energy or lyric card
   - section change → lighting / location shift
4. Quantize cuts to the beat grid. Humans prefer picture slightly early (~20–40ms), not late.
5. Density follows energy — hold verses, cut faster on drops.

Specialist tools: Kaiber Audio-Reactive Precision, Neural Frames stem modulation, BeatSync-class editors, Seedance multi-audio input, Magic Hour multi-track.

Prompt levers when the model takes audio: "pulse on kick", "cut on downbeat", "camera matches tempo", "no generated music".

## Video effects that read as "musical"
Use effects as instruments, not decoration.

| Driver | Effect |
| kick / bass | zoom pulse, UV warp, chromatic split, exposure pop |
| snare | hard cut, strobe, color invert frame |
| vocal | lip lock, lyric card, light on face |
| section lift | grade warmer/cooler, lens change, location jump |
| breakdown | longer holds, shallower motion |

Keep one driver per layer. Stacking kick-warp + snare-strobe + vocal-morph in the same frame looks cheap.

GPU/shader path (post, deterministic): bind onset/band energy to GLSL uniforms. This is more frame-accurate than asking a generative model to "be on beat."

## Production rule for this studio
- Generate clips mute or strip native audio.
- Lay the real master on the timeline first.
- Detect beats once; reuse the grid for every cut and effect.
- Lip-sync only designated close-ups.
- Audio-reactive effects live in post unless a specialist reactive generator is the look.
- QC: play at 0.5x around hooks; if the hit feels late, pull the picture earlier by 1–2 frames.
