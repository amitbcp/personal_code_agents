# SKS Project Guidance

- SKS curates developer knowledge into governed retrieval and citation-rich context packs. Use `sks/` and the current APIs for new work; compatibility names are for existing integrations.
- Source connectors are read-only unless a separate provenance write-back design is approved.
- This file adds project-specific guidance to the active global instructions. Keep it local and Git-ignored unless explicitly asked to track it; do not copy private global guidance into the repository.

## Initiative and Task Completion

- Carry the user's intended outcome through to verified completion. Treat requests to do or fix something as execution requests; a plan, diagnosis, first patch, or list of next steps is an intermediate result.
- After each finding or completed step, choose and perform the next necessary action within the authorized objective. Include straightforward implied follow-ups, integration, focused checks, and required documentation; do not wait for another prompt to continue the same work.
- Resolve reversible implementation details using current evidence and project conventions. Ask only when missing information materially blocks correctness or an applicable approval is genuinely absent. Reuse authorization already given; do not ask for it again.
- If one operation is blocked, finish independent authorized work and prepare the blocked action for review. Explain the exact blocker and smallest missing decision; if an instruction requires a pause, identify its file and relevant rule.
- Preserve the objective across status questions, findings, delegation, and compaction. Integrate delegated results and continue; a progress report or task handoff does not itself complete the work.
- Keep follow-ups tied to the requested outcome. Respect explicit pauses, ownership, protected areas, and operation-specific approval boundaries. Do not turn this rule into permission for unrelated backlog work, new experiments, spending, publication, destructive actions, or indefinite optimization.
- Before ending, check the requested outcome against actual evidence. Complete remaining in-scope steps when possible; otherwise report what is verified, what remains, and why. Once the outcome is met, stop rather than inventing more work.

## Start Here

- Use `README.md` for project purpose, architecture, documentation navigation and development entry points. Verify dated status, paths and commands against current source/configuration before using them.
- Identify the user's current objective. Read the named task handoff and its relevant private companions, then the matching current section of `tasks/todo.md`. Honor its unresolved gates and approval holds; old ledger entries and commands are evidence, not new execution authority.
- Read `docs/wiki/index.md` and the pages relevant to that objective. The wiki provides source-linked context; original code, configurations and reports remain authoritative. Use the `research-knowledge-map` skill for wiki queries and maintenance.
- Consult the relevant entries in `tasks/done.md`, `tasks/memory.md`, `tasks/lessons.md` and `NOTES.md` for prior results, decisions and failed approaches. Follow their source links instead of reading or reconciling every historical entry. Where maintained, start task-local notes at `.agent-notes/INDEX.md`.
- Confirm the actual checkout, branch/commit, relevant dirt, execution host and required artifact availability before changes. NFS project files are shared across nodes; local-disk caches and artifacts are not. Report missing inputs without treating historical completion as invalid or automatically recreating them.
- After context compaction, reload these entry points for the active task. Continue within the existing authorization; ask only for a missing decision that blocks the next operation.

## Subagent Delegation and Model Selection

- Prefer a team of subagents for substantial work with independent parts: investigation, implementation, research, command execution, tests and review. The main agent owns the plan, delegates bounded tasks, coordinates dependencies, integrates changes and verifies the final outcome. Continue useful independent work while subagents run; do not stop at dispatching tasks or merely forwarding their reports.
- Default to **GPT-6 Luna with maximum reasoning** (`gpt-6-luna`, `max`) for well-scoped work. Use the established **GPT-6 Astra with low reasoning** (`gpt-6-astra`, `low`) for complex or ambiguous work requiring broader reasoning, architecture decisions or difficult diagnosis. Choose by task needs, not by file size alone.
- Apply this preference explicitly when the spawning interface supports model and reasoning overrides; named specialist profiles may have their own defaults. Do not assume this Markdown changes their TOML settings or an already running agent. If the preferred model/effort is unavailable, use the supported configured fallback and report the substitution; never invent a model identifier.
- Give each subagent a self-contained brief: objective, relevant context, exact files or responsibility, permissions, expected artifact and acceptance checks. Tell editing agents that others share the checkout, to preserve others' changes and to coordinate overlapping files. Assign one writer to each shared file, wiki page, mutable cache or index.
- Parallelize independent tasks within the session's actual agent and resource limits. Keep trivial, tightly coupled or sequential work local when delegation would add overhead. Avoid duplicate searches, redundant tests, idle polling and competing writers; reuse agents for related follow-ups. Subagents must not delegate further unless explicitly authorized.
- The main agent reviews outputs, resolves conflicts, runs appropriate integration checks and carries the authorized task through completion. Delegation does not expand permission for destructive actions, external changes, service operations, embedding or index rebuilds. Stop completed agents and retain their useful findings in the task record or scoped wiki update.

