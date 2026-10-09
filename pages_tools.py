"""AB6.com — home + interactive tool pages."""
from common import (HP, MSG, CONSENT, ICON, phero, ad, faq, band, card, sidebar, crumb, VIDEOS, video_cards, pubmed)

PAGES = []

def add(**kw):
    PAGES.append(kw)

def choice(name, value, label, sub="", typ="radio", req=True, checked=False):
    r = " required" if req and typ == "radio" else ""
    c = " checked" if checked else ""
    s = f"<em>{sub}</em>" if sub else ""
    return f'<label class="choice"><input type="{typ}" name="{name}" value="{value}"{r}{c}><span>{label}{s}</span></label>'

SEX = ('<div><label>Sex <span class="faint small">(formulas differ)</span></label><div class="choices">'
       + choice("sex", "m", "Male", checked=True) + choice("sex", "f", "Female") + "</div></div>")

def units(form_id):
    return (f'<div class="unit-toggle" data-for="{form_id}" role="group" aria-label="Units"><button type="button" class="on" data-units="metric">Metric</button>'
            '<button type="button" data-units="imperial">Imperial</button></div>')

def u(m, i):
    return f'<span data-m="{m}" data-i="{i}">{m}</span>'

# ---------------------------------------------------------------- HOME
home_faq, home_faq_schema = faq([
    ("Can you spot-reduce belly fat with ab exercises?", "No. Controlled studies show ab training alone does not significantly reduce belly fat. Ab work builds the muscle; an overall calorie deficit reveals it. AB6 plans combine both."),
    ("What body fat percentage do you need to see abs?", "As a rule of thumb, most men see a clear six-pack around 10–12% body fat and most women around 16–19%. Genetics, ab thickness and where you store fat shift this a few points either way."),
    ("How often should I train abs?", "Two to four focused core sessions per week is enough for most people. Treat abs like any other muscle: progressive overload, good form and recovery."),
    ("Is AB6 really free?", "Yes. Every calculator, the workout generator, the exercise library and the 6-week challenge are free. We are funded by ads, optional coaching referrals, sponsors and reader support."),
    ("Is AB6 related to AB6IX or any AB6 brand?", "No. AB6.com reads as “Ab Six” — as in six-pack abs. It is an independent fitness site with no affiliation to AB6IX, Brand New Music or any company using “AB6”."),
])

COREMAP_TEASER = ""

