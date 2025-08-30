from pathlib import Path

import tools.toolfunc as tf
from tomlkit import dumps, parse

ENCODING = "utf8"
SECTION = "contest"


def main(new_id: str) -> str:
    app_root = tf.find_project_root(Path(__file__), target_name="app")
    config_file_path: Path = app_root / "config.toml"

    # TOMLファイルを読み込んでパース（コメントや順序も保持）
    with open(config_file_path, "r", encoding=ENCODING) as f:
        toml_content = f.read()
        toml_data = parse(toml_content)

    # contest セクションが存在しない場合は作成
    if SECTION not in toml_data:
        toml_data[SECTION] = {}

    # id を更新
    toml_data[SECTION]["id"] = new_id

    # TOMLファイルに書き戻す（構造・コメント保持）
    with open(config_file_path, "w", encoding=ENCODING) as f:
        f.write(dumps(toml_data))

    return f"✅ Updated {config_file_path} [contest].id to: {new_id}"
