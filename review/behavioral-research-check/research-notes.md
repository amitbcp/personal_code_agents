# ContextGate: bounded survey and learning note

This is a local exercise using invented sources, not a real literature review. Only the supplied excerpts were read. Source: [fixture](../../tests/fixtures/research-reading-case.md).

## Survey conclusion

The corrected experiment does **not establish an improvement** from ContextGate: P:v2 Table 1 reports 0.64 versus 0.65 for Baseline B. P:v1's earlier 0.71 versus 0.67 result was superseded after correcting candidate generation. The unchanged abstract claim of consistent improvement conflicts with the corrected table. Neither table provides uncertainty, and Q influenced alpha selection, so these are exploratory observations, not confirmation of superiority or inferiority.

### Evidence matrix

| Source | Available evidence and setup | Result | Interpretation and limitations |
|---|---|---|---|
| fixture:P:v1, Section 2 and Table 1 | Corpus C, 60 queries from 6 source documents; same 100 candidates per query for both rerankers, augmented with known relevant documents; best of four alpha values on Q | ContextGate .71, B .67 nDCG@10; difference +.04 | Historical selected result under augmented candidates, superseded. Gold insertion changes retrieval coverage; selection on Q and dependent queries limit inference. No uncertainty. |
| fixture:P:v2, Section 3 and Table 1 | Same Q, genuine retriever top100; graded judgments; Q influenced selection | ContextGate .64, B .65; difference −.01 | Current table supersedes v1; does not substantiate abstract's consistent-improvement claim. Appendix A unavailable; other implementation details unknown. |
| fixture:R:v1, abstract and Table 2 caption only | Different corpus D; 1000 candidates; binary judgments; methods unavailable | .74 nDCG@10 | Cannot rank against P: corpus, candidate budget and judgments differ. Comparator, split, uncertainty and detailed method unavailable. “Broadly competitive” is an author claim, not independently established here. |

P's two versions are one study lineage, not independent studies. The numeric deltas are arithmetic differences, not significance tests. Six source groups cannot be treated as 60 independent replicates. R is retained as an adjacent candidate-budget lead, not comparable effectiveness evidence.

### Search and screening record

- Question: Does the added context score improve reranking under genuine, fixed candidate pools, and what evidence explains its role?
- Scope: brief narrative survey of supplied synthetic records as of 2026-09-16; no publication-date filter or other filters supplied. No new search performed.
- Endpoint S query `reranking context gate`: first page only, 3 records (P:v1, P:v2, R:v1); remaining pages not fetched. Deduplicate P versions while preserving both evidence states.
- A second contrary-results query timed out; its exact query text was not supplied. It supplies no evidence of absence. No other databases or citation searches were performed.
- Include P as direct reranking evidence and R as an adjacent comparison with restricted assessment. No records excluded. Appendix A and R's full methods are unavailable here.
- Coverage remains incomplete. No systematic-review, exhaustive search or novelty claim is justified. A future search could include context-score aliases, fixed-pool reranking, candidate recall and contrary results, plus citation tracing; that work has not occurred.

## Explain the scoring rule

P:v1 Section 2 defines `score(q,d) = b(q,d) + alpha * h(q,d)`. For one query-document pair, b and h are real-valued scalar scores; alpha is a scalar multiplier. q and d identify the query and document, but their representation shapes are unspecified. Scores have no supplied physical units; alpha must put the h contribution on a compatible score scale. No probability or positive-alpha constraint is stated. The fixture does not specify how alpha is learned or selected beyond trying four values on Q, nor that this rule changed in v2.

**Invented illustration, not a paper result:** for a single query, document A has b=.6 and h=.4; document B has b=.7 and h=.1.

| alpha | A score | B score | Ordering |
|---|---:|---:|---|
| 0 | .6 | .7 | B above A: baseline recovered |
| .5 | .8 | .75 | A above B |
| −.5 | .4 | .65 | B above A; positive h subtracts from score |

