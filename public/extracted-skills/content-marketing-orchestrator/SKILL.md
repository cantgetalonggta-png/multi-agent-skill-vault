---
name: content-marketing-orchestrator
description: Thin orchestrator that sequences specialized skills for end-to-end content marketing campaigns. Use when the user wants a full content package involving keyword research, blog or long-form content, AI video production, and music beds from local-music-generation. Triggers include content marketing campaign, full content package, keyword to video workflow, multi-asset content production, and campaign brief.
---

# Content Marketing Orchestrator

## Overview

Coordinate a sequence of specialized skills to produce a coherent multi-asset content package. This skill does not re-implement domain logic; it routes work to the appropriate specialized skills and maintains overall campaign context.

## Typical Sequence

1. Keyword and topic research (keyword-research or SEO skill when available)
2. Long-form or blog content creation (blog / content skill when available)
3. Video production derived from the content (ai-video-production-pipeline)
4. Music bed or sonic branding (local-music-generation)
5. Final packaging and platform adaptation

## How to Operate

- Maintain a shared campaign brief (topic, audience, primary keyword, brand voice, target platforms).
- Invoke each specialized skill in turn, passing relevant context from previous stages.
- After each major stage, summarize outputs and confirm next steps with the user.
- Allow the user to skip, reorder, or stop at any stage.
- When a specialized skill is missing, fall back to general best-practice instructions and note the gap.

## Campaign Brief Template

Capture at the start:
- Primary topic / keyword
- Audience and intent
- Brand voice and constraints
- Target platforms and formats
- Desired assets (blog, short video, long video, audio, social variants)
- Deadline or priority

## Quality and Consistency

- Ensure messaging, terminology, and visual/sonic style remain consistent across assets.
- Re-use key phrases, CTAs, and brand elements.
- Document generation parameters so assets can be iterated later.

## References

- references/campaign-brief-template.md
- references/handoff-checklist.md

This skill is intentionally thin. Prefer loading the specialized skills for deep work.
