# AGENTS.md

Local Codex guidance for `/mnt/rag/aamita/project/sks_media` — the **media
production checkout** on branch `main` (`mm_deploy` is retired). Verify current HEAD and `origin/main`; historical switch commits are not current identity. Serving processes run from detached candidate worktrees under `sks_media_candidates/`, never from this checkout.

This file is local-only and gitignored. Do not track or commit it unless the
user explicitly asks. It is the checkout-local operator overlay; stable product
semantics live in `docs/engineering/sks-invariants.md`, and Codex execution
policy lives in the installed sealed suite
`${CODEX_HOME:-$HOME/.codex}/skills/_agentic-sks/operational-contract.md`
(the skill source tree is kept only in the primary checkout
`/mnt/rag/aamita/project/agentic_sks/automation/codex/`).

# SKS Project Guide

SKS is the governed knowledge-curation and retrieval layer for Oracle developer
knowledge. The current Python package and API namespace are `sks`; compatibility
names are not the path for new work. Source connectors are read-only unless a
separate provenance write-back design is approved.

## Initiative and Task Completion

- Carry the user's intended outcome through to verified completion. Treat requests to do or fix something as execution requests; a plan, diagnosis, first patch, or list of next steps is an intermediate result.
- After each finding or completed step, choose and perform the next necessary action within the authorized objective. Include straightforward implied follow-ups, integration, focused checks, and required documentation; do not wait for another prompt to continue the same work.
- Resolve reversible implementation details using current evidence and project conventions. Ask only when missing information materially blocks correctness or an applicable approval is genuinely absent. Reuse authorization already given; do not ask for it again.
- If one operation is blocked, finish independent authorized work and prepare the blocked action for review. Explain the exact blocker and smallest missing decision; if an instruction requires a pause, identify its file and relevant rule.
- Preserve the objective across status questions, findings, delegation, and compaction. Integrate delegated results and continue; a progress report or task handoff does not itself complete the work.
- Keep follow-ups tied to the requested outcome. Respect explicit pauses, ownership, protected areas, and operation-specific approval boundaries. Do not turn this rule into permission for unrelated backlog work, new experiments, spending, publication, destructive actions, or indefinite optimization.
- Before ending, check the requested outcome against actual evidence. Complete remaining in-scope steps when possible; otherwise report what is verified, what remains, and why. Once the outcome is met, stop rather than inventing more work.

## Subagent Delegation and Model Selection

- Prefer a team of subagents for substantial work with independent parts: investigation, implementation, research, command execution, tests and review. The main agent owns the plan, delegates bounded tasks, coordinates dependencies, integrates changes and verifies the final outcome. Continue useful independent work while subagents run; do not stop at dispatching tasks or merely forwarding their reports.
- Default to **GPT-6 Luna with maximum reasoning** (`gpt-6-luna`, `max`) for well-scoped work. Use the established **GPT-6 Astra with low reasoning** (`gpt-6-astra`, `low`) for complex or ambiguous work requiring broader reasoning, architecture decisions or difficult diagnosis. Choose by task needs, not by file size alone.
- Apply this preference explicitly when the spawning interface supports model and reasoning overrides; named specialist profiles may have their own defaults. Do not assume this Markdown changes their TOML settings or an already running agent. If the preferred model/effort is unavailable, use the supported configured fallback and report the substitution; never invent a model identifier.
- Give each subagent a self-contained brief: objective, relevant context, exact files or responsibility, permissions, expected artifact and acceptance checks. Tell editing agents that others share the checkout, to preserve others' changes and to coordinate overlapping files. Assign one writer to each shared file, wiki page, mutable cache or index.
- Parallelize independent tasks within the session's actual agent and resource limits. Keep trivial, tightly coupled or sequential work local when delegation would add overhead. Avoid duplicate searches, redundant tests, idle polling and competing writers; reuse agents for related follow-ups. Subagents must not delegate further unless explicitly authorized.
- The main agent reviews outputs, resolves conflicts, runs appropriate integration checks and carries the authorized task through completion. Delegation does not expand permission for destructive actions, external changes, service operations, embedding or index rebuilds. Stop completed agents and retain their useful findings in the task record or scoped wiki update.

