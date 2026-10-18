# Export Targets and Loudness Guidelines

Apply these when the user requests platform-ready files. Always measure after processing.

## Common Targets

| Platform     | Target Loudness     | True Peak     | Notes |
|--------------|---------------------|---------------|-------|
| Spotify      | –14 LUFS            | ≤ –1 dBTP     | Integrated loudness |
| YouTube      | –14 LUFS            | ≤ –1 dBTP     | Similar to Spotify |
| TikTok / Reels / Shorts | –12 to –9 LUFS | ≤ –1 dBTP | Often louder for mobile |
| Apple Music  | –16 LUFS            | ≤ –1 dBTP     | Slightly quieter |
| Podcast / Spoken | –16 to –19 LUFS | ≤ –1 dBTP | Clarity preferred |
| Generic / Archive | –14 LUFS         | ≤ –1 dBTP     | Safe default |

## Technical Defaults
- Sample rate: 44.1 kHz or 48 kHz (prefer 48 kHz for video sync)
- Bit depth: 16-bit or 24-bit
- Channels: Stereo
- Format: WAV for masters, MP3/AAC for delivery when size matters

## Process
1. Analyze current loudness.
2. Apply gain + limiter to hit target LUFS and true-peak.
3. Re-measure.
4. Convert/containerize if needed.
5. Validate with the export validation script.

Never clip. Prefer transparent limiting. Inform the user of the final measured values.