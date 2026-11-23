"""Run the whole graph once, node by node.

Each check node either passes (go to the next node) or fails and says which node to
loop back to. This is the same graph drawn on the homepage.

  [lint_wiki]      fail -> back to INGEST (fix wiki pages)
  [check_outline]  fail -> back to QUERY (fix slides/outline.json; or back to INGEST if the wiki lacks it)
  [check_slides]   fail -> back to GENERATE (fix slides/index.html)
  [build_site]     render wiki to HTML
  [visual review]  human / AI looks at screenshots -> may send back to GENERATE
"""
import subprocess
import sys

NODES = [
    ("lint_wiki", "tools/lint_wiki.py", "回到 INGEST：修 wiki 頁"),
    ("check_outline", "tools/check_outline.py", "回到 QUERY：修 outline（或 wiki 沒寫到就回 INGEST）"),
    ("check_slides", "tools/check_slides.py", "回到 GENERATE：修簡報 HTML"),
    ("build_site", "tools/build_site.py", "建站失敗"),
]

for name, script, back in NODES:
    print(f"\n▶ {name}")
    r = subprocess.run([sys.executable, script])
    if r.returncode != 0:
        print(f"✗ {name} 沒通過 → {back}")
        sys.exit(1)
    print(f"✓ {name} 通過")
print("\n全部自動檢查通過 → 下一步：截圖做視覺檢查（visual review）")
