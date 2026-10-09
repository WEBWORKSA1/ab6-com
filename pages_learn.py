"""AB6.com — guides, nutrition, videos, gear."""
from common import (HP, MSG, CONSENT, ICON, phero, ad, faq, band, card, sidebar, article, pubmed, VIDEOS, video_cards)

PAGES = []

def add(**kw):
    PAGES.append(kw)

L = ("guides.html", "Guides")

# ---------------------------------------------------------------- PILLAR
body = f'''
<p>Everyone already has abs. The rectus abdominis — the “six-pack” muscle — is there under the fat for all of us. Getting visible abs comes down to two jobs done at the same time: <b>build the muscle</b> so it shows through, and <b>lower your body fat</b> enough to reveal it. Most people do the first and skip the second. Here is the full system.</p>
<h2 id="truth">1. The two-part truth about abs</h2>
<p>Ab exercises make the muscle stronger and thicker. They do not burn the fat sitting on top of it in any meaningful local way. In a frequently cited controlled trial, six weeks of ab-only training did not significantly reduce abdominal fat compared with a control group ({pubmed("Vispute+abdominal+exercises+abdominal+fat+2011", "Vispute et al., 2011")}). Fat loss comes from an overall energy deficit; where you lose it first is mostly genetic.</p>
<div class="callout"><b>The AB6 rule:</b> Train abs 2–4× a week for the muscle. Eat in a modest deficit for the reveal. Sleep and walk to make the deficit easy.</div>
<h2 id="bodyfat">2. Know your number: body fat</h2>
<p>Abs typically become clearly visible around <b>10–12% body fat for men</b> and <b>16–19% for women</b>, with faint outlines a few points higher. Your exact number depends on genetics, ab thickness and fat distribution. Measure it with the <a href="body-fat-calculator.html">AB6 body fat calculator</a> and then plug it into the <a href="abs-timeline-calculator.html">abs timeline</a> to get a realistic date.</p>
<h2 id="diet">3. Diet: the deficit that reveals abs</h2>
<ul>
 <li><b>Calories:</b> aim 15–25% below maintenance — usually 0.5–1% of body weight lost per week. Get your number from the <a href="macro-calculator.html">macro calculator</a>.</li>
 <li><b>Protein:</b> about 1.6–2.2 g per kg of body weight daily to protect muscle ({pubmed("Morton+2018+protein+meta-analysis+resistance+training", "Morton et al., 2018")}).</li>
 <li><b>Fibre and volume:</b> vegetables, fruit, potatoes, legumes and lean proteins keep you full on fewer calories.</li>
 <li><b>Consistency over perfection:</b> the best diet is the one you can repeat on a Tuesday when you're tired.</li>
</ul>
<h2 id="training">4. Training: build abs that pop</h2>
<p>Your core does four jobs. Train all four, 2–4 times a week, with progressive overload:</p>
<div class="table-wrap"><table><thead><tr><th>Job</th><th>What it trains</th><th>Best exercises</th></tr></thead><tbody>
 <tr><td>Spinal flexion</td><td>Rectus abdominis (“six-pack”)</td><td>Crunch, cable crunch, weighted decline sit-up</td></tr>
 <tr><td>Hip flexion + pelvic tilt</td><td>Lower rectus, hip flexors</td><td>Reverse crunch, hanging knee/leg raise</td></tr>
 <tr><td>Rotation / anti-rotation</td><td>Obliques</td><td>Pallof press, woodchop, side plank</td></tr>
 <tr><td>Anti-extension</td><td>Deep core, transversus abdominis</td><td>Dead bug, plank, ab-wheel rollout</td></tr>
</tbody></table></div>
<p>Treat abs like any muscle: 3–4 sets per exercise, in the 8–20 rep range or 20–60s holds, adding reps, load or harder variations week to week. Heavy compound lifts (squats, deadlifts, overhead presses) add core work too. Browse the full <a href="exercises.html">exercise library</a> or let the <a href="workout-generator.html">generator</a> build your session.</p>
<h2 id="sleep">5. Sleep, steps and stress</h2>
<p>In one controlled study, dieters who slept 5.5 hours lost a smaller share of their weight as fat than when they slept 8.5 hours ({pubmed("Nedeltcheva+2010+insufficient+sleep+undermines+dietary+efforts", "Nedeltcheva et al., 2010")}). Aim for 7–9 hours. Daily steps (8,000–10,000) quietly add hundreds of calories burned without extra hunger or recovery cost.</p>
<h2 id="timeline">6. A realistic timeline</h2>
<p>If you are at 20% body fat (men) and want 11%, a sustainable rate of ~0.75% body weight per week usually means roughly 4–6 months. Starting closer? Weeks, not months. Use the <a href="abs-timeline-calculator.html">timeline calculator</a> for your own projection — and expect plateaus.</p>
<h2 id="mistakes">7. Seven mistakes that keep abs hidden</h2>
<ol>
 <li>Doing 500 crunches a day and ignoring diet.</li><li>Crash dieting, losing muscle, then rebounding.</li><li>Undereating protein.</li>
 <li>Never progressing the ab exercises (same 3×20 forever).</li><li>Judging progress by the scale alone — track waist and photos.</li>
 <li>Sleeping 5–6 hours on a diet.</li><li>Quitting at the plateau that happens to everyone around week 3–6.</li>
</ol>
<h2 id="plan">8. Your 6-week starter plan</h2>
<p>Take the <a href="abs-quiz.html">Find My Abs Plan quiz</a> for a version tailored to your level, equipment and schedule, or follow the free <a href="challenge.html">6-Week AB6 Challenge</a> with a day-by-day tracker.</p>
'''
html, schema = article("The complete guide", "How to get six-pack abs", "The no-nonsense, evidence-informed playbook: what actually reveals abs, what doesn't, and the exact steps to follow.",
    [L, (None, "Six-Pack Abs")],
    [("truth", "The two-part truth"), ("bodyfat", "Know your body fat"), ("diet", "Diet that reveals abs"), ("training", "Training"), ("sleep", "Sleep, steps &amp; stress"), ("timeline", "Realistic timeline"), ("mistakes", "7 mistakes"), ("plan", "Your 6-week plan"), ("faq", "FAQ")],
    body,
    [("How long does it take to get a six-pack?", "It depends on your starting body fat. From average levels, many people need roughly 3–6 months at a sustainable deficit; leaner starters may need only weeks."),
     ("Do I need a gym to get abs?", "No. Bodyweight exercises and a calorie deficit are enough to reveal abs. Equipment like an ab wheel or pull-up bar helps you keep progressing."),
     ("Should I train abs every day?", "Not necessary. 2–4 quality sessions a week with progression beats daily low-effort sets. Light core work daily is fine if you recover well."),
     ("Why can I see my upper abs but not my lower abs?", "Many people store more fat around the lower belly, so lower abs usually appear last. Keep losing fat; training can't target that fat specifically.")])
