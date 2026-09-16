# Orchestra applicability review and paper-writing adaptation

Reviewed 2026-09-16. Source: `<source-checkouts>/Orchestra-Research--AI-Research-SKILLs`, revision `773a52944ba4747a18bd4ae9ade53fff041adcbc`; source checkout remains clean. No upstream scripts, installers, model downloads, builds, or services were executed.

## Outcome and exact coverage

The applicability catalog covers **98 skills: 3 include/adapt, 86 defer, 9 exclude unchanged**. Every entrypoint has its own path, decision, reason, dependencies, and review status in `orchestra.csv`.

**69 entrypoints received complete semantic reads; 29 are explicitly scope-only decisions and were not semantically read.** Those 29 are unselected robotics, cloud provisioning, agent/safety/interpretability frameworks, specialized RL, and alternative distributed/engine stacks. Their exact paths and reasons are preserved in the CSV and `orchestra-progress.json`. This completes the scoped selection catalog under the coordinator's scope-only allowance; it does **not** satisfy or claim a full semantic read of all 98 entrypoints. Future full-read continuation must use `scope_only_skill_paths`, not infer completion from decision coverage.

All **529 tracked files (24,593,146 bytes)** received a full-byte inventory/static scan: **506 UTF-8 text files and 23 binary assets**. Static scanning classified scripts/configuration, dependency/action patterns, relative links, and Python code-fence syntax without execution. **21 supporting files received direct complete semantic reads**, including installer/CLI paths, license/package/workflows, FAISS's sole reference, and all five ML-paper references plus its template overview. Oversized reference dumps were scanned in full, not semantically read line by line. Binary PDFs/images/audio were classified only, not rendered. `orchestra-files.csv` preserves these distinct statuses. The final adapted paper package contains only five directly inspected text files.

## Strongest candidates

1. **ML paper writing — selected and adapted.** Strong fit for research manuscripts, IR/reranking, agentic RAG, and spotdiff/media studies. The adapted package keeps evidence-to-claim mapping, verified citations, reproducibility, honest limits, and current venue checks. It removes compulsory confirmation, tool/provider assumptions, stale rules, broken citation automation, and bundled dated templates.
2. **Brainstorming research ideas — optional adaptation candidate.** Full entrypoint read; no support files. Useful rival hypotheses, failure probes, fair simple baselines, and bounded feasibility work. Existing selected hypothesis-generation skill overlaps; do not install both by default.
3. **FAISS — conditional reference candidate.** Full entrypoint and sole reference read. Useful exact-search baselines, normalization, and ANN recall/latency comparisons. Remove fixed quality/scale promises and unsafe deserialization examples before reuse; use only when FAISS is actually in the project.

`include` means an adaptation candidate, not approval to install unchanged. Systems-paper writing, FSDP2, NeMo evaluator, and serving tools remain conditional deferred options; their full support corpora were not deeply reviewed. Generic CLIP/VLM benchmarks do not validate paired-image change detection. No new vector database, agent runtime, tracker, cloud platform, or distributed trainer is justified merely by catalog availability.

## Consequential source findings

- **Installer ownership checks are insufficient.** `packages/ai-research-skills/src/installer.js` recursively removes existing same-named destinations before symlinking/copying, without verifying ownership. `uninstallAllSkills` removes all symlinks in selected skill directories without checking their targets. A shared fixed temporary clone also lacks concurrency isolation. Do not use this installer/uninstaller on existing profiles.
- Installer metadata records a constant version rather than source revision; `agents.js` hardcodes home `.codex/skills` and ignores custom CODEX_HOME. Category enumeration omits category 22, and the two-digit sync regex misses `0-autoresearch-skill`. Deployment must use actual host/profile discovery and preserve manual CBM indexing and node-local live databases/caches.
- **Autoresearch is excluded unchanged:** mandatory scheduling, never-stop scope expansion, broad compute use, and unsolicited external messaging exceed ordinary task authorization. Its useful protocol/negative-result ideas overlap local research guidance.
- **Training correctness:** knowledge-distillation labels teacher cross-entropy as reverse KL and reverses mode-covering/seeking explanations; causal logits and soft-loss masks are mishandled. Model-pruning overwrites calibration stats, retains a sequence dimension incompatible with weight masking, assumes dense zeros reduce storage/activate sparse kernels, and subtracts result dictionaries. These are exclusions of the recipes, not certifications of the algorithms.
- **Memory and scale:** PEFT/bitsandbytes claims of 70B at 4 bits in 24GB contradict the 35GB raw-weight minimum before overhead. Serving examples materialize entire corpora; this does not become bounded simply because engine GPU batching is automatic. TorchTitan's Slurm example launches eight tasks each spawning eight processes. Runtime claims require real configuration and workload measurements.
- **RAG/evaluation:** substring matching is presented as correctness in tracker examples; schema validity and judge pass flags do not establish factual correctness. CLIP uses a shared softmax over independent questions. Corpus deduplication and multimodal examples do not specify pair/group-preserving splits. Calibration, held-out task metrics, and operational budgets require explicit project design.
- **Paper reference defects corrected in adaptation:** citation automation selects first search result, continues after failed verification, caches it as verified, uses keyword containment as claim checking, and can overwrite the bibliography. Source references contain dated venue rules, unsupported statistics, and rhetoric encouraging disguise of incremental work. The revised package requires authoritative identity checks and direct claim-support reading while preserving uncertainty.

## Owned adaptation and validation

Destination: `<collection-checkout>/skills/ml-paper-writing`, compared with imported baseline `fcf3ff0`.

- Replaced the 984-line entrypoint with a concise model-neutral workflow and three focused references covering writing, citations, and handoff checks.
- Preserves the existing manuscript, bibliography/build system, project instructions, authorized drafting, and experiment development/test separation. Adds concrete IR candidate/rerank, agentic RAG judge, and paired-image/spotdiff reporting distinctions.
- Removed the copied template directory and redundant reviewer/source reference catalogs; their upstream baseline remains in Git. The package obtains exact current venue instructions/templates only when a real venue task needs them.
- Preserved the repository-level Orchestra MIT notice and copied it into the portable skill package. No third-party style/template assets remain in the adapted package.
- `git diff --check -- skills/ml-paper-writing` passed. All retained relative Markdown links resolve. Manual instruction review covered authorized edit, missing citation, conflicting evidence, venue preparation, and spotdiff-result scenarios; no new experiments, external publication, or compulsory approval is implied. No model-behavior or manuscript-render test was run.
- Skill Creator `quick_validate.py` passed using an existing Python environment with PyYAML. System and bundled Python lacked PyYAML; no dependency installation was needed.

Only the owned paper package and Orchestra review files were changed; no commit, push, or active-profile installation was made.

## License and limits

Root LICENSE is MIT, copyright 2025 Claude AI Research Skills Contributors. Nested npm package declares MIT while root package.json declares ISC; preserve original notices and provenance. Bundled third-party template/style notices were not comprehensively legally audited; those assets were removed from the adapted package.

This is a static applicability review, not an algorithm/security certification or runtime benchmark. API compatibility, remote links, venue rules, prices, model availability, and performance assertions were not externally verified. Code-fence syntax diagnostics include deliberate pseudocode and require triage. A deferred framework may be appropriate for a future explicit task; its scope-only row is not a quality judgment.
