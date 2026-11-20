# Apply to a copy of the complete current Netlify source after adding the two staged HTML articles.
# Run from the deployment root. The separately prepared bread-storage patch remains independent.
from pathlib import Path
import json

EDITS = json.loads('[["index.html", "<section class=\\"welcome\\"", "<section class=\\"more-guides\\" id=\\"make-ahead-holidays\\"><h2>Make ahead for the holidays</h2><div class=\\"grid recipe-grid\\"><article class=\\"card\\"><a href=\\"/make-ahead-thanksgiving-dinner-rolls\\"><figure class=\\"photo\\"><img src=\\"/images/bread-storage.jpg\\" alt=\\"Original illustration of homemade bread storage.\\" width=\\"1536\\" height=\\"1024\\" loading=\\"lazy\\" decoding=\\"async\\"></figure><div class=\\"cardtext\\"><p class=\\"eyebrow\\">Holiday baking</p><h3>Make-ahead Thanksgiving dinner rolls</h3><p>Choose when to bake, freeze and warm your rolls around a busy oven.</p><span class=\\"read\\">Read the guide →</span></div></a></article><article class=\\"card\\"><a href=\\"/freeze-cookie-dough-holiday-baking\\"><figure class=\\"photo\\"><img src=\\"/images/holiday-cookies-nov10.jpg\\" alt=\\"Chocolate chip cookies on a rimmed baking sheet.\\" width=\\"1536\\" height=\\"1024\\" loading=\\"lazy\\" decoding=\\"async\\"></figure><div class=\\"cardtext\\"><p class=\\"eyebrow\\">Holiday baking</p><h3>Freeze cookie dough for holiday baking</h3><p>Plan which dough to scoop, roll into a log or flatten before freezing.</p><span class=\\"read\\">Read the guide →</span></div></a></article></div></section><section class=\\"welcome\\"", "id=\\"make-ahead-holidays\\""], ["sitemap.xml", "</urlset>", "<url><loc>https://prettypractical.netlify.app/make-ahead-thanksgiving-dinner-rolls</loc></url><url><loc>https://prettypractical.netlify.app/freeze-cookie-dough-holiday-baking</loc></url></urlset>", "/make-ahead-thanksgiving-dinner-rolls</loc>"], ["holiday-cookie-baking-sheet.html", "</article>", "<aside class=\\"next-read\\"><p class=\\"eyebrow\\">Plan the next batch</p><a href=\\"/freeze-cookie-dough-holiday-baking\\">Freeze cookie dough for your holiday cookie tin →</a></aside></article>", "href=\\"/freeze-cookie-dough-holiday-baking\\""], ["sandwich-bread-tools.html", "</article>", "<aside class=\\"next-read\\"><p class=\\"eyebrow\\">Plan the next batch</p><a href=\\"/make-ahead-thanksgiving-dinner-rolls\\">Plan your make-ahead Thanksgiving dinner rolls →</a></aside></article>", "href=\\"/make-ahead-thanksgiving-dinner-rolls\\""]]')
planned = []
for filename, old, new, marker in EDITS:
    path = Path(filename)
    content = path.read_text()
    if marker in content:
        continue
    if content.count(old) != 1:
        raise ValueError(f"Expected one insertion point in {filename}")
    planned.append((path, content.replace(old, new, 1)))

for path, content in planned:
    path.write_text(content)
    print(f"Updated {path}")
