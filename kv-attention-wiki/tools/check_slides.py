"""Check the generated slides/index.html against the outline and the wiki.

  S1  slide count matches outline.json
  S2  each slide's data-wiki matches the outline's wiki list (same pages)
  S3  every number shown on a slide (years excluded) appears in the wiki pages that slide cites
  S4  every ../wiki/*.html link points to a wiki page that exists
  S5  (v2) every number shown on a slide was declared in that slide's outline "facts"

Text inside class="kicker" (section labels like 「問題 1」) or data-check="skip"
(question numbering, the fictional demo KV) is not fact-checked: it is structure or
made-up stimulus, not a claim taken from the wiki.
"""
import html.parser
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
NUM = re.compile(r"(?<![\w.])\d+(?:\.\d+)?")


class Slides(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides, self.cur, self.skip = [], None, 0
        self.stack = []  # (tag, skipping?) for nested no-check zones
        self.void = {"br", "img", "input", "meta", "link", "hr", "circle", "rect", "path"}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if tag not in self.void:
            nocheck = "kicker" in (a.get("class") or "").split() or a.get("data-check") == "skip"
            self.stack.append(nocheck)
            if nocheck:
                self.skip += 1
        if tag == "section" and "slide" in (a.get("class") or ""):
            self.cur = {"wiki": [w for w in (a.get("data-wiki") or "").split(",") if w],
                        "text": [], "links": []}
            self.slides.append(self.cur)
        if self.cur is not None:
            href = a.get("href") or ""
            if href.startswith("../wiki/"):
                self.cur["links"].append(href)
            for key in ("data-why", "aria-label"):
                if a.get(key) and not self.skip:
                    self.cur["text"].append(a[key])

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        if tag not in self.void and self.stack:
            if self.stack.pop():
                self.skip -= 1

    def handle_data(self, data):
        if self.cur is not None and not self.skip:
            self.cur["text"].append(data)


def check():
    outline = json.loads((ROOT / "slides/outline.json").read_text(encoding="utf-8"))["slides"]
    p = Slides()
    p.feed((ROOT / "slides/index.html").read_text(encoding="utf-8"))
    errors = []
    if len(p.slides) != len(outline):
        errors.append(f"S1 投影片 {len(p.slides)} 張，outline 有 {len(outline)} 張")
    for n, (s, o) in enumerate(zip(p.slides, outline), 1):
        if set(s["wiki"]) != set(o["wiki"]):
            errors.append(f"S2 第{n}張 data-wiki {sorted(s['wiki'])} ≠ outline {sorted(o['wiki'])}")
        wiki_text = ""
        for ref in s["wiki"]:
            f = WIKI / ref
            if f.exists():
                wiki_text += f.read_text(encoding="utf-8")
        text = " ".join(s["text"])
        for num in sorted(set(NUM.findall(text))):
            if re.fullmatch(r"(19|20)\d\d", num):
                continue
            if not re.search(rf"(?<![\d.]){re.escape(num)}(?![\d])", wiki_text):
                errors.append(f"S3 第{n}張 出現數字 {num}，但它引用的 wiki 頁裡沒有")
        declared = set(NUM.findall(" ".join(o.get("facts", []))))
        for num in sorted(set(NUM.findall(text))):
            if re.fullmatch(r"(19|20)\d\d", num):
                continue
            if num not in declared:
                errors.append(f"S5 第{n}張 出現數字 {num}，但 outline 沒有宣告這個 fact")
        for href in s["links"]:
            md = WIKI / href[len("../wiki/"):].replace(".html", ".md")
            if not md.exists():
                errors.append(f"S4 第{n}張 連結到不存在的 wiki 頁：{href}")
    return errors


if __name__ == "__main__":
    errs = check()
    for e in errs:
        print(e)
    print(f"check_slides: {len(errs)} 個問題")
    sys.exit(1 if errs else 0)
