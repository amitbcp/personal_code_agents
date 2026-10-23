# Research & Engineering Practices

**Applies to:** Experiments, evaluations, benchmarks, model or prompt changes, data pipelines that feed research, code/paper/design reviews, and reports.
**Context:** Outputs are judged on rigor, reproducibility, and clarity for both technical and leadership audiences.

## 1. Experimental Rigor
*   **Define Success First:** State the hypothesis and the success criterion before running anything. Explicitly define the metric, dataset, threshold, and what result would make us abandon the idea.
*   **Mandatory Baselines:** Run the baselines first. Include trivial baselines such as the majority class, retrieval-only, or the previous system. A method without a baseline is not a result.
*   **Isolate Variables:** Change one thing at a time. Every claim about a component requires an ablation.
*   **Quantify Variance:** Quantify variance when it matters by using multiple seeds or resamples. Report the mean with a spread (std or CI). Do not claim differences that fall inside the noise.
*   **Strict Data Hygiene:** Keep evaluation honest. Held-out test data is touched exactly once, at the very end. No tuning, prompt iteration, or few-shot example selection may occur on the test set. Always check for contamination between training/prompt data and evaluation data.
*   **Trust But Verify:** Sanity-check inputs before trusting outputs. Inspect data statistics, label distributions, a handful of examples by hand, and a known-answer case.
*   **Record Everything:** Record every run, including negative results. Log the config, code commit, data version and hash, model and prompt version, hardware, wall time, and cost.

## 2. LLM-Specific Workflows
*   **Treat Prompts as Code:** Pin the model version and decoding parameters. Prompts must be versioned, diffed, and reviewed.
*   **Cache Aggressively:** Cache responses keyed by `(model, prompt version, input)`. This ensures reruns are cheap and as deterministic as the provider allows.
*   **Validate Judges:** LLM-as-judge is a measurement instrument. Validate it against human labels on a sample and report agreement before relying on it.
*   **Cost-Aware Metrics:** Report cost and latency alongside quality. A one-point gain at five times the cost is a product decision, not an automatic win.

## 3. Engineering for Research Code
*   **Config-Driven:** Enforce one config file per run. No code edits are allowed between runs of the same experiment.
*   **Deterministic Pipelines:** Ensure deterministic, versioned data pipelines with hashed inputs, idempotent stages, and resumable runs.
*   **Graduation Rule:** Exploration lives in notebooks; anything run twice becomes a script or module with a documented invocation.
*   **Test Silent Failures:** Write tests specifically for code that can silently invalidate results, such as data transforms, metric implementations, evaluation harnesses, and prompt templating.
*   **Incremental Optimization:** Keep changes small and reviewable. Split large optimizations into a sequence: measurement first, then each change with its own before/after numbers.

## 4. Reviewing (Code & Papers)
*   **Code Review Triage:** Lead with the most consequential issue. Explicitly separate blocking from non-blocking feedback.
*   **Verify, Don't Vibe:** Run the code, read the diff, and check the numbers. Watch for common silent failures: data leakage, wrong metric implementation, statistical claims the data cannot support, unreproducible setups, performance claims without a baseline, and scope creep.
*   **Actionable Feedback:** Be specific. Provide the file, line, exact wording, and the smallest fix that resolves the issue.
*   **Enforce Size Limits:** Prefer changes under roughly 800 changed lines, and under 500 for complex logic. Ask the author to split the work into reviewable stages when size hides substance.
*   **Paper Reviews:** Provide a two-sentence summary in your own words. List strengths and weaknesses ordered by severity, backed by evidence from the paper. Include questions the rebuttal can answer, and a clear score rationale. Keep it concise, direct, and human-sounding with no boilerplate.

## 5. Reporting
*   **Top-Down Structure:** State the outcome first: what changed, what was learned, and what decision is needed. Follow this with evidence, then details.
*   **Contextualized Numbers:** Numbers must come with baselines, uncertainty, and the conditions they were measured under. A results table always beats prose.
*   **Separate Fact from Fiction:** Clearly separate facts, interpretations, and recommendations. Explicitly state limitations and what was not tested.
*   **Audience-Specific Formatting:**
    *   **Leadership Status:** Limit to three to five lines covering the status against the milestone, risks, decisions or resources needed, and the next milestone.
    *   **Technical Report:** Must include the setup, a results table, analysis, limitations, and exact reproduction pointers (config, commit, command).
*   **Decision Log:** Keep a decision log containing the date, the decision made, alternatives considered, and the owner.

## 6. Leading & Delegating
*   **Define Boundaries:** Define success metrics and non-goals at the start of a product or research effort. Write them down where the work lives.
*   **Timebox POCs:** Timebox proofs of concept with explicit go/no-go criteria. Carry what is understood into the delivery path and record the production gaps.
*   **Risk Tracking:** Track risks and unknowns explicitly. Assign each an owner and a resolution date.
*   **Delegation Briefs:** Whether delegating to people or agents, provide the objective, constraints, acceptance criteria, deadline, and where to record results. Review the result against the acceptance criteria, not the effort expended.
*   **Async First:** Prefer written proposals with async feedback over meetings. Reserve meetings strictly for decisions that require discussion.