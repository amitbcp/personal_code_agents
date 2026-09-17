# Research workflow and expanded source review

Reviewed 2026-09-16. This is a selection recommendation for retrieval/reranking, agentic systems, multimodal/spot-difference research, and paper learning/writing. It is not evidence that a skill improves acceptance rates or Astra performance.

## Recommended collection

Keep **five standing agents**. Literature investigation, evaluation, implementation, performance work and independent correctness review are distinct responsibilities already represented. Paper writing and tutoring are task procedures that the main agent or an ordinary worker can use; they do not need additional permanent personas.

Expand from six to **nine skills**, adding three original, compact procedures:

| Need | Component | Useful output |
|---|---|---|
| Understand a field and closest work | literature-survey + scientific-literature-researcher | Query/screening record, evidence matrix, bounded novelty statement |
| Learn a specific paper | paper-reading | Mechanism/derivation, worked example, optional self-checks, unresolved questions |
| Retain research understanding | research-knowledge-map | Linked paper/concept notes and source-backed relationships |
| Turn a finding into a test | hypothesis-generation + eval-engineer | Rival explanations, discriminating experiment and analysis plan |
| Test component contributions | hypothesis-generation's ML ablation reference | Matched comparisons, interactions, uncertainty and selection protocol |
| Run retrieval experiments | train-sentence-transformers + ordinary worker | Project-specific training/evaluation plan and reproducible artifacts |
| Prepare a manuscript/rebuttal | ml-paper-writing | Claim-to-evidence manuscript with verified citations and current venue checks |
| Check resource feasibility | get-available-resources, hf-mem, performance-engineer | Allocation-aware estimates and measured bottlenecks |
| Inspect data or illustrate a mechanism | jupyter-notebook | Reproducible notebook in the working project |

Use only what the task needs. Do not invoke all agents or all nine skills for each paper. Existing artifact tools handle figures, PDFs, documents and presentations. Framework-specific training skills remain optional until the project uses that framework.

## ICLR, CVPR and ACL preparation

Build a claim/evidence matrix early. For each contribution, identify the experiment, derivation or source supporting it, its conditions, and the strongest alternative explanation. Let this determine the ablations and manuscript structure. A paper does not become stronger by accumulating unrelated benchmarks or mandatory experiments that do not test its claims.

