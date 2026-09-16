# K-Dense applicability review and selected adaptations

Reviewed revision `330c8e764435a731eff571e3efdda70b363d0792` of [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792). Review date: 2026-09-16. Selection targets ML/IR/reranking, agentic RAG, multimodal media, papers and high-volume pipelines on Mac and SSH/Enroot.

## Recommendation

1. **get-available-resources**: include adapted. Its incremental value is bounded local collection that distinguishes host, affinity, cgroup and scheduler resources, plus explicit unknown accelerator usability.
2. **hypothesis-generation**: include adapted. Use rival predictions and falsifiers with the existing research guidance; structured validators are optional for formal records.
3. **optimize-for-gpu**: optional later for frequent NVIDIA pipeline/ANN porting. Good CPU correctness, recall and synchronized end-to-end benchmark discipline; not a Mac GPU recipe.
4. **paper-lookup**: optional later for scholarly API routing/pagination. Existing browsing plus the selected paper-writing skill may suffice.

The CSV's four `include` entries mean strong upstream candidates, not a request to install all four. Only the first two were assigned for adaptation.

## Exact coverage and limitations

- Every one of 166 skill packages has a decision, path, rationale, dependencies and risks in `kdense.csv`.
- Every one of 2,484 tracked files was classified: 2,313 UTF-8 text files (27,934,705 bytes) mechanically scanned in full; 171 binary assets (169 PNG, 2 GIF) classified, not decoded or executed. All 692 Python sources parsed with AST successfully. Inventory: `kdense-files.csv`; matching lines: `kdense-signals.jsonl`; scope: `kdense-static-summary.json`.
- All skill descriptions/dependency declarations received applicability triage. **44 full entrypoints received direct semantic reading**; their CSV status identifies them. Repeated identical citation boilerplate was reviewed once. Excluded domain packages are applicability exclusions, not security certifications.
- All 38 deferred and four included candidates received full entrypoint semantic reading; two additional fully read entries are excluded. The other 122 packages are explicitly scope-based applicability exclusions, using their full descriptions/dependencies and whole-package static scan. No decision is pending. This is a completed applicability selection review, not a semantic security audit of every supporting file or domain algorithm.
- Both retained packages' entire 13 Python supporting scripts were read semantically: five resource scripts and eight hypothesis scripts, including input/output helpers. References/assets were mechanically scanned; selected instructions and schema templates were inspected, but not all reference prose fully semantically read.
- Root README installation guidance, plugin manifest, pyproject, license, and relevant CI packaging/test workflows inspected. Upstream scanners/report inspected as evidence; never executed. No external API/provider calls or package installations performed for this review.
- No Astra-specific comparative evaluation found. Codex-compatible Markdown is not evidence of Astra quality. No Enroot deployment test or Linux accelerator execution performed.

## Material findings

- Resource planner can return one suggested worker with `MEMORY_REQUIREMENT_EXCEEDS_BUDGET`; that is not a feasible launch plan. Adapted entrypoint makes this explicit. Detection is read-only; timeout cleanup kills only its own probe subprocess, never healthy workload jobs.
- Resource detector supports cgroup v2 and Slurm observations, but does not specifically identify Enroot. Run inside the actual allocation/container; inspect quota/namespace limitations. Apple CPU/GPU memory is shared, not additive.
- Hypothesis formal schemas retain strict controls and domain gate declarations. Making them optional avoids requiring biomedical checklists for every ML experiment. Causal-language lint is lexical and can flag normal “improves” benchmark prose; advisory only.
- LiteParse recursive batch wrapper flattens output to basename stem, allowing same-name files in different directories/extensions to overwrite. Fix collision handling before corpus use. Default OCR concurrency also needs actual allocation bounds.
- Polars example has multiple unaliased expressions with the same output name. Correct examples before using as a production recipe.
- Arbor repeatedly feeds test results into selection; adapt to train/dev/validation plus one untouched final test. Claude Agent/worktree assumptions need translation.
- Exa includes an integration tracking header mandate; literature/research/image skills frequently mandate particular external providers. Broad search/artifact triggers duplicate existing installed capabilities.
- Root MIT license does not govern every vendored package identically: docx/pdf/pptx/xlsx have Anthropic-specific license files. Plugin/pyproject version 2.69.0 differs from README badge 2.68.0. Repository Python >=3.13 tooling requirement is not a requirement for every skill.
- Upstream security report is a mix of fresh and reused scans, not an independent certification. Heuristic credential/network findings include legitimate API examples; do not label them confirmed exfiltration without evidence.