add(slug="how-to-get-six-pack-abs", priority="0.9", og_type="article", schema=schema, body=html,
    title="How to Get Six-Pack Abs: The Complete Evidence-Based Guide | AB6",
    desc="The complete guide to getting six-pack abs: body fat targets, calorie deficit, protein, the 4 core training jobs, sleep, realistic timelines and a free 6-week plan.")

# ---------------------------------------------------------------- LOWER ABS
body = f'''
<p>“Lower abs” aren't a separate muscle — they're the lower portion of the rectus abdominis. But training it with hip-flexion and pelvic-tilt movements does change how hard that region works, and many people simply store more fat there. So the plan is the same two-part system, with smarter exercise choice.</p>
<h2 id="why">Why lower abs show last</h2>
<p>Fat distribution is largely genetic and hormonal; the lower belly is a common last-to-go area for both men and women. That's normal. Keep the deficit going — the <a href="abs-timeline-calculator.html">timeline calculator</a> helps you stay patient with real numbers.</p>
<h2 id="moves">The 6 best lower-ab exercises</h2>
<ol>
 <li><b>Reverse crunch</b> — curl the pelvis, don't swing the legs. 3×12–15.</li>
 <li><b>Dead bug</b> — anti-extension with the lower back pinned. 3×8 per side.</li>
 <li><b>Hollow body hold</b> — shorten the lever until your back stays down. 3×20–40s.</li>
 <li><b>Lying leg raise</b> — stop before your back arches. 3×10–12.</li>
 <li><b>Hanging knee raise → hanging leg raise</b> — the progression that builds real lower-ab strength. 3×8–12.</li>
 <li><b>Ab-wheel rollout</b> — brutal anti-extension; start kneeling. 3×6–10.</li>
</ol>
<h2 id="workout">10-minute lower-abs workout</h2>
<div class="table-wrap"><table><thead><tr><th>Exercise</th><th>Work</th><th>Rest</th></tr></thead><tbody>
 <tr><td>Reverse crunch</td><td>40s</td><td>20s</td></tr><tr><td>Dead bug</td><td>40s</td><td>20s</td></tr>
 <tr><td>Flutter kicks</td><td>30s</td><td>30s</td></tr><tr><td>Hollow body hold</td><td>30s</td><td>30s</td></tr>
 <tr><td>Lying leg raise</td><td>40s</td><td>20s</td></tr></tbody></table></div>
<p>Repeat twice. Or let the <a href="workout-generator.html">workout generator</a> build it with “Lower abs” focus and run the voice timer for you.</p>
<h2 id="form">The one form cue that matters: posterior pelvic tilt</h2>
<p>At the top of every lower-ab rep, tuck your tailbone slightly (flatten your lower back). Without that tilt, leg raises turn into a hip-flexor exercise and your lower back takes the strain.</p>
'''
html, schema = article("Workout", "Lower abs workout that actually works", "Why lower abs show last, the 6 exercises that train them best, and a 10-minute routine you can do anywhere.",
    [L, (None, "Lower Abs")],
    [("why", "Why lower abs show last"), ("moves", "6 best exercises"), ("workout", "10-minute workout"), ("form", "Key form cue"), ("faq", "FAQ")], body,
    [("Can you target lower belly fat?", "No — spot reduction doesn't work. You can target the lower ab muscle, but fat comes off according to your overall deficit and genetics."),
     ("Why do leg raises hurt my lower back?", "Usually the pelvis tips forward and your back arches. Bend the knees, reduce the range, or switch to reverse crunches and dead bugs until you can hold a posterior tilt.")])