The reviewed [ICLR 2026 guidance](https://iclr.cc/Conferences/2026/ReviewerGuide), [CVPR 2026 guidance](https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelines), and [ARR reviewer guidance](https://aclrollingreview.org/reviewerguidelines) emphasize evidence, contribution and appropriate scope. They are dated references, not reusable guarantees about later cycles. For an actual submission, verify the exact year/track's author instructions, templates, anonymity, disclosure and supplements.

For your projects, useful checks include candidate recall versus reranking quality; retrieval versus answer/judge effects; image-pair/source grouping and change/no-change slices; independent evaluation units; resource-matched comparisons; and preserved negative results. A point-score improvement alone cannot establish a mechanism or statistically reliable gain.

Author-side critique and personal reading of public papers differ from assigned confidential peer review. CVPR 2026's reviewer policy restricts LLM-assisted review writing; check the actual venue policy before processing confidential review material. Do not silently reuse author-side skills for that different task. See also [ARR author guidance](https://aclrollingreview.org/authors) and [responsible NLP research](https://aclrollingreview.org/responsibleNLPresearch/).

## Research notes and personal learning

Reuse the project's current notes layout. If none exists, a small `research/` folder with a literature index, paper notes, concept notes and experiment links is enough. This is an example, not a required scaffold. Preserve sources and your own annotations separately from generated synthesis. Link each consequential relationship to its source, version and conditions; preserve contradictions instead of merging them into a confident summary.

Karpathy's public [LLM Wiki note](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) motivates maintained synthesis over source material. We use that idea as a design reference, without copying the gist or installing a wiki runtime. Project Markdown can be shared on NFS; coordinate edits as with other project files. It does not require sharing Codex conversations or live SQLite indexes.

For learning, choose the needed depth, explain a mechanism with a small example, and optionally test understanding through an actual learner answer. [Keshav's reading method](https://cs.uwaterloo.ca/~Brecht/courses/856/readings/how-to-read/keshav-paper-reading.pdf) informs layered reading. Generated notes and quiz solutions are aids, not evidence of mastery. No reminder service or learner-profile database is needed by default.

## Official and author-maintained sources

The original six catalogs have their own full-entrypoint completion ledgers. The additional repositories below were cloned and inventoried at pinned revisions in `additional-sources.json`; `additional-entrypoints.json` records which additional definitions received a complete semantic read. These large new catalogs were investigated for relevant workflows, **not all semantically audited**. A clone or file inventory is not a full review of its scripts, references, binaries or dependency chain.

| Source | Recommendation and reason |
|---|---|
| [OpenAI skills](https://github.com/openai/skills) | Native packaging and useful operational/artifact procedures. Retain the adapted notebook skill; avoid duplicating installed system/artifact skills. Official origin does not make every skill necessary. |
| [Hugging Face skills](https://github.com/huggingface/skills) | Strong fit for model/retrieval workflows. Keep the adapted retrieval and memory skills; choose cloud/jobs/Hub tooling only when the task uses those services. |
| [Anthropic skills](https://github.com/anthropics/skills) | Borrow independent-reader checking and focused skill design. Claude tool names, runtime assumptions and hooks need translation. Public document skills have distinct source-available terms; do not treat the entire repo as uniformly Apache-licensed or copy duplicate artifact packages. |
| [Anthropic Claude Code](https://github.com/anthropics/claude-code) | Public plugins/examples can inform tooling; this is not access to Anthropic's private internal skill inventory. No package from this repo is selected for installation. |
| [DeepMind science skills](https://github.com/google-deepmind/science-skills) | Relevant arXiv/OpenAlex lookup candidates, but lookup clients do not replace survey methodology. The reviewed arXiv helper needs fixes before adoption. Most catalog entries serve other scientific domains. Observe code/material license distinctions. |
| [Microsoft skills](https://github.com/microsoft/skills) | Deep-wiki concepts overlap code orientation already provided by CBM; Copilot continual-learning hooks are not a personal paper-learning workflow. No new runtime selected. |
| [Google skills](https://github.com/google/skills) | Useful when using the corresponding cloud products. The reviewed evaluation flywheel contains workflow pitfalls; no generic research-method advantage established. |
| [Gemini skills](https://github.com/google-gemini/gemini-skills) | API/SDK integration reference when a project uses Gemini. Repository overview inspected; no new research-method skill selected. |
| [NVIDIA skills](https://github.com/NVIDIA/skills) | Nemotron retrieval recipes are a conditional reference if those models/recipes are adopted. NeMo auto-research offers bounded experiment ideas; avoid importing its runtime for an unrelated stack. |
| [Karpathy autoresearch](https://github.com/karpathy/autoresearch) | Author-maintained experimental example: useful baseline/harness/logging ideas. Its unbounded loop, fixed timeout, permission advice and discard workflow are unsuitable defaults for these shared servers. Do not run it as an installation step. |
| [Community Karpathy skills](https://github.com/jokim1/karpathy-skills) | Explicitly community-authored, not Karpathy's own package. Wiki/diff ideas overlap existing guidance; additional helper state and gates are unnecessary here. |

### What Anthropic actually shares about internal use

Anthropic's [public account of internal skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) describes focused categories, concrete failure cases, progressive disclosure and measuring use. These are useful design lessons. It does not publish the complete private inventory. We adopt narrow procedures and concrete checks, without claiming access to internal prompts or importing company-specific automation.

### Concrete findings behind the decisions

- DeepMind's reviewed `search_arxiv.py` prints an accumulating JSON object inside the result loop. An offline fixture produced no JSON for zero results and concatenated objects for two results. The download helpers also return normally after a caught 404. The local reproduction is included under `probes/`; no remote API or upstream dependencies were executed. These findings apply to the pinned revision.
- Anthropic's reviewed skill optimizer describes selecting the best description using repeated “test” scores. That set functions as development data. Keep independent final evaluation separate from iterative selection. This is a methodological issue in the prescribed workflow, not a claim that every skill fails.
- Google's reviewed evaluation flywheel can rerun grading after a code fix without regenerating responses. A research evaluation must connect the current system to newly generated outputs; cached old answers do not test the fix.
- Community wiki guidance adds a manifest, helper workflow and setup gates before some ordinary repo questions. That is avoidable overhead for these projects; the original research-map procedure keeps source links and deliberate updates without introducing a second code-indexing system.

Reproduce the arXiv observation against the pinned checkout without network access:

```bash
python3 review/probes/probe_arxiv_json.py /path/to/science-skills
```

The probe executes only the extracted parser/search functions with a stubbed transport and synthetic XML; it does not import upstream client dependencies. Expected observations are in [arxiv-json-result.json](probes/arxiv-json-result.json).

## New procedure provenance

The three new skills and ML ablation reference are original project instructions, not unchanged upstream imports. They reuse general research methods and cite reviewed inspirations. No new executable dependency is introduced. Earlier unchanged imports remain recoverable from the baseline commit.

Relevant K-Dense source paths at the pinned revision recorded in `sources.json`: `skills/literature-review/SKILL.md`, `skills/scientific-critical-thinking/SKILL.md`, `skills/market-research-reports/SKILL.md`, `skills/ncats-arax/SKILL.md`, `skills/ontology-term-resolution/SKILL.md`, and `skills/hypogenic/SKILL.md`. Their transferable ideas concern search boundaries, validity, claim ledgers, typed relationships and identifier status; their domain runtimes and mandatory workflows are not bundled.

## Validation boundary

All nine skills passed Codex Skill Creator frontmatter checks. The repository's TOML/provenance/Python checks and both notebook regression tests passed. An independent agent completed [a synthetic research task](../tests/fixtures/research-reading-case.md) with the new procedures: its [outputs](behavioral-research-check/outcome.md) preserved a superseded result and personal annotation, caught selection leakage and incomparable scores, explained negative alpha correctly, and drafted a bounded experiment and manuscript statement. Five local output links and the toy arithmetic were checked. This is one behavioral smoke case, without a no-skill comparison.

Frontmatter, local references and repository checks establish packaging consistency. Behavioral smoke cases can reveal obvious mistakes but are not an Astra benchmark, an acceptance-rate study or proof of scientific correctness. Improve these procedures from real project use rather than expanding the catalog preemptively. Nothing in this review installs skills on Mac or servers, launches training, or changes CBM indexing.
