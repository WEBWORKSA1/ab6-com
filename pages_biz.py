"""AB6.com — lead gen, monetisation, community and legal pages."""
from common import (HP, MSG, CONSENT, ICON, phero, ad, faq, band, card, sidebar)

PAGES = []
INQ = "https://web.works/contact"

def add(**kw):
    PAGES.append(kw)

def opts(*o):
    return '<option value="">Choose…</option>' + "".join(f"<option>{x}</option>" for x in o)

# ---------------------------------------------------------------- COACHING (dedicated lead generation)
co_faq, co_schema = faq([
    ("Is the consultation really free?", "Yes. The first 15-minute call is free and there is no obligation to sign up for anything."),
    ("How are coaches vetted?", "Network coaches must hold a recognised certification (for example NASM, ACE, ISSA, NSCA, ACSM, CSEP or equivalent) and provide proof before receiving client requests."),
    ("Online or in person?", "Both. Online coaching works anywhere; in-person depends on coach availability in your area."),
    ("What does coaching cost?", "It varies by coach, format and location. As a guide, online coaching commonly runs about $100–$400 per month, and US in-person trainers average around $55 per hour according to Thumbtack's cost guide. You'll get a clear price before you commit."),
])
add(slug="coaching", priority="0.95", schema=[co_schema], no_modal=True,
    title="Get Matched With an Abs & Fat-Loss Coach — Free Consult | AB6",
    desc="Get matched with a certified personal trainer or online coach for six-pack abs, fat loss, core rehab or postnatal core. Free 15-minute consult, no obligation.",
    body=phero("1-on-1 coaching", "Get a coach. Get there faster.", "Tell us your goal in 2 minutes. We match you with a certified coach for a free, no-obligation 15-minute consult.", [(None, "Coaching")],
               '<div class="hero-ctas"><a class="btn btn-primary" href="#apply">Start my free match →</a><a class="btn btn-ghost" href="#coaches">I\'m a coach</a></div><div class="trust"><span>Free consult</span><span>Certified coaches</span><span>Online or in-person</span><span>Reply in 1 business day</span></div>') + f'''
<section class="alt"><div class="wrap">
 <div class="grid g3">
  <div class="card"><div class="ico">{ICON["quiz"]}</div><h3>1 · Tell us your goal</h3><p class="muted small">Two-minute form: goal, schedule, budget and preferences.</p></div>
  <div class="card"><div class="ico">{ICON["user"]}</div><h3>2 · Get matched</h3><p class="muted small">We pair you with a certified coach who specialises in your goal.</p></div>
  <div class="card"><div class="ico">{ICON["bolt"]}</div><h3>3 · Free consult</h3><p class="muted small">15 minutes to see if it's a fit. Decide with zero pressure.</p></div>
 </div>
</div></section>

<section id="apply"><div class="wrap split" style="align-items:start">
 <div class="leadbox" data-steps>
  <div class="steps-bar"><i></i></div><div class="small muted" data-step-label></div>
  <form class="form" data-form="Coaching application (full)" data-lead data-ok="Request received! Your coach match will contact you within 1 business day. Check your inbox (and spam).">
   <div class="step"><h3 style="font-size:1.5rem">What do you want to achieve?</h3>
    <div><label for="c-goal">Main goal</label><select id="c-goal" name="goal" required>{opts("Visible six-pack", "Lose belly fat / body fat", "Stronger core & better posture", "Back pain-friendly core training", "Post-pregnancy core rebuild", "Sport / athletic performance", "Build muscle overall")}</select></div>
    <div><label for="c-tl">Timeline</label><select id="c-tl" name="timeline" required>{opts("ASAP — I'm ready now", "Within 1 month", "1–3 months", "Just researching")}</select></div>
    <div><label for="c-why">What's held you back so far? <span class="faint small">optional</span></label><textarea id="c-why" name="obstacles" style="min-height:80px" placeholder="e.g. consistency, not sure what to eat, injuries…"></textarea></div>
    <div class="step-nav"><span></span><button type="button" class="btn btn-primary" data-next>Next →</button></div>
   </div>
   <div class="step"><h3 style="font-size:1.5rem">Where are you starting?</h3>
    <div class="row"><div><label for="c-lvl">Training experience</label><select id="c-lvl" name="experience" required>{opts("Beginner", "Some experience", "Intermediate", "Advanced")}</select></div>
    <div><label for="c-days">Days you can train</label><select id="c-days" name="days_per_week" required>{opts("2", "3", "4", "5", "6+")}</select></div></div>
    <div class="row"><div><label for="c-age">Age range</label><select id="c-age" name="age_range" required>{opts("18–24", "25–34", "35–44", "45–54", "55+")}</select></div>
    <div><label for="c-bf">Body fat (if known)</label><input id="c-bf" name="body_fat" placeholder="e.g. 22%"></div></div>
    <div><label for="c-inj">Injuries or conditions a coach should know about? <span class="faint small">optional</span></label><input id="c-inj" name="limitations"></div>
    <div class="step-nav"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next>Next →</button></div>
   </div>
   <div class="step"><h3 style="font-size:1.5rem">Your preferences</h3>
    <div class="row"><div><label for="c-fmt">Format</label><select id="c-fmt" name="format" required>{opts("Online coaching (app + check-ins)", "In-person sessions", "Hybrid", "Not sure — advise me")}</select></div>
    <div><label for="c-bud">Monthly budget</label><select id="c-bud" name="budget" required>{opts("Under $100", "$100–$200", "$200–$400", "$400+", "Not sure yet")}</select></div></div>
    <div class="row"><div><label for="c-city">City</label><input id="c-city" name="city" required autocomplete="address-level2"></div>
    <div><label for="c-cty">Country</label><input id="c-cty" name="country" required autocomplete="country-name"></div></div>
    <div><label for="c-pref">Coach preference <span class="faint small">optional</span></label><select id="c-pref" name="coach_preference"><option value="">No preference</option><option>Female coach</option><option>Male coach</option><option>Nutrition-certified</option><option>Postnatal-qualified</option></select></div>
    <div class="step-nav"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next>Last step →</button></div>
   </div>
   <div class="step"><h3 style="font-size:1.5rem">Where should we send your match?</h3>
    <div class="row"><div><label for="c-n">Full name</label><input id="c-n" name="name" required autocomplete="name"></div>
    <div><label for="c-e">Email</label><input id="c-e" name="email" type="email" required autocomplete="email"></div></div>
    <div class="row"><div><label for="c-p">Phone / WhatsApp <span class="faint small">optional</span></label><input id="c-p" name="phone" type="tel" autocomplete="tel"></div>
    <div><label for="c-t">Best time to reach you</label><select id="c-t" name="best_time">{opts("Morning", "Afternoon", "Evening", "Weekend")}</select></div></div>
    {CONSENT}{HP}
    <button class="btn btn-primary btn-block" type="submit">Get my free coach match →</button>{MSG}
    <div class="step-nav"><button type="button" class="btn btn-ghost btn-sm" data-prev>← Back</button><span class="form-note">Free · No obligation · Unsubscribe anytime</span></div>
   </div>
  </form>
 </div>
 <div>
  <h2 style="font-size:2rem">What a good coach adds</h2>
  <ul class="ticks"><li>A plan built around your schedule, injuries and food preferences</li><li>Weekly check-ins and adjustments when progress stalls</li><li>Form feedback on video so every rep counts</li><li>Accountability — the #1 reason people finally get results</li></ul>
  <div class="table-wrap"><table><thead><tr><th>Option</th><th>Typical cost*</th><th>Best for</th></tr></thead><tbody>
   <tr><td>Online coaching</td><td>~$100–$400 / month</td><td>Flexible schedules, any location</td></tr>
   <tr><td>In-person trainer</td><td>~$40–$100 / hour (US avg ≈ $55)</td><td>Hands-on form coaching</td></tr>
   <tr><td>Hybrid</td><td>Varies</td><td>Monthly in-person + online check-ins</td></tr>
  </tbody></table></div>
  <p class="small faint">*Market ranges, not AB6 prices. In-person data: <a href="https://www.thumbtack.com/p/personal-trainer-cost" target="_blank" rel="noopener">Thumbtack cost guide</a>. Your coach quotes before you commit.</p>
  {ad("sidebar")}
 </div>
</div></section>

<section class="alt"><div class="wrap">
 <div class="head center"><div class="eyebrow">Specialisms</div><h2>Coaches for every core goal</h2></div>
 <div class="grid g4">
  <div class="card"><h3>Six-pack &amp; fat loss</h3><p class="small muted">Calorie targets, training and accountability to get lean enough for visible abs.</p></div>
  <div class="card"><h3>Core &amp; back health</h3><p class="small muted">Stability-first programming that works alongside your physio's advice.</p></div>
  <div class="card"><h3>Postnatal core</h3><p class="small muted">Diastasis-aware, pelvic-floor-friendly progressions after clearance.</p></div>
  <div class="card"><h3>Athletes</h3><p class="small muted">Rotational power, bracing and sport-specific core work.</p></div>
 </div>
</div></section>

<section id="coaches"><div class="wrap split" style="align-items:start">
 <div>
  <div class="eyebrow">For coaches &amp; trainers</div>
  <h2>Join the AB6 Coach Network</h2>
  <p class="muted">Get matched with motivated clients who have already set goals, budgets and timelines. Flexible terms: pay-per-qualified-lead or revenue share. Certified professionals only.</p>
  <ul class="ticks"><li>Pre-qualified requests by goal, budget and location</li><li>Featured profile on AB6 (coming soon)</li><li>Create paid content and challenges with us</li></ul>
 </div>
 <form class="form card" data-form="Coach network application" data-ok="Application received — we'll verify your certification and get back to you within 3 business days.">
  <div class="row"><div><label for="k-n">Full name</label><input id="k-n" name="name" required></div><div><label for="k-e">Email</label><input id="k-e" name="email" type="email" required></div></div>
  <div class="row"><div><label for="k-c">Certification(s)</label><input id="k-c" name="certifications" required placeholder="e.g. NASM-CPT, PN1"></div><div><label for="k-y">Years coaching</label><select id="k-y" name="years" required>{opts("<1", "1–3", "3–5", "5–10", "10+")}</select></div></div>
  <div class="row"><div><label for="k-f">Format</label><select id="k-f" name="format" required>{opts("Online", "In-person", "Both")}</select></div><div><label for="k-l">City / country</label><input id="k-l" name="location" required></div></div>
  <div><label for="k-s">Specialties</label><input id="k-s" name="specialties" placeholder="fat loss, postnatal, athletes…"></div>
  <div class="row"><div><label for="k-cap">New clients you can take / month</label><input id="k-cap" name="capacity" type="number" min="1"></div><div><label for="k-m">Preferred terms</label><select id="k-m" name="terms">{opts("Pay per qualified lead", "Revenue share", "Open to either")}</select></div></div>
  <div><label for="k-w">Website / Instagram</label><input id="k-w" name="website" placeholder="https://"></div>
  {CONSENT}{HP}<button class="btn btn-primary" type="submit">Apply to the network</button>{MSG}
 </form>
</div></section>
<section class="alt"><div class="wrap" style="max-width:860px"><h2>Coaching FAQ</h2>{co_faq}</div></section>''')

