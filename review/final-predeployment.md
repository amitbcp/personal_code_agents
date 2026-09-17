# Final predeployment review — 2026-09-17

> Historical snapshot of the d3554c8 audit. Later user-directed workspace-write permissions and bullet formatting supersede the role boundaries and size table below. See [current design](current-design.md).

## Verdict

The five agents and nine skills follow native Codex package conventions and form a coherent collection for the intended research work. The concrete defects found in this pass were fixed and re-reviewed. The repository is ready for a bounded deployment/discovery pilot. This does not establish a best possible prompt, Astra-specific superiority, or that every remote profile will discover and enforce these settings correctly.

This collection is **not a lightly edited upstream mirror**. Native structure was preserved; instruction bodies and selected scope often changed substantially. Restoring upstream length or bullet layout would not itself improve correctness. Readability comes from clear purpose, routing, steps and references, rather than a mandatory Markdown style.

## Sources and change scope

The original four requested catalogs were VoltAgent, K-Dense, Orchestra and Agency Agents. Active imports come from the first three; no whole Agency persona was selected. Hugging Face and OpenAI are the two additional sources of active skills. Three research skills are original project procedures. Source revisions and licenses remain in provenance.json; the unchanged baseline remains recoverable at fcf3ff0.

| Components | Extent of adaptation | Rationale/tradeoff |
|---|---|---|
| Five VoltAgent agents | Substantial instruction-body rewrites; same native TOML shape and role names | Research-specific evidence checks and distinct execution boundaries. Model/effort follow owner policy. Paragraph form replaces much of the upstream bullet layout. |
| hypothesis-generation | Substantial entrypoint rewrite; broad references/helpers retained | Compact ML workflow with optional formal schemas. Restored consistency between references and routine authorized analysis. |
| ml-paper-writing | Substantial workflow/package reduction; 47 original files removed, including dated templates | Current venue rules and evidence-linked writing replace fixed recipes. Offline venue templates and some editorial examples are no longer bundled. |
| train-sentence-transformers | Substantial replacement: 31 original files become three active files | Project-oriented protocol replaces executable recipes. Specialized cookbooks must be obtained from matching library-version documentation. |
| get-available-resources, hf-mem | Light targeted adaptation | Most upstream text/structure retained, with allocation and interpretation limits. |
| jupyter-notebook | Narrow portability adaptation plus inherited schema fixes | Keeps helper/templates/references; fixes output placement, valid cell IDs and unobserved kernel version metadata. |
| literature-survey, paper-reading, research-knowledge-map | Original procedures | Clear task-specific workflows rather than claimed upstream copies; the map now implements OKF wiki maintenance. |

### Entrypoint size comparison

Counts compare the pinned unchanged baseline with the reviewed result. Lines include frontmatter, configuration and blank lines; fewer lines are not evidence of fewer requirements or better performance. Machine-readable word/line counts: [final-change-counts.json](final-change-counts.json).

| Component | Baseline lines | Current lines |
|---|---:|---:|
| `agents/data-engineer.toml` | 41 | 18 |
| `agents/eval-engineer.toml` | 36 | 16 |
| `agents/performance-engineer.toml` | 41 | 16 |
| `agents/reviewer.toml` | 41 | 14 |
| `agents/scientific-literature-researcher.toml` | 41 | 16 |
| `skills/get-available-resources/SKILL.md` | 277 | 273 |
| `skills/hf-mem/SKILL.md` | 79 | 87 |
| `skills/hypothesis-generation/SKILL.md` | 281 | 61 |
| `skills/jupyter-notebook/SKILL.md` | 107 | 108 |
| `skills/literature-survey/SKILL.md` | Original | 39 |
| `skills/ml-paper-writing/SKILL.md` | 982 | 52 |
| `skills/paper-reading/SKILL.md` | Original | 38 |
| `skills/research-knowledge-map/SKILL.md` | Original | 41 |
| `skills/train-sentence-transformers/SKILL.md` | 109 | 49 |

## Findings resolved

