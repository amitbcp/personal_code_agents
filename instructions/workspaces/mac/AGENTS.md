# Repository Guidelines

## Scope & Workspace Structure

`/Users/aamita` is the macOS operations workspace, not a Git repository. Use this guide for system-wide maintenance and standalone tasks. Explicit user instructions and project-level `AGENTS.md` files override these defaults. Keep this file and `~/.codex/guidance/` local; never copy them into repositories.

- `PROJECT_MEMORY.md`: durable machine context and recent work.
- `docs/handoffs/`: dated operational and artifact handoffs.
- `Code/`, `Code_Projects/`, `github/`, `Oracle/`: locations to check for the requested project.
- `Documents/`, `Downloads/`: standalone documents and assets; confirm the current source before editing.
- `.ssh/`, `.oci/`, `.codex/`: sensitive configuration and runtime state.

## Context & Continuity

Read the relevant entries in `PROJECT_MEMORY.md` and the matching `docs/handoffs/` file before execution and after compaction. For repository work, start with canonical docs and `.agent-notes/INDEX.md` where present.

Read applicable guidance under `~/.codex/guidance/`: `karpathy-coding-principles.md` for substantial code work, `scale-and-concurrency.md` for pipelines/services, and `research-engineering-practices.md` for experiments/reports.

Treat historical versions, routes, paths, and fixes as dated evidence. Recheck consequential facts; distinguish observation, inference, and unknowns.

## Commands & Validation

There is no root build command, test framework, or coverage target. Use the target project's documented commands.

- `rg --files docs/handoffs`: locate previous task records.
- `git -C <project> status --short`: inspect repository changes.
- `ssh -G <alias>`: inspect effective SSH configuration without connecting.
- `bash -n <script>`: check Bash syntax without execution.

Run focused checks for changed behavior, preserve exit status, and inspect bounded log excerpts. Verify document renders visually. Ask before jobs expected to exceed ten minutes unless already authorized.

## Style & Change Safety

Match existing indentation and formatting tools. Use descriptive names, quoted shell paths, and `YYYY-MM-DD-topic.md` handoff names. Keep Markdown soft-wrapped.

Make scoped, reversible changes; preserve backups, profiles, sessions, and unintegrated work. Diagnose SSH routing, authentication, and editor failures separately. Verify host identity independently before changing trusted keys. Revalidate historical VPN workarounds before reuse. Preserve the documented ORD separation of durable sessions and local SQLite runtime.

Never print credentials or copy secrets into notes. Obtain authorization for production changes, spending, destructive cleanup, and consequential external actions; do not re-request existing authorization.

## Commits & Handoff

The home directory has no Git history. Within repositories, follow local conventions; use imperative commit subjects and describe behavior, rationale, and validation in PRs. Ask before shared-branch pushes or merges.

Update `PROJECT_MEMORY.md` after significant work. Record outcomes, verification dates, saved paths, blockers, and exact next steps in the matching handoff.

## Task-Based Skill Selection

These project routes supplement the global guidance and current session skill catalog. Automatically select the narrowest applicable skill, read its `SKILL.md`, and load references only as needed; this is not an all-skills checklist. Existing project-specific routes, admission checks, ownership and delegation policies remain authoritative. Name the selected skill and its relevant instructions in any subagent brief; routing adds no execution authority.

- Module/interface design: `codebase-design`; scoped architecture audits or boundary improvements: `improve-codebase-architecture`.
- Defect diagnosis: `diagnosing-bugs`; domain-wide invariants or generated-input tests: `property-based-testing`.
- Exportable research figures and figure QA: `scientific-visualization`; substantial architecture or dataflow diagrams: `archify`.
- Application UI design: `frontend-design`; measured web loading or rendering performance: `web-performance`.
