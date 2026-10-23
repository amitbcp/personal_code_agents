# System design checklist

Use for a substantial system design or when a scoped refactor changes service/data boundaries; skip irrelevant items.

- Requirements: functional behavior, latency, availability, scale, cost, team, delivery constraints and existing stack. Separate measured facts, forecasts and assumptions.
- High-level design: components, data flow, API contracts and storage choices. Show the critical path with a compact diagram when useful.
- Deep dive: data model, API semantics, caching and invalidation, event/queue ordering, error handling, retry budgets and idempotency. Cover only decisions implicated by this change.
- Load and reliability: estimate workload from evidence, identify resource limits, compare vertical/horizontal scaling, failover and redundancy, and actionable monitoring. Include backpressure, bounded concurrency and recovery for pipelines. Do not claim capacity from an unmeasured sketch.
- Tradeoffs: complexity, cost, team familiarity, time to deliver, compatibility and maintainability. State why the selected option fits and what measurable change would cause reconsideration.
- Output: a bounded design record with explicit assumptions, unresolved risks, verification evidence and revisit conditions in existing canonical docs.

Adapted 2026-10-05 from [Anthropic system-design](https://github.com/anthropics/knowledge-work-plugins/tree/8444efcd48f7012f09797778a36a33e73d0861f4/engineering/skills/system-design), revision `8444efcd48f7012f09797778a36a33e73d0861f4`, Apache-2.0. Changes add evidence bounds and project-scope guidance. License bundled as `ANTHROPIC-LICENSE.txt` in this skill.
