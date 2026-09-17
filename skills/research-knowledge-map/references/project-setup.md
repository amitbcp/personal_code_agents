# Enable a project wiki

This setup is performed only for projects included in the deployment request. Updating this library alone does not enable any project. The skill remains usable directly for explicit wiki tasks without persistent installation.

## Install once per active profile

Use the library's `skills/research-knowledge-map` directory, including references. Inspect existing discovery locations and same-named skills before copying or symlinking. Current Codex supports personal `~/.agents/skills/` and repository `.agents/skills/`; wrappers and existing `~/.codex/skills` installations require checking the actual profile rather than duplicating definitions. A symlink must resolve on the execution host. Verify discovery separately from Mac and each remote profile using a fresh task. See [official skill discovery](https://learn.chatgpt.com/docs/build-skills).

A shared, reviewed instruction directory can serve multiple projects and hosts. Each project keeps its own wiki. Do not share live databases or change CBM settings as part of this setup.

## Choose the project layout

- Reuse an established wiki path; otherwise use `docs/wiki/` as the bundle root.
- Use the following default organization. These folder names are our workflow convention, not mandatory OKF categories. Create only directories and pages supported by the selected sources; do not create empty placeholders.

```text
docs/
├── handoffs/
│   ├── <existing-handoff>.md          # Preserve existing documents
│   └── YYYY-MM-DD-<task>-migration.md # New, unique migration handoff
└── wiki/
    ├── index.md                      # Wiki entry point
    ├── log.md                        # Wiki change history
    ├── overview.md                   # Purpose, scope and orientation
    ├── architecture/
    ├── decisions/
    ├── operations/
    ├── research/
    ├── experiments/
    └── questions/
```

- Begin with the bundle index, log and supported knowledge pages. Add directory indexes as navigation grows; extend the layout for project-specific needs.
- Follow [OKF conventions](okf-conventions.md) for metadata and reserved files. `overview.md` and all other non-reserved Markdown pages inside the bundle need a nonempty `type`; folder names do not replace page metadata.
- Keep reusable knowledge in the wiki and time-sensitive migration state in a new handoff. Link between them and to authoritative source documents.
- Keep personal notes distinguishable from generated prose and define whether they belong in Git. Preserve the project's existing backup and access rules.

## Preserve documents and coordinate migration handoffs

- Do not overwrite, rename, move or delete existing handoffs or source documentation as part of wiki initialization or migration preparation. Link to sources in place.
- Create each requested migration handoff under `docs/handoffs/` with a unique date-and-task filename; choose another name if it exists. Begin with a START HERE brief linking the wiki entry point, essential reading, current work and next steps.
- Update existing wiki pages carefully, preserving personal annotations, historical decisions, unfamiliar metadata and other tasks' edits. Do not replace an established wiki with a second generated structure.
- Keep sensitive operational details in an established approved private documentation location and link to it appropriately. If none is known, omit sensitive details and report the gap; never include secrets.
- For a fresh-session handoff, use available task context and relevant project files. Do not bulk-import conversation archives unless explicitly requested. Disclose compacted or missing context and record reviewed versus unread source areas.
- When tasks share a project on NFS, use one writer for overlapping pages and indexes. If overlapping edits are underway, save a unique task contribution under `docs/handoffs/wiki-contributions/` outside the OKF bundle, then report the exact consolidation needed. Do not overwrite shared pages or assume Git provides a cross-host lock.

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