- **Inherited notebook validity:** both templates declared nbformat 4.5 while every cell lacked the required ID. Added stable unique IDs. Removed fixed Python 3.12 metadata because a scaffold does not know the future kernel version; the helper no longer adds it.
- **Conflicting hypothesis instructions:** retained references required human review after every command and human-only citation/novelty verification, contrary to the adapted entrypoint. Routine authorized source checks now agree across references; actual domain approvals and human accountability remain.
- **Historical validation provenance:** the retained security report referred to upstream-only tests/scanners as though available here. It is now explicitly historical, with current checks reported separately.
- **Optional formal schema limitation:** the unchanged hypothesis validator rejects all external sensitive/unpublished-data history, including authorized use. This limitation is explicit in the entrypoint and tool guide; use the Markdown workflow rather than falsely declaring no transfer.
- **Lost retrieval safeguards:** restored train/evaluation/inference prompt, tokenization, pooling, normalization and scoring consistency, save/reload retention, and in-batch false-negative checks.
- **Role routing/coverage:** reviewer now falls back to source search without CBM; performance description exposes its existing read-only analysis scope; data engineering restores conditional late-arrival, coercion, versioning and backfill considerations. Sandbox settings remain unchanged.
- **Paper preparation:** restored a concise safe template-migration procedure and clarified that point estimates alone do not establish statistical significance.
- **Change reporting:** corrected the earlier description of resource guidance as compact; it was a targeted adaptation.

## Structure and instruction quality

Agents carry name, description and developer_instructions, with explicit model/effort and sandbox settings. Four are read-only analysis/review roles; data-engineer can implement within workspace scope. They do not replace ordinary workers or CBM exploration roles. No requirement invokes all roles for every task.

Skills retain name/description frontmatter, focused entrypoints and relative supporting resources. Optional UI metadata is not required for every skill. Shared scientific checks are complementary cross-checks; the distinction between literature search, single-paper learning, hypothesis design, manuscript writing and durable wiki upkeep is explicit. Knowledge-map upkeep is triggered by project instructions or a user request, not an always-running process.

No new orchestration service, database, paid job, credential requirement or deployment hook was added. hf-mem remains an optional tool workflow with disclosed external package/model-metadata dependencies; none were executed during this audit. Legal/scientific correctness is not implied by successful package validation.

## Coverage

Three independent scoped reviewers compared all five agents and the six imported skills against baseline/pinned upstream material. All current imported entrypoints and their retained textual references were read. Notebook helper/templates and selected hypothesis/resource helper paths were inspected. All five agent baseline files, all 44 baseline HF/OpenAI package files, and the three K-Dense/Orchestra entrypoints were directly checked against pinned source bytes in this pass. Historical complete-import verification remains separately recorded.

The coordinating review read the three original skills and OKF setup/format references, checked all skill Markdown local links, integrated findings, and reviewed returned evidence. Deleted source catalogs were compared by inventory/diff and relevant removed sections, not given a fresh all-lines semantic audit. This pass is not a new security audit of every helper internal or every upstream asset.

## Validation actually performed

- Nine Skill Creator frontmatter checks passed.
- Native TOML/provenance/Python validator passed (five agents, fourteen retained Python files, eleven import mappings).
- Notebook regression: the new cell-ID test failed for both kinds before correction, then all three tests passed after correction.
- Both raw templates and generated notebook kinds passed installed nbformat 5.10.4 validation with warnings treated as errors. No notebook kernel or training job was launched by the coordinator; the scoped reviewer also ran the small template code cells in isolated Python namespaces.
- Skill/README local-reference checks and Git whitespace checks passed.
- Independent follow-up reviews confirmed the scoped fixes; the final novelty-reference inconsistency was aligned with the same conditional review policy.

Existing behavioral research/wiki smoke records remain in the review dossier. They are not comparative benchmarks and do not demonstrate optimal prompts. Final server preparation still needs fresh checks of active CODEX_HOME, discovery paths, name collisions, model availability and one representative task per selected role/skill. No live Mac/server installation, CBM setting change or conversation migration occurred in this audit.

Official format references: [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Codex skills](https://learn.chatgpt.com/docs/build-skills), [notebook cell IDs](https://nbformat.readthedocs.io/en/latest/format_description.html#cell-ids).