add(slug="index", priority="1.0",
    title="AB6.com — Six-Pack Abs Workouts, Calculators & Free 6-Week Core Plan",
    desc="Get visible abs with free tools: body-fat & macro calculators, abs timeline, workout generator with timer, 35-exercise library, a 6-week challenge with prizes and 1-on-1 coaching.",
    tools=True,
    schema=[{"@context": "https://schema.org", "@type": "WebSite", "name": "AB6.com", "alternateName": "Ab Six", "url": "https://ab6.com/"},
            {"@context": "https://schema.org", "@type": "Organization", "name": "AB6.com", "url": "https://ab6.com/", "logo": "https://ab6.com/assets/img/icon-512.png"},
            home_faq_schema],
    body=f'''
<section class="hero">
 <div class="wrap split">
  <div>
   <div class="eyebrow">Free tools · Real plans · Zero fluff</div>
   <h1>Six-pack abs,<br><span class="hl">engineered.</span></h1>
   <p class="lead">AB6 turns “get abs” into numbers you can act on: your body-fat %, your calorie target, your weeks-to-abs date and a workout that fits your time and equipment. All free.</p>
   <div class="hero-ctas">
    <a class="btn btn-primary" href="abs-quiz.html">Build my free abs plan →</a>
    <a class="btn btn-ghost" href="body-fat-calculator.html">Check my body fat</a>
   </div>
   <div class="trust"><span>No sign-up to use tools</span><span>Evidence-informed</span><span>Home or gym</span></div>
  </div>
  <div class="center">
   <div class="sixpack" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
   <p class="small muted" style="margin-top:14px">Train the muscle. Reveal it with fat loss. Repeat for 6 weeks.</p>
  </div>
 </div>
 <div class="wrap"><div class="stats">
  <div class="stat"><b data-count="35">35</b><span>Core exercises with form cues</span></div>
  <div class="stat"><b data-count="7">7</b><span>Free interactive tools</span></div>
  <div class="stat"><b data-count="42">42</b><span>Day guided challenge</span></div>
  <div class="stat"><b>$0</b><span>To use everything</span></div>
 </div></div>
</section>
{ad("top")}
<section class="alt"><div class="wrap">
 <div class="head center"><div class="eyebrow">Start here</div><h2>Three steps to visible abs</h2><p class="lead">Most people train abs hard and never see them. The fix is a system: measure, plan, train — in that order.</p></div>
 <div class="grid g3">
  {card("body-fat-calculator.html", "fat", "1 · Measure", "Find your body-fat % with a tape measure and see how close your abs are to showing.")}
  {card("macro-calculator.html", "fire", "2 · Plan", "Get your daily calories and protein, then your realistic weeks-to-abs date.")}
  {card("workout-generator.html", "bolt", "3 · Train", "Generate a core workout for your time and gear — with a built-in voice timer.")}
 </div>
</div></section>

<section><div class="wrap">
 <div class="head"><div class="eyebrow">Free tools</div><h2>Your abs toolkit</h2></div>
 <div class="grid g3">
  {card("abs-quiz.html", "quiz", "Find My Abs Plan", "7 questions → a personalised 6-week plan you can print.", "Popular")}
  {card("body-fat-calculator.html", "fat", "Body Fat Calculator", "US Navy tape method with an ab-visibility rating.")}
  {card("macro-calculator.html", "fire", "Calorie &amp; Macro Calculator", "Mifflin-St Jeor or Katch-McArdle with protein-first macros.")}
  {card("abs-timeline-calculator.html", "cal", "Abs Timeline", "How many weeks until your abs show — with a projected curve.")}
  {card("workout-generator.html", "clock", "Workout Generator + Timer", "5–30 minute circuits with voice cues and beeps.")}
  {card("core-test.html", "target", "Core Strength Test", "Plank, side plank and hollow hold — graded and saved.")}
 </div>
</div></section>

<section class="alt"><div class="wrap split">
 <div>
  <div class="eyebrow">Workout of the day</div>
  <h2>Today's 15-minute ab circuit</h2>
  <p class="muted">A new balanced bodyweight circuit every day — lower abs, obliques and deep core.</p>
  <div id="wod"></div>
  <a class="btn btn-primary" href="workout-generator.html?wod=1">Start with the timer →</a>
 </div>
 <div class="card">
  <div class="eyebrow">Season challenge</div>
  <h3 style="font-size:1.6rem">The 6-Week AB6 Challenge</h3>
  <p class="muted">42 days of guided core training, steps and check-ins. Track progress on your phone and earn prize-draw entries for every week you complete.</p>
  <ul class="ticks"><li>Day-by-day calendar with progress ring &amp; streaks</li><li>Weekly check-ins = prize-draw entries</li><li>Beginner to advanced scaling</li></ul>
  <a class="btn btn-dark" href="challenge.html">Join the challenge free</a>
 </div>
</div></section>

<section id="coach"><div class="wrap">
 <div class="leadbox split">
  <div>
   <div class="eyebrow">Fast-track · 1-on-1 coaching</div>
   <h2>Get matched with a certified abs &amp; fat-loss coach</h2>
   <p class="muted">Tools get you started. A coach gets you there faster — with a custom plan, weekly check-ins and accountability.</p>
   <ul class="ticks"><li>Free 15-minute consult, no obligation</li><li>Online or in-person, matched to your budget</li><li>Certified trainers and nutrition coaches only</li><li>Reply within 1 business day</li></ul>
   <a href="coaching.html" class="small">Prefer the full application? →</a>
  </div>
  <form class="form" data-form="Coaching lead — home page" data-lead data-ok="You're matched in our queue! A coach will reach out within 1 business day.">
   <div><label for="h-goal">Main goal</label><select id="h-goal" name="goal" required><option value="">Choose…</option><option>Visible six-pack</option><option>Lose belly fat</option><option>Stronger core / back health</option><option>Post-pregnancy core rebuild</option><option>Sport performance</option></select></div>
   <div class="row">
    <div><label for="h-when">Timeline</label><select id="h-when" name="timeline" required><option value="">Choose…</option><option>ASAP</option><option>Within 3 months</option><option>3–6 months</option><option>Just exploring</option></select></div>
    <div><label for="h-budget">Monthly budget</label><select id="h-budget" name="budget" required><option value="">Choose…</option><option>Under $100</option><option>$100–$200</option><option>$200–$400</option><option>$400+</option></select></div>
   </div>
   <div class="row">
    <div><label for="h-name">First name</label><input id="h-name" name="name" required autocomplete="given-name"></div>
    <div><label for="h-email">Email</label><input id="h-email" type="email" name="email" required autocomplete="email"></div>
   </div>
   {CONSENT}{HP}
   <button class="btn btn-primary btn-block" type="submit">Match me with a coach →</button>
   {MSG}
   <p class="form-note">Free to request. We never sell your details to unrelated third parties.</p>
  </form>
 </div>
</div></section>
{ad("inContent")}
<section class="alt"><div class="wrap">
 <div class="head" style="display:flex;justify-content:space-between;align-items:end;gap:16px;flex-wrap:wrap"><div><div class="eyebrow">Follow along</div><h2>Ab workouts on video</h2></div><a class="btn btn-ghost btn-sm" href="videos.html">All videos →</a></div>
 <div class="grid g4" data-own-videos></div>
 <div class="grid g4" style="margin-top:20px">{video_cards(VIDEOS[:4])}</div>
</div></section>

<section><div class="wrap">
 <div class="head"><div class="eyebrow">Learn</div><h2>Guides that cut through the noise</h2></div>
 <div class="grid g3">
  {card("how-to-get-six-pack-abs.html", "book", "How to Get Six-Pack Abs", "The complete, evidence-informed playbook: training, diet, sleep and timelines.")}
  {card("lower-abs-workout.html", "target", "Lower Abs Workout", "Why lower abs show last and the 6 moves that train them best.")}
  {card("nutrition.html", "fire", "Abs Nutrition Guide", "Calories, protein, meal templates and a 1-day sample menu.")}
 </div>
</div></section>

<section class="alt"><div class="wrap">
 <div class="grid g3">
  {card("contests.html", "trophy", "Win prizes", "Transformation, consistency and creator contests every season.")}
  {card("support.html", "heart", "Support AB6", "Keep the tools free — fund operations, prizes and new features.")}
  {card("careers.html", "brief", "Join the team", "Coaches, writers, editors and creators — remote roles &amp; gigs.")}
 </div>
</div></section>

<section><div class="wrap" style="max-width:860px">
 <div class="head center"><div class="eyebrow">FAQ</div><h2>Quick answers</h2></div>
 {home_faq}
</div></section>
{band("Advertise or sponsor on AB6", "Reach people actively working on their fitness — banners, sponsored challenges, prize partnerships and coach-lead programs.", "advertise.html", "See packages →")}
''')

