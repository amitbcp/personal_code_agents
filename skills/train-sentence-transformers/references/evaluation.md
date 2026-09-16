# Retrieval evaluation

Define the corpus, query set, relevance judgments, candidate generator, candidate depth and primary metric before comparing systems. State whether relevance is graded or binary, how unjudged documents and queries without positives are handled, and how ties are broken.

Keep the candidate pool fixed for an isolated reranker comparison. Measure candidate recall separately: a reranker cannot recover a relevant document that was never retrieved. Do not insert gold documents into candidates when claiming end-to-end retrieval quality; an oracle-candidate diagnostic must be labeled separately.

Compare systems on the same queries. Use per-query metric differences and a paired bootstrap or appropriate randomization test. Resample independent groups when queries share sources, users or topics; row-wise resampling can understate uncertainty. Report sample/group counts, effect sizes and uncertainty, not only a p-value. Account for repeated model/metric comparisons and do not silently tune on the final test.

Record nDCG/MRR/Recall cutoffs, score direction and relevance conventions. Use the project's tested evaluator rather than reimplementing metrics inside the skill. Check a hand-worked tiny ranking with ties and missing positives when changing metric code.

Benchmark latency/throughput with stated sequence lengths, candidate count, batch size, concurrency, hardware, warmup and synchronization. Separate loading/tokenization/transfer from model scoring where relevant, and include end-to-end results. Avoid extrapolating capacity from a single small batch.

When using a library evaluator, inspect actual returned keys and primary_metric in a small run. Names and defaults vary by version; configure checkpoint selection from observed output.
