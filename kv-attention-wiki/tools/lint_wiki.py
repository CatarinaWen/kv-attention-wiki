"""Lint the LLM Wiki.

Checks
  L1  every bullet in concept / synthesis / source pages carries a source tag 〔S0x〕
      (bullets under "相關頁面" / "待補" / "寫進了哪些概念頁" are exempt)
  L2  every source tag points to an existing wiki/sources/S0x.md and raw/S0x-*.md
  L3  every Markdown link to a .md file resolves
  L4  no orphan concept / synthesis pages (each linked from at least one other page)
  L5  numbers in a tagged bullet (years excluded) appear in the raw note of a cited source
  L6  every concept page has a one-line explanation ("> 一句話")
Exit code 1 if any error.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"

TAG = re.compile(r"〔(S\d\d)〕")
LINK = re.compile(r"\[[^\]]*\]\(([^)#]+\.md)\)")
NUM = re.compile(r"(?<![\w.])\d+(?:\.\d+)?")
EXEMPT_SECTIONS = ("相關頁面", "待補", "寫進了哪些概念頁")


def raw_text(sid):
    hits = list(RAW.glob(f"{sid}-*.md"))
    return hits[0].read_text(encoding="utf-8") if hits else None


def numbers(text):
    out = []
    for n in NUM.findall(text):
        if re.fullmatch(r"(19|20)\d\d", n):
            continue  # years
        out.append(n)
    return out


def lint():
    errors = []
    pages = sorted(p for p in WIKI.rglob("*.md"))
    inbound = {p: 0 for p in pages}

    for page in pages:
        rel = page.relative_to(ROOT)
        text = page.read_text(encoding="utf-8")
        section = ""
        for i, line in enumerate(text.splitlines(), 1):
            if line.startswith("## "):
                section = line[3:]
            # L3 links
            for target in LINK.findall(line):
                dest = (page.parent / target).resolve()
                if not dest.exists():
                    errors.append(f"L3 {rel}:{i} 死連結 → {target}")
                elif dest in inbound and dest != page:
                    inbound[dest] += 1
            kind = page.parent.name
            if kind not in ("concepts", "synthesis", "sources"):
                continue
            if not line.startswith("- "):
                continue
            if any(s in section for s in EXEMPT_SECTIONS):
                continue
            tags = TAG.findall(line)
            # L1 tag present
            if not tags:
                errors.append(f"L1 {rel}:{i} 沒有標來源：{line[:40]}")
                continue
            # L2 tag resolves
            for t in tags:
                if not (WIKI / "sources" / f"{t}.md").exists() or raw_text(t) is None:
                    errors.append(f"L2 {rel}:{i} 來源 {t} 不存在")
            # L5 numbers traceable to raw
            body = TAG.sub("", line)
            body = re.sub(r"\(([^)]*)\)", "", body)  # drop link targets
            raws = "".join(raw_text(t) or "" for t in tags)
            for n in numbers(body):
                # whole-number match, so "36" does not pass because raw has "1363"
                if not re.search(rf"(?<![\d.]){re.escape(n)}(?![\d])", raws):
                    errors.append(f"L5 {rel}:{i} 數字 {n} 在 {'/'.join(tags)} 的 raw 筆記找不到")
        # L6 one-liner
        if page.parent.name == "concepts" and "> 一句話" not in text:
            errors.append(f"L6 {rel} 缺少「一句話」解釋")

    # L4 orphans
    for p, n in inbound.items():
        if p.parent.name in ("concepts", "synthesis") and n == 0:
            errors.append(f"L4 {p.relative_to(ROOT)} 是孤兒頁（沒有其他頁連到）")
    return errors


if __name__ == "__main__":
    errs = lint()
    for e in errs:
        print(e)
    print(f"lint_wiki: {len(errs)} 個問題")
    sys.exit(1 if errs else 0)
