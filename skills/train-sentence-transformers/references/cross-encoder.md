# CrossEncoder checks

A CrossEncoder scores query-document pairs jointly. Verify the intended output contract: binary relevance logit, probability, multi-class logits, regression score or pair/listwise rank score.

Match the loss to both supervision and output shape:

- Pointwise binary relevance: a BCE-style objective may fit; determine whether the implementation expects logits or probabilities.
- Multi-class classification: verify number of labels and class-index targets.
- Distillation: distinguish teacher scores from teacher margins; retain the teacher's scale/normalization contract.
- Pairwise/listwise ranking: inspect the installed loss's grouping, padding/masking and graded-label requirements.

A sigmoid is monotone in exact arithmetic, so it does not inherently change ranking. Finite-precision saturation can introduce ties, and probability calibration may still be wrong for the objective. Compare raw and transformed scores on a small evaluation batch before changing activation behavior. Do not treat one upstream failure report as a universal loss requirement.

Class weights and negative counts are experiment choices. Check mined negatives for false negatives; random negatives can be useful as a baseline even when harder negatives improve discrimination.

Validate checkpoint reload from a fresh process. Custom scoring heads must be importable and use the installed library's expected feature keys. Verify input truncation and query/document ordering at both training and inference.

Use development-only early stopping when appropriate; choose patience from evaluation frequency/noise rather than a mandatory constant. Preserve all agreed baseline and final-test boundaries.