# ---------------------------------------------------------------- CONTESTS
add(slug="contests", priority="0.8",
    title="AB6 Contests & Prizes — Transformation, Consistency & Creator Challenges",
    desc="Enter free AB6 seasonal contests: 6-week transformation, consistency prize draws, creator and referral challenges. Official rules, eligibility and how winners are chosen.",
    body=phero("Win", "Contests &amp; prizes", "Every AB6 season runs free contests for effort, consistency and creativity. No purchase necessary.", [(None, "Contests")],
               '<div class="hero-ctas"><a class="btn btn-primary" href="#enter">Enter now →</a><a class="btn btn-ghost" href="#rules">Official rules</a></div>') + f'''
<section><div class="wrap">
 <div class="grid g4">
  <div class="card"><div class="ico">{ICON["trophy"]}</div><h3>Transformation</h3><p class="small muted">Finish the 6-week challenge and submit before/after waist + photos. Judged on effort, consistency and progress — not genetics.</p></div>
  <div class="card"><div class="ico">{ICON["cal"]}</div><h3>Consistency draw</h3><p class="small muted">Every completed challenge week = 1 entry (max 6). Random draw among all valid entries.</p></div>
  <div class="card"><div class="ico">{ICON["play"]}</div><h3>Creator contest</h3><p class="small muted">Best original core workout video or reel tagged for AB6. Judged on quality, safety and creativity.</p></div>
  <div class="card"><div class="ico">{ICON["heart"]}</div><h3>Bring-a-friend</h3><p class="small muted">Refer friends who join and complete Week 1. Top referrers win.</p></div>
 </div>
</div></section>
<section class="alt"><div class="wrap split">
 <div>
  <div class="eyebrow">Prize structure</div><h2>What you can win</h2>
  <p class="muted">Prizes are funded by sponsors and supporters. Each season's exact prizes and values are published on this page before entries open.</p>
  <div class="table-wrap"><table><thead><tr><th>Category</th><th>Prize type</th></tr></thead><tbody>
   <tr><td>Grand prize — Transformation</td><td>Coaching package + home gear bundle</td></tr>
   <tr><td>Runners-up (2)</td><td>Gear bundle or gift card</td></tr>
   <tr><td>Consistency draw (10 winners)</td><td>Gift cards / sponsor products</td></tr>
   <tr><td>Creator contest</td><td>Paid AB6 original video commission</td></tr>
   <tr><td>Bring-a-friend</td><td>Sponsor products</td></tr></tbody></table></div>
 </div>
 <div class="card" style="border-color:var(--accent)"><div class="eyebrow">Brands</div><h3>Sponsor a prize</h3><p class="muted small">Put your product in the hands of motivated winners and in front of every participant. Logo placement, social mentions and winner content included.</p><a class="btn btn-primary" href="advertise.html#form">Sponsor this season →</a><hr style="border:0;border-top:1px solid var(--line);margin:20px 0"><h3>Fund the prize pool</h3><p class="muted small">Supporters help grow the prizes for everyone.</p><a class="btn btn-ghost" href="support.html">Support AB6</a></div>
</div></section>
<section id="enter"><div class="wrap" style="max-width:820px">
 <div class="leadbox">
  <h2 style="font-size:2rem">Enter a contest</h2>
  <form class="form" data-form="Contest entry" data-lead data-ok="Entry received! We'll confirm eligibility by email. Good luck!">
   <div class="row"><div><label for="e-c">Contest</label><select id="e-c" name="contest" required>{opts("Transformation", "Consistency draw", "Creator contest", "Bring-a-friend")}</select></div><div><label for="e-n">Full name</label><input id="e-n" name="name" required></div></div>
   <div class="row"><div><label for="e-e">Email</label><input id="e-e" name="email" type="email" required></div><div><label for="e-cty">Country / province / state</label><input id="e-cty" name="region" required></div></div>
   <div><label for="e-l">Link to your entry (photo album, video, post)</label><input id="e-l" name="entry_link" type="url" placeholder="https://"></div>
   <div><label for="e-d">Tell us about your journey</label><textarea id="e-d" name="story"></textarea></div>
   <div><label for="e-r">Referred by (optional)</label><input id="e-r" name="referred_by"></div>
   <label class="check"><input type="checkbox" name="age_18" value="yes" required> I am 18+ (or the age of majority where I live) and accept the official rules.</label>
   <label class="check"><input type="checkbox" name="publicity" value="yes"> AB6 may feature my entry (first name + photos) if I win. (Optional)</label>
   {HP}<button class="btn btn-primary btn-block" type="submit">Submit my entry</button>{MSG}
  </form>
 </div>
</div></section>
<section class="alt" id="rules"><div class="wrap prose">
 <h2>Official rules (summary)</h2>
 <ol>
  <li><b>No purchase necessary.</b> A purchase or donation does not increase your chances of winning.</li>
  <li><b>Eligibility:</b> open to individuals 18+ (or the age of majority in their jurisdiction). Void where prohibited or restricted by law. Employees of AB6 and its sponsors for that season are not eligible.</li>
  <li><b>Entry period:</b> each season's opening and closing dates are posted on this page. Late entries are not accepted.</li>
  <li><b>Selection:</b> judged contests are scored by an AB6 panel on the published criteria; draws are random among valid entries. Odds depend on the number of eligible entries.</li>
  <li><b>Skill-testing question:</b> where required by law (for example, in Canada), selected entrants must correctly answer a skill-testing question before being declared winners.</li>
  <li><b>Verification &amp; notification:</b> winners are contacted by email and must respond within 14 days, or an alternate winner may be selected.</li>
  <li><b>Prizes:</b> as described for the season; non-transferable; no cash alternative unless stated; sponsors may substitute a prize of equal or greater value.</li>
  <li><b>Content:</b> entries must be your own, safe and appropriate. AB6 may disqualify entries that are misleading, edited to misrepresent results, or unsafe.</li>
  <li><b>Privacy:</b> entry data is used to run the contest and is handled under our <a href="privacy.html">Privacy Policy</a>.</li>
  <li><b>Not affiliated:</b> contests are not sponsored, endorsed or administered by Instagram, YouTube, TikTok or any platform used to share entries.</li>
 </ol>
 <p class="small muted">Full season-specific terms are published with each season and prevail over this summary.</p>
 <h2>Hall of fame</h2><p class="muted">Season winners will be featured here.</p>
</div></section>''')