# ---------------------------------------------------------------- QUIZ
quiz_steps = [
    ("Who is this plan for?", SEX.replace("<label>Sex", "<label>Sex").replace('<div><label>Sex <span class="faint small">(formulas differ)</span></label>', '<div>')),
    ("What's your main goal?", '<div class="choices">' + choice("goal", "abs", "Visible six-pack") + choice("goal", "fat", "Lose belly fat") + choice("goal", "core", "Stronger core") + choice("goal", "perf", "Sport performance") + "</div>"),
    ("Your training experience?", '<div class="choices">' + choice("level", "1", "Beginner", "New or returning") + choice("level", "2", "Intermediate", "6+ months consistent") + choice("level", "3", "Advanced", "2+ years, strong core") + "</div>"),
    ("What equipment do you have?", '<p class="small muted">Pick all that apply — or none for bodyweight only.</p><div class="choices">' + "".join(choice("eq", v, l, typ="checkbox", req=False) for v, l in [("band", "Resistance band"), ("dumbbell", "Dumbbell / kettlebell"), ("bar", "Pull-up bar"), ("wheel", "Ab wheel"), ("bench", "Bench"), ("cable", "Gym cables"), ("ball", "Stability ball")]) + "</div>"),
    ("Minutes per session?", '<div class="choices">' + "".join(choice("minutes", v, v + " min") for v in ["10", "15", "20", "30", "45"]) + "</div>"),
    ("Days per week you can train?", '<div class="choices">' + "".join(choice("days", v, v + " days") for v in ["2", "3", "4", "5", "6"]) + "</div>"),
    ("Which best describes your midsection now?", '<div class="choices">' + choice("shape", "lean", "Lean", "Abs partly visible") + choice("shape", "athletic", "Athletic", "Firm, no clear lines") + choice("shape", "average", "Average", "Soft, some belly") + choice("shape", "above", "Above average", "Belly is the main focus") + "</div>"),
]
qsteps = ""
for i, (q, inner) in enumerate(quiz_steps):
    last = i == len(quiz_steps) - 1
    prev = '<button type="button" class="btn btn-ghost" data-prev>← Back</button>' if i else "<span></span>"
    nxt = '<button type="button" class="btn btn-primary" id="quizFinish">See my plan →</button>' if last else '<button type="button" class="btn btn-primary" data-next>Next →</button>'
    qsteps += f'<div class="step"><h3 style="font-size:1.5rem">{q}</h3>{inner}<div class="step-nav">{prev}{nxt}</div></div>'

add(slug="abs-quiz", priority="0.9", tools=True, no_modal=True,
    title="Find My Abs Plan — Free Personalised 6-Week Six-Pack Plan (Quiz) | AB6",
    desc="Answer 7 quick questions and get a free personalised 6-week abs plan: weekly schedule, exercises for your equipment, progression and an estimated timeline.",
    body=phero("Free · 60 seconds", "Find my abs plan", "Seven quick questions. One personalised 6-week plan — matched to your level, time and equipment.", [(None, "Abs Plan Quiz")]) + f'''
<section><div class="wrap" style="max-width:820px">
 <form id="absQuiz" onsubmit="return false">
  <div id="quizSteps" class="card" data-steps>
   <div class="steps-bar"><i></i></div><div class="small muted" data-step-label></div><br>
   {qsteps}
  </div>
 </form>
 <div id="quizResult" hidden>
  <div class="card">
   <div class="eyebrow">Your plan</div><h2 id="planName">AB6 Plan</h2>
   <div id="planSummary"></div>
  </div>
  <div id="planGate" class="leadbox" style="margin-top:20px">
   <h3 style="font-size:1.5rem">Unlock the full 6-week plan</h3>
   <p class="muted">Core B session, week-by-week progression, test targets and the printable version — free. We'll also email you one new ab workout per week.</p>
   <form id="gateForm" class="form" data-form="Abs plan quiz lead" data-lead data-keep data-ok="Unlocked! Scroll down for your full plan.">
    <div class="row"><div><label for="g-name">First name</label><input id="g-name" name="name" required autocomplete="given-name"></div>
    <div><label for="g-email">Email</label><input id="g-email" type="email" name="email" required autocomplete="email"></div></div>
    <label class="check"><input type="checkbox" name="coach_interest" value="yes"> I'd also like a free 15-minute consult with a coach.</label>
    {CONSENT}{HP}
    <button class="btn btn-primary btn-block" type="submit">Unlock my full plan →</button>{MSG}
   </form>
  </div>
  <div id="planFull" class="card" style="margin-top:20px" hidden></div>
  <p class="center" style="margin-top:16px"><button class="btn btn-ghost btn-sm" id="quizRestart">↺ Retake the quiz</button></p>
 </div>
 {ad("inContent")}
 <div class="callout blue small">Estimates are planning ranges based on typical fat-loss rates (~0.5–1% of body weight per week) and rough body-fat guesses. For a precise number, use the <a href="body-fat-calculator.html">body fat calculator</a> and <a href="abs-timeline-calculator.html">abs timeline</a>.</div>
</div></section>''')