## Execution Principles

- Define the requested outcome and a practical completion check before substantial changes. State material assumptions and resolve contradictions against current evidence; use reasonable defaults for reversible details and ask only when a missing decision blocks safe, correct progress.
- Apply the global Karpathy-inspired principles: prefer simple existing code paths, make surgical changes, avoid speculative abstractions and dependencies, and verify the result. Keep implementation scope proportional to the problem; report unrelated findings without expanding the task.
- For substantial workloads, inspect effective CPU, RAM, GPU, disk and scheduler limits; measure a representative baseline and identify the bottleneck before scaling. Use bounded concurrency, batching and resumable checkpoints where useful. Avoid arbitrary worker counts or claiming scale from tiny samples.
- Project sources on NFS are shared; node-local NVMe is suitable for permitted scratch/cache and high-I/O work. Record where results live and preserve durable outputs before cleanup or migration. Coordinate shared writers and avoid concurrent index mutations.
- Write maintainable Markdown with descriptive headings, complete bullets and one logical paragraph or bullet per source line. Let the editor wrap visually; preserve intentional formatting inside code blocks and tables. Reinforce important rules where they affect a decision without duplicating entire global guides.

## Work Narrowly and Evidence-First

Start from the exact request. Do not reconcile the whole repository, task ledger, archive, or session history unless the user asks or a concrete contradiction requires it.

Use evidence in this order:

1. Current `sks/`, `scripts/`, `config/`, `evaluation/`, and `tests/` code.
2. The single applicable tracked guide or API/config contract.
3. The exact runtime process, log, ledger, cache, backend state, API output, or sealed packet relevant to the claim.
4. Only the named local lineage entry under `NOTES.md` or `tasks/`, followed by Git history when intent or ownership remains unclear.

Plans and reports are leads. Revalidate drift-prone claims against current code, config, or runtime. For a mutation or durable claim, use the applicable per-operation identity receipt described in `automation/codex/skills/_agentic-sks/identity-receipt.md`; add a second evidence surface when a wrong target could affect persistent data, privacy, users, or shared services.

Autonomously repair safe, reversible, in-scope problems. For missing authority, an unsafe or destructive target, a product-policy choice, or a frozen-interface change, pause the affected operation and continue independent authorized work. Existing authorization remains valid within its stated scope.

## Checkout and Runtime Scope

- Resolve the current checkout with `git rev-parse --show-toplevel`; do not assume a handoff's path or branch is still current.
- Python environment: `okb_dev`
- Product package: `sks/`
- No Docker for local development unless explicitly requested.
- Do not modify `/mnt/shared/aamita/project/okb` unless explicitly requested.
- Do not inspect or modify `sks_support/` unless the user reopens it.
- Preserve unrelated dirt. Inspect `git status --short --branch` before edits, switching, cleaning, merging, or archival.

Common local ports:

- development API `8810`; development Oracle Docs UI `8314`;
- demo API `8800`; demo Oracle Docs UI `8307`.

Before trusting a service, verify its process command, checkout, commit, environment, organization, bind address, port, and effective search/rerank settings. A listener alone is not proof of the intended deployment.

## Environments, Cache Reuse and Storage