# ---------------------------------------------------------------- SUPPORT / DONATE
add(slug="support", priority="0.7",
    title="Support AB6 — Keep the Abs Tools Free | Donate",
    desc="Support AB6.com: fund free fitness tools, hosting, contest prizes, promotion and hiring coaches and creators. One-time or monthly support.",
    body=phero("Support", "Keep AB6 free for everyone", "AB6's calculators, plans and challenge are free. Your support pays for the running costs, prizes, promotion and the people who make it better.", [(None, "Support")]) + f'''
<section><div class="wrap split" style="align-items:start">
 <div class="leadbox">
  <h2 style="font-size:2rem">Choose your support</h2>
  <form class="form" data-form="Donation pledge" data-ok="Thank you! We'll send secure payment details to your email shortly.">
   <div class="tiers">
    <label class="tier"><input type="radio" name="amount" value="$6" required><span><b>$6</b><small class="muted">Ab Six</small></span></label>
    <label class="tier"><input type="radio" name="amount" value="$26" checked><span><b>$26</b><small class="muted">Core crew</small></span></label>
    <label class="tier"><input type="radio" name="amount" value="$66"><span><b>$66</b><small class="muted">Prize booster</small></span></label>
    <label class="tier"><input type="radio" name="amount" value="Custom"><span><b>Any</b><small class="muted">Custom</small></span></label>
   </div>
   <div class="row"><div><label for="d-f">Frequency</label><select id="d-f" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div>
   <div><label for="d-c">Custom amount / currency <span class="faint small">optional</span></label><input id="d-c" name="custom_amount" placeholder="e.g. 50 CAD"></div></div>
   <div><label for="d-p">Direct my support to</label><select id="d-p" name="purpose"><option>Where it's needed most</option><option>Operations &amp; hosting</option><option>Contest prizes</option><option>Promotion &amp; marketing</option><option>Hiring coaches, writers &amp; creators</option><option>New free tools</option></select></div>
   <div class="row"><div><label for="d-n">Name</label><input id="d-n" name="name" required></div><div><label for="d-e">Email</label><input id="d-e" name="email" type="email" required></div></div>
   <label class="check"><input type="checkbox" name="public_thanks" value="yes"> Thank me publicly on the supporters wall (first name only).</label>
   {HP}<button class="btn btn-primary btn-block" type="submit">Pledge my support →</button>{MSG}
   <p class="form-note">We'll email you a secure payment link (card, PayPal or bank). AB6 is not a registered charity; contributions are not tax-deductible.</p>
  </form>
  <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:16px">
   <a class="btn btn-dark btn-sm" data-donate="paypal" href="#">PayPal</a><a class="btn btn-dark btn-sm" data-donate="stripe" href="#">Card (Stripe)</a>
   <a class="btn btn-dark btn-sm" data-donate="buymeacoffee" href="#">Buy Me a Coffee</a><a class="btn btn-dark btn-sm" data-donate="kofi" href="#">Ko-fi</a><a class="btn btn-dark btn-sm" data-donate="patreon" href="#">Patreon</a>
  </div>
 </div>
 <div>
  <h2 style="font-size:2rem">Where your support goes</h2>
  <p class="muted small">Planned allocation of supporter funds:</p>
  <div><b>Operations, hosting &amp; tools</b> — 25%<div class="bar"><i style="width:25%"></i></div></div>
  <div><b>Contest prizes</b> — 25%<div class="bar"><i style="width:25%"></i></div></div>
  <div><b>Promotion &amp; marketing</b> — 20%<div class="bar"><i style="width:20%"></i></div></div>
  <div><b>Hiring talent (coaches, writers, editors)</b> — 20%<div class="bar"><i style="width:20%"></i></div></div>
  <div><b>New free features</b> — 10%<div class="bar"><i style="width:10%"></i></div></div>
  <div class="card" style="margin-top:20px"><h3>Other ways to help</h3><ul class="ticks small"><li>Share a tool with a friend who's working on their fitness</li><li><a href="contests.html">Sponsor a contest prize</a></li><li><a href="careers.html">Volunteer or contribute content</a></li><li><a href="advertise.html">Corporate wellness partnerships</a></li></ul></div>
 </div>
</div></section>''')

