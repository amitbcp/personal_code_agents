# Repository Guidelines

This repository is an experiment platform for:

1. Benchmarking embedding and reranking models.
2. Training an in-house reranker, including multimodal reranking with `ms-swift`.
3. Preparing, collating, mining, filtering, and synthesizing training/evaluation data.
4. Developing and evaluating new retrieval, reranking, loss, and downstream RAG ideas.

## Initiative and Task Completion

- Carry the user's intended outcome through to verified completion. Treat requests to do or fix something as execution requests; a plan, diagnosis, first patch, or list of next steps is an intermediate result.
- After each finding or completed step, choose and perform the next necessary action within the authorized objective. Include straightforward implied follow-ups, integration, focused checks, and required documentation; do not wait for another prompt to continue the same work.
- Resolve reversible implementation details using current evidence and project conventions. Ask only when missing information materially blocks correctness or an applicable approval is genuinely absent. Reuse authorization already given; do not ask for it again.
- If one operation is blocked, finish independent authorized work and prepare the blocked action for review. Explain the exact blocker and smallest missing decision; if an instruction requires a pause, identify its file and relevant rule.
- Preserve the objective across status questions, findings, delegation, and compaction. Integrate delegated results and continue; a progress report or task handoff does not itself complete the work.
- Keep follow-ups tied to the requested outcome. Respect explicit pauses, ownership, protected areas, and operation-specific approval boundaries. Do not turn this rule into permission for unrelated backlog work, new experiments, spending, publication, destructive actions, or indefinite optimization.
- Before ending, check the requested outcome against actual evidence. Complete remaining in-scope steps when possible; otherwise report what is verified, what remains, and why. Once the outcome is met, stop rather than inventing more work.

## Start Here

Start with the smallest evidence packet that can safely route the work:

1. Confirm the live root is `/mnt/rag/aamita/project/rerank`; treat `/mnt/shared/aamita/project/rerank` as a historical pre-migration path.
2. Inspect concise root and affected nested-repository Git summaries. Preserve unrelated dirty/untracked work; do not dump a large untracked inventory unless it is in scope.
3. For a quick question, orientation, or read-only diagnosis, read only the current-workstream portion of [PROJECT_MEMORY.md](PROJECT_MEMORY.md), the matching row in [changelog/INDEX.md](changelog/INDEX.md), and its open gates in [knowledge/task_gates.md](knowledge/task_gates.md).
4. For a durable change, additionally read the active ledger's current-state/next-action sections and the directly affected source/configuration or primary evidence. Read the full ledger only when unresolved history requires it.
5. For an experiment, data operation, benchmark, training/evaluation run, or other high-risk action, additionally load the one relevant repository skill and follow primary manifests, run metadata, logs, raw eval artifacts, and checkpoints.
6. Before substantive changes, read [knowledge/index.md](knowledge/index.md) and the relevant wiki or task-contribution pages alongside the active routing surfaces; keep the lightweight scope in step 3 for quick read-only questions. Use [research/README.md](research/README.md) when a detailed literature review, public-model watchlist, benchmark-gap analysis, or publication roadmap is material. Use [lineage/SESSION_INDEX.md](lineage/SESSION_INDEX.md) only when prior-session ownership or chronology materially affects the task.
7. Create or update the canonical task plan before implementation or execution. At compaction/final handoff, update one concise current-state checkpoint rather than copying the narrative into several files.

For the consolidated T1/T2 migration context, use [the September 18 restart route](docs/handoffs/2026-09-18-project-wiki-consolidation.md). It is a dated navigation snapshot, not runtime authority; current owning ledgers and primary evidence take precedence. Documentation completion never closes scientific, release, or deployment gates.

If an index is missing or stale, continue from primary evidence and repair the index in the active continuity task; do not silently trust an older synthesis.

## Context and Token Discipline

Use progressive disclosure. Traceability is required; exhaustive rereading is not.

