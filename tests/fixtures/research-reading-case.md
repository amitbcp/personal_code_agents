# Synthetic research fixture

These are invented mini-papers for a local behavior check, not real publications. No external search, training or publishing is needed.

## Paper P, version 1 — “ContextGate for Reranking”

Identifier: fixture:P:v1. Section 2: score(q,d) = b(q,d) + alpha * h(q,d). b and h are real-valued scalar scores; alpha is a scalar. The paper does not constrain alpha to be positive. Table 1 reports nDCG@10=0.71 for ContextGate and0.67 for Baseline B on corpus C's query set Q, reranking the same100 candidates per query. The candidate lists were augmented to contain known relevant documents. Four alpha values were tried on Q and the best was reported. Q contains60 queries derived from6 source documents. No uncertainty is reported.

## Paper P, version 2 — “ContextGate for Reranking”

Identifier: fixture:P:v2. Section 3 says this supersedes version1's main table after a candidate-generation correction. Table 1 reports0.64 for ContextGate and0.65 for Baseline B on the same Q, using genuine retriever top100 candidates. The paper says results are exploratory because Q influenced alpha selection. Appendix A is listed but unavailable in this fixture. The abstract still says “ContextGate consistently improves ranking.”

## Paper R — “Larger Candidate Sets for Retrieval”

Identifier: fixture:R:v1. Table 2 reports nDCG@10=0.74 using1000 candidates on a different corpus D, with binary judgments. P used graded judgments. R's abstract says its method is broadly competitive. The fixture supplies only this abstract and table caption, not the methods or uncertainty.

## Search record

On2026-09-16, fixture search endpoint S returned P:v1,P:v2,R:v1 for query “reranking context gate”. Retrieval stopped at the first page of3results; additional pages were not fetched. A second query for contrary results failed with a timeout. No other databases were queried.

## Existing personal note

User annotation: “I suspect alpha learns whether the context is reliable. Need to understand why.” Preserve this as a question from the learner.

Existing concept record: “ContextGate improves ranking”, citing P:v1 Table1. Its last-reviewed version isv1. There are no source-backed links to R yet.

## Requested task

Using the three research skills, write a brief survey from the supplied sources, explain the scoring rule to a learner (including a numeric example), and update the supplied concept note into a small source-linked map. Include an optional self-check with a separate answer. Recommend the next experiment and how to describe the findings in an author-side draft. Save outputs only in the evaluator's designated directory. Do not fabricate additional sources or learner responses.
