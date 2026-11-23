"""Check slides/outline.json before generating HTML.

  O1  every wiki reference exists
  O2  every term in "uses" was introduced on the same or an earlier slide (先教再用)
  O3  every term introduced is introduced only once
  O4  every concept page in the wiki is referenced by at least one slide (coverage)
  O5  every introduced term appears in the referenced wiki pages (so the definition comes from the wiki)
  O6  every declared fact (number + unit, e.g. "100 毫秒") appears in the referenced wiki pages
      -> added in workflow v2: numbers are checked at the plan stage, before any HTML exists
"""
import json
import re
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"

ALIASES = {  # term -> strings that count as "the wiki explains it"
    "bottom-up": ["bottom-up"],
    "top-down": ["top-down"],
    "注視": ["注視", "fixation"],
    "gist": ["gist", "Gist"],
    "AUC": ["AUC"],
}


def check():
    outline = json.loads((ROOT / "slides/outline.json").read_text(encoding="utf-8"))
    errors, seen, cited = [], {}, set()
    for s in outline["slides"]:
        sid = s["id"]
        texts = []
        for ref in s["wiki"]:
            p = WIKI / ref
            if not p.exists():
                errors.append(f"O1 第{sid}張 引用不存在的 wiki 頁：{ref}")
            else:
                cited.add(ref)
                raw = p.read_text(encoding="utf-8")
                # link labels like [遷移學習](...) don't count as an explanation
                texts.append(re.sub(r"\[[^\]]*\]\([^)]*\)", "", raw))
        for t in s["introduces"]:
            if t in seen:
                errors.append(f"O3 第{sid}張 重複介紹「{t}」（第{seen[t]}張已介紹）")
            seen.setdefault(t, sid)
            keys = ALIASES.get(t, [t])
            if not any(k in txt for k in keys for txt in texts):
                errors.append(f"O5 第{sid}張 介紹「{t}」但引用的 wiki 頁裡沒有解釋它")
        for fact in s.get("facts", []):
            squash = fact.replace(" ", "")
            if not any(squash in txt.replace(" ", "") for txt in texts):
                errors.append(f"O6 第{sid}張 打算放「{fact}」，但引用的 wiki 頁裡找不到（含單位）")
        for t in s["uses"]:
            if t not in seen:
                errors.append(f"O2 第{sid}張 用到「{t}」但前面還沒教")
    for p in sorted((WIKI / "concepts").glob("*.md")):
        ref = f"concepts/{p.name}"
        if ref not in cited:
            errors.append(f"O4 概念頁 {ref} 沒有任何投影片引用")
    return errors


if __name__ == "__main__":
    errs = check()
    for e in errs:
        print(e)
    print(f"check_outline: {len(errs)} 個問題")
    sys.exit(1 if errs else 0)
