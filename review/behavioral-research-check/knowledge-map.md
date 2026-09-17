# ContextGate knowledge map

Index: [survey, mechanism and plan](research-notes.md); [separate exercise answer](self-check-answer.md); [supplied source fixture](../../tests/fixtures/research-reading-case.md).

## Source records

- `fixture:P:v1` — ContextGate for Reranking, v1. Section 2 equation and Table 1 excerpt available. Historical main table superseded.
- `fixture:P:v2` — same study lineage, v2. Section 3, Table 1 and abstract excerpt available; Appendix A unavailable. Current main-table version.
- `fixture:R:v1` — Larger Candidate Sets for Retrieval. Abstract and Table 2 caption only. No source-backed connection to P supplied.

All IDs resolve to the corresponding headings in the linked fixture. These are synthetic local records, not verified external publications.

## Concept record C1: additive context scoring

**History retained:** “ContextGate improves ranking”, citing P:v1 Table1; last reviewed against v1. This earlier broad concept claim is superseded as a current conclusion, not deleted as history.

**Updated claim:** P:v1 reported a selected gain with augmented candidates; P:v2's corrected genuine-pool result is −.01 nDCG@10 versus B and remains exploratory. Neither consistent improvement nor general inferiority is established. Last reviewed 2026-09-16 against supplied P:v2 evidence. The additive rule is documented in v1 Section 2; no further mechanism is inferred from the title “gate.”

| From | Relation | To | Source/location | Conditions/version | Evidence status |
|---|---|---|---|---|---|
| fixture:P:v1 | defines | additive score C1 | P:v1 Section 2 | real scalar b,h,alpha; alpha sign unrestricted | source-backed definition |
| fixture:P:v1 Table1 | reports gain under conditions | C1 performance claim | P:v1 Table1 | gold-augmented top100, selected alpha on Q | historical exploratory result; superseded |
| fixture:P:v2 Table1 | supersedes | fixture:P:v1 Table1 | P:v2 Section3 | candidate-generation correction | explicit source-backed version relation |
| fixture:P:v2 Table1 | does not support under conditions | consistent improvement claim | P:v2 Table1 and abstract | genuine top100; .64 versus .65 on selected-on Q | source-backed point estimates; no uncertainty |
| fixture:R:v1 | reports | .74 nDCG@10 | R:v1 Table2 caption | corpus D,1000 candidates,binary labels | partial-source result; comparability unresolved |
| learner question Q1 | asks whether | alpha captures context reliability | user annotation in fixture | no specified learner answer | personal question, not empirical edge |
| experiment proposal E1 | would test | useful fixed-pool contribution of h | plan in research-notes.md | fresh source groups; matched candidates | generated proposal, unperformed |

There is no P→R *extends*, *supports* or *contradicts* edge: no citation or comparable experiment establishes one. Candidate-budget differences are a generated comparison note, not a scientific relationship asserted by either source. Appendix A's absence is an access gap, not retraction or negative evidence.

## Personal annotation preserved verbatim

“I suspect alpha learns whether the context is reliable. Need to understand why.”

## Change record — 2026-09-16

Affected records: existing improvement concept C1; P source-version lineage; new partial R source record; preserved learner question Q1. Retained the original claim and locator, qualified current conclusion using v2, recorded the abstract/table tension and missing appendix, and added only supported typed relationships. No original source or user annotation was overwritten, no database/index rebuilt and no background memory process created. Files are confined to the designated evaluator directory.
