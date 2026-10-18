---
name: keyword-research-pro
description: Local-first and API-assisted keyword research skill with exportable clustered reports. Use for keyword discovery, clustering, search volume analysis, competitor terms, content gap identification, and handoff to content-marketing-orchestrator or blog/video skills. Triggers include keyword research, keyword clustering, SEO keywords, search volume, content gaps, and keyword reports.
---

# Keyword Research Pro

## Overview

Perform structured keyword research that produces actionable, clustered keyword sets and clear reports. Prefer local or BYOK (bring-your-own-key) data sources when available. Output should be ready for content planning and handoff to writing or video skills.

## Core Workflow

1. Clarify seed keywords, target market, language, and goal (informational, commercial, transactional).
2. Expand seeds into related terms, questions, and long-tails.
3. Gather metrics (volume, difficulty, CPC, trend) from available sources.
4. Cluster by intent and semantic similarity.
5. Identify content gaps and prioritization scores.
6. Produce a structured report (tables + recommendations) and optional CSV/JSON export.

## Clustering Principles

- Group by search intent first, then by topical similarity.
- Keep primary keywords and their supporting long-tails together.
- Flag branded vs non-branded when relevant.
- Surface people-also-ask and related questions as separate opportunity lists.

## Report Structure

See references/report-template.md for the preferred output format.

## Data Sources

- Prefer structured APIs the user has access to (DataForSEO style or equivalents).
- Fall back to publicly available insights and search suggest patterns when APIs are unavailable.
- Always disclose the data source and freshness of metrics.

## Scripts

Use scripts/ for deterministic report generation and simple exports when tabular data is ready.

## Quality Gates

- Every recommended keyword has clear intent and a suggested content type.
- Clusters are mutually coherent.
- Prioritization is explained (volume x relevance x feasibility).
- User can export and reuse the data.

Load references only when building the full report or when the user asks for methodology details.
