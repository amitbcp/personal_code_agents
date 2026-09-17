# Adaptations from the upstream baseline

Baseline: fcf3ff0 (2026-09-16). Original files are recoverable from that commit; provenance.json points to upstream revisions. This document identifies changes to imported material, including Apache-licensed files.

## Agents

The five VoltAgent definitions use the owner's Astra/low policy and explicit read-only versus implementation boundaries. Adaptations cover evidence-based code review, retrieval/multimodal evaluation, primary-source research, reliable pipelines and measured performance. Remove exceptions permitting omitted contrary evidence or unsupported claims. Agent invocation does not authorize deployments, publishing, resource changes or termination of another task.

## Skills

- **train-sentence-transformers:** replaced the entrypoint and broad training recipes with a focused workflow and two evaluation/CrossEncoder references. Removed default public Hub publishing, prescribed trackers/verdicts, fixed loss/activation/early-stopping recipes and cloud-job defaults. Preserve project model family/environment/trainer; check installed APIs, split hygiene, real candidate pools, paired uncertainty and checkpoint reload. Distinguish sigmoid monotonicity from finite-precision saturation.
- **hf-mem:** added limits of estimates, allocation/unified-memory interpretation, runtime overhead and credential handling. Tool versions must be recorded if installed; this skill does not launch jobs.
- **jupyter-notebook:** resolve the helper relative to the loaded skill instead of rewriting CODEX_HOME. Default output now derives from the working project, not the skill checkout. Preserve overwrite protection; test output location, notebook shape and overwrite behavior. Clarify compute/execution boundaries.
- **hypothesis-generation:** compact ML rival-test workflow with conditional domain-specific gates and existing authorization; retained local validators are optional aids, not scientific proof.
- **get-available-resources:** targeted additions to the upstream allocation/resource guidance; planning is advisory and never authorizes terminating healthy work. A memory-budget warning is not a safe-to-launch decision. Retained scripts remain unchanged.
- **ml-paper-writing:** narrow, model-neutral paper workflow with verified citations and current venue requirements. Retained three focused writing/citation/checklist references and a portable MIT license; removed dated conference templates and redundant reference catalogs. Acquire the official current template only for an actual venue task.

Whole upstream catalogs, installers, invented agent histories, cloud orchestration layers and duplicate artifact tools are not bundled as active components. The baseline retains removed material for provenance, not recommended execution.

## Expanded research workflow review

Add three original project procedures: literature-survey, paper-reading, and research-knowledge-map. These are not unchanged upstream imports; their conceptual sources are identified in the research workflow guide. No new runtime, watcher, index database or cloud dependency is introduced.

Add an ML ablation design reference to hypothesis-generation, covering matched budgets, component interactions, retraining versus inference removal, independent final evaluation, preserved run records and shared-server execution boundaries. Clarify author-side writing versus assigned confidential peer review in ml-paper-writing. Keep the existing five agent roles.

## OKF project wiki setup

Expand research-knowledge-map in place for Google OKF v0.2, preserving its name and the five-agent/nine-skill collection. Add self-contained format and project setup references, including an original project-root maintenance rule. Routine task-end updates use standing project authorization; bulk imports remain explicitly scoped. Preserve raw sources, personal annotations and historical verification context, and coordinate shared-file writers. No runtime, hooks or active-profile changes.

## Final predeployment audit — 2026-09-17

This is not a minimally edited mirror. All five agent instruction bodies were rewritten; hypothesis-generation, ml-paper-writing and train-sentence-transformers were substantially narrowed. hf-mem, get-available-resources and jupyter-notebook retain most upstream structure. The three original research skills have no upstream file baseline. See [change scope and final audit](review/final-predeployment.md).

Resolve inherited hypothesis-reference human-review gates to agree with the entrypoint, identify the historical upstream-only security report, and document the optional formal schema's inability to represent authorized external sensitive-data use. Helpers remain unchanged; do not falsify declarations to satisfy them. Restore concise retrieval prompt/scoring parity and in-batch false-negative checks, pipeline evolution semantics, and manuscript template-migration guidance. Clarify CBM fallback and performance-role scope.

Fix inherited nbformat 4.5 templates by adding stable unique cell IDs and removing an unobserved Python version claim; the helper also stops imposing that version. A new generated-notebook regression failed for both kinds before the fix and passed afterward. Both templates and generated outputs were checked with the installed nbformat validator.

## Write-enabled agents, autonomy and bullet formatting — 2026-09-17

- Set all five agents to workspace-write and remove role-wide analysis-only restrictions. Evaluation and performance can implement and run assigned work; literature can maintain artifacts; reviewer can reproduce/test and fix when included in the task. Explicit review/planning-only requests remain scoped.
- Use headings and bullets in every agent instruction body and all nine skill entrypoints, retaining substantive content. This formatting change makes historical line counts incomparable without word counts.
- Explain shared Vulcan NFS versus node-local NVMe and ownership of shared writes. Use local storage for staging/scratch/caches where suitable and preserve durable results; no existing cache or database is migrated.
- Clarify autonomous routine choices and existing authorization. Resource detection remains non-executing; its output no longer reads as a prohibition on continuing an already-authorized workload. Remove human-brainstorming and unconditional preregistration-review prerequisites while retaining actual study/policy requirements.
- Separate earlier optional-cookbook removals from necessary corrections in the current design report. Those reductions were design choices, not native-format requirements. No further supporting recipes are removed in this update.