- Default initial orientation budget: at most four files, 400 lines, or 64 KB of tool output combined. Exceed it only when primary evidence requires it, and state why.
- Before opening a file larger than 64 KB, inspect `wc -lc`, headings with `rg -n`, and hashes/mtime; then read only the relevant bounded ranges. Never read a file larger than 100 KB in full by default.
- Cap ordinary command output at roughly 200 lines or 10 KB. For large inventories, return counts, summaries, and the top relevant entries; save full output as a local artifact only when needed.
- Do not reread unchanged files or repeat unchanged command output. Reuse an authenticated hash and inspect the delta or affected symbols.
- Do not put raw logs, giant diffs, full test payloads, or candidate-by-candidate prose in prompts or continuity Markdown. Link to the primary artifact and record its identity plus the decision it supports.
- Keep one logical work package per session when practical. Start a new session from the concise current-state handoff instead of carrying a long unrelated transcript.
- If context growth becomes the work, stop and compact the routing surface before continuing implementation.

## Evidence Hierarchy and Safety

Use this order for task-specific claims:

1. Live source/configuration and primary run/eval/data artifacts.
2. Canonical task ledger with exact command, paths, status, metrics, and verification time.
3. `PROJECT_MEMORY.md` current synthesis.
4. Curated knowledge/lineage pages and generated artifact digest.
5. Raw Codex transcript only when an unresolved historical claim requires it.

Important boundaries:

- Raw per-dataset benchmark JSON outranks a stale or partial `summary.json`.
- `benchmark_report_v2.xlsx`, `team_benchmark_report.md`, and `team_benchmark_report_v2.md` are synthetic goal-target outputs, not measured benchmark evidence.
- Do not copy raw Codex transcripts into Git, QMD, or a shared index. Historical transcripts may contain plaintext credentials.
- Do not index raw logs, datasets, prediction payloads, model/optimizer tensors, caches, notebook binary output, or unallowlisted environment/run fields.
- Local LLM summaries are synthesis aids only. Every promoted claim needs a task or artifact evidence link.

<!-- codebase-memory-mcp:start -->
## Codebase Knowledge Graph

This project uses `codebase-memory-mcp`. Prefer graph tools over grep/glob/file search for code discovery:

1. `search_graph` for functions, classes, routes, and variables.
2. `trace_path` for callers, callees, and data flow.
3. `get_code_snippet` for exact symbol source.
4. `query_graph` for complex relationships.
5. `get_architecture` for high-level structure.

Use graph lookup for indexed documentation sections and ADRs where coverage is verified; read the source directly for missing or changed sections. Fall back to `rg`/file reads for string literals, errors, configs, shell scripts, artifacts, or insufficient graph results. The local [`.cbmignore`](.cbmignore) keeps one combined code-and-documentation graph for this project. Maintained Markdown, guides, changelog, and local instructions are included. Reference clones, linked worktrees, raw datasets, generated results, checkpoints, logs, bulk artifacts, and historical transcript caches remain outside it. Do not remove those boundaries merely to increase graph coverage. Exclude `original/` reference clones from active architecture counts and transitive claims unless comparison with upstream is the task.
<!-- codebase-memory-mcp:end -->

## Knowledge and Local Search

- The CBM graph combines code and maintained documentation in one project index; it is not an experiment/artifact registry.
- On nodes 7783 and 6269, verify the installed CBM version and use the node-local wrapper `/mnt/localdisk/enroot/sks/tools/codebase-memory/cbm`; the project graph name is `mnt-rag-aamita-project-rerank`. This names the intended graph, not proof that indexing is ready: check live index status and per-file `check_index_coverage` before relying on it. The intended graph source is the actual NFS project root `/mnt/rag/aamita/project/rerank`; verify the graph metadata before assuming migration from the previous node-local snapshot is complete. Compare consequential findings with current source and the affected worktree, and read missed or changed lines directly. Refresh indexing manually until background watching is explicitly enabled and verified; this migration does not itself enable automatic indexing or watching. Keep live SQLite databases and runtime state node-local, preserve `.cbmignore` boundaries, and do not restore historical shared graph backups into active storage. On other nodes, verify their local CBM deployment and graph status independently; do not assume the 7783 path, version or snapshot is available.
- `.project_knowledge/catalog.sqlite3` is a generated, local SQLite/FTS catalog of allowlisted metadata. Regenerate it; never treat the binary cache as committed truth.
- [knowledge/artifacts.md](knowledge/artifacts.md) is the human-readable catalog digest.
- QMD searches allowlisted curated Markdown only: `knowledge/`, top-level `research/` notes, active `changelog/` ledgers, lineage Markdown, repository skill Markdown, `PROJECT_MEMORY.md`, and selected Markdown reports. Local historical archives under `.project_knowledge/continuity_archive/` are excluded from default retrieval and opened only through an explicit pointer.
- The optional local Qwen/vLLM service may synthesize redacted retrieved context. The startup path must work while that service is offline.

