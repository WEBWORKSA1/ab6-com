# AB6.com — Phase-wise Build Prompt

Reusable, phase-by-phase prompt used to build AB6.com. Run each phase in order; each phase ends with a check that must pass before the next one starts.

> **Owner inbox:** referred to below as `[OWNER_INBOX]`. It is never written into HTML, docs or visible text. It exists only as an encoded value inside `assets/js/app.js`, and all forms post to it through FormSubmit.

---

## Phase 0 — Concept lock

**Prompt:**
> Domain **AB6.com** reads as "Ab Six", meaning six-pack abs. Build **the free, tool-first six-pack abs and core training hub**.
>
> - **Audience:** adults aged 18–55 who want visible abs, a stronger core or less belly fat. They train at home or in a gym.
> - **Revenue stack, in order:**
>   1. Coaching lead generation: sell qualified client requests to certified coaches per lead or on revenue share.
>   2. Google AdSense, publisher `ca-pub-6620975821265271`.
>   3. YouTube: embeds now, an owned channel later.
>   4. Affiliate gear links.
>   5. Sponsorships and prize partnerships.
>   6. Donations.
> - **Name rule:** do not use the AB6IX name, imagery or brand assets. Add a trademark and copyright non-affiliation notice.

**Check:** the concept, revenue model and disclaimer are written down in `docs/RESEARCH.md`.

## Phase 1 — Competitive teardown (35+ sites)

**Prompt:**
> Visit at least 35 world-class sites in the fitness, abs and coaching niche:
> - Men's Health, Muscle & Strength, Athlean-X, DAREBEE, Fitness Blender, Nerd Fitness, ACE, MuscleWiki, ExRx, StrengthLog
> - Chloe Ting, Sweat, Centr, Freeletics, Jefit, StrongLifts, Legion, Precision Nutrition, Examine, BarBend, Garage Gym Reviews, Shape
> - Healthline, SELF, Women's Health, calculator.net, TDEEcalculator, NASM, ISSA, Thumbtack, Trainerize, Mindbody, Gymshark, Peloton, Bodybuilding.com, Verywell Fit
>
> For each site, extract its tools, content types, lead forms and fields, monetisation and UX patterns. Aggregate the results into a must-have feature list.

**Check:** the feature matrix is in `docs/RESEARCH.md`.

## Phase 2 — Design system and shell

**Prompt:**
> Build a static HTML/CSS/vanilla-JS site that runs on the free GitHub Pages plan, with no build server and no backend.
>
> **Design system**
> - Dark athletic theme: background `#0a0c0f`, lime accent `#c4ff3d`, cyan secondary `#3dd6ff`.
> - Fonts: Anton for display headings, Inter for body text.
> - Light-mode toggle, with the choice remembered in localStorage.
> - Mobile-first with a 16px gutter and no horizontal scroll.
> - Respect `prefers-reduced-motion`. Meet WCAG AA contrast.
>
> **Every page includes**
> - A full-width top bar with the exact text "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership", linked to `https://web.works/contact`.
> - A sticky header with dropdown navigation (Tools, Train, Learn), plus Get a Coach, Contests, Support and a "Free Plan" call-to-action button.
> - A footer with a newsletter form, link columns and a trademark/copyright notice.
> - A cookie consent banner.
> - An exit-intent / 45-second lead-magnet modal, shown at most once per 3 days.
> - A sticky mobile call-to-action bar (Free Abs Plan / Get a Coach).
> - SEO tags: canonical, Open Graph and Twitter tags, JSON-LD, the AdSense auto-ads script and the `google-adsense-account` meta tag.
>
> **Generator:** use a Python generator (`build.py`) with one shared layout, page content kept in `pages_*.py`, and a sitemap built automatically.

**Check:**
- `python3 build.py` builds every page.
- No horizontal overflow at 390px or 1280px.
- The top bar appears on every page.

## Phase 3 — Interactive tools (the traffic engine)

**Prompt:**
> Build these tools in `assets/js/tools.js`, all running on the client, with results kept on the device:
> 1. **Body-fat calculator** using the US Navy method, with a metric/imperial toggle. Output an ACE category, fat and lean mass, and an ab-visibility rating. It deep-links into the timeline calculator.
> 2. **Calorie and macro calculator.** Use Mifflin-St Jeor, or Katch-McArdle when body fat is given, with 5 activity levels and 5 goals. Set protein first, keep fat at 25% or more of calories, enforce a safety calorie floor, and show fibre.
> 3. **Abs timeline calculator.** Hold lean mass constant, apply a weekly loss of 0.5–1% of body weight, and output weeks, target date, goal weight and an SVG projection curve.
> 4. **Exercise library** of 35+ exercises tagged by area, level and equipment, each with steps, a coaching cue, the main mistake and a demo link. Include an interactive SVG core muscle map that filters the list, and an "add to my workout" list stored in localStorage.
> 5. **Workout generator** with a balanced core-function selection, level-based work/rest intervals, and rounds that fit the chosen time. Add an interval timer with beeps (WebAudio), spoken exercise names (speechSynthesis) and a screen wake lock.
> 6. **Core strength test** for plank, side plank and hollow hold: countdown, stopwatch, grades, and personal records saved locally.
> 7. **6-week challenge tracker:** a 42-day calendar, a daily plan, a progress ring, a streak counter and prize-draw entries (one per week with at least 5 of 7 days done).
> 8. **Workout of the day**, chosen deterministically from the date.

