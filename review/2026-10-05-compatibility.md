# Codex / GPT-6 compatibility — 2026-10-05

- Target: eight selected additions, plus scoped manuscript/wiki/reviewer improvements; no model-default changes.
- Skills use standard `SKILL.md` YAML name/description manifests. Optional UI metadata does not select or require a particular model.
- Official guidance consulted: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra and https://developers.openai.com/api/docs/guides/tools-skills . Descriptions stay task-specific, substantial references load on demand, and completion follows the authorized outcome.
- Remove mandatory Claude-only tools, setup commands, redundant checkpoints and competing knowledge trees. Available host tools and explicit project rules remain authoritative.
- GPT-6 compatibility means parse/discovery and executable-helper/runtime compatibility, plus bounded behavioral checks where performed. It is not a vendor certification or demonstrated improvement on every task.
- Mac and both Vulkan node-local Codex CLIs were observed at 0.160.0. The installation does not restart active tasks, alter authentication, change CBM indexing, or modify customer services.
- Research and visual runtime dependencies are validated separately from Markdown discovery. Headless rendering checks do not certify visual appearance.

## Existing reviewer changes

- Adapted the independent requirements/standards axes from Matt code-review and behavior-facing test principles from Matt tdd at revision 4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d (MIT).
- Retained impact-ranked concrete findings and task scope. Did not import mandatory issue trackers, sub-agent counts, confirmation gates or internal-test prohibitions.
- Parent repository provenance contains original reviewer attribution; these are additional influences, not replacement authorship.

## Verified deployment

- 17/17 skill manifests validate; repository validator accepts five agent TOMLs, 23 Python sources and 24 provenance mappings.
- Existing 30 regression tests pass. Scientific figure integration passes paired uncertainty/missing-data/export checks, and its local PNG was visually inspected.
- Archify standalone rendering, strict provenance, update suppression and failed-delivery preservation checks pass locally. Figure and Archify delivery/provenance fixtures also pass on both Vulkan nodes using installed runtime dependencies.
- Fresh owned Codex app-server probes on Mac and both node-local profiles discover all 17 selected skills enabled with zero errors. 236 skill/agent files match the deployment package on each profile.
- A bounded GPT-6 Luna/max forward test repairs the supplied normalization defect (four passing tests including 512 generated strings), then respects an assessment-only architecture request. This does not establish automatic routing accuracy or general model-quality improvement.
- Global routing is updated on all three profiles. Existing project instructions, model defaults, auth, sessions, CBM configuration and running tasks were preserved. No live daemon restart was required for the fresh discovery probes.
- Runtime skills can be discovered on subsequent turns; already-loaded text may remain in old context. A fresh chat is the clearest adoption boundary.
