# Visual workflow imports — 2026-10-05

## Scope and provenance

Imported three pinned upstreams, with records in `visual-imports.json`. Original packages are under `upstream-2026-10-05/{archify,frontend-design,web-performance}`; original skill entrypoints use `SKILL.md.txt` so they cannot be accidentally installed as skills. Archify snapshot includes the full original runtime and tests; performance snapshot also includes the referenced Core Web Vitals entrypoint and LCP/INP/CLS references. No package installation, commit, push, or deployment was performed by this import task.

- Archify: tt-a1i/archify `73aaa0696e8f72c232ea710e6fa94fd953f3e773`, actual `archify/` package, version 3.0.1. Includes renderers, schemas, standalone validators, examples, viewer, delivery/provenance workflow, repair references, migrations and delta support. It was not replaced with a generic diagram instruction.
- Frontend design: anthropics/skills `683bc88e56f3e09ba94f7055977f3d3aa499f202`, actual frontend-design directory.
- Web performance: addyosmani/web-quality-skills `afa8da942115f2961fdbfa80807ea0b232ff6c00`, performance plus required measurement/RUM and Core Web Vitals references. Renamed to avoid claiming all system performance work.

## Licensing

Archify's own code is MIT; frontend-design carries Apache-2.0 in its own LICENSE.txt; Addy is MIT with its copyright preserved. Copies live both in installed skill directories and repository licenses. The frontend modified file carries its required change notice.

Archify's third-party notice and JetBrains Mono OFL text are retained. Its optional vector catalog has separate logo licenses and trademark conditions, including Vue NC-SA and Jenkins/Rust SA; the MIT license does not supersede them. The skill defaults to no requested brand marks and calls for checking relevant terms before redistribution of marked outputs. This is a private-library import, not clearance for arbitrary commercial redistribution or endorsement. The original catalog metadata and notices remain available rather than silently claiming all bundled art is MIT.

## Adaptations

Archify retains all five modes, typed JSON authoring, validation, source evidence, automated rendering, strict artifact checks, bounded repair, and optional browser/perceptual review. The main workflow explicitly substitutes `deliver` then strict `check` for browser-only `finalize` on a headless host. Browser absence must be reported; no skipped gate is called passed. The update runtime now requires `ARCHIFY_UPDATE_CHECK_ENABLED=1`; ordinary delivery performs no implicit update request. Update and delivery references state this precedence. Required runtime is Node >=18; compiled validators/viewer mean no npm install is needed for ordinary rendering. Removed installed upstream test directory and package scripts referring outside the standalone skill; full originals remain in the snapshot. This is a runtime distribution, not the full upstream development checkout; rebuilding generated viewer/catalog files requires the pinned upstream source tree.

Durable JSON/HTML/receipts go in established project documentation/wiki paths. Runtime caches, browser profiles and temporary traces use the remote host's configured local NVMe location, without inventing host paths. Existing code evidence distinguishes committed revision from dirty working-tree observations. Small diagrams still route to Mermaid.

Frontend design retains the concrete palette/type/layout planning, subject-grounded aesthetic decisions, restrained motion, responsive/focus requirements, and UI copy guidance. It removes the invented premise that a client rejected previous work, avoids redundant confirmation when the brief is inferable, preserves existing component/token systems, and puts dashboard task completion ahead of novelty. Screenshot review is conditional on actual browser availability.

Web performance retains field/lab/static evidence distinctions, target conditions, repeated measurements, traces, measurement fallbacks and RUM. Tool names are conditional examples; no new browser install is required. Public performance services are not a destination for private URLs. Non-performance Lighthouse categories no longer expand every task automatically. Fixed the responsive hero example's lazy-loading contradiction and removed stale browser-share percentages. Core Web Vitals references are local and linked; no sibling skill dependency remains.

## Validation and limits

- All three entrypoints passed `quick_validate.py` using `/Users/aamita/miniconda3/bin/python3` (default Python lacked PyYAML; no package was installed).
- On Node v24.10.0, real Archify architecture delivery passed 9/9 checks, zero errors/warnings, followed by strict artifact verification with current provenance. Fixture artifacts and receipt are in the private operational handoff `archify-validation/` (the reproducible test remains in `fixtures/visual-2026-10-05/`).
- `node review/fixtures/visual-2026-10-05/verify.mjs` passed: default update check is disabled even with a nonexistent checker, standalone delivery and strict provenance succeed, malformed candidate is rejected, and previous HTML survives failed delivery. The test uses a temporary workspace and removes only its own files.
- Inspected CLI dispatch, shared renderer loader/imports, update child-spawn boundary, package runtime requirements, and relevant original test before executing. This is scoped helper review, not an exhaustive security audit of every renderer/browser/export function.
- Checked relative Markdown file references across all three installed skills: none missing.
- Headless acceptance walkthrough: a private dashboard with only source available yields static hypotheses and a reproducible trace plan, never fabricated field metrics or a browser installation. Existing-dashboard design preserves its tokens and density while using the original planning/copy rubric. These are workflow reviews, not independent model benchmarks.
- No application performance claim, browser visual inspection, remote-host runtime certification, or measured frontend quality improvement is claimed. Runtime delivery is verified locally; remote/browser compatibility remains host-specific.
