---
name: evidence-hypothesis-pipeline
description: Domain-agnostic Bayesian-style evidence and hypothesis pipeline. Updates belief weights only from evidence found, provided, or publicly supported. Use for any research or analysis domain — not tied to a single case.
version: "1.0.0"
tags: [bayesian, evidence, hypothesis, epistemology, general]
---

# Evidence–Hypothesis Pipeline (Domain-Agnostic)

## Purpose
Maintain a living set of **hypotheses** and **evidence records**. Update confidence only when new evidence appears. Never invent evidence. Never treat narrative or persona prose as primary evidence.

## Objects

### Hypothesis
- `id` (H1, H2, …)
- `statement` (falsifiable claim)
- `prior` (0–1, operator or literature seed)
- `posterior` (updated)
- `status`: open | supported | weakened | retired
- `supporting_evidence_ids[]`
- `contradicting_evidence_ids[]`
- `notes`

### Evidence
- `id` (E1, E2, …)
- `source` (URL, doc title, file hash, citation)
- `type`: primary | secondary | tertiary | process_note
- `summary` (what it actually shows)
- `reliability` (0–1)
- `tags[]`
- `linked_hypotheses[]`

## Update rule (simple log-odds friendly)
For each new evidence item E affecting hypothesis H:
1. Classify direction: supports | weakens | neutral
2. Weight = reliability × relevance (0–1)
3. Nudge posterior toward support or away; clamp to (0.01, 0.99)
4. Log the update with timestamp and reason
5. **Do not** update posteriors for hypotheses the evidence does not touch

## Fence
- Only evidence that is found, provided, or publicly supported may move posteriors
- Process notes (operator hygiene, tooling) never move claim posteriors
- Restricted / illegal sources: CATALOG_ONLY — do not execute; may list as process notes if relevant
- Guilt or liability for persons requires adjudicated public facts only

## Cycle output
1. Evidence ledger delta
2. Hypothesis table (prior → posterior, delta, reason)
3. Open questions ranked by value of information
4. Explicit “no new evidence” if empty
