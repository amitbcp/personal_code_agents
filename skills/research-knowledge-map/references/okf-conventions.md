# OKF conventions for project wikis

Target the [canonical OKF v0.2 specification](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md), checked 2026-09-16. This is a focused implementation guide, not a replacement specification. The old `knowledge-catalog/okf` copy is frozen. No Google account, SDK or reference agent is required.

## Bundle boundary and format

The wiki directory is the bundle root, even when nested inside a project. Every Markdown file within it, except reserved `index.md` and `log.md`, is a concept and needs YAML frontmatter with a nonempty `type`. Keep project instructions and raw Markdown sources outside this boundary unless deliberately represented as concepts. Types are extensible; our useful examples are Concept, Paper, Decision, Experiment and Question.

For authored pages, our local convention adds a title, short description, source records and generation metadata where known. These additions improve our workflow; they are not all required by OKF. Preserve unfamiliar fields and do not invent unavailable metadata. Use timezone-qualified ISO datetimes.

An illustrative source-backed page (fictional data, not a result to copy):

```markdown
---
type: Experiment
title: Candidate-pool comparison
description: What a development-set comparison can establish.
status: draft
generated:
  by: codex/example-model
  at: '2026-09-16T12:00:00Z'
sources:
  - id: dev-report
    resource: ../../reports/candidate-pool.md
    title: Candidate-pool development report
---
# Finding

The comparison used a development split; it does not establish final-test performance.[^dev-report]

[^dev-report]: Development report, Evaluation section, run identifier recorded there.
```

Here the page is `docs/wiki/candidate-pool.md` and the report is `reports/candidate-pool.md` at project root. Replace example identities, times and claims with observed facts. Use stable source IDs for footnote attribution, not list positions. Record paper versions, report sections, code revisions or run IDs where they disambiguate evidence.

## Indexes, logs and links

Use `index.md` as the directory listing and `log.md` as update history. Follow the specification's reserved-file structure rather than treating either as an ordinary concept. A bundle-root index may declare `okf_version: "0.2"` as its only frontmatter key; non-root indexes have no frontmatter. Keep each directory index focused on that directory's pages and subdirectories. Add subdirectory indexes when navigation needs them.

Log changes under newest-first `## YYYY-MM-DD` headings; add new records without rewriting old entries. Include the operation, affected pages and source/result changes. Logs have no frontmatter.

Use standard Markdown links. A leading `/` means the bundle root in OKF, not the filesystem or Git repository root. Relative links are also supported; prefer them for our in-repository browsing, resolving from the referring page. Links outside the bundle are external project dependencies and may not survive exporting the wiki alone. Record that limitation; do not claim such an export is self-contained. Broken links are tolerated by OKF consumers but should be surfaced and repaired or explicitly recorded as planned pages in our upkeep checks.

## Verification and freshness

Use `generated` for actual authorship and `verified` only for checks actually performed against sources. `human:<id>` denotes an actual person's verification; an agent must not grant it to itself. Machine verification is also a recorded action, not a consequence of successful YAML parsing. Record scope/conditions in prose when only part of a page was checked.

`status` can mark draft, stable or deprecated; it is distinct from proof of correctness. Use `stale_after` only when there is a meaningful review deadline, not an arbitrary expiry for every paper. New writing does not make its sources current. Reconcile old verification with changed claims rather than presenting historical approval as current approval.

We do not use OKF's optional attested-computation execution machinery for ordinary wiki upkeep. An experiment page links to actual configs/results; it does not launch or rerun a job.