add(slug="lower-abs-workout", priority="0.8", og_type="article", schema=schema, body=html,
    title="Lower Abs Workout: 6 Best Exercises + 10-Minute Routine | AB6",
    desc="Train your lower abs the right way: why they show last, the 6 most effective exercises, a 10-minute routine and the form cue that protects your back.")

# ---------------------------------------------------------------- AT HOME
body = f'''
<p>You don't need a gym for great abs. Bodyweight core work plus a calorie deficit is enough to reveal a six-pack. Below are three no-equipment routines — beginner, intermediate, advanced — and how to progress them for months.</p>
<h2 id="beginner">Beginner (12 minutes)</h2>
<p>3 rounds · 30s work / 20s rest: Dead bug · Crunch · Forearm plank · Heel taps · Bird dog</p>
<h2 id="intermediate">Intermediate (15 minutes)</h2>
<p>3 rounds · 40s / 20s: Reverse crunch · Bicycle crunch · Hollow body hold · Side plank (20s each side) · Mountain climbers</p>
<h2 id="advanced">Advanced (20 minutes)</h2>
<p>4 rounds · 45s / 15s: V-up · Lying leg raise · Plank shoulder taps · Russian twist (weighted) · L-sit hold or jackknife</p>
<div class="callout">Prefer it done for you? The <a href="workout-generator.html">AB6 workout generator</a> builds these circuits automatically and runs a voice timer.</div>
<h2 id="progress">How to keep progressing at home</h2>
<ul>
 <li><b>Slow the tempo:</b> 3 seconds down on every rep.</li><li><b>Lengthen the lever:</b> bent knees → straight legs.</li>
 <li><b>Add load:</b> a backpack with books, a water jug or a single dumbbell.</li><li><b>Cheap upgrades:</b> an ab wheel and a doorway pull-up bar open up the hardest, most effective moves — see the <a href="gear.html">gear guide</a>.</li>
</ul>
<h2 id="videos">Follow along on video</h2>
<p>Want a coach on screen? Our <a href="videos.html">video hub</a> collects popular follow-along ab workouts.</p>
'''
html, schema = article("Home workouts", "Ab workout at home — no equipment", "Three bodyweight routines for every level, plus how to keep progressing without a gym.",
    [L, (None, "Ab Workout at Home")],
    [("beginner", "Beginner routine"), ("intermediate", "Intermediate routine"), ("advanced", "Advanced routine"), ("progress", "Progression"), ("videos", "Videos"), ("faq", "FAQ")], body,
    [("How many days a week should I do home ab workouts?", "Three to four days a week is plenty for most people. Rest or walk on other days."),
     ("Are home ab workouts enough for a six-pack?", "Yes, when combined with a calorie deficit to lower body fat. The workouts build the muscle; the diet reveals it.")])
