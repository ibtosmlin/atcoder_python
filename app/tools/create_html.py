import json
from collections import defaultdict
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

import tools.toolfunc as tf

ENCODING = "utf8"
SEGMENTS = [
    ("A", "一般アルゴリズム"),
    ("D", "データ構造"),
    ("Q", "クエリ"),
    ("G", "グラフ"),
    ("GB", "二部グラフ"),
    ("GD", "有向グラフ"),
    ("GT", "木"),
    ("SP", "最短経路"),
    ("N", "整数"),
    ("M", "行列"),
    ("Str", "文字列"),
    ("AL", "幾何"),
    ("O", "その他"),
]


def parse_lib_file(filepath: Path) -> dict | None:
    with filepath.open("r", encoding=ENCODING) as f:
        lines = [line.strip() for line in f]

    title, subtitle = None, []
    mode = None
    for line in lines:
        if line in {"#title#", "#subtitle#", "#name#"}:
            mode = line.strip("#")
            continue
        if mode == "name":
            break
        content = line[2:]
        if content:
            if mode == "title":
                title = content
            elif mode == "subtitle":
                subtitle.append(content)

    if title:
        return {"fname": filepath.name, "title": title, "subtitle": subtitle}
    return None


def collect_contents(lib_dir: Path, exclude: list[Path]) -> dict:
    contents = defaultdict(list)
    for filepath in sorted(lib_dir.glob("Lib_*.py")):
        if filepath in exclude:
            continue
        key = filepath.stem.split("_")[1]
        parsed = parse_lib_file(filepath)
        if parsed:
            contents[key].append(parsed)
    return contents


def collect_memos(memo_dir: Path) -> list[str]:
    return [fp.name for fp in sorted(memo_dir.glob("Memo_*.md"))]


def load_links(links_path: Path) -> dict:
    with links_path.open("r", encoding=ENCODING) as f:
        return json.load(f)


def render_html(template_dir: Path, output_path: Path, context: dict):
    env = Environment(loader=FileSystemLoader(template_dir, encoding=ENCODING))
    template = env.get_template("template.html")
    html = template.render(context)
    output_path.write_text(html, encoding=ENCODING)
    return f"✅ HTML generated: {output_path}"


def main():
    root = tf.find_project_root(Path(__file__))
    lib_dir = root / "library"
    template_dir = root / "web/templates"
    output_path = root / "index.html"
    exclude = [lib_dir / "Lib_templete.py"]

    context = {
        "segments": [[code, label, []] for code, label in SEGMENTS],
        "memos": collect_memos(lib_dir),
        "links": load_links(lib_dir / "Links.json"),
    }

    contents = collect_contents(lib_dir, exclude)
    for segment in context["segments"]:
        segment[2] = contents.get(segment[0], [])

    return render_html(template_dir, output_path, context)


if __name__ == "__main__":
    main()