## Project Wiki Maintenance

- Use the `research-knowledge-map` skill for source-linked OKF knowledge under `knowledge/`. Before substantive work, read its index and relevant contribution pages alongside canonical sources and the matching `docs/handoffs/` record. Before finishing durable decisions, experiments or meaningful changes, update affected pages, directory indexes and the newest-first change log with source links, actual verification dates, negative findings and unresolved questions. Routine scoped upkeep is authorized; routine questions and trivial edits need no wiki entry. Bulk ingestion, including conversation archives, requires explicit scope; this maintenance rule does not authorize unrelated remote operations, software installation or background indexing.

- Preserve personal annotations, unknown metadata, contradictions, historical decisions and private-source boundaries. Original code, reports and source documents remain authoritative; the wiki is navigational synthesis. Preserve existing `docs/handoffs/` records in place and create uniquely named handoffs when a new record is needed. Use one coordinating writer for shared indexes or overlapping pages; NFS and Git history are not locks. While tasks contribute separately, use unique paths under `knowledge/contributions/` and record the exact merge work for the designated consolidator; do not replace the broader project account with one task's view. Report changed pages and deferred knowledge work in the handoff. If the skill is unavailable, preserve a concise handoff and report the gap. This rule creates no background watcher or automatic indexing job.

## Continuity Placement and Closure

Keep one canonical home for each kind of continuity evidence:

| Need | Canonical surface |
|---|---|
| Stable repository rules and routing | `AGENTS.md` |
| Current cross-thread operational synthesis | `PROJECT_MEMORY.md` |
| Current task narrative, decisions, evidence identities, next action, and acceptance | numbered `changelog/` ledger |
| Superseded detailed history that must remain lossless but should not enter startup retrieval | hash-bound `.project_knowledge/continuity_archive/<task>/` snapshot |
| Task allocation and status routing | `changelog/INDEX.md` |
| Objective remaining gates and repository-relative closure evidence | `lineage/tasks.jsonl` |
| Human gate/closure view | generated `knowledge/task_gates.md` |
| Reusable cross-task prevention rules | `knowledge/lessons.md` |
| Research direction and promotion state | `knowledge/research.md`, with detailed evidence in the owning ledger |
| Detailed literature/model/benchmark/paper synthesis | `research/*.md`, routed from `research/README.md`; never a substitute for measured task evidence |
| Large approved implementation design/plan | `docs/superpowers/specs/` and `docs/superpowers/plans/` |

An `active` or `partial` task must have at least one objective remaining gate; a `complete` task must have resolvable closure evidence. Edit the JSONL and canonical ledger, then regenerate the human view—never maintain a parallel TODO/DONE list or hand-edit the generated page. Keep `PROJECT_MEMORY.md` current rather than chronological, and keep approved plans/designs normative rather than appending review diaries. When an active ledger exceeds roughly 100 KB or 1,500 lines, freeze an exact hash-bound local snapshot and replace the startup-facing ledger with a concise current-state router. Before claiming clone durability, ensure authored continuity files and their generators are intentionally tracked or explicitly classified local-only.

## Shared Skills and Sub-agent Routing

