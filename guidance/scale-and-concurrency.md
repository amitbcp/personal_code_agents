# Scale & Concurrency Principles

**Applies to:** Designing or optimizing data paths, ingestion workstreams, RAG pipelines, or LLM-backed extraction services where risks depend on volume, throughput, or parallelism.
**Default Goal:** Saturate the current machine correctly and resumably before reaching for a cluster. 

## 1. The Baseline (DO THIS FIRST)
Never parallelize blindly. Before adding workers or async loops:
1.  **Smoke Test:** Run a single-process baseline on a ~100-record representative sample.
2.  **Identify the Bound:** Determine if the pipeline is constrained by CPU (pure-Python), I/O (disk/network), external rate limits (LLM/embedding APIs), memory, or cross-process serialization.
3.  **Profile:** Use `cProfile`, `py-spy`, or per-stage timers to find exactly where time is spent. Record records/sec, p50/p95 latency, and peak RSS.

## 2. Select the Mechanism by Bound

| Bound | Mechanism | Execution Notes |
| :--- | :--- | :--- |
| **CPU (Pure Python)** | `ProcessPoolExecutor`, `multiprocessing` | ~1 worker per core. Leave 1-2 cores for parent/IO. |
| **CPU (Vectorizable)** | Native libs (Polars, DuckDB, NumPy, Arrow) | Relies on internal multithreading. Releases the GIL. |
| **I/O or API (Many calls)** | `asyncio` + `Semaphore`, or Thread Pool | Async handles thousands in-flight; threads cap at ~hundreds. |
| **Mixed CPU & I/O** | Process per core + internal async/thread pool | Standard shape for high-volume LLM extraction pipelines. |
| **GPU Inference** | Batching + CPU prefetch workers | An idle GPU means the CPU pre-processing is the bottleneck. |

**Python Concurrency Rules:**
*   **The GIL:** Threads share the GIL in CPython. Pure-Python CPU work does not scale across threads. (Do not rely on Python 3.13+ free-threading unless every C-extension in the pipeline explicitly supports it).
*   **Start Methods:** Enforce `spawn` or `forkserver`. Never use `fork` when the parent holds threads, large memory, or GPU handles (`fork` + threads = deadlocks; `fork` + large RAM = copy-on-write churn).
*   **LLM API Limits:** Concurrency here is bounded by external rate limits, not cores. Enforce bounded async concurrency, cost budgets, exponential backoff with jitter, and aggressive request caching (keyed by model, prompt version, and input hash).

## 3. Sharding & Data Layout
*   **Partitioning:** Partition by a stable key (hash of record ID, ID ranges) so each shard is independent, deterministic, and idempotent.
*   **Sizing:** Aim for 4–10× more shards than workers to allow load balancing, but ensure each shard contains enough work (seconds-to-minutes) to amortize startup costs. 
*   **Skew:** Track per-shard elapsed time. Split hot keys or oversized records; never let one massive shard hold a run hostage.
*   **Layout:** Output to columnar files (Parquet, Arrow) with row groups sized for parallel readers, or partitioned directories. Avoid single giant files or millions of tiny ones. Do not force global ordering; sort within shards or carry sequence numbers.

## 4. Memory & Data Movement
*   **Memory Budget:** `(Workers × Peak per-worker RSS) + Parent RSS ≤ 75% Total RAM`. 
*   **Reduction:** Before cutting worker counts, reduce peak RSS via streaming, chunked reads, and generators.
*   **IPC Limits:** Pass paths, IDs, or shard descriptors between processes. **Never pass large data objects.** Pickling large objects across process boundaries is a fatal bottleneck. For shared read-only data, use memory-mapped files or Arrow.
*   **Sinks:** Batch writes to databases and vector stores. Use bulk-load paths with connection pools and bound in-flight writes.

## 5. Resilience & Backpressure
*   **Queues:** Connect pipeline stages with bounded queues. A slow consumer must block producers, not grow memory infinitely.
*   **Failures & Retries:** Every external call must have a timeout. Limit retries to retryable errors. Ensure sinks are idempotent (upsert/dedupe) so rerunning is safe.
*   **Poison Records:** Quarantine failing records with full context (shard, offset, hash, error). Let the batch continue. Only abort the run if the failure rate exceeds a systematic threshold.
*   **Manifests:** Checkpoint per shard in a run manifest (recording seeds, input hashes, model versions) so interrupted runs can skip completed shards safely. Listen for `SIGINT`/`SIGTERM` to flush partials and exit cleanly.

## 6. Verification & Reporting
*   **Validation:** A pipeline is only complete if it runs identically at three scales: a 100-record smoke test, a single-shard run, and a full run. 
*   **Observability:** If CPU utilization is not near `N × 100%` across workers, you are bottlenecked by I/O, the sink, lock contention, or serialization. Find it.
*   **Evidence Required:** When reporting completion, state the baseline vs. result, including throughput, p95 latency, peak memory, and cost. Do not extrapolate production-scale behavior from a 5-record demo.