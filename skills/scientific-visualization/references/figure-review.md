# Figure review at delivery size

Inspect the rendered artifact at its intended manuscript, slide or web size. Link findings to the actual panel and source data; mark taste judgments as opinions. Metadata checks cannot certify the meaning of a figure.

## Scientific meaning before appearance

- Label quantities, units and dimensionless measures. State transforms and log bases, normalization references, bins and smoothing.
- Keep axes honest: zero for bars/areas unless clearly justified; disclose breaks and nonzero line/point limits; compare panels on consistent scales where comparison is intended. Efficient use of space never justifies misleading limits.
- Name uncertainty (SD, SE, CI, posterior interval), estimation method, confidence level where relevant, sample count and independent sampling unit. Preserve pairing/clustering and distinguish variability from estimator uncertainty. Overlap of error bars alone is not a significance test.
- Preserve missingness as gaps or explicit modeled segments; distinguish zero, missing, censored and excluded data. Show raw observations when feasible.
- Match every caption and visual conclusion to source measurements. Aesthetic salience must not suppress contradictory observations.

## Visual inspection

Check alignment, grouping and edge padding; panel order and labels; consistent fonts, sizes and spacing; readable ticks and lines at final size; legends that do not occlude data; unclipped labels and scale bars. Use a limited semantically appropriate palette with redundant markers/line styles. Check contrast and grayscale readability without claiming full color-vision accessibility. Verify vector/raster format, physical size and raster resolution in the exported file.

Report each material finding with location, evidence, severity, and a concrete fix; distinguish verified, needs review and not applicable. Apply fixes already within the request, render again, and report remaining limitations. Do not require a scorecard for a minor edit or an approval round already covered by authorization.

Adapted from QuantumBFS/sci-brain's figure rubric; the explicit units, honest-axes and uncertainty checks fill gaps identified in that upstream rubric. License: the bundled `LICENSE.sci-brain`.
