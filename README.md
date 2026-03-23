# repo-trend-content-engine

An engine for discovering trending open-source repositories from multiple sources, curating them into dated archives, and turning them into reusable inputs for posts, threads, videos, and multi-channel publishing workflows.

## Why this exists

Trending repositories appear across many channels, but the raw feeds are noisy, overlapping, and hard to reuse. This repository is the working system for:

- collecting trending repositories from multiple discovery sources
- deduping and archiving them by date
- enriching them with summaries and usage angles
- preparing structured inputs for social and media content generation

## Current scope

- archive repository snapshots by date
- dedupe across sources and prior snapshots
- generate Korean summaries and repository-specific usage examples
- keep reusable workflow skills for repeatable curation work

## Planned scope

- add more discovery sources beyond Trendshift
- normalize repository signals across channels
- generate post drafts, hooks, thread outlines, and video scripts
- prepare outputs for Instagram, Threads, X, and YouTube
- add scheduling and publishing integrations

## Repository layout

- `archives/`
  Dated and cumulative markdown outputs for curated repository snapshots.
- `skills/curating-trendshift-archives/`
  Reusable skill for fetching Trendshift pages, deduping repositories, and updating archive sections by date.

## Current artifacts

- [archives/trendshift-50-repos-summary.md](./archives/trendshift-50-repos-summary.md)
- [archives/trendshift-summary-2026-03-23.md](./archives/trendshift-summary-2026-03-23.md)
- [skills/curating-trendshift-archives/SKILL.md](./skills/curating-trendshift-archives/SKILL.md)

## Suggested GitHub repo metadata

- Description: Discover trending open-source repositories, curate dated archives, and turn them into social and video content workflows.
- Topics: `open-source`, `trending-repositories`, `content-engine`, `social-media-automation`, `trend-discovery`, `content-pipeline`, `github-trending`, `creator-tools`

## License

MIT