add(slug="ab-workout-at-home", priority="0.8", og_type="article", schema=schema, body=html,
    title="Ab Workout at Home (No Equipment): Beginner to Advanced Routines | AB6",
    desc="Three no-equipment ab workouts for beginner, intermediate and advanced levels, plus progression tips and a free voice-guided timer.")

# ---------------------------------------------------------------- WOMEN
body = f'''
<p>The process for women is the same as for men — build the muscle, reduce body fat — but the numbers and some considerations differ. Women naturally carry more essential fat, so visible abs typically appear at a higher body-fat percentage.</p>
<h2 id="numbers">The numbers for women</h2>
<ul><li>Faint ab outline: roughly 20–24% body fat</li><li>Clear definition: roughly 16–19%</li><li>Below ~14% is very lean and can be hard to sustain; for some women it affects energy and menstrual health.</li></ul>
<p>Use the <a href="body-fat-calculator.html">body fat calculator</a> (it includes the hip measurement used in the female equation).</p>
<h2 id="cycle">Training around your cycle</h2>
<p>Energy, hunger and water retention can shift through the menstrual cycle. Compare progress photos and waist measurements at the same point of each cycle, and don't panic over week-to-week scale swings.</p>
<h2 id="postpartum">Postpartum and diastasis recti</h2>
<p>After pregnancy, a widening of the gap between the two sides of the rectus abdominis (diastasis recti) is common. Get cleared by your doctor or a pelvic-floor physiotherapist before intense core work. Gentle breathing, dead-bug and bird-dog progressions are often used early; high-pressure moves like full sit-ups and planks may need to wait. Our <a href="coaching.html">coach-matching</a> can connect you with postnatal-qualified coaches.</p>
<h2 id="plan">A balanced weekly plan</h2>
<div class="table-wrap"><table><tbody>
<tr><td><b>Mon</b></td><td>Lower-body strength + Core A</td></tr><tr><td><b>Tue</b></td><td>Walk 8–10k steps</td></tr>
<tr><td><b>Wed</b></td><td>Upper-body strength + Core B</td></tr><tr><td><b>Thu</b></td><td>Rest or yoga/mobility</td></tr>
<tr><td><b>Fri</b></td><td>Full-body strength + Core A</td></tr><tr><td><b>Sat</b></td><td>Long walk, hike or sport</td></tr><tr><td><b>Sun</b></td><td>Rest</td></tr></tbody></table></div>
<p>Get the personalised version from the <a href="abs-quiz.html">abs plan quiz</a>.</p>
'''
html, schema = article("For women", "Abs for women: the complete guide", "Body-fat targets, training around your cycle, postpartum considerations and a balanced weekly plan.",
    [L, (None, "Abs for Women")],
    [("numbers", "Body-fat numbers"), ("cycle", "Your cycle"), ("postpartum", "Postpartum &amp; diastasis"), ("plan", "Weekly plan"), ("faq", "FAQ")], body,
    [("Will ab training make my waist bulky?", "Very unlikely. Ab muscles add little width. Waist size is driven mostly by body fat and bone structure; obliques built through normal training rarely add noticeable size."),
     ("Is it healthy for women to have a six-pack?", "It can be, but very low body fat isn't sustainable for everyone. A strong, functional core at a healthy body fat is a great goal on its own.")])
add(slug="abs-for-women", priority="0.8", og_type="article", schema=schema, body=html,
    title="Abs for Women: Body Fat Targets, Workouts & Postpartum Tips | AB6",
    desc="How women can get visible abs: body-fat targets, training around the menstrual cycle, postpartum and diastasis recti considerations, and a weekly plan.")

