---
name: ai-music-video-realism
description: Produce ultra-realistic AI music videos with natural body movement, lip-sync, character consistency, and beat-locked edits. Use when the user wants an AI music video, performance video, dance clip, lip-synced artist video, cinematic MV, or photoreal motion from a song or stems. Triggers include music video, lip sync, natural movement, ultra-realistic video, Kling, Veo, Seedance, Runway Gen-4, motion transfer, and beat-sync video.
metadata:
  type: workflow
  version: "1.0"
  pairs-with: local-music-generation, ai-video-production-pipeline
---

# AI Music Video Realism

## Overview

Turn a finished track (or stems) into a performance-grade music video. Prioritize photoreal humans, physically believable motion, locked identity, and edits that hit the beat. Do not treat this as a generic clip generator — music videos fail on identity drift, rubber limbs, unsynced mouths, and cuts that ignore tempo.

## Core Pipeline

1. Lock the song — title, BPM if known, structure map (intro/verse/chorus/bridge/outro), duration, mood, lyric moments that need lip-sync vs B-roll.
2. Lock the artist look — one approved character sheet (front, 3/4, full-body, costume). Identity lives in references, not in rewritten prompts.
3. Plan shots to the music — 4–8s clips. Lip-sync only on slower melodic lines looking at camera. Fast syllable runs become performance/B-roll, not mouth-lock shots.
4. Generate by job, not by one model for everything:
   - Photoreal performer + natural body motion → Kling 3 / Seedance 2 / motion-transfer
   - Cinematic lighting and glossy hero frames → Veo 3.1 / Runway Gen-4.5
   - Abstract or effects-driven cuts → Runway / Pika / visualizer tools
   - Full-song assembly + beat sync → NLE or music-video workflow tools
5. Assemble on a timeline to the audio master. Never leave generated native music under the real track.
6. Quality-gate every clip before it ships (see references/quality-gates.md).
7. Export platform masters (16:9 YouTube, 9:16 Reels/TikTok, optional 1:1).

Pair audio work with `local-music-generation`. Pair generic video logistics with `ai-video-production-pipeline`. This skill owns realism, motion, and music-video craft.

## Non-Negotiable Rules

- Image-to-video for any complex body work. Text-to-video is for landscapes, crowds, and mood plates — not dance or limb-heavy performance.
- Match reference framing to the shot. Full-body motion needs a full-body still. Close-up lip-sync needs a clean face still.
- One primary action per clip. Start pose → main action → end pose. No stacked contradictory motion adjectives.
- Keep clips short (4–8s typical; 10–15s only when the model holds identity).
- Generate 2–3 takes per hero beat. Repair the weak shot, do not reroll the whole video.
- Prompt for action, camera, lighting. Lock identity in the reference pack.
- Disable or override model-generated music. Use the user's track as the only music bed.
- Consent and likeness — never clone a real person for a performance video without explicit user-owned reference of themselves or a fictional character they created.

## Shot Prompt Pattern

```
IDENTITY — use uploaded character refs. Same face, age, skin, hair, body, costume.
SHOT — [size] [lens] [camera move]. [one action]. Ends in [stable pose].
MOTION — weight, momentum, natural blink/breath, stable hands, fabric follows body. 2-3 motion words only.
CONTINUITY — lighting direction, palette, location, props stay locked.
AVOID — extra fingers, sliding feet, identity swap, rubber spine, snapped cuts between poses.
```

Motion language that works: fluid transition, graceful arc, continuous sweep, measured steps, weight shift, grounded stance.
Motion language that breaks bodies: chaotic, exploding, teleport, snap, extreme contortion, plus mixed "staccato + flowing" in one prompt.

## Lip-Sync Rules

- Character faces camera. Profile lip-sync fails.
- Use slower verses/choruses. Fast rap/melisma → performance energy shots without mouth lock.
- Prompt "no generated music, natural production sound only" when the model adds audio.
- Align clip in/out to lyric phrases, not arbitrary seconds.
- If mouth timing is off, shorten the line or cut away on the downbeat rather than stretching the clip.

## Natural Body Movement

Treat kinematics as a first-class spec:

- Neutral prep pose in the still (limbs separated, balanced stance).
- Describe start / action / end. Do not invent mid-air poses with no landing.
- Prefer I2V + motion reference video (dance, walk, performance) over text-only choreography.
- Match proportions between still and motion plate (full-body plate ↔ full-body still).
- Leave headroom and floor room so limbs are not cropped mid-move.
- For advanced retargeting, extract 3D body motion then re-shoot camera in a 3D package and re-render through a reference-to-video model. See references/motion-systems.md.

## Ultra-Real Look

Photoreal is lighting + lens + skin + physics, not the word "realistic" alone.

Specify: time of day, key/fill direction, practical sources, lens mm, depth of field, film stock or digital cinema camera language, sweat/skin oil only if motivated, wardrobe fabric weight.
Avoid: beauty-filter skin, extra limbs, morphing jewelry, floating hair sheets, looping idle sway that ignores the beat.

## Beat-Locked Edit

- Cut on downbeats and phrase ends.
- Hold hero performance through chorus hooks.
- Use B-roll / insert / environment on bars that cannot hold identity.
- Match energy of camera move to section (slow push on verse, harder moves on drop).
- Keep generated clip native fps; conform in the NLE, do not resample twice.

See references/tool-matrix.md, references/shot-templates.md, references/quality-gates.md, references/motion-systems.md, references/av-sync-and-effects.md.

## Scripts

- `scripts/shot_plan.py` — turn duration + BPM into a bar/shot grid
- `scripts/validate_clips.py` — probe resolution, fps, duration of a folder of clips
