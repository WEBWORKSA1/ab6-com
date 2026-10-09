# AB6.com — "Ab Six": the six-pack abs & core training hub

Free, tool-first fitness site: body-fat / macro / abs-timeline calculators, workout generator with voice timer, 35-exercise library with an interactive core map, core strength test, 6-week challenge tracker with prize-draw entries, an abs-plan quiz funnel, coach-matching lead engine, YouTube video hub, gear affiliate guide, donations, contests, careers and sponsorship pages.

Static HTML/CSS/vanilla JS — runs on the **GitHub Pages free plan**.

## Structure
- `build.py` — shared layout (top inquiry bar, header, footer, AdSense, consent, lead modal) → generates all pages + `sitemap.xml`.
- `pages_tools.py`, `pages_learn.py`, `pages_biz.py` — page content. `common.py` — shared snippets.
- `assets/js/app.js` — `SITE` config, form delivery, nav, theme, consent, modal, YouTube, donations.
- `assets/js/tools.js` — calculators, quiz, library, generator, timer, core test, challenge.
- `assets/js/data.js` — exercise database + video list.
- `docs/PROMPTS.md` — phase-wise build prompt. `docs/RESEARCH.md` — concept decision, market data, 36-site teardown.

Edit content in `pages_*.py` and push — the **Build site** GitHub Action runs `python build.py` and `tools/make_images.py` and commits the generated `*.html` and images automatically. (Locally: `python3 build.py`.)

## Launch checklist
1. **GitHub Pages:** Settings → Pages → Build and deployment → *Deploy from a branch* → `main` / `(root)` (or `gh-pages` if it was auto-enabled; the workflow keeps `gh-pages` in sync with `main`).
2. **Custom domain:** DNS A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`; `www` CNAME → `webworksa1.github.io`. Then enter `ab6.com` in Pages settings and tick *Enforce HTTPS*.
3. **Forms:** submit any form once on the live site and click the activation link FormSubmit sends to the owner inbox (the address is encoded in `app.js` and never shown on the site).
4. **AdSense:** add the site in AdSense (`ads.txt` included). Optional manual units: fill `SITE.adSlots` in `app.js`. Enable a Google-certified CMP for EEA/UK/CH traffic.
5. **YouTube:** add your video IDs to `SITE.youtube` and channel URL to `SITE.youtubeChannel`.
6. **Donations:** add PayPal / Stripe / Buy Me a Coffee / Ko-fi / Patreon links to `SITE.donate` (the pledge form works without them).
7. **Affiliate:** set your Amazon Associates tag in `SITE.amazonTag`.
8. Submit `sitemap.xml` in Google Search Console.

## Legal
“AB6” is used only as a descriptive reading of the domain (“Ab Six”). AB6.com claims no trademark rights in “AB6” and is not affiliated with AB6IX, Brand New Music, AB6 Holdings LLC or any brand using “AB6”. See `disclaimer.html`. © AB6.com — original content and code all rights reserved; embedded videos belong to their creators.