# ---------------------------------------------------------------- ADVERTISE
pk = [("mega", "Display &amp; native placements", "Banner and native slots across tools and guides — high-intent fitness readers."),
      ("cal", "Sponsored challenge", "Title sponsorship of a 6-week AB6 season: branding on the tracker, emails and winners' content."),
      ("trophy", "Prize partnership", "Supply contest prizes in exchange for logo placement and winner features."),
      ("user", "Coach-lead program", "Gyms, studios and coaching brands: receive pre-qualified client requests by area."),
      ("book", "Content partnership", "Co-branded guides, tools or video series, clearly labelled as sponsored."),
      ("brief", "Acquire or partner on AB6.com", "Interested in this website or the AB6.com domain itself? Talk to us directly.")]
add(slug="advertise", priority="0.7",
    title="Advertise, Sponsor or Partner with AB6.com",
    desc="Advertising, sponsorship and partnership options on AB6.com: display placements, sponsored challenges, prize partnerships, coach-lead programs and content partnerships.",
    body=phero("Partners", "Advertise &amp; sponsor", "Reach people actively working on their core, fat loss and fitness — at the moment they're making decisions.", [(None, "Advertise")],
               f'<div class="hero-ctas"><a class="btn btn-primary" href="#form">Request the media kit →</a><a class="btn btn-ghost" href="{INQ}" target="_blank" rel="noopener">Domain / website inquiry ↗</a></div>') + f'''
<section><div class="wrap"><div class="grid g3">{"".join(f'<div class="card reveal"><div class="ico">{ICON[i]}</div><h3>{t}</h3><p class="small muted">{d}</p></div>' for i, t, d in pk)}</div></div></section>
<section class="alt"><div class="wrap split">
 <div><div class="eyebrow">Audience</div><h2>Who you reach</h2><ul class="ticks"><li>Adults building a stronger core and losing body fat</li><li>Home-workout and gym users researching gear, nutrition and coaching</li><li>Challenge participants with weekly engagement</li></ul><p class="small muted">Current traffic and audience data are shared in the media kit on request. All sponsored content is clearly labelled; we don't accept ads for unsafe supplements, extreme diets or misleading health claims.</p></div>
 <form id="form" class="form card" data-form="Advertising / sponsorship inquiry" data-ok="Thanks — we'll send the media kit and options within 2 business days.">
  <div class="row"><div><label for="a-co">Company</label><input id="a-co" name="company" required></div><div><label for="a-n">Your name</label><input id="a-n" name="name" required></div></div>
  <div class="row"><div><label for="a-e">Work email</label><input id="a-e" name="email" type="email" required></div><div><label for="a-w">Website</label><input id="a-w" name="website" placeholder="https://"></div></div>
  <div class="row"><div><label for="a-i">Interested in</label><select id="a-i" name="interest" required>{opts("Display / native ads", "Sponsored challenge", "Prize partnership", "Coach-lead program", "Content partnership", "Buy / partner on AB6.com", "Other")}</select></div>
  <div><label for="a-b">Budget</label><select id="a-b" name="budget">{opts("Under $500", "$500–$2,000", "$2,000–$10,000", "$10,000+", "Prize / in-kind")}</select></div></div>
  <div><label for="a-m">Message</label><textarea id="a-m" name="message"></textarea></div>
  {CONSENT}{HP}<button class="btn btn-primary" type="submit">Send inquiry</button>{MSG}
 </form>
</div></section>''')

