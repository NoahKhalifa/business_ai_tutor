"""CLI subprocess tests: argparse, cache hit, --force, --components, --quiet."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.pdf_extract.tests import fixtures


def run_cli(*args, cwd: Path):
    env = {"PYTHONIOENCODING": "utf-8"}
    proc = subprocess.run(
        [sys.executable, "-m", "tools.pdf_extract", *args],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        encoding="utf-8",
        env={**env, **dict(__import__("os").environ)},
    )
    return proc


class CLITests(unittest.TestCase):
    PROJECT_ROOT = Path(__file__).resolve().parents[3]

    def test_help_runs(self):
        proc = run_cli("--help", cwd=self.PROJECT_ROOT)
        self.assertEqual(proc.returncode, 0)
        self.assertIn("pdf_extract", proc.stdout)

    def test_convert_then_cached(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            pdf = fixtures.make_text_pdf(tmp / "t.pdf")

            first = run_cli(str(pdf), "-o", str(tmp), cwd=self.PROJECT_ROOT)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertIn("converting:", first.stdout)
            self.assertTrue((tmp / "t.md").exists())

            second = run_cli(str(pdf), "-o", str(tmp), cwd=self.PROJECT_ROOT)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertIn("cached:", second.stdout)

    def test_force_bypasses_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            pdf = fixtures.make_text_pdf(tmp / "t.pdf")

            run_cli(str(pdf), "-o", str(tmp), cwd=self.PROJECT_ROOT)
            proc = run_cli(
                str(pdf), "-o", str(tmp), "--force", cwd=self.PROJECT_ROOT
            )
            self.assertEqual(proc.returncode, 0)
            self.assertIn("converting:", proc.stdout)
            self.assertNotIn("cached:", proc.stdout)

    def test_components_filter(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            pdf = fixtures.make_combined_pdf(tmp / "c.pdf")
            proc = run_cli(
                str(pdf), "-o", str(tmp), "--components", "text",
                cwd=self.PROJECT_ROOT,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            # No assets dir or empty since images/math disabled
            assets = tmp / "assets"
            if assets.exists():
                self.assertEqual(list(assets.iterdir()), [])

    def test_unknown_component_errors(self):
        proc = run_cli(
            "anything.pdf", "--components", "bogus", cwd=self.PROJECT_ROOT,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("Unknown components", proc.stderr)

    def test_quiet_suppresses_progress(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            pdf = fixtures.make_text_pdf(tmp / "t.pdf")
            proc = run_cli(
                str(pdf), "-o", str(tmp), "--quiet", cwd=self.PROJECT_ROOT,
            )
            self.assertEqual(proc.returncode, 0)
            self.assertEqual(proc.stdout.strip(), "")

    def test_folder_input_recursive(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            sub = tmp / "nested"
            sub.mkdir()
            fixtures.make_text_pdf(sub / "a.pdf")
            fixtures.make_text_pdf(sub / "b.pdf")
            proc = run_cli(str(tmp), "-o", str(tmp / "out"), cwd=self.PROJECT_ROOT)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertIn("[1/2]", proc.stdout)
            self.assertIn("[2/2]", proc.stdout)
            self.assertTrue((tmp / "out" / "a.md").exists())
            self.assertTrue((tmp / "out" / "b.md").exists())


if __name__ == "__main__":
    unittest.main()