- Development/tests use `okb_dev` by default (`scripts/start_dev.sh`); the demo launcher defaults to `okb` (`scripts/start_demo.sh`). `SKS_CONDA_ENV` selects an override. Verify the selected environment and interpreter on the execution node before running; environment names alone do not prove installed dependencies.
- Development loads the checkout's `.env`; demo uses `DEMO_ENV_FILE` (default `.env.demo`) with `.env` fallback. For org-specific work, follow `docs/guides/quickstart.md`, `config/README.md` and the relevant release runbook rather than loading every `.env*` file.
- `docs/guides/sks-release-inventory.md` owns cache paths and scopes. The documented release cache root is `/mnt/localdisk/enroot/rag/aamita/agentic_sks/output/release/shared/`, including dense embeddings, Jira source hydration and image enrichment. Veritas has a distinct embedding cache; preserve its documented namespace and writer constraints.
- Prefer compatible warm caches for reruns and related jobs; resolve the existing cache from the run manifest, launcher and release inventory before creating another. Match model/revision, input type, preprocessing/chunking and provenance before reuse; report cache hits/misses and distinguish warm-cache timing from cold computation. Do not clear, merge or repoint shared caches as an incidental fix.
- `/mnt/rag` project paths are shared NFS. `/mnt/localdisk` is node-local storage; use an existing writable project cache/scratch location there for high-I/O work. “Shared” in a local cache path means reuse across compatible runs on that node, not availability on other nodes. Verify mounts, ownership, free space and permissions; do not assume `/var/tmp`, a home/root cache or the same pathname on another node is NVMe or contains the same data.
- Coordinate cache writers and honor the cache format's locking rules, particularly SQLite; reuse read-only artifacts where possible. Preserve manifests, logs and irreplaceable outputs in the approved durable location before local cleanup or node migration. A missing local cache does not invalidate historical results or authorize recomputation.
- Treat `.env*` files as private runtime inputs. Use the task's approved profile and documented launcher/loading order; record the selected filename and variable names needed for reproduction, never secret values. Keep files Git-ignored, preserve restrictive permissions and avoid shell tracing or environment dumps. Do not substitute a different org/backend/credential profile merely to make a command run.
- Standard dev ports are API `8810` and Oracle Docs UI `8314`; demo ports are API `8800` and UI `8307`. See `docs/runbooks/operations.md` and the start scripts for loading, logs and lifecycle. These are configured defaults, not a live service inventory; inspect the intended host's listener/process/checkout and health before reuse or launch.

## Current Sources of Truth

Open only the authority relevant to the task:

- stable product rules: `docs/engineering/sks-invariants.md`
- runtime defaults: `config/capabilities.yaml` and `docs/design-decisions/tech-stack.md`
- org/source/phase definitions: `config/orgs/`, `config/sources/`, `config/phases/`
- release inputs: `docs/guides/sks-release-inventory.md`
- REST/MCP contracts: `docs/api/rest-endpoints.md`, `docs/api/mcp-tools.md`, `docs/api/context-pack-schema.md`
- phased ingestion: `docs/guides/phased-ingestion-onboarding.md` and `docs/guides/opensearch-phased-ingestion-onboarding.md`
- media: `docs/guides/media-ingestion.md` and the applicable modality guide
- Veritas: `docs/guides/veritas-public-eval-ingestion.md` and `docs/guides/veritas-public-eval-api-handoff.md`
- tests/CI: `docs/guides/test-suite.md`, `tox.ini`, `ocibuild.conf`
- shared-package changes: `docs/refactor-consolidation-signoff-protocol.md` and the applicable handoff

`kcm_config.yaml` is not the current source of truth. Jira release/capture locations are resolved through the release inventory and source configuration, not copied into this overlay.

## Runtime, Branch, and Worktree Safety

- Inspect `HEAD`, `main`, `origin/main`, worktree registration, and dirt before branch/worktree actions.
- Never switch a dirty root checkout merely to isolate work. Use an isolated worktree, and remember that ignored local notes do not follow it.
- Classify tracked dirt, untracked evidence, ignored runtime artifacts, secrets, and caches before integration or archival.
- Never reset, clean, delete, or overwrite unrelated user work. Use `git worktree move` for registered worktrees.
- Historical claims start from the named `tasks/memory.md` pointer or sealed archive index, then are revalidated against current code/config.
- Never mutate an existing release org to test a new ingestion contract; use a bounded or newly named org.

Long-running jobs and services need persistent ownership (`tmux` or the approved supervisor), stable logs, and recorded command/checkout/commit/env/ org/port/bind identity. Validate health and a representative request through the same login-node, proxy, tunnel, or compute-node path users will use.

Status reports distinguish live from historical state and include owner, stage, completed denominator, timestamp, observed throughput/ETA, cache behavior, backend visibility, and errors/retries. Separate embedding, staging, sink writes, graph replay, and finalize. Configuration alone does not prove batching or concurrency.

## Task-Scoped Validation

Run the smallest proof covering the changed behavior:

