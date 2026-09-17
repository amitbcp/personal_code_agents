# Enable a project wiki

This setup is performed only for projects included in the deployment request. Updating this library alone does not enable any project. The skill remains usable directly for explicit wiki tasks without persistent installation.

## Install once per active profile

Use the library's `skills/research-knowledge-map` directory, including references. Inspect existing discovery locations and same-named skills before copying or symlinking. Current Codex supports personal `~/.agents/skills/` and repository `.agents/skills/`; wrappers and existing `~/.codex/skills` installations require checking the actual profile rather than duplicating definitions. A symlink must resolve on the execution host. Verify discovery separately from Mac and each remote profile using a fresh task. See [official skill discovery](https://learn.chatgpt.com/docs/build-skills).

A shared, reviewed instruction directory can serve multiple projects and hosts. Each project keeps its own wiki. Do not share live databases or change CBM settings as part of this setup.

## Choose the project layout

Reuse an established wiki path; otherwise `docs/wiki/` is a reasonable bundle root. Initially create only the index, log and pages supported by the chosen source set. Concepts, decisions, experiments and questions can become subdirectories as the content grows. Keep personal notes distinguishable from generated prose and define whether they belong in Git. Preserve the project's existing backup and access rules.

Add the maintenance rule to the existing project-root `AGENTS.md` (or the effective project instruction file), merging with local guidance. Do not overwrite the file or copy global user guidance into it. A nested wiki-only instruction is insufficient for work performed elsewhere in the project. See [instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## Suggested project rule

Adapt the paths and scope, then insert this original project-specific block:

```markdown
## Project wiki maintenance

Use the research-knowledge-map skill for the OKF wiki at docs/wiki/.
Before substantive work, read its index and relevant pages alongside canonical sources.
Before finishing work that changes durable project knowledge, update the affected
wiki pages with source-backed decisions, completed experiment results, verified
findings and unresolved questions. Update relevant indexes and the change log.
This authorizes scoped upkeep during the task; routine questions and trivial edits
need no wiki change. Bulk ingestion and broad refreshes require an explicit scope.
Preserve personal annotations, contradictory evidence and historical decisions.
Coordinate overlapping edits with other sessions; do not overwrite their work.
In the final handoff, state which pages changed or any deferred update and why.
```

The rule establishes standing authorization for routine updates within the task. It does not authorize external publication, experiment execution or ingestion of unrelated/private material. If the skill is unavailable, report the discovery issue and preserve a concise task handoff instead of claiming wiki upkeep succeeded.

## Initialize and verify

1. Inventory canonical docs and select a bounded first ingestion: current overview, architecture/decisions and a few important reports. Record exclusions and unresolved historical contradictions. Avoid ingesting all Markdown by default.
2. Build the initial pages using the OKF reference. Check actual source paths and links from each page, not from the repository root. Existing raw files remain unchanged.
3. In a fresh task, ask a decision question and verify the answer traces to a source without modifying files. Then complete a small authorized knowledge-changing task and verify only affected wiki pages, indexes and log are updated. Check personal notes and unrelated files remain intact.
4. For NFS projects, verify the same Markdown is accessible from each node. Assign a single writer for overlapping pages or merge worktree changes. Do not infer locking from shared storage or Git.

No hooks are installed by this procedure. Project instructions guide the active agent; they do not guarantee perfect maintenance or run while idle. Consider a small advisory check only after observing actual missed updates. Any future hook needs deployed-version verification and must avoid recursive continuations or a second concurrent wiki writer.