# ---------------------------------------------------------------- CAREERS
roles = [("Certified coaches (network)", "Remote / local · per client", "Coach AB6 members online or in person. Certification required."),
         ("Fitness writer (CPT / RD / MSc)", "Remote · freelance", "Evidence-based guides with sources. Credentials preferred."),
         ("Video editor", "Remote · per project", "Edit follow-along workouts and shorts for YouTube, Reels and TikTok."),
         ("Short-form creator / presenter", "Remote · per video", "Demo exercises on camera with great form and energy."),
         ("Community &amp; challenge moderator", "Remote · part-time", "Run challenge check-ins, answer questions and keep things positive."),
         ("Partnerships &amp; sponsorship (commission)", "Remote · commission", "Bring in sponsors, prize partners and coach-lead clients."),
         ("Front-end developer", "Remote · contract", "Build new interactive tools in vanilla JS — fast, accessible, mobile-first."),
         ("Ambassador program", "Anywhere · volunteer + perks", "Share AB6 with your community and get early access, merch and contest perks.")]
add(slug="careers", priority="0.6",
    title="Careers at AB6 — Coaches, Writers, Editors & Creators",
    desc="Join AB6.com: certified coaches, fitness writers, video editors, creators, moderators, partnerships and developers. Remote roles and freelance gigs.",
    body=phero("Careers", "Build the best free abs platform with us", "Remote, flexible roles for people who love training and making useful things.", [(None, "Careers")]) + f'''
<section><div class="wrap"><div class="grid g2">{"".join(f'<div class="card reveal"><h3>{t}</h3><span class="tag">{m}</span><p class="small muted" style="margin-top:8px">{d}</p></div>' for t, m, d in roles)}</div></div></section>
<section class="alt"><div class="wrap" style="max-width:820px"><div class="leadbox">
 <h2 style="font-size:2rem">Apply</h2>
 <form class="form" data-form="Careers application" data-ok="Application received — thank you! We review every application and reply if there's a fit.">
  <div class="row"><div><label for="j-r">Role</label><select id="j-r" name="role" required>{opts(*[r[0].replace("&amp;", "&") for r in roles], "Other")}</select></div><div><label for="j-n">Full name</label><input id="j-n" name="name" required></div></div>
  <div class="row"><div><label for="j-e">Email</label><input id="j-e" name="email" type="email" required></div><div><label for="j-l">Location / time zone</label><input id="j-l" name="location" required></div></div>
  <div class="row"><div><label for="j-p">Portfolio / LinkedIn / channel</label><input id="j-p" name="portfolio" type="url" placeholder="https://"></div><div><label for="j-c">Certifications</label><input id="j-c" name="certifications"></div></div>
  <div class="row"><div><label for="j-a">Availability</label><select id="j-a" name="availability">{opts("A few hours/week", "Part-time", "Full-time", "Per project")}</select></div><div><label for="j-rate">Expected rate</label><input id="j-rate" name="rate"></div></div>
  <div><label for="j-m">Why you?</label><textarea id="j-m" name="message" required></textarea></div>
  {CONSENT}{HP}<button class="btn btn-primary btn-block" type="submit">Submit application</button>{MSG}
 </form>
</div></div></section>''')

