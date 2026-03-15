import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "ban-check.py"


class BanCheckCliTests(unittest.TestCase):
    def run_script(self, *paths: Path) -> subprocess.CompletedProcess[str]:
        command = [sys.executable, str(SCRIPT), *[str(path) for path in paths]]
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        return subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
            env=env,
        )

    def test_returns_exit_code_one_and_reports_matches(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            chapter = Path(temp_dir) / "chapter-001.md"
            chapter.write_text(
                "\n".join(
                    [
                        "这不是愤怒，是恐惧。",
                        "她心里一酸，还是把话咽了回去。",
                        "他没说话，因为他知道这时候说什么都没用。",
                    ]
                ),
                encoding="utf-8",
            )

            result = self.run_script(chapter)

            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("[反模板] “不是X，是Y”句式", result.stdout)
            self.assertIn("[审稿] 直接心理描写", result.stdout)
            self.assertIn("[审稿] 沉默后补一句解释", result.stdout)
            self.assertIn("共发现 3 处问题", result.stdout)

    def test_returns_exit_code_zero_when_no_matches(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            chapter = Path(temp_dir) / "chapter-002.md"
            chapter.write_text(
                "\n".join(
                    [
                        "她把杯子放回桌上，没有立刻接话。",
                        "屋里安静了片刻，门外的风声先钻了进来。",
                    ]
                ),
                encoding="utf-8",
            )

            result = self.run_script(chapter)

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("共发现 0 处问题", result.stdout)


if __name__ == "__main__":
    unittest.main()