## Work Narrowly and Evidence-First

Start from the exact request. Do not reconcile the whole repository, task
ledger, archive, or session history unless the user asks or a concrete
contradiction requires it.

Use evidence in this order:

1. Current `sks/`, `scripts/`, `config/`, `evaluation/`, and `tests/` code.
2. The single applicable tracked guide or API/config contract.
3. The exact runtime process, log, ledger, cache, backend state, API output, or
   sealed packet relevant to the claim.
4. Only the named local lineage entry under `NOTES.md` or `tasks/`, followed by
   Git history when intent or ownership remains unclear.

Use the project Codebase Memory MCP first for architecture, relationships,
call paths, and impact discovery when it is configured and healthy. Verify its
repository root, branch, HEAD, index identity, and node-local cache before
trusting it. Nodes 7783 and 6269 use node-local CBM installations and separate caches; verify the installed version and index status before relying on them. On node 7783, the Media graph indexes this live NFS checkout; verify consequential
findings against current files and check index freshness. Use the active Codex profile's configured node-local launcher; verify its
resolved command and cache on the current node. Global auto_index=false disables session-start indexing; auto_watch=true and
watcher_enabled=true enable watching, whose active status still depends on
project/session registration. Verify registration rather than inferring it from these flags. Projects and worktrees have distinct
path-based index identities on each node. Refresh the existing project index
explicitly when authorized; verify the local launcher's supported CLI before
running an index command. Use `rg`, `rg --files`, focused reads, and tests for
exact symbols and proof. The approved 2026-09-17 index scope includes all CBM-supported files under
`docs/`, `poc/`, `scripts/`, and `tasks/`, plus Markdown elsewhere with traversable
parents. CBM intrinsic filters and nested Git ignore rules still apply;
`sks_support` and nested worktrees remain excluded. The three installed dependency
directories `.venv/`, `.venv-torch210/`, and `.transformers56-overlay/` directly
under `poc/video_fast_profile_nemotron_omni/` are also excluded; that POC's source,
configuration, and reports remain in scope.

Plans and reports are leads. Revalidate drift-prone claims against current
code, config, or runtime. For a mutation or durable claim, use the applicable
per-operation identity receipt described in the installed
`identity-receipt.md`; add a second evidence surface when a wrong target could
affect persistent data, privacy, users, or shared services.

Autonomously repair safe, reversible, in-scope problems. For missing authority, an unsafe or destructive target, a product-policy choice, or a frozen-interface change, pause the affected operation and continue independent authorized work. Existing authorization remains valid within its stated scope.

## Checkout and Runtime Scope

- Repository: `/mnt/rag/aamita/project/sks_media` (own `.git`; detached
  releases live under `sks_media_candidates/`; the published OU source branch
  remains under `sks_media_worktrees/`; the former `sks_media_fix` evidence
  worktree is preserved under
  `sks_media_local_docs_archive_20260826/worktrees/sks_media_fix-f34960c5-20260830`).
- Branch policy: `main`; verify current HEAD and its relationship to `origin/main`. Never push `main` from here
  and never merge or rebase the retired `mm_deploy` line. Product code changes normally start from `main` in the
  primary checkout.
- Python environments: `okb_dev` for tests/tools; `sks_media` for governed
  media production (`make media-prod-setup`, `requirements/media-prod-lock.txt`).
- `sks_core/` is present on `main`; `sks/utils/env.py`, `sks/config.py`, and
  `sks/models/` remain available. `sks_retrieval`, `sks_reranker`,
  `sks_contextpack`, `sks_generation`, and `sks_support` are also present.
- Untracked local evidence is intentional (`NOTES.md`, `docs/customer_*`,
  `docs/notes/*`, `docs/designs/*`, `docs/runbooks/iad-sstk-*`,
  `.tmp_build_d10_delta.py`); classify before any cleanup.
  `docs/engineering/sks-invariants.md` is an untracked byte-identical copy of
  the tracked file on the primary repo's `codex/sks-setup-alignment-20260829`
  branch — delete it before merging a `main` that already contains it.
