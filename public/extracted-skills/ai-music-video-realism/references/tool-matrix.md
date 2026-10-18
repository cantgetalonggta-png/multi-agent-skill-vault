# Tool Matrix — AI Music Videos (2026)

Choose by job, not by brand loyalty. Specs change; the job mapping is the durable part.

## Performance / photoreal humans
- Kling 3.0 / 3.0 Omni — strongest raw pick for a real performer, natural weight, lip-sync in multiple languages, longer clips, multi-cut in one gen.
- Seedance 2.0 — prompt fidelity, dynamic camera, native audio, avatar-style full-body performance, good character lock when refs are clean.
- MiniMax Hailuo / H3 — motion quality, reference-to-video, cheaper iteration; pair with a locked character sheet.

## Cinematic hero frames
- Google Veo 3.1 — glossy lighting, 4K, strong establishing and performance still-energy shots.
- Runway Gen-4 / 4.5 — camera control, physics, effects, in-tool edit. Best when you will assemble the MV yourself.

## Fast / stylized / lyric
- Pika 2.x — short lyric moments, keyframe extensions.
- Luma Dream Machine / Ray — photoreal mood and highlight latitude; short clips.
- Visualizer suites (Neural Frames, Kaiber-class tools) — audio-reactive, not identity-locked performers.

## Full-song assemblers
- Music-video workflow apps (Atlabs, Neural Frames Autopilot, VidMuse-class agents) — upload the track, get beat-matched assembly. Use when speed matters more than shot-level craft.
- Manual NLE (Resolve / Premiere / CapCut) — required for a release-grade cut even if generation is automated.

## Motion systems
- Image-to-video with a still + text action (default).
- Motion transfer / motion control (Kling-class) — plate video drives body; still drives identity.
- 3D body extract (SAM 3D Body-class) → camera re-shoot in Blender → reference-to-video re-render when you need a new lens on real choreography.

## Local Grok Imagine path
When working inside this agent, use the Imagine video tools already available:
- text-to-video for mood plates and environments
- image-to-video for performer clips from an approved still
- reference-to-video when identity + location + motion must bind together
- Keep clips 6–10s, stitch in ffmpeg, replace or mix audio with the real track

Do not invent API access you do not have. If a named cloud model is required, say so and hand the user a shot list + prompts they can run.