# ---------------------------------------------------------------- CALCULATOR HUB
add(slug="calculators", priority="0.8",
    title="Free Abs & Fat-Loss Calculators — Body Fat, Macros, Abs Timeline | AB6",
    desc="All AB6 tools in one place: body fat calculator, calorie & macro calculator, abs timeline, workout generator, core strength test and the abs plan quiz.",
    body=phero("Tools", "Abs calculators &amp; tools", "Every tool is free, works on your phone and needs no account. Results stay on your device.", [(None, "Tools")]) + f'''
<section><div class="wrap"><div class="grid g3">
  {card("abs-quiz.html", "quiz", "Find My Abs Plan", "Personalised 6-week plan from 7 questions.")}
  {card("body-fat-calculator.html", "fat", "Body Fat Calculator", "Tape-measure method + ab visibility rating.")}
  {card("macro-calculator.html", "fire", "Calorie &amp; Macro Calculator", "Daily calories, protein, carbs, fat and fibre.")}
  {card("abs-timeline-calculator.html", "cal", "Abs Timeline Calculator", "Weeks until your abs show, with a projection chart.")}
  {card("workout-generator.html", "clock", "Ab Workout Generator", "Custom circuits + voice interval timer.")}
  {card("core-test.html", "target", "Core Strength Test", "Benchmark your plank, side plank &amp; hollow hold.")}
  {card("exercises.html", "grid", "Exercise Library", "35 core exercises with an interactive muscle map.")}
  {card("challenge.html", "trophy", "6-Week Challenge Tracker", "Daily plan, streaks, prize-draw entries.")}
 </div>{ad("inContent")}</div></section>''')

# ---------------------------------------------------------------- BODY FAT
bf_faq, bf_schema = faq([
    ("How accurate is the US Navy body fat method?", "It is a practical estimate. Compared with lab methods like DEXA it is typically within a few percentage points for most people, but can be off more for very lean or very muscular bodies. Use it to track trends with consistent measurements."),
    ("How do I measure my waist correctly?", "Men: measure horizontally at the navel. Women: measure at the narrowest point of the waist. Stand relaxed, exhale normally and keep the tape snug but not compressing the skin."),
    ("What body fat do you need for visible abs?", "Roughly 10–12% for men and 16–19% for women for clear definition, with outlines often appearing a few points higher."),
])
add(slug="body-fat-calculator", priority="0.9", tools=True, schema=[bf_schema],
    title="Body Fat Calculator (US Navy Method) + Ab Visibility Check | AB6",
    desc="Free body fat percentage calculator using the US Navy tape method. See your category, fat and lean mass, and how close your abs are to showing.",
    body=phero("Calculator", "Body fat calculator", "All you need is a tape measure. Get your body-fat %, category and an honest ab-visibility rating.", [("calculators.html", "Tools"), (None, "Body Fat")]) + f'''
<section><div class="wrap layout"><div>
 <div class="card">
  {units("bfCalc")}
  <form id="bfCalc" class="form" data-units="metric">
   {SEX}
   <div class="row"><div><label for="bf-h">Height ({u("cm", "in")})</label><input id="bf-h" name="height" type="number" step="0.1" min="50" required inputmode="decimal"></div>
   <div><label for="bf-w8">Weight ({u("kg", "lb")}) <span class="faint small">optional</span></label><input id="bf-w8" name="weight" type="number" step="0.1" min="20" inputmode="decimal"></div></div>
   <div class="row"><div><label for="bf-n">Neck ({u("cm", "in")})</label><input id="bf-n" name="neck" type="number" step="0.1" min="10" required inputmode="decimal"></div>
   <div><label for="bf-wa">Waist ({u("cm", "in")})</label><input id="bf-wa" name="waist" type="number" step="0.1" min="20" required inputmode="decimal"></div></div>
   <div data-hip><label for="bf-hp">Hips ({u("cm", "in")})</label><input id="bf-hp" name="hip" type="number" step="0.1" min="20" inputmode="decimal"></div>
   <button class="btn btn-primary" type="submit">Calculate body fat</button>
  </form>
  <div id="bfOut" class="result" hidden aria-live="polite"></div>
 </div>
 {ad("inContent")}
 <article class="prose" style="margin-top:30px">
  <h2>How this calculator works</h2>
  <p>It uses the U.S. Navy circumference equations, which estimate body density from your height, neck and waist (plus hips for women). It is the same approach many militaries use for fitness standards because it is cheap, fast and repeatable.</p>
  <h3>Body fat categories (American Council on Exercise ranges)</h3>
  <div class="table-wrap"><table><thead><tr><th>Category</th><th>Men</th><th>Women</th></tr></thead><tbody>
   <tr><td>Essential fat</td><td>2–5%</td><td>10–13%</td></tr><tr><td>Athletes</td><td>6–13%</td><td>14–20%</td></tr>
   <tr><td>Fitness</td><td>14–17%</td><td>21–24%</td></tr><tr><td>Average</td><td>18–24%</td><td>25–31%</td></tr>
   <tr><td>Above average</td><td>25%+</td><td>32%+</td></tr></tbody></table></div>
  <h3>Measuring tips for consistent results</h3>
  <ul><li>Measure first thing in the morning, before eating.</li><li>Use a flexible, non-stretch tape and take each measurement twice.</li><li>Neck: just below the larynx, tape sloping slightly down to the front.</li><li>Re-measure every 2 weeks — trends matter more than any single number.</li></ul>
  <h2>FAQ</h2>{bf_faq}
 </article>
</div>{sidebar()}</div></section>''')

