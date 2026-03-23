# Roadmap

## Phase 1: Ingestion Foundation

- Define a source-agnostic normalized repository schema
- Build Trendshift ingestion as the first source adapter
- Save dated source snapshots and extracted records
- Add duplicate removal across pages and prior archive dates

## Phase 2: Scoring and Selection

- Add quality scoring for novelty, utility, and content potential
- Rank repositories for different audience types
- Separate developer-interest and business-interest signals

## Phase 3: Content Generation

- Generate X post drafts
- Generate Threads post variants
- Generate YouTube short script outlines
- Add reusable prompts and templates per channel

## Phase 4: Review and Publishing

- Add human review checkpoints
- Add export bundles for approved content
- Add publishing integrations and scheduling

## Phase 5: Analytics Loop

- Track what content performed best by source and category
- Feed engagement back into scoring and selection

## Immediate next tasks

1. Finish Trendshift source adapter
2. Save normalized repository JSON outputs by date
3. Add one content generator for X
4. Add score fields to the normalized schema