- No Docker for local development unless explicitly requested.
- Do not inspect or modify `sks_support/` unless the user reopens it.
- Preserve unrelated dirt. Inspect `git status --short --branch` before edits,
  switching, cleaning, merging, or archival.

Common local ports: development API `8810`, Oracle Docs UI `8314`; demo API
`8800`, demo UI `8307`. Before trusting a service, verify its process command,
checkout, commit, environment, organization, bind address, port, and effective
search/rerank settings. A listener alone is not proof of the intended
deployment.

## Environments, Cache Reuse and Storage

- Tests/tools default to `SKS_CONDA_ENV=okb_dev`; governed production uses `SKS_MEDIA_PROD_CONDA_ENV=sks_media` (`Makefile`, `requirements/media-prod-lock.txt`). Verify the interpreter and approved dependency profile on the actual execution node; do not replace a serving environment during unrelated work.
- The production Makefile defaults `SKS_MEDIA_PROD_ENV_FILE` to `.env.media.v023` and conditionally loads `SKS_MEDIA_RELEASE_ENV_FILE` for the selected release descriptor. Customer ingestion has its own loader: `MEDIA_ENV_FILE`, then `SKS_MEDIA_GATEWAY_ENV_FILE` (default `~/.sks-secrets/embed-gateway.env`). Follow the selected entrypoint's documented loading order; do not mix these conventions. See `scripts/release/media/lib/media_ingest_common.sh` and `docs/guides/immutable-media-release-operations.md`.
- The Makefile's media cache root defaults to `/mnt/localdisk/enroot/sks/cache`; its shared text embedding cache defaults to `/mnt/localdisk/enroot/rag/aamita/agentic_sks/output/release/shared/embedding_cache/oci-cohere-search_document.sqlite3`. Resolve effective overrides before reuse. Customer ingestion retries should retain the compatible `MEDIA_EMBED_CACHE_PATH`; omitting it can create a cold per-run cache under `/mnt/localdisk/enroot/sks/cache/tests/media-ingest`.
- Prefer compatible warm caches for reruns and related jobs; resolve the existing cache from the run manifest, launcher and release inventory before creating another. Match model/revision, input type, preprocessing/chunking and provenance before reuse; report cache hits/misses and distinguish warm-cache timing from cold computation. Do not clear, merge or repoint shared caches as an incidental fix.
- `/mnt/rag` project paths are shared NFS. `/mnt/localdisk` is node-local storage; use an existing writable project cache/scratch location there for high-I/O work. “Shared” in a local cache path means reuse across compatible runs on that node, not availability on other nodes. Verify mounts, ownership, free space and permissions; do not assume `/var/tmp`, a home/root cache or the same pathname on another node is NVMe or contains the same data.
- Coordinate cache writers and honor the cache format's locking rules, particularly SQLite; reuse read-only artifacts where possible. Preserve manifests, logs and irreplaceable outputs in the approved durable location before local cleanup or node migration. A missing local cache does not invalidate historical results or authorize recomputation.
- Treat `.env*` files as private runtime inputs. Use the task's approved profile and documented launcher/loading order; record the selected filename and variable names needed for reproduction, never secret values. Keep files Git-ignored, preserve restrictive permissions and avoid shell tracing or environment dumps. Do not substitute a different org/backend/credential profile merely to make a command run.

- Standard dev/demo ports remain API/UI `8810`/`8314` and `8800`/`8307`; multimodal runbook examples use `8956`/`8317`. See `docs/runbooks/operations.md` and `docs/guides/kcm-multimodal-e2e-runbook.md`. Deployed customer/OU services can use different ports; consult the active release handoff and inspect the listener, process checkout and health before launch or reuse. Never stop an existing listener merely to reclaim an example port.

## Current Sources of Truth

Open only the authority relevant to the task:

