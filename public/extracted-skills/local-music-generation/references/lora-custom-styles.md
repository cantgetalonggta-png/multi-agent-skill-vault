# LoRA-style Custom Style Notes and Style Cards

## Style Card Template

```
Style name:
Reference tracks:
Instrumentation palette:
Drum / groove character:
Harmonic language / common progressions:
Vocal production signature:
Mix references (loudness, width, low-end, top end):
Forbidden or avoided elements:
Keywords / prompt fragments that reliably evoke the style:
Version / date:
```

## Practical Use

- Create a style card when the user supplies 1+ reference tracks or repeatedly requests the same aesthetic.
- Store cards in a local notes folder or inside the skill’s assets for reuse.
- On new generations, prepend or inject the style card keywords and constraints.
- For models that support actual LoRA / fine-tuning:
  - Collect 10–50 high-quality, consistent examples.
  - Document recommended rank, learning rate schedule, and number of steps.
  - Evaluate on held-out prompts for style fidelity vs. prompt adherence.
  - Version the resulting adapter and note the base model it was trained on.

## Example Style Card (Soul Rhodes)

```
Style name: Warm Soul Rhodes
Instrumentation: Rhodes electric piano, soft electric bass, light brushed or tight kit, subtle strings or pads
Drum character: Laid-back pocket, soft attack
Harmonic language: 7ths, 9ths, smooth voice leading, occasional secondary dominants
Vocal signature: Intimate, slightly breathy, plate reverb, gentle doubles
Mix: Warm low-mids, controlled highs, –14 LUFS target, moderate stereo width
Avoid: Aggressive distortion, hyper-compressed modern pop drums, harsh digital reverb
Prompt fragments: "warm rhodes soul", "smooth 70s neo-soul", "intimate vocal plate"
```

Update cards as the user’s taste evolves.