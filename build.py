#!/usr/bin/env python3
"""AB6.com static site generator.
Every page shares one layout (top inquiry bar, header, footer, AdSense, consent, lead modal).
Edit page content in pages_*.py, then run:  python3 build.py   (add --preview for fully rendered local copies)
Output: _layouts/default.html + one Jekyll page per *.html + sitemap.xml.
GitHub Pages (free plan) runs Jekyll automatically and merges each page into the shared layout."""
import json, os, sys, datetime
from pages_tools import PAGES as P1
from pages_learn import PAGES as P2
from pages_biz import PAGES as P3

DOMAIN = "https://ab6.com"
ADS = "ca-pub-6620975821265271"
INQUIRY_URL = "https://web.works/contact"
TODAY = datetime.date.today().isoformat()
ROOT = os.path.dirname(os.path.abspath(__file__))
PREVIEW = "--preview" in sys.argv  # also write fully rendered pages to _preview/ for local testing

LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="10" fill="#c4ff3d"/>'
        + "".join(f'<rect x="{9 + c * 12}" y="{7 + r * 9.5}" width="10" height="7.5" rx="2.4" fill="#0a0c0f"/>'
                  for r in range(3) for c in range(2)) + "</svg>")

NAV = [
    ("Tools", [("abs-quiz.html", "Find My Abs Plan (quiz)"), ("body-fat-calculator.html", "Body Fat Calculator"),
               ("macro-calculator.html", "Calorie &amp; Macro Calculator"), ("abs-timeline-calculator.html", "Abs Timeline Calculator"),
               ("workout-generator.html", "Ab Workout Generator + Timer"), ("core-test.html", "Core Strength Test"), ("calculators.html", "All tools →")]),
    ("Train", [("exercises.html", "Ab Exercise Library"), ("challenge.html", "6-Week AB6 Challenge"),
               ("videos.html", "Follow-Along Videos"), ("gear.html", "Home Ab Gear Guide")]),
    ("Learn", [("how-to-get-six-pack-abs.html", "How to Get Six-Pack Abs"), ("lower-abs-workout.html", "Lower Abs Workout"),
               ("ab-workout-at-home.html", "Ab Workout at Home"), ("abs-for-women.html", "Abs for Women"),
               ("nutrition.html", "Abs Nutrition Guide"), ("guides.html", "All guides →")]),
    ("coaching.html", "Get a Coach"),
    ("contests.html", "Contests"),
    ("support.html", "Support"),
]

def nav_html():
    out = []
    for item in NAV:
        if isinstance(item[1], list):
            subs = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in item[1])
            out.append(f'<li><button class="dd" type="button" aria-haspopup="true">{item[0]} ▾</button><ul class="sub">{subs}</ul></li>')
        else:
            out.append(f'<li><a href="{item[0]}">{item[1]}</a></li>')
    return "".join(out)