- stable product rules: `docs/engineering/sks-invariants.md`
- runtime defaults: `config/capabilities.yaml` and
  `docs/design-decisions/tech-stack.md`
- org/source/phase definitions: `config/orgs/`, `config/sources/`,
  `config/phases/`
- release inputs: `docs/guides/sks-release-inventory.md`
- media releases: `docs/guides/immutable-media-release-operations.md`,
  `docs/guides/kcm-multimodal-e2e-runbook.md` and `docs/guides/media-ingestion.md`, and the applicable modality guide
- REST/MCP contracts: `docs/api/rest-endpoints.md`,
  `docs/api/mcp-tools.md`, `docs/api/context-pack-schema.md`
- tests/CI: `docs/guides/test-suite.md`, `tox.ini`, `ocibuild.conf`

`kcm_config.yaml` is not the current source of truth. Release/capture
locations are resolved through the release inventory and source configuration,
not copied into this overlay.

## Production Branch Guardrails

Treat `mm_deploy` (and any `mm_prod` release worktree) as a release line: keep
changes narrow, reversible, and evidence-first. Prefer `SKS_*` configuration;
do not add new KCM-only controls or infer behavior from org names.

Use fresh orgs for new release contracts, allow only the planned reset, pin
stage fingerprints, and keep force-merge disabled until full-corpus validation
passes. Validate vector, graph, API, permissions/privacy, and retrieval quality
independently. Never commit owner-private `.env.media*` files; if an explicitly
approved copy is needed locally, keep it ignored, mode `0600`, and hash-pinned,
and let release manifests identify it without exposing values.

Until the multimedia production freeze is lifted, do not use test-first/TDD or
create broad new test suites here. Reconstruct the checked-in behavior first,
then make the smallest change at an existing product seam; prefer existing
config validation, lint, dry-run/preflight commands, and bounded E2E evidence.
Add a focused regression test only when a high-risk correctness, privacy, or
recovery contract cannot be demonstrated with existing coverage; record
deferred tests in the release handoff.

## Multimedia Ingestion Lanes and Data Placement

Create or use a dedicated worktree for `mm_fix`-derived ingestion and
performance work, starting from an explicitly verified base. Inventory
registered worktrees before mutation; never switch, merge, rebase, or copy
across a dirty or branch-owning sibling. Keep mutable branch heads and worktree
status in a scoped handoff or continuity pointer, not in this file.

Bind every benchmark, validation, and release claim to the exact HEAD, relevant
dirt, configuration, inputs, cache posture, stage filesystem, interpreter, and
SQLite version. Material code, configuration, staging, or runtime changes
invalidate affected historical rungs. Cache-hit evidence does not validate a
cold/provider path. Never profile a graded arm or edit executable surfaces in a
worktree while its ladder is running; attribute a performance change causally
only when the treatment isolates the variable and retains a control.

Reserve the top levels of `/mnt/localdisk/enroot/sks/data/` and
`/mnt/localdisk/enroot/sks/cache/` for active or deferred production assets
shared across data sources; content/model-keyed extraction and embedding caches
may remain there for cross-org reuse. Development, smoke, bounded, failed, and
performance runs go under `/mnt/localdisk/enroot/sks/data/tests/<category>/<run-id>/`
with their staging, query, and run-specific caches under
`/mnt/localdisk/enroot/sks/cache/tests/<category>/<run-id>/`. Never use a
repository-relative stage-ledger or SQLite path for those lanes (the checkout
is on NFS); preflight and receipts record the resolved path, filesystem kind,
and controlling fingerprint. Do not create test-shaped `mm_prod*` directories
under either shared root. Before relocating historical evidence, confirm no
process owns it, compare pre/post hash manifests, retain a relocation receipt,
and never rewrite a sealed release contract during archival.

## Runtime, Branch, and Worktree Safety

- Inspect `HEAD`, `main`, `origin/main`, worktree registration, and dirt before
  branch/worktree actions.
- Never switch a dirty root checkout merely to isolate work; use an isolated
  worktree, and remember that ignored local notes do not follow it.