The pairwise difference is `score(A)−score(B)=−.1+.3*alpha`. A overtakes B only when alpha>1/3; equality ties. This shows a tunable additive contribution. It does not show that alpha senses reliability per query: a single scalar need not vary with the query, and the definition of h is absent. Reliability-aware behavior might reside in h, in an unspecified adaptive alpha, or nowhere; these remain questions.

**Preserved learner annotation:** “I suspect alpha learns whether the context is reliable. Need to understand why.” This is a learner question, not a demonstrated mechanism or an answered comprehension test.

### Optional self-check

Using the same A and B values, what happens at alpha=1/3? If h is the same constant for every candidate of one query, can adding alpha*h change the within-query order?

Answer separately: [self-check answer](self-check-answer.md). No learner response or mastery is inferred.

## Next experiment: fixed-pool confirmation and mechanism probe

Cheapest first step: verify on development data that alpha=0 reproduces B's scores/order and that both systems receive identical genuine candidate IDs and graded judgments. Audit for gold insertion and document-group overlap. This is a proposed check, not an executed experiment.

| Candidate explanation | Rival | Predicted contrast and falsifier | Control and analysis |
|---|---|---|---|
| h supplies useful ranking signal | v1 gain came from augmented candidates and selection | Frozen ContextGate outperforms B on fresh genuine pools; failure to exceed a predeclared practical threshold challenges useful gain in that setting | Same top100/query, judgments and query population; alpha=0 baseline; matched selection budgets. Paired query differences summarized with source-document-aware uncertainty. |
| h captures reliable context | generic score shift or unrelated correlation | Relevant-context h outperforms shuffled/mismatched-context h, especially in independently labeled reliability slices; no such contrast challenges this account | Small development-only factorial: original versus degraded context crossed with h active versus alpha=0. Keep candidate IDs fixed; do not use relevance labels to create favored candidates. Freeze corruption and slice rules before observing comparisons. Interaction is evidence about this intervention, not proof alpha learns reliability. |

Q is development data because it influenced selection. Obtain new source-document groups for confirmation; do not relabel Q as held out. Use enough independent groups to target the desired precision; the fixture cannot determine sample size or a meaningful practical threshold. Specify that threshold from application costs before new outcomes, then freeze the primary contrast, grouping/weighting, exclusions, tuning budget, stopping rule and uncertainty procedure. Report both query-weighted metric and group-sensitive uncertainty with the aggregation rule explicit. A small number of groups may make intervals unstable.

Record all four historical choices where available, all new runs including nulls/failures, data/candidate/model/code versions, seeds, allocation, wall time and latency. Final confirmation is one frozen evaluation after development, with no post-test alpha selection. If the lower uncertainty bound exceeds the predeclared worthwhile gain, support a bounded improvement claim; a bound ruling out that gain challenges the practical hypothesis; otherwise remain inconclusive. No training, retrieval or final evaluation was launched.

## Author-side draft

“Our initial exploratory evaluation on corpus C reported nDCG@10 of 0.71 for ContextGate and 0.67 for Baseline B on candidate lists augmented with known relevant documents (fixture:P:v1, Table 1). After correcting candidate generation to genuine retriever top100 lists, the revised results were 0.64 and 0.65, respectively (fixture:P:v2, Section 3 and Table 1). These corrected results supersede the earlier table and do not support a claim of consistent improvement. Q comprised 60 queries derived from six source documents and influenced alpha selection; uncertainty was not reported. Independent group-held-out confirmation and context perturbation experiments remain planned.”

Replace the abstract's improvement claim with “We study an additive context score for reranking; corrected exploratory results do not establish a benefit over the baseline.” Do not claim significance, causal reliability gating, reproduction, or competitiveness against R from these excerpts. These fixture identifiers are local source locators, not real bibliographic records. Authors, venues, dates and DOI metadata are unspecified; no fabricated bibliography or venue compliance claim is made.
