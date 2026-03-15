from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Rule:
    label: str
    pattern: re.Pattern[str]


RULES: tuple[Rule, ...] = (
    Rule(
        label="[反模板] “不是X，是Y”句式",
        pattern=re.compile(r"不是\s*[^，。！？；\n]{1,20}[，,]\s*是\s*[^，。！？；\n]{1,20}"),
    ),
    Rule(
        label="[审稿] 直接心理描写",
        pattern=re.compile(
            r"(心里一酸|心头一酸|心里一紧|心里发紧|感到一阵|感到温暖|感到委屈|感到难过|意识到自己|意识到他|意识到她)"
        ),
    ),
    Rule(
        label="[审稿] 沉默后补一句解释",
        pattern=re.compile(r"(沉默了|没说话|没有说话)[^。！？\n]{0,30}(因为|他知道|她知道|是在|只是)"),
    ),
    Rule(
        label="[审稿] 解释性动机从句",
        pattern=re.compile(r"(因为她不想|因为他不想|因为不想|源于|本能让)"),
    ),
    Rule(
        label="[审稿] 直接点名情绪",
        pattern=re.compile(r"(他很愤怒|她很愤怒|他很难过|她很难过|他很伤心|她很伤心|他很委屈|她很委屈)"),
    ),
    Rule(
        label="[反模板] 单行比喻过密",
        pattern=re.compile(r"(像[^。！？\n]{0,20}){2,}"),
    ),
)

TEXT_SUFFIXES = {".md", ".txt"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="扫描章节文本里的常见套句、反模板和审稿风险信号。"
    )
    parser.add_argument("paths", nargs="+", help="要扫描的文件或目录")
    return parser.parse_args()


def iter_target_files(raw_paths: list[str]) -> list[Path]:
    targets: list[Path] = []

    for raw_path in raw_paths:
        path = Path(raw_path)
        if not path.exists():
            raise FileNotFoundError(f"找不到路径：{raw_path}")

        if path.is_dir():
            for file_path in sorted(path.rglob("*")):
                if file_path.is_file() and file_path.suffix.lower() in TEXT_SUFFIXES:
                    targets.append(file_path)
            continue

        if path.suffix.lower() in TEXT_SUFFIXES:
            targets.append(path)

    deduped: list[Path] = []
    seen: set[Path] = set()
    for target in targets:
        resolved = target.resolve()
        if resolved not in seen:
            seen.add(resolved)
            deduped.append(target)
    return deduped


def display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(Path.cwd().resolve()))
    except ValueError:
        return path.name


def scan_file(path: Path) -> list[tuple[Path, int, str]]:
    issues: list[tuple[Path, int, str]] = []

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        for rule in RULES:
            if rule.pattern.search(raw_line):
                issues.append((path, line_number, rule.label))

    return issues


def main() -> int:
    args = parse_args()

    try:
        files = iter_target_files(args.paths)
    except FileNotFoundError as error:
        print(str(error), file=sys.stderr)
        return 2

    if not files:
        print("没有找到可扫描的 .md 或 .txt 文件。", file=sys.stderr)
        return 2

    issues: list[tuple[Path, int, str]] = []
    for file_path in files:
        issues.extend(scan_file(file_path))

    for file_path, line_number, label in issues:
        print(f"{display_path(file_path)}:{line_number}  {label}")

    print(f"共发现 {len(issues)} 处问题")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
