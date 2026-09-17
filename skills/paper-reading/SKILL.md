---
name: paper-reading
description: Teach or critically read an AI research paper, explain its equations and experiments, and create personal learning notes or comprehension exercises. Use for understanding a specific paper; use a literature survey procedure for multi-paper search and synthesis.
---

# Paper Reading and Learning

Help the reader understand what the paper establishes, how it works, and what remains uncertain. Match the requested depth and existing background; explaining one equation does not require a full review.

## Anchor the reading

Load the actual paper and identify its version. Use supplements or code when the question depends on them. State what was accessible and read. An abstract supports an overview, not claims about unseen proofs, experiments or implementation. Preserve the user's notation where possible and map any renamed symbols explicitly.

Offer a layered reading when useful: orient on the question and claimed contribution; work through the mechanism and evidence; reconstruct the difficult derivation or experimental logic. Let the learning goal determine depth. A summary is not evidence that the user understands the paper.

## Explain mechanisms precisely

- Connect each important symbol to its mathematical meaning, shape or units, and role in the method. State assumptions and distinguish definitions from derived results.
- Explain a derivation step by step where requested. Check dimensions and a simple limiting case. If a step is missing or cannot be justified from the source, name the gap rather than inventing a proof.
- Use a small worked example to expose the mechanism. Label invented examples as illustrations, not published results. Execute a toy calculation only when useful and permitted; do not launch paper-scale training to teach a concept.
- Read key figures/tables in context: axes, denominator, comparison, uncertainty and scope. Explain what would change the interpretation. Treat examples, aggregate measurements, theoretical guarantees and hypotheses as different evidence types.
- Compare the method with the closest relevant baseline, using verified sources when bringing in other papers. Explain what is held fixed and what actually changes.

## Critique without inventing defects

Check whether the evidence supports the stated claim under its assumptions. Consider split leakage, selection, dependence, missing controls, judge validity and alternative explanations when relevant. Tie criticism to a source location and consequence; no quota of weaknesses or mandatory rejection verdict. Distinguish missing reporting from demonstrated implementation errors. Proposed experiments remain proposals.

For author-side rehearsal or public-paper study, critique normally. If this is an assigned confidential peer review, check the applicable venue's current AI/confidentiality rules before processing the material. A public-paper learning workflow does not override those rules or authorize disclosure.

## Support personal learning

When the user wants interactive learning, offer a targeted teach-back, derivation exercise or prediction question and evaluate their actual answer. Keep hints and solutions distinguishable so the learner can try first. Do not invent learner responses or infer mastery from silence. For noninteractive notes, include optional self-check questions with separate answers; do not force a quiz before answering the request.

Useful notes include the paper/version, key idea in the reader's terms, prerequisites, one worked mechanism, evidence and limits, unresolved questions, and a next learning step. Preserve the user's own annotations separately from generated explanations. Store notes only in the requested or established project/personal location. Scheduling reminders or maintaining a learning profile requires a corresponding request.

## Design provenance

Original project procedure. Layered reading draws on Keshav's paper-reading note; validity checks were informed by the reviewed K-Dense scientific-critical-thinking skill. See [research workflow and sources](https://github.com/amitbcp/personal_code_agents/blob/main/review/research-workflow.md). This is learning support, not a validated assessment of the reader's expertise.