**Check:** a Playwright run of every tool shows correct numbers and no console errors.

## Phase 4 — Lead generation (highest revenue per visitor)

**Prompt:**
> 1. **Quiz funnel** (`abs-quiz.html`).
>    - 7 steps: sex, goal, level, equipment, minutes, days and current midsection.
>    - Show the summary plan and week 1 without asking for anything.
>    - Ask for name and email to unlock the full 6-week plan and the print/PDF version, with an optional checkbox for a free coach consult.
> 2. **Dedicated coaching page** (`coaching.html`).
>    - 4-step application with a progress bar: goal and timeline → starting point → format, budget and location → contact details with consent.
>    - Include market price ranges with a cited source, a "how it works" section and specialisms.
>    - Add a coach-network B2B application (certification, capacity, pay-per-lead or revenue-share terms).
> 3. **Short coaching form on the home page.**
> 4. **Lead magnets everywhere else:** the challenge signup, the exit-intent modal and the newsletter form in the footer.
> 5. **Form delivery:** every form sends JSON to `formsubmit.co/ajax/[OWNER_INBOX]`, where the inbox is decoded at runtime from char codes. Each form has a honeypot field, a subject tag, and the page URL attached.

**Check:**
- Searching the built HTML, CSS and JS for the plaintext inbox finds nothing.
- Each form shows its success or error message.

## Phase 5 — Content and SEO

**Prompt:**
> 1. **Articles.** Write evidence-informed long-form pages, each with a table of contents, byline, cited PubMed sources, a health note, an FAQ with FAQPage schema and a sidebar call to action:
>    - the pillar "How to get six-pack abs"
>    - Lower abs workout
>    - Ab workout at home
>    - Abs for women
>    - Abs nutrition
> 2. **Hub pages:** guides, all tools and videos.
> 3. **Tool pages:** each one carries explanatory content below the tool so it ranks for searches.

**Check:**
- Every page has a unique title and meta description.
- The sitemap lists every indexable page.

## Phase 6 — Monetisation layers

**Prompt:**
> - **AdSense:**
>   - Load the auto-ads script on every page.
>   - Add manual `.ad-slot` placeholders (top, inContent, sidebar). They stay hidden until slot IDs are added to `SITE.adSlots`.
>   - Add `ads.txt`.
> - **YouTube:**
>   - Use a click-to-load player on `youtube-nocookie.com` and verify embeddable video IDs with oEmbed.
>   - Your own videos come from `SITE.youtube`, and a subscribe button appears once `SITE.youtubeChannel` is set.
> - **Affiliate:** a gear guide whose links are built from Amazon searches plus `SITE.amazonTag`, with a clear disclosure and no claims that products were tested.
> - **Donations** (`support.html`):
>   - Tiers of $6, $26, $66 and a custom amount, with a choice of one-time, monthly or yearly.
>   - Donors can direct their money to operations, prizes, promotion, hiring or new tools.
>   - Show the planned allocation as bars.
>   - Payment buttons appear only after you add links in `SITE.donate`; until then, a pledge form handles donations.
> - **Sponsorship** (`advertise.html`): 6 package types and an inquiry form.

## Phase 7 — Community: contests, hiring, trust

**Prompt:**
> - **Contests:** transformation, a consistency draw, a creator contest and bring-a-friend. Include a prize structure template, a "sponsor a prize" call to action, an entry form with age and rules confirmation, and an official rules summary (no purchase necessary, eligibility, odds, skill-testing question, verification, substitution), plus a hall of fame.
> - **Careers:** 8 role types and an application form.
> - **Trust pages:** about, privacy, terms and disclaimer. The disclaimer covers the trademark/name notice, copyright, medical, results and affiliate disclosures. Privacy covers the AdSense cookie wording, YouTube, local storage and GDPR/PIPEDA/Law 25/CCPA rights.

## Phase 8 — QA

**Prompt:**
> Use Playwright to:
> - load every page and fail on JavaScript errors or horizontal overflow;
> - run each calculator with known inputs;
> - complete the quiz end to end;
> - take mobile and desktop screenshots.
>
> Also check that keyboard focus is visible, labels are present and reduced motion is respected.

## Phase 9 — Deploy (GitHub Pages, free plan)

**Prompt:**
> 1. Push to `WEBWORKSA1/AB6-com` on the `main` branch, with the site at the repo root.
> 2. Include `.nojekyll`, `404.html`, `robots.txt`, `sitemap.xml` and `ads.txt`.
> 3. Enable Pages under Settings → Pages → Deploy from a branch → `main` / root.
> 4. For the custom domain:
>    - DNS A records: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
>    - `www` CNAME → `webworksa1.github.io`.
>    - Then set `ab6.com` in Pages settings and turn on Enforce HTTPS.
> 5. Submit the first live form once and confirm the FormSubmit activation email.

## Phase 10 — Expansion roadmap

- An owned YouTube channel: "AB6 Originals", 10–20 minute follow-alongs, plus Shorts made from the exercise library.
- Public coach profiles, coach reviews and city landing pages (for example `/coaches/toronto`) for local SEO.
- A premium printable program (a PDF sold through Gumroad, Lemon Squeezy or similar) and a paid ad-free tier.
- More calculators: protein, waist-to-height ratio, ideal weight for abs, plus more programmatic exercise pages.
- A multilingual version (FR/ES/HI) built with the same `build.py` pipeline.
- A season leaderboard, once a backend is added (Supabase free tier).
