# Evidence-led manuscript revision

## Contribution and structure

State what the work establishes, under which conditions, and why that finding matters. Use the strongest supported claim, not the strongest sounding claim. An informative negative result, careful evaluation, or useful extension can be a contribution without pretending to introduce a new method.

For each experiment, make its question explicit and explain what alternative explanation it tests. Keep competing explanations and failures visible. Compare against fair, appropriately tuned baselines and distinguish a controlled ablation from a change to several components at once.

An abstract usually needs the problem, method or insight, evidence, and conclusion within the actual venue limit. Include numbers only when they are traceable and representative. Adapt the introduction and section order to the manuscript; fixed sentence formulas and page budgets are optional editing aids, not requirements.

Organize related work by the scientific distinction that matters to the contribution. Compare the closest approaches accurately, including strengths. Avoid citation padding and unsupported claims of being first or state of the art.

## Clarity without changing meaning

Give each paragraph one purpose. Introduce context before unfamiliar notation, define symbols at first use, and keep terminology consistent. Prefer concrete verbs and explicit measurements over vague claims of improved performance. Preserve necessary uncertainty and causal qualifications.

A result table should identify the dataset/split, metric direction, baseline, aggregation, and uncertainty method. Distinguish percentage points from relative percentage change. Do not average incompatible metrics or present selected best runs as typical performance.

For mathematical claims, state assumptions and domains. Separate theorem, intuition, proof sketch, and empirical observation. Check that changed notation stays consistent across equations, captions, and implementation descriptions.

## Figures and captions

Use the project's plotting pipeline so figures remain reproducible from recorded results. Label units, sample sizes, splits, and uncertainty. Keep scales and visual encodings comparable across methods. Explain what a shaded band represents.

Captions should explain the question, setup, and main observation without overstating it. Show failure cases or qualitative examples with selection criteria when selection could bias interpretation. For spotdiff, preserve image ordering, annotations, and the actual paired example; do not synthesize an image and present it as experimental evidence.

Inspect figures at the size they appear in the compiled document. Use readable labels and redundant line/marker distinctions for accessibility. Follow the venue's actual figure requirements rather than generic resolution or font rules.

## Reviewer response

Group comments by reviewer/question or the project's established convention. Answer the central concern directly, cite the exact evidence or revised location, and acknowledge valid limitations. Respectfully explain why a requested experiment would test a different question when appropriate. Keep completed changes, planned changes, and unresolved disagreements distinct.
