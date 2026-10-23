# Research Workspace Guidelines

## Initiative and Task Completion

- Carry the user's intended outcome through to verified completion. Treat requests to do or fix something as execution requests; a plan, diagnosis, first patch, or list of next steps is an intermediate result.
- After each finding or completed step, choose and perform the next necessary action within the authorized objective. Include straightforward implied follow-ups, integration, focused checks, and required documentation; do not wait for another prompt to continue the same work.
- Resolve reversible implementation details using current evidence and project conventions. Ask only when missing information materially blocks correctness or an applicable approval is genuinely absent. Reuse authorization already given; do not ask for it again.
- If one operation is blocked, finish independent authorized work and prepare the blocked action for review. Explain the exact blocker and smallest missing decision; if an instruction requires a pause, identify its file and relevant rule.
- Preserve the objective across status questions, findings, delegation, and compaction. Integrate delegated results and continue; a progress report or task handoff does not itself complete the work.
- Keep follow-ups tied to the requested outcome. Respect explicit pauses, ownership, protected areas, and operation-specific approval boundaries. Do not turn this rule into permission for unrelated backlog work, new experiments, spending, publication, destructive actions, or indefinite optimization.
- Before ending, check the requested outcome against actual evidence. Complete remaining in-scope steps when possible; otherwise report what is verified, what remains, and why. Once the outcome is met, stop rather than inventing more work.

## Research API authorization

- Owner authorization recorded September 18, 2026: use OCI services and available models through instance-principal authentication as needed for authorized research tasks. Sending task-relevant project data to model/service APIs is pre-authorized; do not repeatedly request data-transfer approval.
- This authorization covers API inference needed for the agreed work, not unrelated uploads, publication, credential disclosure, infrastructure changes, or unbounded spending. Preserve explicit dataset/license restrictions and higher-priority security requirements. Record model, inputs, request settings, usage and cost where available; use bounded runs and existing credentials without copying secrets into documentation. Existing approval requirements for jobs likely to exceed about 20 minutes remain in force.

## Scope and startup

- This workspace contains separate research repositories and manuscript worktrees. Select the owning worktree before editing or running Git commands; the parent `.git` directory does not establish a usable repository. Follow applicable nested `AGENTS.md` instructions and preserve unrelated dirty and untracked work.
- Start with the matching record under [docs/handoffs/](docs/handoffs/), then the owning project's canonical sources and current local state. The [T1 START HERE handoff](docs/handoffs/2026-09-15-story-to-frames-t1-START-HERE.md), [main manuscript handoff](docs/handoffs/2026-09-15_iclr-visual-unit-research-migration_185228Z.md) and [alternative manuscript handoff](docs/handoffs/2026-09-15_iclr-alternative-submission-migration_204124Z.md) describe separate scopes; their dated status is historical evidence, not current execution authority.
- For Story-to-Frames, read its [project guidance](tasks/research/story_to_frames_eval/AGENTS.md) and existing [OKF wiki index](tasks/research/story_to_frames_eval/docs/wiki/index.md), including the relevant contribution and current handoff it links. Reuse this wiki for that project; do not create a competing workspace-wide account or merge distinct manuscript ownership by assumption.

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

## Project wiki maintenance

- Use the `research-knowledge-map` skill and the owning project's established wiki. Before substantive work, read its index, relevant pages and original sources. Before finishing work that changes durable project knowledge, update affected pages with source-backed decisions, completed results, verified findings, limitations and unresolved questions; update relevant indexes and the change log. Routine scoped upkeep is authorized. Routine questions and trivial edits need no entry; bulk ingestion and broad refreshes require explicit scope. Do not bulk-import conversation archives.
- Original code, protocols, reports, receipts and signed decisions remain authoritative. Keep observation dates and evidence status explicit; preserve personal annotations, unknown metadata, contradictory evidence and historical decisions. Wiki maintenance does not authorize experiments, remote operations, publication, authentication changes or background indexing.
- Preserve existing handoffs and source documents in place. Put time-sensitive continuity in uniquely named `docs/handoffs/` records in the owning project and link reusable knowledge to its wiki. Keep restricted material at existing approved retrieval references and never copy credentials or raw private conversations.
- Use one coordinating writer for shared indexes and overlapping wiki pages. NFS and Git history are not cross-host locks. Respect the owning project's established contribution paths; Story-to-Frames uses `docs/wiki/contributions/<team>-<date>-<task-id>/`. If coordination is unresolved, save a unique contribution handoff under `docs/handoffs/wiki-contributions/` and specify the exact consolidation needed. Do not overwrite another session's work.
- Report updated pages, source coverage and deferred consolidation in the final handoff. If the skill or relevant wiki is unavailable, report that gap and preserve a concise task handoff instead of claiming successful upkeep.

## Codebase knowledge graph

- Use CBM graph tools for structural code discovery, then verify consequential findings against current source in the owning worktree. Use `search_graph`, `trace_path` and `get_code_snippet`; check per-file `check_index_coverage`, read missed lines directly and qualify incomplete coverage. Use graph Section nodes and document links for indexed Markdown when available; use text search and file reads for literals, configuration, coverage gaps and unavailable graph results.
- On `vulcan-a100v2-7783` only, the node-local CBM wrapper is `/mnt/localdisk/enroot/sks/tools/codebase-memory/cbm` and the project graph name is `mnt-rag-aamita-research-amit`. This names the intended graph, not proof that indexing is ready; inspect live status before relying on it. The graph indexes the actual NFS source root `/mnt/rag/aamita/research/amit`; inspect `index_status` for its current generation after the 2026-10-21 upgrade. Check its recorded root, indexing time and per-file coverage before treating findings as current; later source edits are not automatically reflected. On other nodes, verify the local deployment and graph status independently instead of assuming the 7783 path or index exists.
- Refresh this graph explicitly. At the 2026-10-21 verification on 7783, `auto_index=false`, `auto_watch=true`, `watcher_enabled=true` and `watch_non_git=false`; this workspace root has no valid Git repository, so it is not automatically watched. Inspect the current wrapper configuration and native `index_status` watch object before relying on refresh behavior. Git-ignored wiki/task edits also require explicit refresh because Git-status-based polling does not report them. These are shared daemon settings, so enabling them globally also affects other projects and requires deployment-level verification. Starting a Codex session does not automatically refresh this graph. Keep live SQLite databases and runtime state node-local, preserve `.cbmignore` exclusions, and keep CBM independent from wiki upkeep and conversation management. An index is a discovery aid, not a research evidence registry.

## Task-Based Skill Selection

These project routes supplement the global guidance and current session skill catalog. Automatically select the narrowest applicable skill, read its `SKILL.md`, and load references only as needed; this is not an all-skills checklist. Existing project-specific routes, admission checks, ownership and delegation policies remain authoritative. Name the selected skill and its relevant instructions in any subagent brief; routing adds no execution authority.

- Module/interface design: `codebase-design`; scoped architecture audits or boundary improvements: `improve-codebase-architecture`.
- Defect diagnosis: `diagnosing-bugs`; domain-wide invariants or generated-input tests: `property-based-testing`.
- Exportable research figures and figure QA: `scientific-visualization`; substantial architecture or dataflow diagrams: `archify`.
- Only for research dashboards or other web UI work: `frontend-design` for UI design and `web-performance` for measured web loading/rendering performance; backend or model throughput is outside the latter skill.