- Never reset, clean, delete, or overwrite unrelated user work. Use
  `git worktree move` for registered worktrees.
- Never mutate an existing release org to test a new ingestion contract; use a
  bounded or newly named org.

Long-running jobs and services need persistent ownership (`tmux` or the
approved supervisor), stable logs, and recorded command/checkout/commit/env/
org/port/bind identity. Validate health and a representative request through
the same login-node, proxy, tunnel, or compute-node path users will use. Status
reports distinguish live from historical state and include owner, stage,
completed denominator, timestamp, observed throughput/ETA, cache behavior,
backend visibility, and errors/retries.

## Task-Scoped Validation

Run the smallest proof covering the changed behavior: vector/OpenSearch
mapping/ID tests plus finalize/visibility and one intended-org query; graph
counts and exact URI preservation; bounded snapshot/load/finalize with reset,
resume, and replay evidence for ingestion; affected API/MCP modes, filters,
graphless behavior, required fields, and privacy; immutable experiment identity
and per-query evidence for evaluation; masked and unmasked privacy surfaces;
the relevant tox lane only (`unit_tests_oci` mirrors CI; `unit_tests_ingestion`
for ingestion changes), excluding `sks_support` unless reopened.

```bash
git status --short --branch
git worktree list --porcelain
make help                         # phase-media-*, media-prod-*, verification targets
conda run --no-capture-output -n okb_dev \
  python -m pytest tests/path/to/test_file.py -q
conda run --no-capture-output -n okb_dev \
  python -m tox -e unit_tests_oci -- --collect-only -q
```

Keep environment/setup failures separate from product-test results.

## Task and Documentation Discipline

- Plan genuinely multi-step or architectural work before editing.
- Use `tasks/todo.md` for objective open gates, `tasks/done.md` for verified
  closure, `tasks/memory.md` for durable state, and `NOTES.md` for user-note
  reconciliation (this checkout keeps its own ledgers; the ADR register lives in
  the primary checkout).
- Keep local plans/research local unless the user requests a tracked surface.
- Never commit generated eval reports, secrets, wallets, local env files, or
  plan drafts without explicit approval.

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

Use the narrowest matching SKS skill and load its sealed operational contract.
The installed-suite admission check remains mandatory per invocation; a valid
SessionStart does not replace it.

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

Use the checkout-configured `sks-terminal-review` profile only when the user
explicitly requests a terminal architecture ruling or release adjudication
(`codex exec --profile sks-terminal-review`, resolved from
`${CODEX_HOME:-$HOME/.codex}/sks-terminal-review.config.toml`). Before launch,
follow the checkpoint-evidence reference in `agentic-sks-release-review`;
terminal review does not broaden mutation authority, and `/tmp`-only evidence
is not durable release evidence. If the profile is unavailable, label the
result preliminary and do not issue terminal approval.


## File Ownership

Use Git history/blame when intent is unclear. Avoid unrelated refactors and
formatting churn. Preserve compatibility deliberately and fix root causes
through existing product paths rather than adding a one-off parallel path.


### Combined CBM code and Markdown index (2026-09-17)

CBM uses one project index containing source plus all supported files recursively in `docs/`, `poc/`, `scripts/`, and `tasks/`, and Markdown elsewhere with traversable parents. Git exclusions relocated into the Git common directory's `cbm-docs-git-excludes`, configured through repository-local `core.excludesFile`, preserve Git ignored status. `.cbmignore` reopens the approved folders and Markdown while retaining the `sks_support` and nested-worktree boundaries. The three installed dependency directories under `poc/video_fast_profile_nemotron_omni/` (`.venv/`, `.venv-torch210/`, and `.transformers56-overlay/`) are excluded explicitly; the POC source and reports remain included. The node-local CBM installations intentionally do not read repository-local `core.excludesFile`, so these Git-only exclusions preserve Git ignored status without blocking CBM; root and nested `.gitignore`, `.git/info/exclude`, and intrinsic filters can still exclude paths. Recheck ignore behavior and Git parity when upgrading. Refresh this existing project index after source or documentation changes only when explicitly authorized; do not create a separate documentation index.