# ---------------------------------------------------------------- NUTRITION
body = f'''
<p>Abs are revealed in the kitchen. You don't need a special “abs diet” — you need a modest calorie deficit, enough protein, and food you can stick to. Here's how to set it up in 10 minutes.</p>
<h2 id="setup">Step 1: Set your targets</h2>
<p>Run the <a href="macro-calculator.html">calorie &amp; macro calculator</a>. Typical starting points: calories 15–25% below maintenance, protein 1.6–2.2 g/kg, fat ~25% of calories, the rest carbs.</p>
<h2 id="plate">Step 2: Build the AB6 plate</h2>
<ul><li><b>½ plate:</b> vegetables or salad</li><li><b>¼ plate:</b> lean protein (chicken, fish, eggs, Greek yogurt, tofu, lean beef, legumes)</li><li><b>¼ plate:</b> smart carbs (rice, potatoes, oats, fruit, whole-grain bread)</li><li><b>+ a thumb</b> of fats (olive oil, nuts, avocado)</li></ul>
<h2 id="day">Step 3: Sample day (~1,900 kcal, ~160 g protein)</h2>
<div class="table-wrap"><table><thead><tr><th>Meal</th><th>Food</th></tr></thead><tbody>
<tr><td>Breakfast</td><td>Greek yogurt (300 g), berries, 30 g oats, cinnamon</td></tr>
<tr><td>Lunch</td><td>Chicken breast (180 g), rice (150 g cooked), big salad, olive-oil dressing</td></tr>
<tr><td>Snack</td><td>Protein shake + an apple</td></tr>
<tr><td>Dinner</td><td>Salmon (150 g), roast potatoes (250 g), green vegetables</td></tr>
<tr><td>Evening</td><td>Cottage cheese (200 g) or skyr</td></tr></tbody></table></div>
<p class="small muted">Values are approximate; adjust portions to your own targets.</p>
<h2 id="levers">Step 4: Hunger levers that work</h2>
<ul><li>Protein at every meal.</li><li>High-volume foods: soups, vegetables, potatoes, berries, popcorn.</li><li>Fewer liquid calories (alcohol, juice, sweet coffee drinks).</li><li>Plan treats instead of banning them.</li></ul>
<h2 id="adjust">Step 5: Adjust every 2 weeks</h2>
<p>Use the weekly average of morning weigh-ins and your waist measurement. If both are flat for 2–3 weeks, reduce ~100–150 kcal per day or add ~2,000 steps. If you're losing faster than 1% of body weight per week and feel drained, eat a bit more.</p>
'''
html, schema = article("Nutrition", "The abs nutrition guide", "Calories, protein, plate building, a sample day and the simple adjustments that keep fat loss moving.",
    [L, (None, "Nutrition")],
    [("setup", "Set your targets"), ("plate", "The AB6 plate"), ("day", "Sample day"), ("levers", "Hunger levers"), ("adjust", "Adjusting"), ("faq", "FAQ")], body,
    [("Do I need to cut carbs to get abs?", "No. Total calories and protein matter far more than carb-vs-fat split. Low-carb can help some people control appetite; it isn't required."),
     ("Do fat burners work?", "Most offer little beyond caffeine. Spend that money on food quality, sleep and steps."),
     ("What about intermittent fasting?", "It's a scheduling tool. If it helps you eat less without losing protein or training quality, use it; it has no special abs effect.")])
add(slug="nutrition", priority="0.8", og_type="article", schema=schema, body=html,
    title="Abs Nutrition Guide: Calories, Protein & Sample Meal Plan | AB6",
    desc="What to eat to get abs: set calorie and protein targets, build the AB6 plate, follow a sample day and adjust every two weeks.")

# ---------------------------------------------------------------- GUIDES HUB
add(slug="guides", priority="0.8",
    title="Abs & Core Guides — Training, Nutrition and Plans | AB6",
    desc="Evidence-informed guides on getting six-pack abs, lower abs training, home ab workouts, abs for women and abs nutrition.",
    body=phero("Learn", "Guides", "Clear, practical guides with the evidence linked. Read one, then use the tools to act on it.", [(None, "Guides")]) + f'''
<section><div class="wrap"><div class="grid g3">
 {card("how-to-get-six-pack-abs.html", "book", "How to Get Six-Pack Abs", "The complete playbook — start here.", "Pillar")}
 {card("lower-abs-workout.html", "target", "Lower Abs Workout", "The 6 best exercises + a 10-minute routine.")}
 {card("ab-workout-at-home.html", "bolt", "Ab Workout at Home", "No-equipment routines for every level.")}
 {card("abs-for-women.html", "user", "Abs for Women", "Targets, cycle, postpartum &amp; weekly plan.")}
 {card("nutrition.html", "fire", "Abs Nutrition Guide", "Calories, protein, sample day.")}
 {card("gear.html", "gear", "Home Ab Gear Guide", "What's worth buying (and what isn't).")}
</div>{ad("inContent")}</div></section>
{band("Stop reading, start training", "Get a plan built for your level, equipment and schedule in 60 seconds.", "abs-quiz.html", "Take the quiz →")}''')

