# Vocal Mastering in the Age of AI — Practical Skills

## Hybrid best practice (human judgment + automated precision)
1. Start with highest-quality source possible (AI cannot invent a great performance).
2. Use AI/automation for: residual denoise, click/clip repair, initial loudness, pitch hints.
3. Use human ear for: emotional dynamics, final EQ taste, de-ess amount, spatial decisions.
4. Always A/B vs reference tracks and check mono compatibility.
5. Target standards: streaming -14 LUFS / -1 dBTP; competitive radio can go -12 to -13 LUFS.

## Recommended signal chain order
HPF → residual denoise → declick/declip → corrective EQ → compression → de-ess → optional warmth/saturation → stereo image → limiter → loudnorm metering

## Delivery targets
- Spotify/YouTube/Apple: -14 LUFS, TP ≤ -1 dBTP
- TikTok/Reels: often louder (-12 to -9) for mobile
- Intimate/ballad: -16 LUFS preserves dynamics
- Always deliver 24-bit masters; bounce 16-bit only for final delivery if required

## Tools map (AI era)
- Repair: RX-style denoise/de-click/spectral repair (afftdn, adeclick, adeclip in ffmpeg)
- Chain building: Nectar-style assistants for starting points
- Mastering: Ozone-style / loudnorm for compliant levels
- Stem separation: only when needed for remix/isolation
- Voice synth/cloning: consent-first; not a substitute for this artist’s own performance

## Ethics
Consent for voice models, clear attribution, no non-consensual cloning of real artists.