FOOT = f'''
<footer class="footer">
 <div class="wrap">
  <div class="cols">
   <div>
    <a class="brand" href="index.html">{LOGO}<span>AB6<small>Ab Six · Core &amp; Six-Pack Hub</small></span></a>
    <p class="muted small" style="margin-top:12px">Free, evidence-informed tools, workouts and plans for a stronger core and visible abs. Built to be useful first.</p>
    <form class="nl-form" data-form="Newsletter signup" data-lead data-ok="You're in! Check your inbox for the weekly AB6 workout.">
     <label for="nl-email" class="small">Get the free weekly ab workout</label>
     <div class="nl"><input id="nl-email" type="email" name="email" placeholder="you@example.com" required autocomplete="email"><button class="btn btn-primary btn-sm" type="submit">Join</button></div>
     <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
     <div class="form-msg small" role="status"></div>
    </form>
   </div>
   <div><h4>Tools</h4><ul>
    <li><a href="abs-quiz.html">Abs Plan Quiz</a></li><li><a href="body-fat-calculator.html">Body Fat Calculator</a></li>
    <li><a href="macro-calculator.html">Macro Calculator</a></li><li><a href="abs-timeline-calculator.html">Abs Timeline</a></li>
    <li><a href="workout-generator.html">Workout Generator</a></li><li><a href="core-test.html">Core Test</a></li></ul></div>
   <div><h4>Train &amp; Learn</h4><ul>
    <li><a href="exercises.html">Exercise Library</a></li><li><a href="challenge.html">6-Week Challenge</a></li>
    <li><a href="videos.html">Videos</a></li><li><a href="guides.html">Guides</a></li>
    <li><a href="nutrition.html">Nutrition</a></li><li><a href="gear.html">Gear Guide</a></li></ul></div>
   <div><h4>Community</h4><ul>
    <li><a href="coaching.html">Get a Coach</a></li><li><a href="coaching.html#coaches">For Coaches</a></li>
    <li><a href="contests.html">Contests &amp; Prizes</a></li><li><a href="support.html">Donate / Support</a></li>
    <li><a href="careers.html">Careers</a></li><li><a href="advertise.html">Advertise &amp; Sponsor</a></li></ul></div>
   <div><h4>Company</h4><ul>
    <li><a href="about.html">About</a></li><li><a href="contact.html">Contact</a></li>
    <li><a href="privacy.html">Privacy</a></li><li><a href="terms.html">Terms</a></li>
    <li><a href="disclaimer.html">Disclaimer &amp; Trademarks</a></li><li><a href="{INQUIRY_URL}" target="_blank" rel="noopener">Buy / Partner</a></li></ul></div>
  </div>
  <div class="legal">
   <p>© <span data-year>2026</span> AB6.com. All original content, tools and code on this site are copyright of AB6.com. “AB6” is used here only as a descriptive reading of the domain name (“Ab Six” — six-pack abs); AB6.com claims no trademark rights in “AB6” and is not affiliated with, endorsed by or connected to AB6IX, Brand New Music, AB6 Holdings LLC or any product or company using “AB6”. Video embeds and brand names belong to their respective owners. Content is educational, not medical advice — <a href="disclaimer.html">read the full disclaimer</a>. Some links may be affiliate links.</p>
  </div>
 </div>
</footer>
<div class="cookie" role="dialog" aria-label="Cookie consent">
 <b>Cookies &amp; ads</b>
 <p class="small muted" style="margin:6px 0 0">We use cookies for ads (Google AdSense), analytics and to remember your tool progress on this device. See our <a href="privacy.html">Privacy Policy</a>.</p>
 <div class="row"><button class="btn btn-primary btn-sm" data-cookie="all">Accept all</button><button class="btn btn-ghost btn-sm" data-cookie="essential">Essential only</button></div>
</div>
<div class="modal" id="leadModal" role="dialog" aria-modal="true" aria-labelledby="lmTitle">
 <div class="box">
  <button class="icon-btn x" data-close aria-label="Close">✕</button>
  <div class="eyebrow">Free · 6-week plan</div>
  <h2 id="lmTitle" style="font-size:2rem">Before you go — want the plan?</h2>
  <p class="muted">Get the printable AB6 6-Week Core Plan plus one new ab workout every week. No spam, unsubscribe anytime.</p>
  <form class="form" data-form="Lead magnet — exit popup" data-lead data-ok="Done! Your plan is on its way. Meanwhile, try the quiz for a personalised version.">
   <input type="text" name="name" placeholder="First name" autocomplete="given-name" aria-label="First name">
   <input type="email" name="email" placeholder="Email address" required autocomplete="email" aria-label="Email">
   <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
   <button class="btn btn-primary btn-block" type="submit">Send me the free plan</button>
   <div class="form-msg small" role="status"></div>
   <a href="abs-quiz.html" class="small center">Or build a personalised plan in 60 seconds →</a>
  </form>
 </div>
</div>
<div class="mcta"><a class="btn btn-primary" href="abs-quiz.html">Free Abs Plan</a><a class="btn btn-dark" href="coaching.html">Get a Coach</a></div>
'''

def page_vars(p):
    """Per-page values that fill the shared Jekyll layout (_layouts/default.html)."""
    slug = p["slug"]
    url = DOMAIN + "/" + ("" if slug == "index" else slug + ".html")
    title, desc = p["title"], p["desc"]
    base_schema = {"@context": "https://schema.org", "@type": "WebPage", "name": title, "description": desc, "url": url,
                   "isPartOf": {"@type": "WebSite", "name": "AB6.com", "url": DOMAIN}}
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in [base_schema] + (p.get("schema") or []))
    scripts = '<script src="assets/js/app.js" defer></script>'
    if p.get("tools"):
        scripts = '<script src="assets/js/data.js" defer></script>' + scripts + '<script src="assets/js/tools.js" defer></script>'
    return {"title": title, "description": desc, "canonical": url,
            "robots": p.get("robots", "index,follow,max-image-preview:large"), "og_type": p.get("og_type", "website"),
            "body_attr": " data-no-modal" if p.get("no_modal") else "", "scripts": scripts, "ld": ld}