# ---------------------------------------------------------------- VIDEOS
add(slug="videos", priority="0.8",
    title="Follow-Along Ab Workout Videos (5–20 Min) | AB6",
    desc="A curated hub of popular follow-along ab and core workout videos from leading fitness creators, plus AB6 originals.",
    body=phero("Watch", "Follow-along ab workout videos", "Press play and train. Videos load only when you click (faster pages, more privacy).", [(None, "Videos")],
               '<div class="hero-ctas"><a class="btn btn-primary" data-channel href="#">Subscribe to AB6 on YouTube</a></div>') + f'''
<section><div class="wrap">
 <div class="grid g3" data-own-videos style="margin-bottom:24px"></div>
 <div class="grid g3">{video_cards(VIDEOS)}</div>
 {ad("inContent")}
 <p class="small muted">Videos are embedded from YouTube using the official embed player and remain the property of their creators. AB6 is not affiliated with these creators. <a href="contact.html">Creators: request removal or feature your video →</a></p>
</div></section>
<section class="alt"><div class="wrap split">
 <div><div class="eyebrow">Creators</div><h2>Get your workout featured</h2><p class="muted">Make great core content? Submit it for the AB6 video hub, or apply to create AB6 originals (paid).</p></div>
 <form class="form card" data-form="Video creator submission" data-ok="Thanks! We review submissions weekly.">
  <div class="row"><div><label for="v-n">Name / channel</label><input id="v-n" name="name" required></div><div><label for="v-e">Email</label><input id="v-e" name="email" type="email" required></div></div>
  <div><label for="v-u">Video or channel URL</label><input id="v-u" name="url" type="url" required placeholder="https://youtube.com/…"></div>
  <div><label for="v-t">Interest</label><select id="v-t" name="interest"><option>Feature my video</option><option>Create paid AB6 originals</option><option>Collaboration / sponsorship</option></select></div>
  {HP}<button class="btn btn-primary" type="submit">Submit</button>{MSG}
 </form>
</div></section>''')

# ---------------------------------------------------------------- GEAR
gear = [
    ("Ab wheel (wide, dual wheel)", "ab wheel roller dual wheel", "The best value-for-money tool in core training. Wide dual wheels are more stable for beginners. Look for a thick knee pad and grippy handles."),
    ("Doorway pull-up bar", "doorway pull up bar", "Unlocks hanging knee/leg raises — the best lower-ab progression. Check door-frame width and the weight rating."),
    ("Resistance band set with anchor", "resistance bands with door anchor", "For Pallof presses and woodchops — anti-rotation work that bodyweight can't easily replace."),
    ("Exercise mat (10–15 mm)", "exercise mat thick", "Comfort for floor work. Thicker for comfort, thinner for stability during planks."),
    ("Adjustable dumbbell or kettlebell", "adjustable dumbbell", "For suitcase carries, weighted crunches and Russian twists. One adjustable pair covers years of progress."),
    ("Gliding discs / sliders", "core sliders gliding discs", "Cheap and surprisingly hard: body saws, mountain climbers and pikes."),
    ("Stability ball (size by height)", "stability ball exercise ball", "Stir-the-pot and ball rollouts. Choose the size for your height (e.g., 55 cm, 65 cm, 75 cm)."),
    ("Kitchen scale + measuring tape", "digital kitchen scale", "Not glamorous — but nothing improves results more than accurate portions and waist tracking."),
]
gear_cards = "".join(f'<div class="card reveal"><h3>{t}</h3><p class="muted small">{d}</p><a class="btn btn-dark btn-sm" data-amz="{q}" href="#">Check price ↗</a></div>' for t, q, d in gear)
add(slug="gear", priority="0.7",
    title="Home Ab Gear Guide — What's Worth Buying for Core Training | AB6",
    desc="The core-training equipment that's worth your money at home: ab wheel, pull-up bar, bands, mat, dumbbells, sliders and more — with what to look for.",
    body=phero("Gear", "Home ab gear guide", "You need nothing to start. These are the few pieces that unlock the hardest, most effective core exercises.", [(None, "Gear")]) + f'''
<section><div class="wrap">
 <div class="callout small"><b>Disclosure:</b> some links are affiliate links. If you buy through them, AB6 may earn a commission at no extra cost to you. Picks are based on usefulness for the exercises in our library, not on payment. We have not lab-tested individual products — use the “what to look for” notes and reviews from verified buyers.</div>
 <div class="grid g2">{gear_cards}</div>{ad("inContent")}
</div></section>
<section class="alt"><div class="wrap split">
 <div><div class="eyebrow">Brands</div><h2>Make fitness gear?</h2><p class="muted">Feature your product, sponsor a challenge prize or run an affiliate partnership with AB6.</p></div>
 <a class="btn btn-primary" href="advertise.html">See partnership options →</a>
</div></section>''')