## Adaptation performed

Destination: `<collection-checkout>`. Changed only `skills/get-available-resources/SKILL.md` and `skills/hypothesis-generation/SKILL.md`; scripts/assets/references retained unchanged after checking script imports and entrypoint call links. No deletion was justified by a demonstrated dependency-free removal benefit. No commit or push performed by this agent.

- Hypothesis entrypoint shortened to an ML experiment procedure: fixed candidate lists for reranking ablation, grouped/paired experimental units, evidence boundaries, rival predictions, falsifiers, untouched final test, explicit negative/indeterminate results. Ordinary authorized analysis proceeds without a new human-review gate. Real domain/data authorization requirements remain conditional and intact.
- Resource entrypoint keeps input/output privacy and bounded probe safeguards. Adds advisory-only planning, infeasible-memory warning interpretation, no healthy-job termination, no automatic indexing, exact remote/container context, node-local DB/cache/spill policy and NFS limitations.
- Removed forced promotional manuscript citations; retained provenance and MIT notices. Moved unsupported `compatibility` frontmatter into body for the current skill validator.
- Scope diff: 2 entrypoints, 46 insertions and 272 deletions at time of review. Parent may perform additional integration edits.

## Verification actually run

`python -B <source-checkouts>/reviews/kdense_smoke.py`

All **12 smoke checks passed**, recorded in `kdense-smoke-results.json`: five known-template hypothesis validators, malformed schema rejection, causal-lint detection, actual local Mac resource detection with accelerator probes skipped, valid snapshot acceptance, nonexecuting accelerator diagnostics, oversized worker-memory warning, malformed snapshot rejection. The first attempt used a memory CLI value above the allowed parser range; corrected to the supported upper bound and reran successfully. This was a test-input correction, not a code fix.

Earlier detector private-file smoke and snapshot validation also succeeded (`kdense-resource-smoke.json`). Tests are bounded local checks, not accuracy validation of scientific claims, preregistration submission, all-platform tests or performance benchmarks. Parent owns integrated skill/frontmatter validation.

## Completed applicability follow-up

Fully read 17 more entrypoints: exploratory-data-analysis, matplotlib, networkx, pymc, pymoo, scientific-visualization, scikit-learn, seaborn, shap, statsmodels, sympy, torch-geometric, umap-learn, uncertainty-and-units, scholar-evaluation, markdown-mermaid-writing, venue-templates. Citation boilerplate reused losslessly from prior review.

Final catalog: 166 decisions = 4 include candidates, 38 defer, 124 exclude. All include/defer entrypoints fully read. The 21 previously deferred scope-only packages were excluded because their named domain workload or separate platform adoption is absent: time-series, GIS, physical flow, RL, MATLAB, external cloud/notebook/literature services, grant/poster work, and alternative data-management systems. Their rows explicitly say applicability exclusion, not full semantic audit.

Additional findings reinforce the existing shortlist: EDA's hard 512 MiB ceiling and reference-only Parquet/Zarr support limit production-corpus applicability; PyMC's divergence advice is internally inconsistent; generic scikit-learn test-performance iteration must use validation data; UMAP's distribution-shift/structure claims require qualification; scholar-evaluation introduces committee gates inappropriate for routine ML review; Mermaid's global formatting mandates overlap existing tools. SHAP's output-space, additivity and non-causal guidance is useful optional reference, not a reason to add a broad trigger. Physical units/metrology is distinct from retrieval confidence intervals.

No additional adaptations or installs recommended or performed after this follow-up. The selected two entrypoints remain unchanged by this review completion.
