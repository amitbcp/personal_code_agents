---
name: get-available-resources
description: Detect host inventory and effective CPU, memory, disk, scheduler, container, and accelerator limits when a user asks for resource-aware planning or before a clearly resource-sensitive local workload. Produces a redacted JSON snapshot and conservative planning helpers without stress tests or assuming visible host hardware is usable.
license: MIT
metadata:
  version: "1.3"
  skill-author: K-Dense Inc.
---

# Get Available Resources

- Build a conservative picture of resources available to the **current process**.
- Keep host inventory, process affinity, cgroup/container limits, scheduler allocation, and accelerator runtime usability separate.

- **Runtime:** Python 3.11+ on Linux, macOS, or Windows; standard library by default, optional psutil 7.2.2; accelerator and scheduler CLIs are optional read-only probes.

## Safety contract

Follow these rules:

- Run detection when the user requests it or a specific workload needs resource
  planning. Do not persist a fingerprint for every scientific task.
- Use stdout by default. When persistence is within the authorized task or
  project scope, choose a generic local filename such as `resource-snapshot.json`
  or use the user-specified filename; no separate filename confirmation is needed.
- Do not run stress tests, benchmarks, large allocations, write probes, device
  resets, driver installation, or clock/power changes.
- Do not dump the environment. Read only the named Slurm and accelerator
  variables implemented by the detector.
- Do not report hostnames, absolute paths, cgroup paths, job IDs, device UUIDs,
  PCI addresses, or raw visibility-variable values.
- Treat a missing observation as unknown. Never convert unknown to unlimited.
- Never infer that a visible host CPU, memory pool, or GPU is usable inside a
  scheduler allocation or container.

- The bundled detector uses only fixed executable/argument tuples, no shell, short timeouts, bounded stdout/stderr, and partial-failure warnings.

## Quick start

- Run from the workload working directory, using the absolute path to this skill’s scripts.
- The detector measures the current process and current filesystem.
- The examples below use paths relative to the skill for readability; resolve them before changing directories.

### Ephemeral stdout snapshot

```bash
python scripts/detect_resources.py
```

- The command emits only JSON to stdout.
- Redirect it only when ordinary shell permissions are acceptable.

### Explicit private file

```bash
python scripts/detect_resources.py --output resource-snapshot.json
```

- Explicit output is restricted to one `.json` filename in the current directory, uses private permissions, rejects symlinks and path traversal, and refuses overwrite unless `--force` is supplied.

### Optional psutil enhancement

- The standard-library detector works without installation.
- For broader cross-platform physical-core, affinity, available-memory, swap, and disk coverage:

```bash
uv pip install "psutil==7.2.2"
```

- The import is lazy.
- Failure to import psutil becomes a warning, not a fatal error.

### Skip management-tool probes

```bash
python scripts/detect_resources.py --skip-accelerators
```

- Use this when accelerator discovery latency is undesirable.
- The detector still summarizes the presence and state of allowlisted visibility variables without returning their values.

## Required interpretation

### CPU

Read these as different facts:

- `cpu.host.logical`: system-visible scheduling units.
- `cpu.host.physical`: physical topology, or null; never inferred from logical
  count.
- `cpu.process.affinity_logical`: current affinity-set size when supported.
- `cpu.cgroup_v2.cpuset_logical`: effective cgroup cpuset size.
- `cpu.cgroup_v2.quota_cores`: finite `cpu.max` capacity, possibly fractional.
- `scheduler.allocation.cpu_per_process`: bounded Slurm per-task
  interpretation when scope is clear.
- `cpu.effective.capacity_cores`: minimum positive observed constraint.
- `cpu.effective.worker_ceiling`: conservative floor for CPU process workers.

- A quota of 1.5 is CPU-time capacity, not 1.5 physical cores.
- Affinity and cpusets constrain placement; quota constrains bandwidth.

### Memory

Keep these separate:

- host total/available memory;
- current cgroup usage, hard `memory.max`, and remaining hierarchical capacity;
- `memory.high`, which is a pressure/throttle boundary rather than a hard cap;
- scheduler memory allocation and its scope; and
- conservative effective hard limit and available estimate.

- On Apple silicon, `memory.model` is `unified_cpu_gpu`.
- Do not add integrated GPU memory to RAM or describe it as separate VRAM.

### Accelerators

Each device is a backend **candidate**:

- NVIDIA GPU → CUDA candidate;
- AMD GPU → ROCm candidate;
- Apple integrated GPU → Metal candidate.

Management-query visibility does not establish:

1. scheduler/container permission;
2. device-node access;
3. driver/runtime compatibility;
4. framework package compatibility; or
5. operator/data-type support.

- Therefore `runtime_usable_devices` remains null and each device says `runtime_compatibility: not_tested`.
- Visibility/allocation counts are upper bounds, not guarantees.

### Disk

- `capacity_bytes`, filesystem `free_bytes`, user-available blocks, and a non-writing permission check are distinct.
- Filesystem or project quotas can still be stricter.
- The absolute working path is always redacted.

### Scheduler and container

- Slurm variables describe allocation scope, but enforcement depends on site configuration such as task affinity or cgroups.
- Prefer affinity and cgroup observations as enforcement evidence.