Use this map when the task needs a reusable workflow or specialist. Select the narrowest matching skill, read its `SKILL.md`, and load supporting references only as needed. Existing project-specific skill routes remain authoritative for their workflows; this is not a startup checklist or a requirement to use every skill.

| Task | Skill |
| --- | --- |
| Project wiki, OKF knowledge map, durable research links | `research-knowledge-map` |
| Literature comparison and novelty search; understanding one paper | `literature-survey`; `paper-reading` respectively |
| Testable hypotheses, rival explanations, discriminating experiments | `hypothesis-generation` |
| Evidence-grounded manuscript, related work or rebuttal | `ml-paper-writing` |
| Retrieval/reranker training and evaluation design | `train-sentence-transformers` |
| Create or maintain an experiment notebook | `jupyter-notebook` |
| Structural code discovery and dependency tracing | `codebase-memory` |
| Resource-sensitive workload planning; model-weight memory estimates | `get-available-resources`; `hf-mem` respectively |

| Bounded delegated task | Sub-agent profile |
| --- | --- |
| Ingestion, transformations and data pipelines | `data-engineer` |
| Evaluation harnesses, metrics and result analysis | `eval-engineer` |
| Profiling and measured performance improvements | `performance-engineer` |
| Evidence-grounded literature research | `scientific-literature-researcher` |
| Correctness/security review and authorized scoped fixes | `reviewer` |
| Routine graph verification; quick provisional lookup; deeper graph audit | `codebase-memory`; `codebase-memory-scout`; `codebase-memory-auditor` respectively |

- Check the current session's skill catalog and available agent types; installations can differ by host/profile. These names describe routing, not installation or permission. If unavailable, use an available equivalent or work directly and disclose the limitation.
- Follow the project's delegation policy, ownership rules and configured model choices. Delegate independent bounded work only when useful; retain integration and verification in the main task. A skill or sub-agent does not expand authorization or trigger indexing, experiments or deployment by itself.

## Repository Skill Routing

Skills are lazy-loaded tools, not a startup checklist. Invoke a repository skill only when the task directly matches its trigger; read its `SKILL.md` then, and open referenced material only as needed. Use one primary skill by default and add another only when the task genuinely crosses domains. Do not load unrelated connector/plugin skills for repository work.

| Skill | Use when |
|---|---|
| [`rerank-review-eval-evidence`](.agents/skills/rerank-review-eval-evidence/SKILL.md) | Reviewing MTEB/BM25/RAG results, summaries, workbooks, dashboards, model comparisons, or uplift claims |
| [`rerank-operate-experiment-run`](.agents/skills/rerank-operate-experiment-run/SKILL.md) | Preparing, launching, resuming, monitoring, stopping, recovering, or finalizing training/eval/data/RAG jobs |
| [`rerank-design-experiment`](.agents/skills/rerank-design-experiment/SKILL.md) | Designing a loss, curriculum, data-mixture, mining, filtering, HPO, fusion, retrieval, model, or RAG hypothesis |
| [`rerank-audit-dataset-lineage`](.agents/skills/rerank-audit-dataset-lineage/SKILL.md) | Creating, mixing, filtering, mining, synthesizing, converting, splitting, validating, or promoting data |

## Review and Subagent Policy

- Do not spawn subagents for orientation, routine implementation, ordinary test iterations, documentation maintenance, or work that one agent can complete directly without material delay or loss of quality.
- At a meaningful milestone, use at most one adversarial reviewer. Reserve a second independent reviewer for the final high-risk release/production decision only.
- Do not send multiple agents the same review packet, and do not repeat a review when the authenticated bytes are unchanged.
- Spawn any reviewer with `fork_turns="none"`. Provide a small explicit packet containing the objective, exact hashes, changed files/symbols, relevant contract excerpts, verification commands, stop boundaries, and requested finding format.
- Review reports are finding-first and concise. Record deduplicated findings and the disposition once in the canonical ledger; keep verbose reviewer output as a local artifact if it must be retained.

## Project Structure

