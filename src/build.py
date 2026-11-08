import json, sys
sys.path.insert(0, ".")
from data import Q, CATS
rows = [dict(c=c, qp=qp, ap=ap, dp=dp, qe=qe, ae=ae, de=de, g=g) for c,qp,ap,dp,qe,ae,de,g in Q]
assert all(r["c"] in CATS for r in rows)
assert len({r["qe"] for r in rows}) == len(rows), "dup"
html = open("template.html", encoding="utf-8").read()
html = (html.replace("__DATA__", json.dumps(rows, ensure_ascii=False))
            .replace("__CATS__", json.dumps(CATS, ensure_ascii=False))
            .replace("__COUNT__", str(len(rows))))
html = html.replace("—", "-")
import os; os.makedirs("site", exist_ok=True)
open("site/index.html", "w", encoding="utf-8").write(html)
print(len(rows), "questions,", sum(r["g"] for r in rows), "in-game verified,", len(html)//1024, "KB")