# ---------------------------------------------------------------- CONTACT
add(slug="contact", priority="0.6",
    title="Contact AB6.com",
    desc="Contact AB6.com about coaching, partnerships, advertising, contests, corrections or anything else.",
    body=phero("Contact", "Get in touch", "Questions, corrections, partnerships or press — send a message and we'll reply within 2 business days.", [(None, "Contact")]) + f'''
<section><div class="wrap split" style="align-items:start">
 <form class="form card" data-form="Contact message" data-ok="Message sent — we'll reply within 2 business days.">
  <div class="row"><div><label for="ct-n">Name</label><input id="ct-n" name="name" required autocomplete="name"></div><div><label for="ct-e">Email</label><input id="ct-e" name="email" type="email" required autocomplete="email"></div></div>
  <div><label for="ct-t">Topic</label><select id="ct-t" name="topic" required>{opts("General question", "Coaching", "Advertising / sponsorship", "Partnership", "Buy this website / domain", "Contests", "Correction / feedback", "Press", "Privacy request")}</select></div>
  <div><label for="ct-m">Message</label><textarea id="ct-m" name="message" required></textarea></div>
  {CONSENT}{HP}<button class="btn btn-primary" type="submit">Send message</button>{MSG}
 </form>
 <div>
  <div class="card"><h3>Quick routes</h3><ul class="ticks small">
   <li><a href="coaching.html">Get matched with a coach</a></li><li><a href="advertise.html">Advertising &amp; sponsorship</a></li>
   <li><a href="contests.html#enter">Contest entries</a></li><li><a href="careers.html">Jobs &amp; gigs</a></li>
   <li><a href="{INQ}" target="_blank" rel="noopener">Website / domain / partnership inquiries ↗</a></li></ul></div>
  {ad("sidebar")}
 </div>
</div></section>''')

