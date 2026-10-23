"""Offline input-boundary and scaffold-provenance regressions, no experiments."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "skills/hypothesis-generation/scripts"


class HypothesisHelperTests(unittest.TestCase):
    def run_python(self, code, *args):
        # Each helper suite owns an unrelated _common module; isolate imports.
        return subprocess.run(
            [sys.executable, "-B", "-c", code, *map(str, args)],
            cwd=SCRIPTS, text=True, capture_output=True,
        )

    def read_json(self, text):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "record.json"
            source.write_text(text, encoding="utf-8")
            return self.run_python(
                "import sys\nfrom _common import read_json, ValidationError, error_exit\n"
                "try:\n read_json(sys.argv[1])\n"
                "except ValidationError as exc:\n sys.exit(error_exit(exc))\n",
                source,
            )

    def assert_input_error(self, result, message):
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn(message, result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_nonstandard_numeric_constants_are_rejected(self):
        for constant in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(constant=constant):
                self.assert_input_error(self.read_json('{"x":' + constant + '}'),
                                        "nonstandard numeric constant")

    def test_numeric_overflow_cannot_bypass_nonfinite_rejection(self):
        for value in ("1e999", "-1e999"):
            with self.subTest(value=value):
                self.assert_input_error(self.read_json('{"x":[' + value + ']}'),
                                        "finite float range")

    def test_valid_numbers_and_duplicate_key_protection(self):
        self.assertEqual(self.read_json('{"x":[0,-1,1.5,1e20]}').returncode, 0)
        self.assert_input_error(self.read_json('{"x":1,"x":2}'), "duplicate key")

    def test_nesting_boundary_and_parser_overflow_are_controlled(self):
        self.assertEqual(self.read_json("[" * 64 + "0" + "]" * 64).returncode, 0)
        for depth in (65, 2000):
            with self.subTest(depth=depth):
                self.assert_input_error(self.read_json("[" * depth + "0" + "]" * depth),
                                        "JSON nesting exceeds")

    def test_dates_require_calendar_form_and_valid_day(self):
        code = (
            "import sys\nfrom _common import require_iso_date, ValidationError, error_exit\n"
            "try:\n require_iso_date(sys.argv[1], 'updated_on')\n"
            "except ValidationError as exc:\n sys.exit(error_exit(exc))\n"
        )
        self.assertEqual(self.run_python(code, "2024-02-29").returncode, 0)
        for value in ("20240229", "2024-W09-4", "2023-02-29", "2024-13-01"):
            with self.subTest(value=value):
                self.assert_input_error(self.run_python(code, value), "YYYY-MM-DD")

    def test_scaffold_retains_record_date_without_claiming_generation_date(self):
        result = self.run_python(
            "from pathlib import Path\n"
            "from _common import read_json\n"
            "from generate_preregistration_scaffold import generate\n"
            "record = read_json(Path('../assets/hypothesis_record_template.json'))\n"
            "record['updated_on'] = '2000-02-29'\n"
            "print(generate(record))\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Record updated: 2000-02-29", result.stdout)
        self.assertNotIn("Generated locally on", result.stdout)
        self.assertNotIn("{{", result.stdout)
        self.assertIn("UNREGISTERED DRAFT", result.stdout)

    def test_cli_rejects_unsafe_input_without_creating_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, target = Path(tmp) / "record.json", Path(tmp) / "draft.md"
            source.write_text('{"updated_on": NaN}')
            result = subprocess.run(
                [sys.executable, "-B", str(SCRIPTS / "generate_preregistration_scaffold.py"),
                 str(source), "-o", str(target)], text=True, capture_output=True,
            )
            self.assert_input_error(result, "nonstandard numeric constant")
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
