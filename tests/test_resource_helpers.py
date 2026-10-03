"""Offline resource regressions adapted from K-Dense MIT tests at 154988403bb5a18e9d3c0ce4e6d5e2e4b184a298.

Copyright (c) 2025 K-Dense Inc. See licenses/K-Dense-AI--scientific-agent-skills/LICENSE.md.
Adaptations: focused cases, isolated module loading, embedded synthetic AMD fixture.
"""
from __future__ import annotations
import contextlib
import importlib.util
import io
import json
import os
import stat
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

SCRIPTS = Path(__file__).resolve().parents[1] / "skills/get-available-resources/scripts"

def load_helpers():
    # Other skill suites have their own _common; do not leak ours into them.
    names = ("_common", "snapshot_tools", "detect_resources", "plan_workload")
    previous = {name: sys.modules.get(name) for name in names}
    loaded = {}
    try:
        for name in names:
            spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + ".py"))
            module = importlib.util.module_from_spec(spec)
            sys.modules[name] = module
            spec.loader.exec_module(module)
            loaded[name] = module
    finally:
        for name, module in previous.items():
            if module is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = module
    return loaded

helpers = load_helpers()
_common = helpers["_common"]
snapshot_tools = helpers["snapshot_tools"]
detect_resources = helpers["detect_resources"]
plan_workload = helpers["plan_workload"]
GIB = 1024**3
CASES = {'amd_smi_current': [{'gpu': 0, 'asic': {'market_name': 'AMD Instinct MI300X', 'asic_serial': 'private-synthetic-serial'}, 'vram': {'type': 'HBM', 'size': {'value': 196608, 'unit': 'MB'}}}]}



def canonical_snapshot() -> dict:
    return {
        "accelerators": {
            "candidate_counts": {"cuda": 1, "metal": 0, "rocm": 0},
            "candidate_upper_bounds": {"cuda": 1, "metal": None, "rocm": None},
            "devices": [
                {
                    "backend_candidate": "cuda",
                    "device_class": "gpu",
                    "device_permission": "not_tested",
                    "local_index": 0,
                    "management_query": "visible",
                    "memory": {
                        "dedicated_free_bytes": 20 * GIB,
                        "dedicated_total_bytes": 40 * GIB,
                        "model": "dedicated",
                    },
                    "name": "Synthetic GPU",
                    "runtime_compatibility": "not_tested",
                    "vendor": "nvidia",
                }
            ],
            "runtime_usable_devices": None,
            "visibility_environment": {},
        },
        "cgroup_v2": {"detected": True, "scope": "non_root"},
        "completeness": "complete_with_informational_notes",
        "container": {
            "detected": True,
            "evidence": ["cgroup_limit", "docker_marker"],
            "runtime": "docker_or_compatible",
        },
        "cpu": {
            "cgroup_v2": {"cpuset_logical": 4, "quota_cores": 3.5},
            "effective": {
                "capacity_cores": 3.5,
                "limiting_sources": ["cgroup_quota"],
                "worker_ceiling": 3,
            },
            "host": {"logical": 32, "physical": 16},
            "process": {
                "affinity_logical": 4,
                "python_available_logical": 4,
            },
        },
        "disk": {
            "capacity_bytes": 100 * GIB,
            "free_bytes": 60 * GIB,
            "scope": "working_filesystem_path_redacted",
            "user_available_bytes": 50 * GIB,
            "writable": True,
            "writability_check": "os_access_only_no_write_probe",
        },
        "memory": {
            "cgroup_v2": {
                "available_bytes": 8 * GIB,
                "current_bytes": 8 * GIB,
                "high_bytes": 14 * GIB,
                "max_bytes": 16 * GIB,
            },
            "effective": {
                "available_bytes": 8 * GIB,
                "available_limiting_sources": ["cgroup_memory_remaining"],
                "hard_limit_bytes": 16 * GIB,
                "hard_limit_sources": ["cgroup_memory_max"],
                "pressure_threshold_bytes": 14 * GIB,
            },
            "host": {"available_bytes": 32 * GIB, "total_bytes": 64 * GIB},
            "model": "system_ram",
            "swap": {"free_bytes": 2 * GIB, "total_bytes": 4 * GIB},
        },
        "observed_at": "2026-07-23T12:00:00Z",
        "platform": {
            "machine": "x86_64",
            "python_version": "3.13.5",
            "system": "Linux",
        },
        "privacy": {
            "absolute_paths_included": False,
            "environment_values_included": False,
            "hostnames_included": False,
            "identifiers_redacted_by_default": True,
        },
        "provenance": [
            {
                "component": "cpu.host.logical",
                "source": "os.cpu_count",
                "status": "ok",
            }
        ],
        "scheduler": {
            "allocation": {
                "cpu_per_process": 4,
                "cpus_on_node": 4,
                "gpus_per_process": 1,
                "gpus_on_node": 1,
                "memory_effective_bytes": 16 * GIB,
                "memory_scope": "shared_per_node",
                "tasks": 1,
            },
            "detected": True,
            "enforcement": "unknown",
            "fields_read": ["SLURM_CPUS_PER_TASK"],
            "kind": "slurm",
        },
        "schema_version": "1.1",
        "snapshot_kind": "effective_resource_snapshot",
        "warnings": [
            {
                "code": "ACCELERATOR_RUNTIME_NOT_TESTED",
                "component": "accelerators",
                "message": "Synthetic informational warning.",
                "severity": "info",
            }
        ],
    }