# ---------------------------------------------------------------- MACRO
mc_faq, mc_schema = faq([
    ("How big should my calorie deficit be to get abs?", "A deficit of 15–25% below maintenance is a common, sustainable range. It typically produces about 0.5–1% body-weight loss per week while protecting muscle if protein and strength training are in place."),
    ("How much protein do I need to keep muscle while cutting?", "Research suggests around 1.6–2.2 g per kg of body weight per day, with leaner people in a deficit often benefiting from the higher end."),
    ("Should I use Katch-McArdle or Mifflin-St Jeor?", "If you know your body fat reasonably well, Katch-McArdle (based on lean mass) can be more accurate. Otherwise Mifflin-St Jeor is a well-validated default. Both are starting points — adjust from real-world weekly averages."),
])
add(slug="macro-calculator", priority="0.9", tools=True, schema=[mc_schema],
    title="Calorie & Macro Calculator for Abs (TDEE + Protein Targets) | AB6",
    desc="Calculate your maintenance calories (TDEE), fat-loss calorie target and protein, carb, fat and fibre macros — built for getting lean enough to see abs.",
    body=phero("Calculator", "Calorie &amp; macro calculator", "Your daily calorie target and protein-first macros for getting lean — without crash dieting.", [("calculators.html", "Tools"), (None, "Macros")]) + f'''
<section><div class="wrap layout"><div>
 <div class="card">
  {units("macroCalc")}
  <form id="macroCalc" class="form" data-units="metric">
   {SEX}
   <div class="row"><div><label for="m-age">Age</label><input id="m-age" name="age" type="number" min="16" max="90" required></div>
   <div><label for="m-h">Height ({u("cm", "in")})</label><input id="m-h" name="height" type="number" step="0.1" required inputmode="decimal"></div></div>
   <div class="row"><div><label for="m-w">Weight ({u("kg", "lb")})</label><input id="m-w" name="weight" type="number" step="0.1" required inputmode="decimal"></div>
   <div><label for="m-bf">Body fat % <span class="faint small">optional</span></label><input id="m-bf" name="bodyfat" type="number" step="0.1" min="3" max="60" inputmode="decimal"></div></div>
   <div><label for="m-act">Activity level</label><select id="m-act" name="activity" required>
    <option value="1.2">Sedentary — desk job, little exercise</option><option value="1.375">Light — 1–3 workouts/week</option>
    <option value="1.55" selected>Moderate — 3–5 workouts/week</option><option value="1.725">Very active — 6–7 workouts/week</option><option value="1.9">Athlete — hard training + active job</option></select></div>
   <div><label for="m-goal">Goal</label><select id="m-goal" name="goal">
    <option value="-0.2" selected>Fat loss — moderate (−20%)</option><option value="-0.25">Fat loss — aggressive (−25%)</option><option value="-0.1">Slow cut (−10%)</option>
    <option value="0">Maintain / recomposition</option><option value="0.1">Lean muscle gain (+10%)</option></select></div>
   <button class="btn btn-primary" type="submit">Calculate my targets</button>
  </form>
  <div id="macroOut" class="result" hidden aria-live="polite"></div>
 </div>
 {ad("inContent")}
 <article class="prose" style="margin-top:30px">
  <h2>The method</h2>
  <p><b>BMR</b> uses Mifflin-St Jeor by default, or Katch-McArdle when you enter body fat. <b>TDEE</b> multiplies BMR by your activity factor. Your <b>target</b> applies your goal adjustment, with a safety floor so the deficit never gets reckless.</p>
  <p><b>Macros:</b> protein is set first (2.0 g/kg when cutting, 1.8 g/kg otherwise — within the 1.6–2.2 g/kg range supported by {pubmed("Morton+2018+protein+supplementation+meta-analysis", "meta-analysis research")}), fat at ~25% of calories (never below 0.6 g/kg) and carbohydrates fill the rest to fuel training.</p>
  <h2>FAQ</h2>{mc_faq}
 </article>
</div>{sidebar()}</div></section>''')

# ---------------------------------------------------------------- TIMELINE
add(slug="abs-timeline-calculator", priority="0.9", tools=True,
    title="Abs Timeline Calculator — How Long Until My Abs Show? | AB6",
    desc="Estimate how many weeks it will take to reach six-pack body fat. Enter weight, body fat and a loss rate to see your goal weight, target date and projection chart.",
    body=phero("Calculator", "How long until my abs show?", "Turn your body-fat number into a date. Pick a sustainable rate and see the projected curve.", [("calculators.html", "Tools"), (None, "Abs Timeline")]) + f'''
<section><div class="wrap layout"><div>
 <div class="card">
  {units("timelineCalc")}
  <form id="timelineCalc" class="form" data-units="metric">
   {SEX}
   <div class="row"><div><label for="t-w">Current weight ({u("kg", "lb")})</label><input id="t-w" name="weight" type="number" step="0.1" required inputmode="decimal"></div>
   <div><label for="t-c">Current body fat %</label><input id="t-c" name="current" type="number" step="0.1" min="4" max="60" required inputmode="decimal"><span class="small"><a href="body-fat-calculator.html">Don't know it? Calculate →</a></span></div></div>
   <div class="row"><div><label for="t-t">Target body fat %</label><input id="t-t" name="target" type="number" step="0.1" min="4" max="40" required inputmode="decimal"></div>
   <div><label for="t-r">Rate of loss per week</label><select id="t-r" name="rate"><option value="0.5">0.5% of body weight — easiest to sustain</option><option value="0.75" selected>0.75% — balanced</option><option value="1">1% — aggressive</option></select></div></div>
   <button class="btn btn-primary" type="submit">Show my timeline</button>
  </form>
  <div id="tlOut" class="result" hidden aria-live="polite"></div>
 </div>
 {ad("inContent")}
 <article class="prose" style="margin-top:30px">
  <h2>How we estimate it</h2>
  <p>We hold your lean mass constant, calculate the body weight at which your target body-fat % is reached, then apply your weekly loss rate to your current weight each week. Rates of roughly 0.5–1.0% of body weight per week are commonly recommended for preserving muscle while dieting (see {pubmed("Helms+2014+evidence-based+recommendations+natural+bodybuilding+contest+preparation", "Helms et al., 2014")}).</p>
  <div class="callout">Default targets: <b>11%</b> for men and <b>18%</b> for women — the range where most people see clear ab definition.</div>
 </article>
</div>{sidebar()}</div></section>''')

