import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import tools.toolfunc as tf
from tomlkit import parse

ENCODING = "utf8"

tool_path = Path(__file__).parent
app_root = tf.find_project_root(tool_path, target_name="app")
root = tf.find_project_root(app_root)

config_file_path: Path = app_root / "config.toml"
work = root / ".work"

with open(config_file_path, "r", encoding=ENCODING) as f:
    toml_content = f.read()
    toml_data = parse(toml_content)

contestid = toml_data["contest"]["id"]


class Task:
    def __init__(self, task: str) -> None:
        self.taskid = ""
        self.contest = ""
        self.url = ""
        _isalp = re.fullmatch(r"[a-zA-Z]", task)
        _isurl = re.fullmatch(
            r"https://atcoder\.jp/contests/([^/]+)/tasks/([^/]+)", task
        )
        assert _isalp or _isurl, f"❌task is invalid ***{task}***"
        if _isurl:
            self.url = task
            self.contest, self.taskid = _isurl.groups()
        else:
            self.contest = contestid
            self.taskid = f"{self.contest}_{task}"
            self.url = f"https://atcoder.jp/contests/{self.contest}/tasks/{self.taskid}"

    def __str__(self) -> str:
        _wk: list[str] = [self.taskid, self.contest, self.url]
        return "\n".join(_wk)


def prepare_task_dir(task: Task) -> Path:
    task_dir = work / task.taskid
    task_dir.mkdir(parents=True, exist_ok=True)
    return task_dir


def download_testcases(task: Task, task_dir: Path) -> None:
    test_dir = task_dir / "test"
    if test_dir.exists():
        return

    original_dir = Path.cwd()
    try:
        os.chdir(task_dir)
        print(f"📥 ダウンロード中: {task.url}")
        subprocess.run(["powershell", "-Command", f"oj d {task.url}"])
    finally:
        os.chdir(original_dir)


def prepare_script(task: Task) -> bool:
    target_script = work / f"{task.taskid}.py"
    no_script = not target_script.exists()
    if no_script:
        template_path = tool_path / "template.py"
        shutil.copy(template_path, target_script)

    with open(target_script, "r", encoding=ENCODING) as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith('"""http'):
        lines.insert(0, f'"""{task.url}"""\n')
        with open(target_script, "w", encoding=ENCODING) as f:
            f.writelines(lines)

    subprocess.run(["code", str(target_script)], check=True, shell=True)
    return no_script  # True if no answer


def run_tests(task: Task, task_dir: Path) -> None:
    print(f"🧪 テスト実行: {task.taskid}")
    main_script = task_dir / "main.py"
    target_script = work / f"{task.taskid}.py"
    shutil.copy(target_script, main_script)

    original_dir = Path.cwd()
    try:
        os.chdir(task_dir)
        subprocess.run(
            ["powershell", "-Command", 'oj t -c "py main.py"'],
            check=False,
            shell=True,
        )
    finally:
        os.chdir(original_dir)


def main():
    parser = argparse.ArgumentParser(description="ジョブとタスクを指定するスクリプト")
    parser.add_argument("task", help="タスク名/url")

    if len(sys.argv) < 2:
        parser.print_usage()
        print("\n❌ エラー: 引数がありません。")
        sys.exit(1)

    args = parser.parse_args()

    task = Task(args.task)

    task_dir = prepare_task_dir(task)
    download_testcases(task, task_dir)
    no_answer = prepare_script(task)

    if no_answer:
        return

    run_tests(task, task_dir)


if __name__ == "__main__":
    main()
