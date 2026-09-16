"""Behavior checks for the portable notebook scaffold; no notebook kernels run."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "skills/jupyter-notebook/scripts/new_notebook.py"


class NotebookScaffoldTests(unittest.TestCase):
    def run_helper(self, cwd, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=cwd,
                              text=True, capture_output=True)

    def test_default_output_belongs_to_working_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / ".git").mkdir()
            nested = project / "research"
            nested.mkdir()
            result = self.run_helper(nested, "--title", "Paired retrieval evaluation")
            self.assertEqual(result.returncode, 0, result.stderr)
            target = project / "output/jupyter-notebook/paired-retrieval-evaluation.ipynb"
            notebook = json.loads(target.read_text())
            self.assertEqual(notebook["nbformat"], 4)
            self.assertIn("Paired retrieval evaluation", notebook["cells"][0]["source"][0])
            for cell in notebook["cells"]:
                if cell["cell_type"] == "code":
                    self.assertEqual(cell["outputs"], [])
                    self.assertIsNone(cell["execution_count"])

    def test_existing_work_requires_explicit_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "notes.ipynb"
            target.write_text("existing work")
            args = ["--kind", "tutorial", "--title", "Example", "--out", str(target)]
            result = self.run_helper(tmp, *args)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(target.read_text(), "existing work")
            result = self.run_helper(tmp, *args, "--force")
            self.assertEqual(result.returncode, 0, result.stderr)
            notebook = json.loads(target.read_text())
            self.assertTrue(notebook["cells"][0]["source"][0].startswith("# Tutorial:"))


if __name__ == "__main__":
    unittest.main()