# ---------------------------------------------------------------- GENERATOR
eq_checks = "".join(choice("eq", v, l, typ="checkbox", req=False) for v, l in [("band", "Band"), ("dumbbell", "Dumbbell / KB"), ("bar", "Pull-up bar"), ("wheel", "Ab wheel"), ("bench", "Bench"), ("cable", "Cables"), ("ball", "Stability ball")])
add(slug="workout-generator", priority="0.9", tools=True,
    title="Ab Workout Generator + Interval Timer (5–30 Min) | AB6",
    desc="Generate a custom ab workout for your time, level and equipment, then follow it with a built-in voice interval timer. Free, no sign-up.",
    body=phero("Tool", "Ab workout generator", "Pick time, level and gear. Get a balanced core circuit and a voice-guided timer — ready in one tap.", [("calculators.html", "Tools"), (None, "Workout Generator")]) + f'''
<section><div class="wrap split" style="align-items:start">
 <div class="card">
  <form id="genForm" class="form">
   <div><label>Time</label><div class="choices">{"".join(choice("minutes", v, v + " min", checked=v == "10") for v in ["5", "10", "15", "20", "30"])}</div></div>
   <div><label>Level</label><div class="choices">{choice("level", "1", "Beginner", "30s on / 20s off", checked=True)}{choice("level", "2", "Intermediate", "40s / 20s")}{choice("level", "3", "Advanced", "45s / 15s")}</div></div>
   <div><label>Focus</label><select name="focus"><option value="balanced">Balanced six-pack</option><option value="lower">Lower abs</option><option value="obliques">Obliques</option><option value="deep">Deep core / stability</option><option value="upper">Upper abs</option></select></div>
   <div><label>Equipment <span class="faint small">(bodyweight always included)</span></label><div class="choices">{eq_checks}</div></div>
   <div style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn btn-primary" type="submit">Generate workout</button><button class="btn btn-ghost" type="button" id="usePicks">Use my library picks</button></div>
  </form>
 </div>
 <div>
  <div id="timer" class="timer" hidden aria-live="polite">
   <div class="now">Press start</div><div class="clock">GO</div><div class="next"></div>
   <div class="ctrl"><button class="btn btn-primary" id="tStart">Start</button><button class="btn btn-dark" id="tSkip">Skip ›</button><button class="btn btn-ghost" id="tReset">Reset</button><button class="btn btn-ghost btn-sm" id="voiceBtn" type="button">🔊 Voice on</button></div>
  </div>
  <div id="genOut" style="margin-top:18px"><p class="muted">Your workout will appear here. Tip: add favourites in the <a href="exercises.html">exercise library</a>, then hit “Use my library picks”.</p></div>
 </div>
</div>{ad("inContent")}</section>
<section class="alt"><div class="wrap prose">
 <h2>How the generator builds your circuit</h2>
 <p>Each workout pulls from the AB6 exercise library and balances the four jobs your core does: flexion (crunch patterns), hip flexion with posterior tilt (lower abs), rotation and anti-rotation (obliques), and anti-extension (deep core). Work and rest intervals scale with your level, and rounds are calculated to fit your time.</p>
 <p>Keep your phone screen on — the timer requests a wake lock where supported and calls out each exercise.</p>
</div></section>''')

# ---------------------------------------------------------------- CORE TEST
add(slug="core-test", priority="0.7", tools=True,
    title="Core Strength Test — Plank, Side Plank & Hollow Hold Benchmarks | AB6",
    desc="Test your core with three timed holds, get an instant grade and track your personal records on your device.",
    body=phero("Test", "Core strength test", "Three timed holds. Instant grades. Personal records saved on this device.", [("calculators.html", "Tools"), (None, "Core Test")]) + f'''
<section><div class="wrap split" style="align-items:start">
 <div class="timer" id="coreTest">
  <div class="choices" role="radiogroup" aria-label="Choose test">{choice("test", "plank", "Plank", checked=True)}{choice("test", "side", "Side plank")}{choice("test", "hollow", "Hollow hold")}</div>
  <div class="clock" id="ctClock">0</div>
  <button class="btn btn-primary" id="ctGo" style="min-width:160px">Start</button>
  <p class="small muted" style="margin-top:12px">3-second countdown, then hold until form breaks. Tap Stop the moment your hips sag or your back arches.</p>
  <div id="ctRes" class="result" hidden aria-live="polite"></div>
 </div>
 <div>
  <h3>Your records</h3>
  <div class="table-wrap"><table><thead><tr><th>Test</th><th>Fair / Strong / Elite</th><th>Best</th><th>Grade</th></tr></thead><tbody id="ctPR"></tbody></table></div>
  <p class="small muted" style="margin-top:10px">Benchmarks are AB6 rule-of-thumb training targets, not clinical norms. Stop if you feel pain.</p>
  {ad("sidebar")}
 </div>
</div></section>''')

