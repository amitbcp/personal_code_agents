# Deployment alignment review — 2026-10-23

## Outcome

- Source baseline before this task: `d31fc18` on `codex/research-helper-refresh-20261002`, last committed October 5. A fresh fetch and remote-head comparison matched local HEAD; there was no unpublished source work or new remote branch commit.
- All 231 selected skill files and five custom-agent files match byte-for-byte on the Mac and both effective node-local Vulkan profiles. No selected file is missing, changed or unexpectedly added inside those components. Generated Python caches were excluded from the comparison.
- All seventeen library skills are present. The five custom agents consistently use `gpt-6-astra`, low reasoning and workspace-write. The broader owner policy also permits Luna/max; this review did not silently change configured agents to another model.
- No runtime library file needed copying, reinstalling or committing from a deployed profile. This update adds reusable instruction examples and maintenance documentation, not a new skill baseline.

## Gaps corrected

- Add [the project AGENTS example](../templates/project-AGENTS.example.md), with canonical-source entry points, completion/delegation, all seventeen skill routes, separately installed CBM, scoped OKF upkeep, single-writer coordination, environment/cache ownership and verification.
- Add [instruction-layer guidance](../docs/instruction-layers.md), explaining what belongs in global versus project instructions, what stays outside Git, and how to check source/deployment parity without installing duplicate skills.
- Both server global guides had strong wiki rules and the engineering routes, but lacked explicit triggers for eight installed research/resource skills. Add the missing routes and five specialist-agent mappings in place with local backups. Preserve existing guidance, model policy and active runtime configuration. Personal global files were not copied into this repository.
- Replace one stale current-version label in a shared project's CBM guidance with a version-neutral description. This changes documentation only; it does not change index settings or authorize a rebuild.

## Ownership boundaries

- The installed profiles also contain system/plugin components, project-owned workflow skills and separately managed CBM components. Those are outside this library's seventeen-skill/five-agent count and were not imported wholesale.
- Project-owned services, ports, environment names, configuration secrets, private receipts and operational paths remain with their approved local/project sources. The template uses portable example paths and must be adapted before installation.
- Existing global/project guides need compatible rules, not byte-identical contents. Project-specific contracts and sources remain authoritative for their scope.
- This branch update does not merge into `main`, overwrite active project guides with the example, install hooks, reindex projects, restart sessions or guarantee automatic skill invocation.

## Verification and limitations

- `python3 scripts/validate.py`: passed five agent definitions, 23 Python sources and 24 provenance mappings.
- `python3 -m unittest discover -s tests -v`: 32 tests passed.
- New/changed document links and whitespace checked; independent guidance review confirmed scoped wiki upkeep, delegation and shared-storage boundaries.
- Selected deployed-file comparison proves source parity at review time. It does not establish that an agent used every skill or that these instructions outperform alternatives. Fresh runtime discovery was separately verified during the preceding deployment/CLI upgrade; this documentation-only update did not repeat those runtime tests.
- A live project's instruction edit can make the copy of that file in its existing graph stale until an authorized refresh. Current instructions must be read from source; no rebuild was started solely for this wording correction.
- Exact host-specific receipts and backups are retained in the operator's private maintenance handoff outside this repository.