- Container markers identify context; cgroup controls identify limits.
- A container with no finite cgroup value can still see host inventory, and a non-root cgroup is not automatically labeled a container.

- See [`references/resource_semantics.md`](references/resource_semantics.md) for the detailed platform rules.

## Plan a workload

- The detector and planner do not execute workloads; the planner consumes a validated snapshot and produces advisory output.
- Recommendations alone do not authorize launching jobs, terminating healthy jobs, changing allocations, or indexing code.
- Separately authorized workloads may proceed within their existing task and project permissions without a new approval request.
- A numeric worker recommendation is not permission or proof of feasibility.
- In particular, `MEMORY_REQUIREMENT_EXCEEDS_BUDGET` can accompany `suggested_workers: 1`; that plan is infeasible under the supplied memory estimate.
- Reduce the workload or obtain a suitable allocation before launch.
- Unknown memory also requires a measured or independently bounded estimate.

```bash
python scripts/plan_workload.py resource-snapshot.json \
  --workload cpu \
  --tasks 100 \
  --memory-per-worker-mib 2048
```

Optional controls:

- `--workers N`: explicit upper bound.
- `--reserve-memory-mib N`: memory kept outside the worker budget.
- `--workload cpu|mixed|io`: selects a bounded worker heuristic.
- `--accelerator none|any|cuda|rocm|metal`: requests a candidate backend
  decision without claiming usability.
- `--output plan.json`: explicit private local output; stdout is default.

- For CPU or mixed work, use `suggested_workers` and `threads_per_worker` together.
- Process workers multiplied by BLAS/OpenMP native threads can oversubscribe an allocation.

- The I/O plan permits bounded oversubscription (maximum 32) but labels it a heuristic.
- Benchmark only the real representative workload and stay within scheduler/container limits.

## Validate or diff snapshots

Validate:

```bash
python scripts/snapshot_tools.py validate resource-snapshot.json
```

Diff resource state while ignoring `observed_at`:

```bash
python scripts/snapshot_tools.py diff before.json after.json
```

- Use `--include-volatile` to include the timestamp.
- Inputs must be regular, non-symlink JSON files no larger than 1 MiB.
- Diffs are bounded.

- The schema and null/zero meanings are documented in [`references/snapshot_schema.md`](references/snapshot_schema.md).

## Optional accelerator diagnostic plan

Generate a plan without executing any diagnostic:

```bash
python scripts/accelerator_diagnostics.py resource-snapshot.json \
  --backend auto
```

- The result contains fixed, read-only management query argument lists and separate gates for visibility, permission, and runtime compatibility.
- Run a framework's official availability check only in the exact environment that will execute the workload.
- Do not install or mutate drivers automatically.

## Partial failures and provenance

One failed probe must not erase successful observations. Inspect:

- `completeness`;
- sorted `warnings` with stable codes;
- sorted `provenance` source/status records; and
- null fields.

- Subprocess stderr and raw exception text are not copied into the snapshot because they can contain identifiers or paths.

## Platform notes

- **Linux:** reads only bounded `/proc` and cgroup v2 files. Ancestor CPU and
  memory limits are considered.
- **macOS:** uses fixed `sysctl` keys and a bounded
  `system_profiler SPDisplaysDataType -json` query. Apple silicon memory is
  unified.
- **Windows:** optional psutil improves physical-core, affinity, available
  memory, and swap observations. Processor-group scope can make host and
  process counts differ.
- **Slurm:** reads an allowlist of allocation variables. It never emits job,
  node, submit-host, GPU-ID, or path values.
- **NVIDIA/AMD:** management CLIs are optional. Absence is normal; timeout,
  truncation, parse failure, and runtime uncertainty remain explicit.

## Mac, SSH, Enroot and storage placement

- Run detection inside the exact SSH host, scheduler allocation and Enroot container that will run the job.
- Do not reuse a Mac snapshot for Linux planning.
- Enroot is not specifically identified by the marker probes; verify effective affinity/cgroup limits and framework availability in that environment.
- Cgroup namespace and site scheduler policies can limit observations.

- On Vulcan, NFS is shared across all nodes; NVMe storage is node-local.
- Keep durable code and results on the project’s chosen shared storage.
- Put SQLite/index databases, temporary spill and high-churn caches on node-local storage according to project policy; the detector does not choose or migrate paths.
- Free space is not an NFS throughput measurement.
- Keep codebase-memory indexing manual.

## Bundled files

- `scripts/detect_resources.py` — redacted snapshot collector.
- `scripts/plan_workload.py` — deterministic worker/memory planner.
- `scripts/snapshot_tools.py` — schema validator and bounded structural diff.
- `scripts/accelerator_diagnostics.py` — non-executing read-only diagnostic
  plan.
- `references/resource_semantics.md` — interpretation and platform details.
- `references/snapshot_schema.md` — schema 1.1 contract.
- `references/sources.md` — dated official-source ledger.

- Official documentation was refreshed on **2026-07-23**; consult [`references/sources.md`](references/sources.md) before changing semantics or dependency pins.

## Provenance

- Adapted from K-Dense Scientific Agent Skills, revision `330c8e764435a731eff571e3efdda70b363d0792`, under MIT.
- Preserve license notices; manuscript citation is an editorial choice, not an automatic action.
