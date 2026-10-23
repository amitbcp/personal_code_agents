# Research workflow selective import — 2026-10-05

## Outcome

Imported the complete K-Dense scientific-visualization directory (18 source files) at `92ace75ac21efe19a620434e0ca4e356081fe807`, preserving all seven Python helpers, palette/style assets, publisher snapshots and references. Added a narrow Codex entrypoint adaptation and explicit figure QA. Merged reverse outlining and story/evidence review into ml-paper-writing; merged domain vocabulary/invariants into research-knowledge-map's existing OKF workflow. No competing wiki, global installation, commit, push or deployment performed.

Exact upstream revisions, repositories, selected source paths and licenses are in `research-imports.json`. Original baseline copies are in `upstream-2026-10-05/`; baseline skill entrypoints are named `SKILL.md.txt` to avoid discovery. Full K-Dense directory baseline is retained. MIT notices are included both in the relevant skills and provenance/license locations.

## Adaptation decisions

Removed unsupported compatibility frontmatter and Claude tool allowlist. Kept Python/environment requirements in prose. Narrowed discovery to scientific/exportable figures, retaining ordinary interactive explanations in visualize. Preserved upstream helper implementations; source inspection covered helper imports, file writes, export and metadata parsing, palette calculations and scoped styles before executing the fixture. This was a bounded source review, not an exhaustive security audit of all code paths or dependencies.

Upstream package/version commands and publisher profiles remain dated source snapshots. The skill explicitly prefers the consuming project's verified environment and records actual versions; it does not claim those upstream pins were locally available/tested. Removed mandatory software-paper citation insertion; the normal verified citation workflow governs manuscript bibliography changes. The small `confirm_profile` helper argument is an explicit caller acknowledgment after checking dated settings, not a requirement to ask the human again.

The sci-brain figure rubric lacked explicit units, honest-axis and uncertainty rules; the adapted review adds these and treats error-bar overlap as insufficient for significance. Reviews proceed within existing authorization without story-confirmation or marked-diff approval gates. Manuscript guidance preserves technical meaning and reports unresolved author judgments. Matt's root glossary/ADR layout is replaced by existing canonical/OKF locations, source-backed invariants and scoped decision records.

## Verification

- `uv run --no-project --with matplotlib==3.9.2 --with pillow==10.4.0 --with pypdf==6.6.2 python skills/scientific-visualization/tests/validate_fixture.py <new-output-directory>` passed. Output must be a fresh directory because overwrite refusal is intentional.
- Fixture checks paired subject bootstrap CI (known differences 1, 2, 3; mean 2; 95% percentile CI 1–3), retained NaN gap, scoped style restoration, PNG 1050×420 dimensions, SVG physical width 177.8 mm, PDF inspection, overwrite refusal, contrast ratios 21:1 and 1:1, publisher phase mismatch, and SVG internal-entity rejection.
- Rendered PNG was visually inspected: both panels readable, missing time point remains a gap, subject differences and interval are distinct, units and independent-unit sample count visible, legend does not cover data. This synthetic fixture validates plumbing and display behavior, not scientific conclusions or journal acceptance.
- Figure, PDF, SVG, export manifest and validation JSON retained at `upstream-2026-10-05/local-validation/`. Fixture source retained in the new skill's `tests/` directory.
- skill-creator `quick_validate.py` passed for all three affected skills using isolated PyYAML. Initial system Python lacked PyYAML; isolated run resolved this without changing the shared environment. Its initial compatibility-frontmatter failure was corrected and rerun.

Not covered: Plotly/Chrome export, all raster formats, all PDF pages/fonts, publisher compliance, complete accessibility audit, or an independent scientific analysis. Existing repo validation/integration remains the coordinator's responsibility.
