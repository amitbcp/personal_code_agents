---
name: literature-survey
description: Build or update a traceable research literature survey, related-work evidence matrix, or bounded novelty search. Use for comparing multiple papers and documenting search coverage; ordinary factual lookup does not require a survey protocol.
---

# Literature Survey

- Produce a synthesis that another researcher can check and extend.
- Reuse the project's bibliography and survey records; keep the procedure proportional to the requested scope.

## Define and preserve the search boundary

- State the research question, relevant task/population, date range, source coverage, and inclusion/exclusion criteria.
- Use existing constraints or state reasonable assumptions; ask only when a missing choice changes the conclusion.
- Distinguish a quick orientation, narrative survey, systematic review, and meta-analysis.
- Do not label a convenience search systematic.

- Record actual queries, source/API, date, filters, pagination or result caps, and inaccessible sources.
- Preserve screening decisions with reasons.
- A timeout or empty API response is not evidence that no papers exist.
- Expand terminology with aliases, older names, adjacent methods, and contrary results.
- Use backward/forward citation searches around relevant seed papers; record this separately from database queries.
- Stop according to the requested scope and disclose residual gaps rather than claiming exhaustiveness.

- Resolve paper identity using verified DOI, arXiv ID/version, proceedings record, or another stable identifier.
- Link preprint and published versions without counting them as independent studies; preserve substantive version differences.
- Search snippets and abstracts support screening, not full methodological assessment.
- Mark abstract-only or unavailable papers explicitly.

## Build an evidence matrix

For each included study, capture only fields relevant to the question:

| Paper/version | Question and method | Data/split/unit | Comparator and budget | Result and uncertainty | Claim support/location | Limitations/status |
|---|---|---|---|---|---|---|

- Read the sections, tables, supplements or code necessary for each claim.
- Attach an exact source location to extracted facts.
- Separate authors' claims, observed results, your interpretation, and untested hypotheses.
- Verify a citation's identity and its support for the specific statement independently.

- Compare like with like.
- Different corpora, candidate pools, label definitions, metrics, evaluation units, data access or compute budgets can invalidate a ranking of reported scores.
- Do not average incompatible results or infer missing denominators.
- A meta-analysis needs a justified estimand, dependence handling and appropriate uncertainty; a spreadsheet of paper scores is insufficient.

- Preserve disagreements and negative results.
- Identify whether a conflict reflects different conditions, measurement, version, or an unresolved scientific difference.
- Citation counts, venue prestige and model agreement do not establish truth.
- Absence from the bounded search supports “not found within this scope,” not a universal novelty claim.

## Deliver and update

- Deliver the synthesis, evidence matrix, verified references, search boundary and unresolved questions.
- For a small request these can be sections of one Markdown file.
- For a growing survey use the existing project layout; create separate query/screening records only when useful.
- Do not impose a bibliography manager, database, or paid API.

- On updates, retain earlier search dates and exclusion reasons, add new records, and explain changed conclusions.
- Do not silently replace historical evidence.
- Public-paper research does not authorize uploading private manuscripts to a new service.
- Follow the user's existing tool and data permissions.

## Design provenance

- Original project procedure informed by the reviewed search/synthesis and evidence-ledger concepts in K-Dense's literature-review and market-research-reports skills.
- No upstream scripts or text are copied.
- See [research workflow and sources](https://github.com/amitbcp/personal_code_agents/blob/main/review/research-workflow.md).