- `Rankify/rankify/`: retrieval, reranking, and RAG toolkit.
- `mteb/mteb/`: MTEB framework and CLI.
- `FlagEmbedding/FlagEmbedding/`: embedding models and utilities.
- `ms-swift/swift/`: modeling, reranker training, custom losses, and helpers.
- `notebooks/`: project-owned experiments, orchestration, evaluation, curation, dashboards, and knowledge tooling.
- `data/`: local datasets, manifests, results, and assets; avoid committing large binaries.
- `reports/`: generated analyses; record generator, inputs, as-of time, provenance class, and refresh safety.
- `research/`: detailed source-linked literature reviews, model watchlists, benchmark gaps, and publication roadmaps; keep concise promotion state in `knowledge/research.md` and measured run evidence in task ledgers/artifacts.
- `changelog/`: canonical numbered task narratives.
- `knowledge/`: concise cross-task wiki and append-only maintenance log.
- `lineage/`: normalized task/session/alias registries and generated session routing.
- `original/`: upstream/reference clones, not active implementation surfaces.

Each major module is a separate Git repository. Inspect its branch, remote, and local changes independently. An upstream `main`/`master` branch is a comparison reference only after its freshness is verified; do not assume it is current.

## Environments and Installation

- Rankify: `conda activate rerank_rankify`
- MTEB current maintenance: use the pinned Python 3.14/uv overlay in
  [notebooks/mteb_runtime/README.md](notebooks/mteb_runtime/README.md). It installs the local
  synchronized MTEB checkout editably and validates the exact code/results identities before use.
- MTEB historical run reproduction only: `conda activate rerank_mteb`
- ms-swift: `conda activate rerank_swift`
- FlagEmbedding: `conda activate rerank_bge`

Modules are developed from source with `pip install -e .` in the appropriate environment.

## Task and Changelog Contract

- Before code or experiment execution, write a plan in `changelog/<number>_<task_name>.md`.
- Allocate IDs through [changelog/INDEX.md](changelog/INDEX.md); never infer the next number from filenames alone. Update the same task file when scope continues.
- Every task ledger must contain, in this order near the top: Date/Status, Plan, then Design.
- It must also contain Changes, Smoke Test, Full Run, Summary, Impact / How to Use, and What I Covered.
- The Design section captures the current architecture, data flow, formulas/metrics, tradeoffs, decisions, and supersession notes needed to operate the task. Once approved, keep the plan/design normative; put implementation history and review dispositions in the ledger or primary evidence rather than duplicating them.
- Use normalized task status: `planned`, `active`, `partial`, `complete`, `blocked`, `superseded`, or `pointer`.
- Track evidence separately: `live-verified`, `documented-history`, `stale-or-contradictory`, or `open`.
- Record dependencies, supersedes/superseded-by, canonical evidence, generated outputs, warnings, and session IDs when relevant.
- Before summarizing/compacting context, update the active task's concise current-state block with decisions, evidence identities, failures, and next action. Do not repeat unchanged history, commands, or hashes across the ledger, plan, design, and `PROJECT_MEMORY.md`.
- When the requested outcome is verified, update the same ledger with completion evidence, final usage, and exact runnable examples without waiting for routine user acceptance. If the task explicitly requires user acceptance, record that gate separately as pending; do not claim acceptance or hold back independently completed documentation.

For every training, eval, data-build, sweep, report, transfer, or long-running command—whether run by the agent or supplied by the user—record:

- the exact command, including environment variables and CLI arguments;
- output/checkpoint directory;
- log path;
- status (`prepared`, `started`, `completed`, `failed`, `stopped`, or `unknown`);
- run/study/model/dataset identifiers;
- key final metrics or counts, when available;
- verification time and evidence path.

Read-only orientation that does not create/change project state may be recorded in an existing catch-up/continuity ledger rather than allocating a new task. Any implementation, experiment, or durable documentation change still requires an active task.

## Coding and Scope Rules

