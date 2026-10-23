---
name: ml-paper-writing
description: Draft, revise, and review ML/IR and multimodal research manuscripts or rebuttals using traceable experimental evidence, verified citations, and current venue requirements. Use for research papers and paper sections; preserve the project's existing writing workflow.
---

# ML Paper Writing

- Turn research artifacts into clear claims a reader can verify.
- Match the requested deliverable: editing a paragraph does not require rebuilding a manuscript or running new experiments.

## Start from the project

- Read the current manuscript, relevant experiment records, figures/tables, bibliography, and project writing instructions.
- Reuse the existing LaTeX/Markdown/Word structure, citation keys, notation, build command, and collaboration conventions.
- Treat draft text and old notes as claims to check against source artifacts.

- Proceed with authorized drafting and revision.
- Ask only for consequential information that is missing, such as which conflicting result is authoritative.
- Continue independent sections while recording the gap.
- Do not impose a confirmation gate before writing.

## Connect claims to evidence

- For each substantive contribution, identify the supporting experiment, derivation, or source and its scope.
- A small claim/evidence table is useful for a new manuscript or major revision:

| Claim | Evidence location | Conditions and limitations | Status |
|---|---|---|---|
| Proposed claim | Existing table/run/section/source | Dataset split, baseline, assumptions | Supported / partial / unresolved |

- Distinguish measured results, interpretation, hypotheses, and planned work.
- Never fill missing results with plausible numbers or convert a qualitative example into an aggregate finding.
- Mark unresolved facts clearly in drafts; remove or qualify them before finalization.

- For empirical results, preserve the actual protocol: dataset/version and grouping, train/development/test boundaries, baselines, selection procedure, model/prompt/checkpoint versions, metric definitions, seeds, hardware, cost and latency where relevant.
- State whether uncertainty is standard deviation, standard error, or a confidence interval and how it was computed.
- Do not claim statistical significance from point estimates alone or invent missing runs.

- Use development data for tuning, prompt selection, calibration, and ablations.
- Preserve the project's held-out test protocol; do not rerun or tune against a test set to improve the story.
- Suggest missing experiments separately with their purpose and resource needs.

- **IR/reranking:** Report retrieval candidate generation, cutoff, relevance judgments, candidate recall, ranking metrics, and aggregation unit. Keep queries/documents or other leakage groups separated according to the protocol. Compare rerankers on the same candidate pool when isolating reranking effects.
- **Agentic RAG:** Separate retrieval, grounding/citation quality, answer quality, tool/task success, and operational cost. Validate any LLM judge against human labels and disclose disagreement.
- **Multimodal/spotdiff:** Preserve image-pair identity and source grouping across splits. Report change/no-change cases, localization or grounding measures when applicable, and error slices such as small changes and distractors. A generic image similarity or VLM benchmark score does not establish paired-image change-detection quality.

## Draft and revise

- Organize the paper around the supported contribution and the questions its experiments answer.
- Explain the problem, closest prior work, method, evidence, and limits in an order suited to the venue and existing draft.
- Do not force a fixed paragraph count or page allocation.

- Use [story-evidence-review.md](references/story-evidence-review.md) for reverse outlining, story-to-result alignment and evidence-anchored review.
- Use [writing-guide.md](references/writing-guide.md) for a substantial drafting or revision pass.
- Preserve technical meaning and uncertainty while improving clarity.
- Describe incremental work honestly; do not disguise extensions as wholly new methods.

- Use [citation-workflow.md](references/citation-workflow.md) whenever adding or checking citations.
- Source metadata verifies a paper's identity; reading the relevant content verifies whether it supports the claim.
- Neither a search ranking nor a keyword match is sufficient.

- For a rebuttal, address each substantive concern with evidence and an exact manuscript location or concrete revision.
- Distinguish completed changes from proposed experiments.
- Do not promise unperformed work or imply submission/publication authorization.

## Venue and final checks

- This skill supports author-side writing and critique.
- For an assigned confidential peer review, first check the venue's current AI and confidentiality policy; permission to write your own paper does not establish permission to process another author's confidential submission.
- For conference-oriented evidence preparation, use [the research workflow guide](https://github.com/amitbcp/personal_code_agents/blob/main/review/research-workflow.md).

- For venue-specific preparation, read the current official instructions for the exact venue, year, track, and submission stage.
- Record the source and access date in the project notes.
- These instructions determine page limits, templates, anonymity, supplements, checklists, disclosure, and bibliography format.
- Do not infer current rules from older papers or this skill.

- Use the project's existing template when appropriate.
- If replacement is necessary, obtain the official current template for the requested venue and preserve its notices; do not change margins/fonts to bypass requirements.
- For a venue/template migration, first compile the untouched target template, then transfer manuscript content and bibliography while retaining the target style; do not carry over the old preamble wholesale.
- Preserve the original manuscript so formatting failures can be isolated.
- Use the existing build/render workflow and inspect the resulting figures, equations, references, and page breaks.

- Use [checklists.md](references/checklists.md) for a full manuscript handoff.
- Report changed sections, checks actually completed, and unresolved evidence/citation/formatting gaps.
- Do not claim a draft is submission-ready when those checks are incomplete.
