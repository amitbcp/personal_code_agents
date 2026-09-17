# ML experiments and ablations

Use this for an experimental campaign, not every small hypothesis question. Reuse the project's run format and existing compute authorization.

## Match the experiment to the claim

Define the effect being estimated: algorithm quality under fixed resources, best achievable quality under a tuning budget, component contribution, robustness, or operating cost. These require different comparisons.

| Claim | Informative comparison | Common confound |
|---|---|---|
| Reranker orders better | Same query/candidate lists and judgments | More candidates or gold insertion |
| RAG component helps | Fixed retrieval context or separately measured retrieval changes | Judge preference, context budget, answer leakage |
| Spot-difference model finds changes | Grouped image pairs, change/no-change slices and appropriate grounding measure | Near-duplicate pairs, source leakage, caption fluency |
| Module explains improvement | Matched removal/replacement plus justified training protocol | Parameter count, compute, tuning effort, incompatible removed module |
| Method is faster | Same quality target, hardware/allocation, batch/concurrency and warmup | Different workloads, caches, precision or hidden preprocessing |

A one-component removal measures a conditional effect in the chosen system, not a universal mechanism. When interaction is the claim, use a small factorial comparison or explicitly test the interaction; one-factor-at-a-time results can miss it. Distinguish inference-time removal from retraining without a component. State whether each baseline gets comparable tuning and compute; report both fixed-budget and tuned comparisons only when they answer the question.

## Separate development from confirmation

Freeze data groups, metrics, baseline versions, selection rule, exclusions, budget and stopping criteria before the target outcomes. Use development results for exploratory sweeps and ablations. Choose paired analysis where systems share evaluation units; resample at the independent group level. Plan seeds or resamples in proportion to variance and claim strength, rather than prescribing a universal count. Report effect sizes and uncertainty; correct for or disclose multiple comparisons and post-hoc selection.

Keep a held-out final evaluation untouched by prompt, checkpoint, threshold or hypothesis selection. Repeatedly choosing the best variant on a set makes that set development data regardless of its filename. If the holdout was already used, label findings exploratory and plan fresh confirmation instead of calling it held out. A benchmark may permit a predeclared comparison of multiple systems; preserve its protocol rather than turning every measurement into another tuning step.

## Keep runs interpretable

Record configuration, code/data/model versions, prompt/decoder settings, allocation, metrics, uncertainty, resource use, status and selection decisions for every run, including failures and null results. Preserve artifacts needed to understand rejected experiments. Do not use destructive resets or untracked-only ledgers as the sole record of a research campaign.

Distinguish smoke tests from scientific results. A tiny fixture can expose plumbing errors but cannot establish generalization or speed at scale. An LLM judge needs human calibration, disagreement/error slices and versioned prompts; rerun inference after a system change before grading its output.

Honor the task's worker/resource limits. When planning is requested, produce the plan without launching training. For execution, use finite authorized experiments and project resource checks. Do not kill a healthy run because an arbitrary file count, output count or guessed duration was exceeded. Investigate lack of progress and report resource evidence; request additional authorization only where the active scope actually requires it.

## Handoff

Summarize what was tested, what the evidence supports, what remains inconclusive, deviations, and the cheapest next discriminating test. Do not optimize the paper's story by dropping inconvenient runs.