## Project Wiki Maintenance and Task Continuity

- Use the installed `research-knowledge-map` skill for this project's existing OKF wiki at `docs/wiki/`; follow its project-setup and OKF references when changing layout or page metadata.
- At task startup and after context compaction, read the named task handoff, `docs/wiki/index.md`, and only the relevant wiki pages and canonical sources. Check `.agent-notes/INDEX.md` and its matching task record where maintained. Follow relevant handoff links to approved private receipts and command notebooks; report missing or inaccessible sources rather than inventing context.
- Keep task-specific objectives, restart prompts, mutable host/artifact state and pending recovery gates in scoped handoffs. Do not turn one task's instructions into project-wide policy or treat a historical command as authorization to execute it.
- Original code, configuration, reports and source documents remain authoritative. Distinguish historical completion from current input availability; preserve source, observation date, execution host/scope and evidence status for consequential claims. A new note does not reverify an old result.
- Before finishing substantive work that changes durable project knowledge, update only affected wiki pages, source references, relevant indexes and the change log. Routine questions, trivial edits and unchanged knowledge need no entry. Routine scoped upkeep is authorized; bulk ingestion and broad refreshes require explicit scope.
- Preserve existing handoffs and source documents in place. Create a uniquely named new handoff for a new migration/continuation receipt; do not overwrite old evidence. Preserve personal annotations, unfamiliar metadata, contradictory findings and negative results.
- On shared NFS, consult the wiki's recorded coordinating writer and current ownership before overlapping edits. Use one writer for shared pages/indexes; Git history is not a cross-host lock. If ownership or overlapping changes are unresolved, save a unique contribution under `docs/handoffs/wiki-contributions/<date-and-task>/` outside the wiki bundle and report exact consolidation needs. Preserve existing published contribution layouts; do not relocate them merely to match this fallback.
- Keep secrets, raw conversation archives and private global guidance out of the wiki. Link approved private companions instead of copying their contents; an ordinary Git clone or wiki export may omit those dependencies.
- Wiki upkeep adds no background writer or automatic execution. It does not authorize embedding, experiments, index mutations, cache merges, authentication changes, service operations or CBM rebuilding. Continue only with the next objective authorized in the active task; obtain missing objective-specific decisions before dependent operations.
- If the knowledge-map skill or a required source is unavailable, report the gap and preserve a concise handoff instead of claiming successful wiki maintenance. Before finishing, verify changed links/metadata and report pages changed, deferred contributions and remaining evidence gaps.

### CBM scope correction (2026-09-17)

- Exclude generated root output/storage/log/runtime trees, installed dependencies, historical CBM snapshots and nested worktrees from the parent index.
- Index a separately used worktree under its own path when explicitly requested; do not mix its branch with the parent graph.
- Keep docs/, tasks/ (except nested worktrees), poc/ and scripts/ source/documentation included, subject to the explicit runtime/dependency boundaries in .cbmignore.
- Media data/ remains excluded. The exact Transformers dependency overlay under the Nemotron POC remains excluded.
- Git ignored status was verified unchanged after this correction. Index builds were restarted with the corrected policy; do not treat the preceding broad build as complete evidence of intended scope.

## Task-Based Skill Selection

These project routes supplement the global guidance and current session skill catalog. Automatically select the narrowest applicable skill, read its `SKILL.md`, and load references only as needed; this is not an all-skills checklist. Existing project-specific routes, admission checks, ownership and delegation policies remain authoritative. Name the selected skill and its relevant instructions in any subagent brief; routing adds no execution authority.

- Module/interface design: `codebase-design`; scoped architecture audits or boundary improvements: `improve-codebase-architecture`.
- Defect diagnosis: `diagnosing-bugs`; domain-wide invariants or generated-input tests: `property-based-testing`.
- Exportable research figures and figure QA: `scientific-visualization`; substantial architecture or dataflow diagrams: `archify`.
- Application UI design: `frontend-design`; measured web loading or rendering performance: `web-performance`.