# Shared layout. GitHub Pages (Jekyll) fills {{ page.* }} and {{ content }} at publish time.
TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ page.title }}</title>
<meta name="description" content="{{ page.description }}">
<link rel="canonical" href="{{ page.canonical }}">
<meta name="robots" content="{{ page.robots }}">
<meta name="theme-color" content="#0a0c0f">
<meta name="google-adsense-account" content="__ADS__">
<meta property="og:type" content="{{ page.og_type }}">
<meta property="og:site_name" content="AB6.com">
<meta property="og:title" content="{{ page.title }}">
<meta property="og:description" content="{{ page.description }}">
<meta property="og:url" content="{{ page.canonical }}">
<meta property="og:image" content="__DOMAIN__/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/icon-192.png">
<link rel="manifest" href="manifest.webmanifest">
<script>try{var t=localStorage.getItem("ab6-theme");if(t)document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=__ADS__" crossorigin="anonymous"></script>
{{ page.ld }}
</head>
<body{{ page.body_attr }}>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><a href="__INQ__" target="_blank" rel="noopener">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership →</a></div>
<header class="header">
 <div class="wrap nav">
  <a class="brand" href="index.html" aria-label="AB6.com home">__LOGO__<span>AB6<small>Ab Six · Core Hub</small></span></a>
  <button class="icon-btn burger" aria-label="Menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
  <ul class="menu">__NAV__<li><a class="btn btn-primary btn-sm cta" href="abs-quiz.html">Free Plan</a></li></ul>
  <button class="icon-btn" data-theme-toggle aria-label="Toggle light/dark theme"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 3a9 9 0 000 18z" fill="currentColor"/></svg></button>
 </div>
</header>
<main id="main">
{{ content }}</main>
__FOOT__
{{ page.scripts }}
</body>
</html>
"""

def layout_source():
    return (TEMPLATE.replace("__ADS__", ADS).replace("__DOMAIN__", DOMAIN).replace("__INQ__", INQUIRY_URL)
            .replace("__LOGO__", LOGO).replace("__NAV__", nav_html()).replace("__FOOT__", FOOT))

def page_source(p):
    """A Jekyll page: YAML front matter (JSON-quoted strings are valid YAML) + raw body."""
    fm = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in page_vars(p).items())
    return f"---\nlayout: default\n{fm}\n---\n{{% raw %}}\n{p['body']}\n{{% endraw %}}\n"

def render_preview(p):
    """Local stand-in for Jekyll: same substitutions GitHub Pages performs (used for testing only)."""
    out = layout_source()
    for k, v in page_vars(p).items():
        out = out.replace("{{ page.%s }}" % k, v)
    return out.replace("{{ content }}", "\n" + p["body"] + "\n\n")


def build():
    pages = P1 + P2 + P3
    os.makedirs(os.path.join(ROOT, "_layouts"), exist_ok=True)
    with open(os.path.join(ROOT, "_layouts", "default.html"), "w", encoding="utf-8") as f:
        f.write(layout_source())
    if PREVIEW:
        os.makedirs(os.path.join(ROOT, "_preview"), exist_ok=True)
    seen = set()
    for p in pages:
        assert p["slug"] not in seen, p["slug"]
        seen.add(p["slug"])
        with open(os.path.join(ROOT, p["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(page_source(p))
        if PREVIEW:
            with open(os.path.join(ROOT, "_preview", p["slug"] + ".html"), "w", encoding="utf-8") as f:
                f.write(render_preview(p))
    urls = []
    for p in pages:
        if p.get("robots", "").startswith("noindex"):
            continue
        loc = DOMAIN + "/" + ("" if p["slug"] == "index" else p["slug"] + ".html")
        pr = p.get("priority", "0.7")
        urls.append(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    print(f"Built {len(pages)} pages + sitemap.xml")

if __name__ == "__main__":
    build()