# ---------------------------------------------------------------- EXERCISE LIBRARY
COREMAP = '''<div class="coremap">
 <svg viewBox="0 0 200 300" role="group" aria-label="Interactive core muscle map — select a region to filter exercises">
  <path class="body" d="M60 18 Q100 4 140 18 L152 62 Q160 140 152 200 Q150 250 132 288 L68 288 Q50 250 48 200 Q40 140 48 62 Z"/>
  <path class="zone" data-area="obliques" tabindex="0" role="button" aria-label="Obliques" d="M54 82 Q48 140 56 200 L72 212 L72 92 Z"><title>Obliques</title></path>
  <path class="zone" data-area="obliques" tabindex="-1" aria-hidden="true" d="M146 82 Q152 140 144 200 L128 212 L128 92 Z"/>
  <rect class="zone" data-area="upper" tabindex="0" role="button" aria-label="Upper abs" x="77" y="68" width="21" height="32" rx="6"><title>Upper abs</title></rect>
  <rect class="zone" data-area="upper" tabindex="-1" aria-hidden="true" x="102" y="68" width="21" height="32" rx="6"/>
  <rect class="zone" data-area="upper" tabindex="-1" aria-hidden="true" x="77" y="105" width="21" height="32" rx="6"/>
  <rect class="zone" data-area="upper" tabindex="-1" aria-hidden="true" x="102" y="105" width="21" height="32" rx="6"/>
  <rect class="zone" data-area="lower" tabindex="0" role="button" aria-label="Lower abs" x="77" y="142" width="21" height="32" rx="6"><title>Lower abs</title></rect>
  <rect class="zone" data-area="lower" tabindex="-1" aria-hidden="true" x="102" y="142" width="21" height="32" rx="6"/>
  <path class="zone" data-area="lower" tabindex="-1" aria-hidden="true" d="M77 179 L98 179 L98 238 Q86 230 77 212 Z"/>
  <path class="zone" data-area="lower" tabindex="-1" aria-hidden="true" d="M102 179 L123 179 L123 212 Q114 230 102 238 Z"/>
  <path class="zone" data-area="deep" tabindex="0" role="button" aria-label="Deep core" d="M58 246 Q100 262 142 246 L136 268 Q100 282 64 268 Z"><title>Deep core (transversus abdominis)</title></path>
 </svg>
 <div class="legend"><button type="button" data-area="upper">Upper abs</button><button type="button" data-area="lower">Lower abs</button><button type="button" data-area="obliques">Obliques</button><button type="button" data-area="deep">Deep core</button><button type="button" data-area="back">Lower back</button></div>
 <p class="small muted" style="margin:10px 0 0">Tap a muscle to filter. Tap again to clear.</p>
</div>'''
add(slug="exercises", priority="0.9", tools=True,
    title="Ab Exercise Library — 35 Core Exercises with Interactive Muscle Map | AB6",
    desc="Browse 35 ab and core exercises by muscle, level and equipment. Step-by-step form, coaching cues, common mistakes and video demos.",
    body=phero("Library", "Ab exercise library", "Tap the core map or filter by level and equipment. Every exercise has steps, a coaching cue and the #1 mistake to avoid.", [(None, "Exercise Library")]) + f'''
<section><div class="wrap layout">
 <div>
  <div class="lib-tools">
   <select id="fArea" aria-label="Muscle area"><option value="">All areas</option><option value="upper">Upper abs</option><option value="lower">Lower abs</option><option value="obliques">Obliques</option><option value="deep">Deep core</option><option value="back">Lower back</option></select>
   <select id="fLevel" aria-label="Level"><option value="">All levels</option><option value="1">Beginner</option><option value="2">Intermediate</option><option value="3">Advanced</option></select>
   <select id="fEq" aria-label="Equipment"><option value="">All equipment</option><option value="none">Bodyweight</option><option value="mat">Mat / sliders</option><option value="band">Band</option><option value="dumbbell">Dumbbell / KB</option><option value="wheel">Ab wheel</option><option value="bar">Pull-up bar</option><option value="cable">Cable</option><option value="ball">Stability ball</option><option value="bench">Bench</option></select>
   <input id="fQ" type="search" placeholder="Search…" aria-label="Search exercises">
  </div>
  <p class="small muted"><span id="libCount"></span> · <a href="workout-generator.html">My workout: <b id="pickCount">0</b> picked → open generator</a></p>
  <div id="library" class="grid g2"></div>
  {ad("inContent")}
 </div>
 <aside class="sidebar"><div class="sticky">{COREMAP}{ad("sidebar")}</div></aside>
</div></section>''')

