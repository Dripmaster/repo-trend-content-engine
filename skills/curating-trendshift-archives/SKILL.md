---
name: curating-trendshift-archives
description: Use when refreshing Trendshift repository summaries from https://trendshift.io/ and https://trendshift.io/github-trending-repositories, especially when the user wants date-based archive updates, duplicate removal, Korean summaries, or "new since last snapshot" filtering.
---

# Curating Trendshift Archives

## Overview

Maintain a date-based Trendshift archive in Markdown. Fetch both Trendshift pages for the requested date, preserve raw HTML snapshots, dedupe repositories, then append a new dated section without destroying earlier sections.

## Core Rules

- Always treat Trendshift data as time-sensitive. Re-fetch for the requested date instead of trusting old memory.
- Always preserve prior dated sections unless the user explicitly asks to replace them.
- Always dedupe in two places: between the two Trendshift pages, and against previously archived repositories when the user asks for "new only".
- Always include GitHub links in the final archive entries.
- Default output language is Korean if the user is speaking Korean.

## Archive Layout

Use a single archive file when the user wants cumulative history:

- Primary archive: `trendshift-50-repos-summary.md`
- Optional dated copy: `trendshift-summary-YYYY-MM-DD.md`

Recommended archive structure:

```md
# Trendshift Repository Archive

This document is maintained as a date-based archive.

## Date: YYYY-MM-DD
- Source: ...
- Rule: ...
- Result: ...

### source-name (N items)
1. **[owner/repo](https://github.com/owner/repo)** [TS|GH]
   - Summary: ...
   - Usage example: ...
```

If the user instead wants "new only", create a dated section that says it contains only repositories not already present in earlier sections.

## Workflow

### 1. Fetch current pages

Fetch both:

- `https://trendshift.io/`
- `https://trendshift.io/github-trending-repositories`

Store raw HTML locally with the date in the filename when possible:

- `trendshift_home_YYYY-MM-DD.html`
- `trendshift_github_YYYY-MM-DD.html`

If a dated filename is not needed, keep stable snapshots too:

- `trendshift_home.html`
- `trendshift_github.html`

### 2. Extract repositories

Trendshift HTML changes over time. Prefer the most stable available source in this order:

1. Embedded JSON fields like `full_name`, `repository_description`, or `description`
2. Card HTML with `/repositories/<id>` links and visible description blocks

Extract at least:

- repository full name
- source page (`TS` for home page, `GH` for GitHub Trending page)
- description if available

### 3. Dedupe correctly

Apply these rules in order:

1. Remove duplicates between the two pages by repository full name
2. If the user asks for "new only", compare against all repository names already present in earlier archive sections
3. Keep counts explicit:
   - raw page totals
   - unique total after page dedupe
   - excluded overlap count
   - remaining new count

### 4. Write the section

For each repository:

- Convert `owner/repo` into a GitHub markdown link
- Write a Korean summary
- Add one concrete usage example tied to that specific repository

Do not use generic repeated usage examples if the user asked for repo-specific scenarios.

### 5. Preserve history

If the archive already exists:

- append or insert a new `## Date: YYYY-MM-DD` section
- keep earlier dated sections intact
- never delete older sections unless the user explicitly asks

## Summary Style

Use short explanatory Korean prose, not keyword fragments.

Good summary:
- what the repository is
- what it is primarily used for

Good usage example:
- a realistic team or product scenario
- concrete enough that a reader can imagine adoption

Avoid:
- vague praise
- repeating the repository name as the only substance
- the same generic example across a whole category

## Verification

Before claiming the archive is updated, verify:

- the archive file exists
- dated sections count is correct
- repository count matches the intended result
- every repository line has a GitHub link
- every repository has both `Summary` and `Usage example` lines, or the localized equivalents the archive uses

Useful checks:

- count section headers: `^## Date:` or the archive's localized date header
- count repository lines: `^\d+\. \*\*\[`
- count summary lines: `^\s+- Summary:` or localized equivalents
- count usage example lines: `^\s+- Usage example:` or localized equivalents

## Common Mistakes

- Replacing the archive instead of accumulating by date
- Forgetting that today's two pages can overlap
- Comparing against only the latest section instead of the whole archive when asked for "new only"
- Leaving out links
- Using stale HTML snapshots without refetching for time-sensitive requests
- Assuming both pages still expose the same HTML structure as before
