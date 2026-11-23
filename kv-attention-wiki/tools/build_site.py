"""Render wiki/*.md, raw/*.md and CLAUDE.md to browsable HTML next to the source files.

Markdown stays the source of truth (the LLM edits .md); the .html files are for GitHub Pages.
Links ending in .md are rewritten to .html.
"""
import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent

CSS = """
body{font-family:"Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif;background:#F5F1EA;color:#1E1C1A;margin:0}
.wrap{max-width:820px;margin:0 auto;padding:36px 28px 80px}
nav{font-size:14px;margin-bottom:26px;display:flex;gap:16px;flex-wrap:wrap}
nav a{color:#1F4E5A}
h1{font-size:32px;line-height:1.3;border-bottom:3px solid #E4572E;padding-bottom:10px}
h2{font-size:22px;margin-top:34px;color:#1F4E5A}
p,li{font-size:17px;line-height:1.75}
a{color:#1F4E5A}
blockquote{margin:18px 0;padding:12px 18px;background:#FFF7E6;border-left:5px solid #E9B44C;border-radius:0 8px 8px 0}
blockquote p{margin:0}
code{background:#EEE7DC;padding:1px 5px;border-radius:4px}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #DDD5C9;padding:6px 10px;text-align:left}
.tag{display:inline-block;font-size:12px;font-weight:700;background:#1F4E5A;color:#fff;border-radius:99px;padding:0 8px;margin:0 2px;text-decoration:none}
"""


def page(title, body, depth):
    up = "../" * depth
    return f"""<!DOCTYPE html><html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title>
<style>{CSS}</style></head><body><div class="wrap">
<nav><a href="{up}index.html">← 作業首頁</a><a href="{up}wiki/index.html">Wiki 目錄</a>
<a href="{up}slides/index.html">教學簡報</a><a href="{up}wiki/log.html">操作紀錄</a></nav>
{body}</div></body></html>"""


def render(md_path):
    rel = md_path.relative_to(ROOT)
    depth = len(rel.parts) - 1
    text = md_path.read_text(encoding="utf-8")
    html = markdown.markdown(text, extensions=["tables", "fenced_code"])
    html = re.sub(r'href="([^"#:]+)\.md"', r'href="\1.html"', html)
    # source tags 〔S01〕 -> link to the source page
    src_dir = "../" * depth + "wiki/sources/"
    html = re.sub(r"〔(S\d\d)〕", lambda m: f'<a class="tag" href="{src_dir}{m.group(1)}.html">{m.group(1)}</a>', html)
    title = (re.search(r"^# (.+)$", text, re.M) or [None, rel.stem])[1]
    md_path.with_suffix(".html").write_text(page(title, html, depth), encoding="utf-8")
    return rel


if __name__ == "__main__":
    files = [ROOT / "CLAUDE.md", *sorted((ROOT / "wiki").rglob("*.md")), *sorted((ROOT / "raw").glob("*.md")),
             *sorted((ROOT / "docs").glob("*.md"))]
    for f in files:
        render(f)
    print(f"build_site: 產生 {len(files)} 個 HTML 頁")
