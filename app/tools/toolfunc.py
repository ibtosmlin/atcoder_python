from pathlib import Path

import tomllib


def get_project_name() -> str:
    """rootのpyprojectに保存されたproject.nameを取得"""
    current = Path(__file__).parent
    toml_file = current / "pyproject.toml"
    while not toml_file.exists():
        current = current.parent
        toml_file = current / "pyproject.toml"

    with open(toml_file, "rb") as f:
        data = tomllib.load(f)
    return data["project"]["name"]


def find_project_root(start: Path, target_name: str = "") -> Path:
    if target_name == "":
        target_name = get_project_name()
    """指定された名前のディレクトリまで親をたどる"""
    while start.name != target_name:
        start = start.parent
    return start