# ---------------------------------------------------------------- ABOUT
add(slug="about", priority="0.5",
    title="About AB6.com — Ab Six",
    desc="AB6.com (Ab Six) is an independent, free platform of tools, plans and guides for a stronger core and visible abs. Our mission, standards and how we're funded.",
    body=phero("About", "About AB6", "AB6 reads as “Ab Six” — six-pack abs. We build the free tools we wish existed when we started training.", [(None, "About")]) + f'''
<section><div class="wrap layout"><article class="prose">
 <h2>Our mission</h2><p>Make visible abs and a strong core achievable for anyone, with honest numbers and plans instead of hype. That means calculators that show the math, plans that fit real schedules, and guides that link the evidence.</p>
 <h2>Editorial standards</h2><ul><li>Claims about training and nutrition link to research or recognised guidance where possible.</li><li>We avoid miracle claims, spot-reduction myths and crash diets.</li><li>Tools explain their formulas and limitations.</li><li>Spotted an error? <a href="contact.html">Send a correction</a> and we'll review it.</li></ul>
 <h2>How AB6 is funded</h2><p>Display advertising (Google AdSense), optional coach matching, affiliate links on the <a href="gear.html">gear guide</a>, sponsors and <a href="support.html">reader support</a>. Sponsored content is always labelled and never changes a tool's math.</p>
 <h2>Independence</h2><p>AB6.com is an independent publication and is not affiliated with AB6IX, Brand New Music, AB6 Holdings LLC or any brand using “AB6”. See our <a href="disclaimer.html">disclaimer &amp; trademark notice</a>.</p>
 <h2>Work with us</h2><p><a href="careers.html">Careers</a> · <a href="advertise.html">Advertise</a> · <a href="{INQ}" target="_blank" rel="noopener">Website / domain inquiries</a></p>
</article>{sidebar()}</div></section>''')

# ---------------------------------------------------------------- LEGAL
LEGAL_UPDATED = "October 9, 2026"
add(slug="privacy", priority="0.3",
    title="Privacy Policy | AB6.com",
    desc="How AB6.com collects, uses and protects information, including cookies, Google AdSense, YouTube embeds, forms and on-device tool data.",
    body=phero("Legal", "Privacy policy", "Last updated " + LEGAL_UPDATED, [(None, "Privacy")]) + f'''
<section><div class="wrap prose">
 <h2>What we collect</h2>
 <ul><li><b>Information you submit</b> in forms (name, email, and the answers you choose to give). Forms are delivered to our inbox through the FormSubmit service.</li>
 <li><b>Tool data</b> (challenge progress, personal records, saved exercises, theme) is stored only in your browser's local storage on your device. We don't receive it unless you submit a form.</li>
 <li><b>Cookies and similar technologies</b> used by Google AdSense and other partners to serve and measure ads, and by embedded YouTube players when you press play.</li></ul>
 <h2>Advertising</h2>
 <p>We use Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits. You can opt out of personalised advertising at <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">aboutads.info</a>. Learn more: <a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener">How Google uses information from sites that use its services</a>.</p>
 <h2>Video embeds</h2><p>Videos load from youtube-nocookie.com only after you click play. YouTube's privacy policy then applies.</p>
 <h2>How we use your information</h2><ul><li>To respond to your request (coach matching, inquiries, contests, applications).</li><li>To send newsletters or plans you asked for (unsubscribe anytime).</li><li>To run contests and verify winners.</li></ul>
 <p>Coach-match requests are shared only with the coach(es) we match you with, for the purpose of contacting you about your request. We do not sell your personal information to unrelated third parties.</p>
 <h2>Retention</h2><p>We keep form submissions only as long as needed for the purpose you submitted them, then delete them, unless the law requires longer.</p>
 <h2>Your rights</h2><p>Depending on where you live (for example under GDPR, UK GDPR, PIPEDA, Québec's Law 25 or US state laws such as the CCPA/CPRA), you may request access, correction, deletion or portability of your data, and object to or limit certain processing. Use the <a href="contact.html">contact form</a> with the topic “Privacy request”.</p>
 <h2>Children</h2><p>AB6 is intended for adults. We do not knowingly collect information from children under 16.</p>
 <h2>Changes</h2><p>We may update this policy and will change the date above when we do.</p>
</div></section>''')