class CommonSafetyTests(unittest.TestCase):
    def test_force_does_not_truncate_another_hard_link(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            alias = Path(directory) / "alias.json"
            target.write_text('{"keep":true}')
            os.link(target, alias)
            with mock.patch.object(_common.Path, "cwd", return_value=Path(directory)):
                with self.assertRaises(_common.ResourceToolError):
                    _common.emit_json({"keep": False}, "alias.json", force=True)
            self.assertEqual(target.read_text(), '{"keep":true}')

    @unittest.skipUnless(hasattr(os, "mkfifo"), "requires POSIX FIFO")
    def test_fifo_input_and_forced_output_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fifo = Path(directory) / "pipe.json"
            os.mkfifo(fifo)
            with self.assertRaises(_common.ResourceToolError):
                _common.read_json_file(str(fifo))
            with mock.patch.object(_common.Path, "cwd", return_value=Path(directory)):
                with self.assertRaises(_common.ResourceToolError):
                    _common.emit_json({"ok": True}, "pipe.json", force=True)
            self.assertTrue(stat.S_ISFIFO(fifo.stat().st_mode))

    def test_extreme_integer_is_rejected_without_overflow(self) -> None:
        self.assertIsNone(_common.bounded_number(10**1000))

    def test_stdout_is_default_and_file_output_is_private(self) -> None:
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            _common.emit_json({"ok": True})
        self.assertEqual(json.loads(captured.getvalue()), {"ok": True})

        old_cwd = Path.cwd()
        try:
            with tempfile.TemporaryDirectory() as directory:
                os.chdir(directory)
                _common.emit_json({"ok": True}, "resource-snapshot.json")
                output = Path("resource-snapshot.json")
                self.assertEqual(json.loads(output.read_text()), {"ok": True})
                self.assertEqual(stat.S_IMODE(output.stat().st_mode), 0o600)
                with self.assertRaises(_common.ResourceToolError):
                    _common.emit_json({"ok": False}, "resource-snapshot.json")
                with self.assertRaises(_common.ResourceToolError):
                    _common.emit_json({"ok": False}, "../escape.json")
        finally:
            os.chdir(old_cwd)

    def test_snapshot_reader_rejects_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            real = Path(directory) / "snapshot.json"
            link = Path(directory) / "link.json"
            real.write_text("{}", encoding="utf-8")
            try:
                link.symlink_to(real)
            except OSError:
                self.skipTest("symlinks unavailable")
            with self.assertRaises(_common.ResourceToolError):
                _common.read_json_file(str(link))

class ParserTests(unittest.TestCase):
    def test_current_amd_smi_nested_units_preserve_memory(self) -> None:
        devices = detect_resources.parse_amd_json(json.dumps(CASES["amd_smi_current"]))
        self.assertEqual(devices[0]["memory"]["reported_total_bytes"], 192 * GIB)
        self.assertIsNone(devices[0]["memory"]["dedicated_total_bytes"])
        self.assertNotIn("private-synthetic-serial", json.dumps(devices))
        self.assertIsNone(detect_resources._amd_memory_bytes({"vram": {"size": "N/A"}}))
        self.assertIsNone(detect_resources._mib_to_bytes("1e308"))

    def test_intel_mac_display_keeps_actual_vendor(self) -> None:
        devices = detect_resources.parse_apple_profiler_json(json.dumps({
            "SPDisplaysDataType": [{"sppci_model": "AMD Radeon Pro", "spdisplays_vendor": "AMD"}]
        }), machine="x86_64")
        self.assertEqual(devices[0]["vendor"], "amd")
        self.assertEqual(devices[0]["backend_candidate"], "metal")
        self.assertEqual(devices[0]["memory"]["model"], "unknown")

class LinuxCgroupTests(unittest.TestCase):
    def test_broad_mount_preserves_ancestors_over_nested_bind_mount(self) -> None:
        mountinfo = (
            "50 20 0:27 / /sys/fs/cgroup rw - cgroup2 cgroup rw\n"
            "51 20 0:27 /parent /run/cg rw - cgroup2 cgroup rw\n"
        )
        root, relative = detect_resources._resolve_cgroup_mount(mountinfo, ("parent", "task"))
        self.assertEqual(root, Path("/sys/fs/cgroup"))
        self.assertEqual(relative, ("parent", "task"))

    def test_delegated_mount_uses_mount_root(self) -> None:
        files = {
            "/proc/self/cgroup": "0::/parent/task\n",
            "/proc/self/mountinfo": "50 20 0:27 /parent /run/cg rw - cgroup2 cgroup rw\n",
            "/run/cg/cgroup.controllers": "cpu memory\n",
            "/run/cg/task/cgroup.controllers": "\n",
            "/run/cg/task/cpu.max": "50000 100000\n",
            "/run/cg/task/memory.max": "104857600\n",
            "/run/cg/task/memory.current": "20971520\n",
        }
        def reader(path):
            if str(path) not in files:
                raise FileNotFoundError()
            return files[str(path)]
        report = detect_resources.detect_cgroup_v2(read_text=reader)
        self.assertEqual(report["cpu_quota_cores"], 0.5)
        self.assertEqual(report["memory_available_bytes"], 80 * 1024**2)

    def test_bad_membership_does_not_substitute_root(self) -> None:
        files = {"/proc/self/cgroup": "0::/../other\n",
                 "/sys/fs/cgroup/cgroup.controllers": "cpu memory\n",
                 "/sys/fs/cgroup/cpu.max": "800000 100000\n"}
        def reader(path):
            if str(path) not in files:
                raise FileNotFoundError()
            return files[str(path)]
        warnings = []
        report = detect_resources.detect_cgroup_v2(read_text=reader, warnings=warnings)
        self.assertIsNone(report["cpu_quota_cores"])
        self.assertEqual(report["scope"], "unknown")
        self.assertIn("CGROUP_MEMBERSHIP_UNKNOWN", {item["code"] for item in warnings})

class SchedulerTests(unittest.TestCase):
    def test_heterogeneous_slurm_node_does_not_inherit_first_node_tasks(self) -> None:
        env = {"SLURM_CPUS_ON_NODE": "16", "SLURM_TASKS_PER_NODE": "1(x2),4"}
        for index, expected in ((None, None), ("0", 16), ("2", None), ("10", None)):
            with self.subTest(index=index):
                current = dict(env)
                if index is not None:
                    current["SLURM_NODEID"] = index
                allocation = detect_resources.detect_scheduler(current)["allocation"]
                self.assertEqual(allocation["cpu_per_process"], expected)
        self.assertIsNone(detect_resources._parse_node_count("1junk", 0))

class PlatformMockTests(unittest.TestCase):
    def test_reserved_blocks_remain_distinct_from_user_available_space(self) -> None:
        with mock.patch.object(detect_resources.shutil, "disk_usage", return_value=SimpleNamespace(
            total=100 * GIB, free=50 * GIB
        )), mock.patch.object(detect_resources.os, "statvfs", return_value=SimpleNamespace(
            f_bfree=60, f_bavail=50, f_frsize=GIB
        ), create=True):
            disk = detect_resources._detect_disk([], [])
        self.assertEqual(disk["free_bytes"], 60 * GIB)
        self.assertEqual(disk["user_available_bytes"], 50 * GIB)

    def test_host_count_does_not_inherit_python_override(self) -> None:
        with mock.patch.object(detect_resources.os, "cpu_count", return_value=1):
            cpu = detect_resources._detect_cpu_inventory(
                system="Darwin", psutil_module=None, mac_sysctl={"logical": 14, "physical": 14},
                read_text=lambda p: "", warnings=[], provenance=[])
        self.assertEqual(cpu["logical"], 14)

class SnapshotToolTests(unittest.TestCase):
    def test_invalid_accelerator_maps_and_backends_are_reported(self) -> None:
        for value in (None, [], {"cuda": True}, {"cuda": -1}):
            snapshot = canonical_snapshot()
            snapshot["accelerators"]["candidate_upper_bounds"] = value
            self.assertFalse(snapshot_tools.validate_snapshot(snapshot)["valid"])
            with self.assertRaises(_common.ResourceToolError):
                plan_workload.build_plan(snapshot, accelerator="any")
        snapshot = canonical_snapshot()
        snapshot["accelerators"]["devices"][0]["backend_candidate"] = []
        self.assertFalse(snapshot_tools.validate_snapshot(snapshot)["valid"])

    def test_extreme_numeric_and_invalid_timestamp_are_rejected(self) -> None:
        snapshot = canonical_snapshot()
        snapshot["memory"]["effective"]["available_bytes"] = 10**1000
        snapshot["observed_at"] = "not-a-timeZ"
        self.assertFalse(snapshot_tools.validate_snapshot(snapshot)["valid"])

    def test_validator_accepts_canonical_snapshot(self) -> None:
        report = snapshot_tools.validate_snapshot(canonical_snapshot())
        self.assertTrue(report["valid"], report["errors"])

class PlannerTests(unittest.TestCase):
    def test_zero_workers_when_no_worker_fits_known_memory(self) -> None:
        plan = plan_workload.build_plan(canonical_snapshot(), memory_per_worker_mib=16384)
        self.assertEqual(plan["recommendation"]["suggested_workers"], 0)
        self.assertEqual(plan["recommendation"]["threads_per_worker"], 0)
        self.assertEqual(plan["recommendation"]["status"], "insufficient_memory")

    def test_unknown_memory_requires_review(self) -> None:
        snapshot = canonical_snapshot()
        snapshot["memory"]["effective"]["available_bytes"] = None
        plan = plan_workload.build_plan(snapshot, memory_per_worker_mib=1024)
        self.assertEqual(plan["recommendation"]["status"], "review_required")

    def test_unknown_cpu_requires_review(self) -> None:
        snapshot = canonical_snapshot()
        snapshot["cpu"]["effective"]["capacity_cores"] = None
        plan = plan_workload.build_plan(snapshot, memory_per_worker_mib=1024)
        self.assertEqual(plan["recommendation"]["status"], "review_required")

    def test_worker_plan_uses_cpu_memory_tasks_and_request(self) -> None:
        plan = plan_workload.build_plan(
            canonical_snapshot(),
            workload="cpu",
            task_count=10,
            requested_workers=8,
            memory_per_worker_mib=2048,
            reserve_memory_mib=1024,
            accelerator="cuda",
        )
        self.assertEqual(plan["limits"]["cpu_worker_ceiling"], 3)
        self.assertEqual(plan["limits"]["memory_worker_ceiling"], 3)
        self.assertEqual(plan["recommendation"]["suggested_workers"], 3)
        self.assertEqual(plan["recommendation"]["threads_per_worker"], 1)
        self.assertEqual(plan["accelerator"]["status"], "diagnostic_required")

if __name__ == "__main__":
    unittest.main()
