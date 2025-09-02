import json
from collections import defaultdict
from pathlib import Path

from . import toolfunc as tf

# 定数
ENCODING = "utf8"
TAG_KEYS = {
    "##############name##############",
    "######prefix######",
    "######body######",
    "######description######",
    "##############end##############",
}


def parse_lib_file(file_path: Path) -> dict:
    """1つのLibファイルからスニペット情報を抽出"""
    snippet_data = {}
    current_key = None
    snippet_name = None
    with file_path.open("r", encoding=ENCODING) as f:
        lines = [line.strip("\n") for line in f]
    for line in lines:
        if line in TAG_KEYS:
            current_key = line.strip("#")
        elif current_key == "name":
            snippet_name = line[2:]
            snippet_data[snippet_name] = {
                "prefix": [],
                "body": [],
                "description": [],
                "scope": "python",
            }
        elif current_key != "end" and snippet_name:
            content = line if current_key == "body" else line[2:]
            snippet_data[snippet_name][current_key].append(content)
    return snippet_data


def collect_snippets(lib_dir: Path) -> dict:
    """Libファイル群からスニペットを収集"""
    snippets = defaultdict(dict)
    for file in lib_dir.glob("Lib_*.py"):
        if file.name == "Lib_templete.py":
            continue
        file_snippets = parse_lib_file(file)
        snippets.update(file_snippets)
    return snippets


def write_snippets_to_file(snippets: dict, output_path: Path) -> None:
    """スニペットをJSON形式で書き出す"""
    with output_path.open("w", encoding=ENCODING) as f:
        json.dump(snippets, f, indent=4, ensure_ascii=False)


def main() -> str:
    project_root = tf.find_project_root(Path(__file__))
    snippets_path = project_root / ".vscode/kyopro.code-snippets"
    lib_dir = project_root / "library"

    snippets = collect_snippets(lib_dir)
    write_snippets_to_file(snippets, snippets_path)

    return f"✅ Snippets generated: {snippets_path}"


if __name__ == "__main__":
    main()
