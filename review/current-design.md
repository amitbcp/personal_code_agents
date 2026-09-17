# Current agent and skill design — 2026-09-17

## Current execution policy

- All five custom agents are `workspace-write`; the old four-read-only/one-writer arrangement is superseded.
- Evaluation can build and run harnesses; performance can profile and implement optimizations; literature research can write surveys, bibliographies and notes; reviewer can create reproductions/tests and apply fixes when the task includes them. Data engineering remains an implementation role.
- Each completes assigned work and necessary follow-through under existing authorization, resolves routine choices, and reports only genuine blockers or missing consequential authorization. Explicit planning-only and findings-only requests retain their scope.
- Write permission is not a request to touch unrelated files. Agents coordinate ownership and preserve other sessions' changes.
- All agent instruction bodies and nine skill entrypoints use headings and bullets. Tables, code examples and ordered workflows remain where they communicate structure better.
- These are repository definitions, not evidence of live installation or host permissions. No Mac or server profile was changed.

## NFS and NVMe

- Vulcan NFS project storage is shared across nodes. Keep durable source, project wiki, final reports and required experiment results there according to project access rules.
- NVMe belongs to one node. Use suitable local paths for scratch work, staged hot inputs, environment/runtime caches and temporary output; verify mount, ownership, capacity and the assigned execution environment.
- Shared source paths do not imply shared processes, CUDA state or usable caches. Coordinate overlapping writes on NFS; use one writer per output or isolated worktrees with deliberate merges.
- Preserve useful results on durable storage before node/allocation loss. Local storage is not a backup.
- Existing CBM/live-database paths require their own compatibility and ownership checks. This policy does not relocate them; CBM indexing remains separately controlled.
- Use assigned CPU/RAM/GPU capacity effectively through measured batching and concurrency. Avoid oversubscription and unnecessary NFS traffic rather than imposing universally low worker counts.

## Why the previous scope was reduced

- The previous adaptations were a discretionary redesign around IR/reranking, agentic RAG, multimodal research and paper workflows. Codex did not require those reductions.
- Corrections to unsuitable defaults were separate from reductions in reusable examples. Removing automatic public Hub uploads, mandatory confirmation gates, fixed log conventions or dated venue rules did not require removing all supporting recipes.
- The smaller entrypoints preserved central research contracts, while some optional procedural coverage was lost. Shorter prompts have not been shown to perform better here.
- This update restores write/implementation scope and changes presentation. It does not remove more recipes or silently claim the earlier deleted examples have been restored.

| Component | What changed before this update | Practical consequence |
|---|---|---|
| Agents | Research emphasis replaced broader engineering wording; long bullet lists became paragraphs. Four read-only sandboxes were inherited from upstream and made more explicit. | Line counts exaggerated the reduction. All five now have write access, task-scoped autonomy, and editable bullet sections. |
| Hypothesis generation | Main workflow was shortened and focused on ML rivals, falsifiers and evaluation. Most broad references, templates and helpers were retained. | Primarily entrypoint/routing reduction; optional formal tools remain, with their limitations documented. |
| Sentence Transformers | 31 files became three: optional LoRA, Matryoshka, distillation, multilingual, static embedding, mining, troubleshooting and other recipes were removed along with executable examples. | Real reduction in packaged convenience, not inability to perform these tasks. The agent must use project code and matching official library documentation. |
| Paper writing | Dated venue template bundles and long editorial/reviewer examples were removed; evidence, citations, rebuttal and venue-check workflow remain. | Current templates must be obtained for the actual venue. Useful optional examples were also lost; their removal was not a Codex requirement. |
| Resources, HF memory, notebooks | Mostly targeted adaptations; notebooks additionally had inherited schema/metadata fixes. | Most upstream package structure remains. |
| Literature survey, paper reading, OKF wiki | New project procedures rather than edited upstream copies. | No meaningful upstream line-count denominator. |

- The unchanged baseline and pinned source provenance preserve the removed material. Useful recipes can be restored as versioned, on-demand references without restoring inappropriate defaults; restoration needs targeted API/example review before claiming executability.
- Supporting references are loaded when relevant. Keeping useful optional material need not mean loading an entire cookbook into every task.

## Current size comparison

- Each value is **lines / whitespace-delimited words**, including metadata and headings. Counts describe packaging, not model quality.
- The previous audit table is historical. Agent word totals at that audit were much closer to baseline than line totals because paragraphs compressed many lines. New autonomy/storage instructions add content; bullet formatting increases lines without deleting instructions.
- Original means there was no file in the unchanged import baseline. [Machine-readable counts](current-change-counts.json).

| Component | Upstream baseline | Prior audit snapshot | Current |
|---|---:|---:|---:|
| data-engineer.toml | 41 / 287 | 18 / 268 | 58 / 480 |
| eval-engineer.toml | 36 / 236 | 16 / 245 | 52 / 460 |
| performance-engineer.toml | 41 / 300 | 16 / 252 | 51 / 462 |
| reviewer.toml | 41 / 295 | 14 / 247 | 50 / 439 |
| scientific-literature-researcher.toml | 41 / 338 | 16 / 253 | 50 / 443 |
| get-available-resources | 277 / 1316 | 273 / 1394 | 270 / 1509 |
| hf-mem | 79 / 440 | 87 / 569 | 97 / 586 |
| hypothesis-generation | 281 / 1946 | 61 / 929 | 97 / 977 |
| jupyter-notebook | 107 / 521 | 108 / 602 | 122 / 628 |
| literature-survey | — / — | 39 / 540 | 68 / 579 |
| ml-paper-writing | 982 / 5246 | 52 / 806 | 84 / 853 |
| paper-reading | — / — | 38 / 586 | 60 / 616 |
| research-knowledge-map | — / — | 41 / 682 | 73 / 724 |
| train-sentence-transformers | 109 / 1176 | 49 / 596 | 62 / 616 |

## Verification and limits

- All five TOMLs parse and select workspace-write; independent review found no remaining blanket read-only/advice-only role restriction.
- All nine skill entrypoints pass frontmatter validation. Eight received formatting-only changes with wording preserved; resources also received the stated authorization/storage clarifications. Code blocks, links and frontmatter were preserved during formatting.
- Removed a human-brainstorming prerequisite and made preregistration review conditional on the actual study/policy. Detector/planner tools remain non-executing, but do not block a separately authorized workload.
- Repository/native/provenance checks, existing notebook regressions, local-link checks and whitespace validation passed. No new runtime or agent efficacy benchmark was run for this instruction update.
- The review supports consistency and deployability for a pilot, not a best-possible-prompt claim. Actual profile discovery, writable roots, model availability and representative tasks still belong to deployment.