- Keep changes scoped to one module/workstream and use that module's tools/configuration.
- Do not reformat unrelated files or broadly refactor vendored/forked projects without discussion.
- Put project-owned experiment/orchestration tools under `notebooks/`. Modify module source/tests in the owning module when the task explicitly changes product behavior; do not force such changes into `notebooks/`.
- Write docstrings, comments for non-obvious logic, and type hints in new/modified Python.
- Research Markdown prose is not subject to an 80- or 120-character hard-wrap rule. Prefer semantic paragraphs and readable tables; this does not change source-code lint or formatting rules.
- Use repo-relative Markdown links for committed navigation so migrations do not break them. Preserve exact historical absolute paths only as evidence; use `/mnt/rag/...` in current runnable commands.
- Keep credentials and secrets out of commands, logs, task ledgers, generated indexes, and model prompts.

## Project-Specific Contracts

- For MTEB-based code, always use `cache_path = "/mnt/rag/aamita/project/rerank/data/mteb_results"`.
- Project MTEB table helpers require an explicit output path, refuse replacement unless
  `--overwrite` is supplied, and may clone an absent official-results checkout but never update an
  existing one. Use Task 0034's audited Git workflow for upstream refreshes.
- The `ms-swift` multimodal reranker baseline came from `support training for multimodal reranker #6192`, commit `4a1437cc2bf9d7ed49cdd6939172bda18033d916`.
- Task 0033 repaired and reconciled summary preservation across the canonical primary-result tree.
  Canonical measured report regeneration remains a separate acceptance/provenance gate; synthetic
  v2 target artifacts remain ineligible as measured evidence.

## Cross-Thread Memory

- `PROJECT_MEMORY.md` is the canonical current cross-thread synthesis.
- `lineage/sessions.jsonl` is the curated logical-session registry; `lineage/SESSION_INDEX.md` is its human-readable view.
- Record the live `CODEX_THREAD_ID`, exact `cwd`, task references, parent/import relationships, and effective repo episode. Do not duplicate the full volatile session list in this file.
- Preserve chronological creation time separately from resumed/imported activity, memory-refresh time, and artifact-observation time.
- Keep physical raw rollout paths outside Git; store only safe symbolic pointers and curated summaries.

## Testing and Style

- This is a research platform: use hypothesis-first development. While an idea, data path, or
  evaluator is still exploratory, prefer bounded probes, invariant checks, and end-to-end smoke
  runs over broad test scaffolding. Add focused deterministic regression tests once a contract,
  metric, promoted artifact, or reusable workflow has stabilized. Do not make test coverage a gate
  for exploratory code that is clearly labeled and cannot affect canonical evidence.
- Framework: `pytest`.
- Test locations: `mteb/tests/`, `ms-swift/tests/`, `Rankify/tests/`, and project-tool tests beside their notebook package.
- Name tests `test_*.py` with small deterministic fixtures. Prefer focused `pytest -q`; for MTEB use `make test` or `pytest -n auto`; coverage uses `make test-with-coverage`.
- Rankify/MTEB: `ruff format . && ruff check .` before commit.
- ms-swift: `flake8 .`, `isort .`, `yapf -ir .` or non-mutating check variants as appropriate.
- New/modified code uses four-space indentation, `snake_case` functions/modules, `PascalCase` classes, and `UPPER_SNAKE_CASE` constants.

## Task-Based Skill Selection

These project routes supplement the global guidance and current session skill catalog. Automatically select the narrowest applicable skill, read its `SKILL.md`, and load references only as needed; this is not an all-skills checklist. Existing project-specific routes, admission checks, ownership and delegation policies remain authoritative. Name the selected skill and its relevant instructions in any subagent brief; routing adds no execution authority.

- Module/interface design: `codebase-design`; scoped architecture audits or boundary improvements: `improve-codebase-architecture`.
- Defect diagnosis: `diagnosing-bugs`; domain-wide invariants or generated-input tests: `property-based-testing`.
- Exportable research figures and figure QA: `scientific-visualization`; substantial architecture or dataflow diagrams: `archify`.
- Only for research dashboards or other web UI work: `frontend-design` for UI design and `web-performance` for measured web loading/rendering performance; backend or model throughput is outside the latter skill.