- vector/OpenSearch: backend mapping/ID tests, finalize/visibility, and one intended-org query;
- graph/schema: focused tests, counts, exact URI preservation, and one path or expansion check;
- phased ingestion: bounded snapshot/load/finalize with source, reset, resume, and replay evidence;
- materialization: sparse, empty, long, typed-only, and affected granularity shapes without duplicated or dropped evidence;
- API/MCP: affected modes, filters, graphless behavior, required fields, privacy, and parity;
- evaluation: immutable experiment identity, arm parity, errors, metric semantics, raw artifacts, and per-query evidence;
- privacy: affected storage and outward surfaces, masked and unmasked;
- CI/tox: the relevant lane only; exclude `sks_support` unless reopened.

Useful commands:

```bash
git status --short --branch
git worktree list --porcelain

bash scripts/start_dev.sh
bash scripts/stop_dev.sh
bash scripts/start_demo.sh
bash scripts/stop_demo.sh

conda run --no-capture-output -n okb_dev \
  python -m pytest tests/path/to/test_file.py -q
conda run --no-capture-output -n okb_dev \
  python -m tox -e unit_tests_oci -- --collect-only -q
```

If the environment fails before collection, keep that infrastructure failure separate from product-test results. Use a writable temporary/cache prefix when the restricted runner requires it.

## Task and Documentation Discipline

- Plan genuinely multi-step or architectural work before editing. Update only the active task's status and evidence; do not rewrite unrelated backlog or history.
- Use `tasks/todo.md` for objective open gates, `tasks/done.md` for verified closure, `tasks/lessons.md` for reusable prevention, `tasks/memory.md` for durable state, and `NOTES.md` for user-note reconciliation.
- Preserve authorship when amending old plans; distinguish implemented, refuted, proved, and remaining work.
- Keep local plans/research local unless the user requests a tracked surface.
- Put team-facing operational contracts in tracked guides and link rather than duplicating mutable commands.
- Never commit generated eval reports, secrets, wallets, local env files, or plan drafts without explicit approval.

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

## Review and Skill Routing

Use the narrowest relevant installed skill. For `agentic-sks-*` skills, load the shared `automation/codex/skills/_agentic-sks/operational-contract.md` and run the installed-suite admission check required by that suite; a valid SessionStart does not replace per-invocation admission. General research and wiki skills follow their own SKILL.md instructions.

| Need | Skill |
| --- | --- |
| significant prospective product/architecture change | `agentic-sks-product-change-design` |
| explicitly requested isolated PoC | `agentic-sks-poc-experiment` |
| new/materially changed source | `agentic-sks-source-onboarding` |
| healthy release ingestion | `agentic-sks-release-ingestion-operator` |
| slow/stalled/failed ingestion | `agentic-sks-ingestion-perf-triage` |
| evaluation evidence claim | `agentic-sks-eval-evidence-review` |
| implemented change/release readiness | `agentic-sks-release-review` |
| privacy/masking/customer safety | `agentic-sks-privacy-release-check` |
| branch/worktree lifecycle | `agentic-sks-worktree-lifecycle` |
| notes/task/session reconciliation | `agentic-sks-task-lineage-reconciliation` |
| OKF wiki queries, durable knowledge updates and migration knowledge maps | `research-knowledge-map` |
| structural code discovery and impact analysis | `codebase-memory` |
| resource planning before substantial compute or data work | `get-available-resources` |
| research questions, hypotheses and discriminating experiments | `hypothesis-generation` |
| literature survey / reading a specific paper | `literature-survey` / `paper-reading` |
| evidence-backed research manuscripts and rebuttals | `ml-paper-writing` |
| retrieval/reranker training and evaluation | `train-sentence-transformers` |
| notebook creation / model-memory estimates | `jupyter-notebook` / `hf-mem` |

Use the checkout-configured `sks-terminal-review` profile only when the user explicitly requests a terminal architecture ruling or release adjudication. Before launch, follow the checkpoint-evidence reference in `agentic-sks-release-review`; terminal review does not broaden mutation authority, and `/tmp`-only evidence is not durable release evidence.


## OKF Wiki Maintenance