add(slug="terms", priority="0.3",
    title="Terms of Use | AB6.com",
    desc="Terms of use for AB6.com, including health disclaimers, intellectual property, user submissions, contests, affiliate links and limitation of liability.",
    body=phero("Legal", "Terms of use", "Last updated " + LEGAL_UPDATED, [(None, "Terms")]) + '''
<section><div class="wrap prose">
 <h2>1. Acceptance</h2><p>By using AB6.com you agree to these terms. If you don't agree, please don't use the site.</p>
 <h2>2. Health and safety</h2><p>AB6 provides general fitness and nutrition education and tools. It is not medical advice, diagnosis or treatment. Consult a qualified health professional before starting any exercise or nutrition program. Stop exercising and seek help if you feel pain, dizziness or shortness of breath. You use the site and its tools at your own risk.</p>
 <h2>3. Tools and estimates</h2><p>Calculator outputs are estimates based on published formulas and assumptions; individual results vary.</p>
 <h2>4. Intellectual property</h2><p>The site's original text, tools, code, design and graphics are owned by AB6.com and protected by copyright. You may share links and short quotes with attribution. You may not copy, republish or resell substantial parts of the site without written permission. Third-party trademarks, videos and content belong to their owners.</p>
 <h2>5. Your submissions</h2><p>When you submit content (e.g., contest entries, stories, videos), you confirm you own it and grant AB6 a non-exclusive, royalty-free licence to use it for the purpose you submitted it and, where you opted in, to feature it.</p>
 <h2>6. Contests</h2><p>Contests are governed by the official rules on the <a href="contests.html">contests page</a> and season-specific terms.</p>
 <h2>7. Coaching referrals</h2><p>Coaches in the AB6 network are independent professionals, not AB6 employees. Any coaching agreement is between you and the coach. AB6 is not responsible for services provided by third parties.</p>
 <h2>8. Affiliate links and ads</h2><p>Some links earn AB6 a commission. Ads are served by third parties; we are not responsible for advertisers' products or claims.</p>
 <h2>9. Limitation of liability</h2><p>To the maximum extent permitted by law, AB6.com is provided “as is” without warranties, and AB6 is not liable for indirect, incidental or consequential damages arising from use of the site.</p>
 <h2>10. Changes</h2><p>We may update these terms; continued use means you accept the updated terms.</p>
 <h2>11. Contact</h2><p>Use the <a href="contact.html">contact form</a>.</p>
</div></section>''')

add(slug="disclaimer", priority="0.3",
    title="Disclaimer, Trademark & Copyright Notice | AB6.com",
    desc="Medical disclaimer, results disclaimer, trademark and copyright notice, and affiliate disclosure for AB6.com.",
    body=phero("Legal", "Disclaimer, trademark &amp; copyright notice", "Last updated " + LEGAL_UPDATED, [(None, "Disclaimer")]) + f'''
<section><div class="wrap prose">
 <h2 id="trademark">Trademark &amp; name notice</h2>
 <p>“AB6” on this website is used solely as a descriptive reading of the domain name AB6.com — “Ab Six”, a reference to six-pack abdominal muscles. AB6.com:</p>
 <ul><li>claims <b>no trademark rights</b> in the term “AB6”;</li>
 <li>is <b>not affiliated with, endorsed by, sponsored by or connected to</b> AB6IX, its members, Brand New Music, AB6 Holdings LLC, or any company, product, artist or brand that uses “AB6” or a similar name;</li>
 <li>does not use any third party's logos, artwork or brand assets. The AB6.com logo (six rounded blocks) is an original design.</li></ul>
 <p>All other trademarks, product names and company names mentioned (for example, YouTube, Google, Amazon, NASM, ACE, ISSA) are the property of their respective owners and are used for identification only. If you believe content on this site infringes your rights, please use the <a href="contact.html">contact form</a> (topic: “Correction / feedback”) and we will review it promptly.</p>
 <h2 id="copyright">Copyright</h2>
 <p>© 2026 AB6.com. Original text, tools, source code, graphics and design are protected by copyright. Embedded YouTube videos remain the property of their creators and are displayed using YouTube's official embed player under YouTube's terms. Research is cited by linking to the original publisher or PubMed.</p>
 <h2 id="medical">Medical disclaimer</h2>
 <p>Content and tools on AB6.com are for general educational purposes only and are not a substitute for professional medical advice, diagnosis or treatment. Always consult a physician or qualified health professional before beginning any exercise, diet or supplement program, particularly if you are pregnant, postpartum, have a medical condition, injury or a history of disordered eating.</p>
 <h2 id="results">Results disclaimer</h2>
 <p>Individual results vary based on genetics, adherence, starting point and other factors. Calculator outputs and timelines are estimates, not guarantees.</p>
 <h2 id="affiliate">Affiliate &amp; advertising disclosure</h2>
 <p>AB6.com displays ads (including Google AdSense) and may earn commissions from affiliate links, at no extra cost to you. Sponsored content is labelled. Compensation does not change calculator formulas or editorial recommendations.</p>
 <h2 id="inquiries">Website &amp; domain inquiries</h2>
 <p>For interest in acquiring or partnering on this website or domain name, visit <a href="{INQ}" target="_blank" rel="noopener">web.works/contact</a>.</p>
</div></section>''')

add(slug="404", robots="noindex,follow", priority="0.1", no_modal=True,
    title="Page not found | AB6.com",
    desc="This page doesn't exist. Try the AB6 tools, exercise library or guides.",
    body=f'''<section class="hero"><div class="wrap center"><div class="eyebrow">404</div><h1>Rep not found.</h1><p class="lead">That page doesn't exist — but your abs still do. Try one of these:</p>
<div class="hero-ctas" style="justify-content:center"><a class="btn btn-primary" href="index.html">Home</a><a class="btn btn-ghost" href="abs-quiz.html">Abs plan quiz</a><a class="btn btn-ghost" href="exercises.html">Exercise library</a></div></div></section>''')