# ---------------------------------------------------------------- CHALLENGE
ch_faq, ch_schema = faq([
    ("Is the challenge free?", "Yes. The plan, tracker and prize-draw entries are free. No purchase is necessary to enter or win."),
    ("How do prize-draw entries work?", "Each challenge week in which you complete at least 5 of 7 days earns one entry (up to 6). Submit your weekly check-in with the form below to register entries for the current season draw."),
    ("I'm a beginner — can I do it?", "Yes. Use the beginner options (shorter holds, bent-knee variations) from the exercise library. The structure stays the same; the difficulty scales to you."),
    ("Where is my progress stored?", "On your device only (browser storage). Clearing your browser data resets it. Your check-ins are what count for the draw."),
])
add(slug="challenge", priority="0.9", tools=True, schema=[ch_schema],
    title="6-Week AB6 Ab Challenge — Free Daily Plan, Tracker & Prizes | AB6",
    desc="Join the free 42-day AB6 core challenge: daily workouts, progress tracker with streaks, weekly check-ins and prize-draw entries.",
    body=phero("Free · 42 days", "The 6-Week AB6 Challenge", "Six themed weeks. Three core sessions, steps, recovery and a check-in every week. Finish weeks, earn prize-draw entries.", [(None, "6-Week Challenge")],
               '<div class="hero-ctas"><a class="btn btn-primary" href="#join">Join free →</a><a class="btn btn-ghost" href="contests.html">See prizes &amp; rules</a></div>') + f'''
<section><div class="wrap split" style="align-items:start" id="challenge">
 <div>
  <div class="card">
   <div style="display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:14px">
    <div><label for="chStart" class="small">Start date</label><input type="date" id="chStart" style="width:auto"></div>
    <b id="chToday" class="accent"></b>
   </div>
   <div class="cal" id="chCal"></div>
   <p class="small muted" style="margin-top:10px">Tap a day to see the workout. Dashed = rest / check-in day.</p>
  </div>
  <div class="card" id="chDay" style="margin-top:16px"></div>
 </div>
 <div>
  <div class="card center"><svg class="ring" id="chRing" viewBox="0 0 150 150" role="img" aria-label="Challenge progress"></svg><div class="kv" id="chStats"></div>
   <button class="btn btn-ghost btn-sm" id="chReset" style="margin-top:14px">Reset progress</button></div>
  {ad("sidebar")}
 </div>
</div></section>
<section class="alt"><div class="wrap">
 <div class="head center"><div class="eyebrow">The structure</div><h2>Six themed weeks</h2></div>
 <div class="grid g3">
  <div class="card"><h3>Week 1 · Foundation</h3><p class="muted small">Learn bracing, breathing and posterior pelvic tilt. 2 rounds, 30s work.</p></div>
  <div class="card"><h3>Week 2 · Control</h3><p class="muted small">Slower reps and longer holds. Same moves, more tension.</p></div>
  <div class="card"><h3>Week 3 · Anti-rotation</h3><p class="muted small">Obliques and stability: Pallof press, side planks, shoulder taps. 3 rounds.</p></div>
  <div class="card"><h3>Week 4 · Power</h3><p class="muted small">Faster concentric reps, V-ups and mountain climbers. Mid-point retest.</p></div>
  <div class="card"><h3>Week 5 · Density</h3><p class="muted small">4 rounds, shorter rest, harder variations from the library.</p></div>
  <div class="card"><h3>Week 6 · Peak</h3><p class="muted small">Max-quality work, final core test, final photos and your last entry.</p></div>
 </div>
</div></section>
<section id="join"><div class="wrap split" style="align-items:start">
 <div class="leadbox">
  <div class="eyebrow">Step 1</div><h2 style="font-size:2rem">Join the challenge</h2>
  <p class="muted">Get the day-1 kit, weekly reminders and season announcements.</p>
  <form class="form" data-form="Challenge signup" data-lead data-ok="You're in! Set your start date above and complete Day 1 today.">
   <div class="row"><div><label for="cj-n">First name</label><input id="cj-n" name="name" required></div><div><label for="cj-e">Email</label><input id="cj-e" name="email" type="email" required></div></div>
   <div class="row"><div><label for="cj-l">Level</label><select id="cj-l" name="level"><option>Beginner</option><option>Intermediate</option><option>Advanced</option></select></div><div><label for="cj-c">Country</label><input id="cj-c" name="country" required></div></div>
   {CONSENT}{HP}<button class="btn btn-primary btn-block" type="submit">Join the 6-week challenge</button>{MSG}
  </form>
 </div>
 <div class="card">
  <div class="eyebrow">Step 2 · Weekly</div><h2 style="font-size:2rem">Submit a check-in</h2>
  <p class="muted small">Your tracker totals are attached automatically. Each completed week (5+ of 7 days) = 1 prize-draw entry.</p>
  <form id="checkinForm" class="form" data-form="Challenge weekly check-in" data-ok="Check-in received — entries logged for this season's draw. Keep going!">
   <div class="row"><div><label for="ci-e">Email used to join</label><input id="ci-e" name="email" type="email" required></div><div><label for="ci-w">Challenge week</label><select id="ci-w" name="week">{"".join(f"<option>Week {i}</option>" for i in range(1, 7))}</select></div></div>
   <div class="row"><div><label for="ci-wa">Waist at navel (optional)</label><input id="ci-wa" name="waist"></div><div><label for="ci-p">Plank best (seconds)</label><input id="ci-p" name="plank_seconds" type="number" min="0"></div></div>
   <div><label for="ci-x">How did the week go? (optional)</label><textarea id="ci-x" name="notes" style="min-height:80px"></textarea></div>
   <div><label for="ci-l">Link to progress photo / post (optional)</label><input id="ci-l" name="photo_link" type="url" placeholder="https://"></div>
   {HP}<button class="btn btn-dark btn-block" type="submit">Submit check-in</button>{MSG}
  </form>
 </div>
</div></section>
<section class="alt"><div class="wrap" style="max-width:860px"><h2>Challenge FAQ</h2>{ch_faq}</div></section>''')
