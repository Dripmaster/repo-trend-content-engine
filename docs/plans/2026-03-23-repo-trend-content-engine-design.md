# Repo Trend Content Engine Design

## Goal

Create the minimum working structure for a repository that can:

- ingest trending repositories from multiple sources
- archive and dedupe snapshots by date
- normalize repository records into a reusable schema
- prepare later content generation for X, Threads, and YouTube

## Chosen approach

Use a layered structure:

1. `sources/` for source-specific collection logic
2. `archives/` for raw curated markdown outputs
3. `normalized/` for source-agnostic repository records
4. `content/` for channel-specific generated content
5. `skills/` for reusable curation workflows

This keeps source ingestion separate from publishing logic and avoids coupling the project to Trendshift alone.

## Initial deliverables

- roadmap document
- normalized repository schema
- Trendshift source module with minimal helper functions
- unit tests for the helper functions
- folder scaffolding for future channel-specific outputs

## Non-goals

- full multi-source ingestion
- direct social publishing
- scheduling or media rendering

## Verification

- unit tests for deterministic helper logic
- repository structure present on disk
- roadmap and schema documents committed alongside code