- Maintain the existing `docs/wiki/` bundle with `research-knowledge-map`; follow its project-setup and OKF references for layout and metadata. Do not create a second wiki. Bulk imports and broad refreshes require explicit scope.
- Before finishing substantive work that changes durable knowledge, update affected pages with source-backed decisions, verified findings, completed experiment results and unresolved questions; update relevant indexes and `docs/wiki/log.md`. Routine scoped upkeep is authorized without another permission request. Trivial edits, routine questions and unchanged knowledge need no entry.
- Record source, observation date, execution host, scope and evidence status for consequential claims. Preserve personal annotations, unfamiliar metadata, contradictory evidence, rejected approaches and historical results; a new document does not reverify an old claim.
- Keep time-sensitive objectives, restart prompts, host/artifact state and recovery gates in scoped task handoffs. Preserve existing handoffs and source documents in place; create a unique new handoff when a new migration/continuation receipt is needed.
- On shared NFS, check the wiki's coordinating writer and current edits before touching overlapping pages or indexes. Use one writer; Git is not a cross-host lock. If ownership or overlap is unresolved, save a unique contribution under `docs/handoffs/wiki-contributions/<date-and-task>/` and report exact consolidation needs. Preserve existing published contribution layouts.
- Link approved private companions instead of copying secrets, raw conversation archives or private global guidance. A Git clone or wiki export may omit those dependencies; report missing or inaccessible sources.
- Wiki upkeep does not run while idle and does not authorize experiments, embedding, cache merges, authentication changes, service/index mutations or CBM rebuilds. Perform those only within the active task's separate authorization.
- If the skill or a required source is unavailable, report the gap and save a concise handoff. Verify changed links/metadata and report pages updated, deferred contributions and unresolved gaps before finishing.

## Codebase Memory (CBM)

- On 7783, use the graph `mnt-rag-aamita-project-agentic_sks`. Inspect its recorded root, indexing time and coverage before relying on results. A graph rooted at this NFS checkout describes files as indexed; verify its generation and actual watcher registration before assuming it has refreshed. A graph rooted at a retained node-local snapshot describes that capture, and snippets refer to the snapshot. In either case, verify consequential findings against current source and the affected worktree. Session-start auto-indexing is disabled. On both nodes 7783 and 6269, the node-local CBM profiles have global auto_index=false, auto_watch=true and watcher_enabled=true; active watching depends on session registration. Manual rebuilds require explicit authorization.

- Use the active profile's CBM for structural discovery when available. Verify the graph's repository/worktree, branch/commit, freshness and node-local cache; it supplements current source and is not live-checkout authority.
- Check index coverage for every file relied on. Read incomplete, skipped or stale source ranges directly; use focused search when no usable graph exists. Do not infer absence or correctness solely from a graph result.
- Keep one combined code/documentation index per project or separately used worktree on each node. Exclude nested worktrees from the parent graph to avoid mixing branches and duplicated code.
- `.cbmignore` is the current indexing-scope policy. Git exclusions and CBM discovery interact; preserve Git ignored status and verify actual CBM inclusion/exclusion when changing scope. Checkout-local Git-only exclusions in `.git/cbm-docs-git-excludes` (configured through `core.excludesFile`) must be carried deliberately to new checkouts. Keep runtime versions, cache locations, build results and migration history in operational handoffs.
- Never print secrets or ENV contents from source files or index results.
- Do not manually rebuild CBM merely because a task starts, documentation changes or a graph is unavailable; use source inspection until a build is authorized. Respect the separately configured watcher lifecycle; global enabled flags alone do not prove this project is actively watched.

## File Ownership

Use Git history/blame when intent is unclear. Avoid unrelated refactors and formatting churn. Preserve compatibility deliberately and fix root causes through existing product paths rather than adding a one-off parallel path.

## Task-Based Skill Selection

These project routes supplement the global guidance and current session skill catalog. Automatically select the narrowest applicable skill, read its `SKILL.md`, and load references only as needed; this is not an all-skills checklist. Existing project-specific routes, admission checks, ownership and delegation policies remain authoritative. Name the selected skill and its relevant instructions in any subagent brief; routing adds no execution authority.

- Module/interface design: `codebase-design`; scoped architecture audits or boundary improvements: `improve-codebase-architecture`.
- Defect diagnosis: `diagnosing-bugs`; domain-wide invariants or generated-input tests: `property-based-testing`.
- Exportable research figures and figure QA: `scientific-visualization`; substantial architecture or dataflow diagrams: `archify`.
- Application UI design: `frontend-design`; measured web loading or rendering performance: `web-performance`.
