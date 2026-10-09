/* AB6.com — interactive tools: calculators, quiz, library, generator, timer, core test, challenge */
(function () {
  "use strict";
  var A = window.AB6 || {}, $ = A.$, $$ = A.$$, store = A.store;
  var EX = window.AB6_EX || [], AREAS = window.AB6_AREAS || {}, EQ = window.AB6_EQ || {};
  var qs = new URLSearchParams(location.search);
  function n(v) { var x = parseFloat(v); return isFinite(x) ? x : NaN; }
  function r1(x) { return Math.round(x * 10) / 10; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function fmtDate(d) { return d.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" }); }
  function val(form, name) { var el = form.elements[name]; if (!el) return ""; if (el.length && !el.tagName) { for (var i = 0; i < el.length; i++) if (el[i].checked) return el[i].value; return ""; } return el.value; }
  function vals(form, name) { return $$('[name="' + name + '"]:checked', form).map(function (e) { return e.value; }); }

  /* ---------- Unit toggles: buttons [data-units] set form.dataset.units and swap labels ---------- */
  $$(".unit-toggle").forEach(function (t) {
    var form = document.getElementById(t.getAttribute("data-for"));
    $$("button", t).forEach(function (b) {
      b.addEventListener("click", function () {
        $$("button", t).forEach(function (x) { x.classList.toggle("on", x === b); });
        form.dataset.units = b.getAttribute("data-units");
        $$("[data-m]", form).forEach(function (s) { s.textContent = form.dataset.units === "imperial" ? s.getAttribute("data-i") : s.getAttribute("data-m"); });
      });
    });
  });
  function imperial(form) { return form.dataset.units === "imperial"; }
  function toCm(form, v) { return imperial(form) ? v * 2.54 : v; }
  function toKg(form, v) { return imperial(form) ? v * 0.453592 : v; }
  function wOut(form, kg) { return imperial(form) ? r1(kg / 0.453592) + " lb" : r1(kg) + " kg"; }

  function absStatus(sex, bf) {
    var t = sex === "f" ? [17, 20, 24] : [10, 13, 17];
    if (bf <= t[0]) return ["Visible six-pack likely", "You're in the range where most people see clear ab definition. Focus on building thicker abs and staying consistent."];
    if (bf <= t[1]) return ["Upper-ab outline likely", "You're close. A few more points of body fat loss usually reveals the lower abs."];
    if (bf <= t[2]) return ["Faint outline in good lighting", "Your abs are there — a steady deficit for a few months is the main lever now."];
    return ["Abs likely hidden by fat", "Training builds the muscle, but fat loss reveals it. Start with the calorie and timeline calculators."];
  }

  /* ======================= Body-fat calculator (US Navy method) ======================= */
  var bf = $("#bfCalc");
  if (bf) {
    var hipRow = $("[data-hip]", bf);
    function sexSync() { var f = val(bf, "sex") === "f"; hipRow.style.display = f ? "" : "none"; $("input", hipRow).required = f; }
    $$('[name="sex"]', bf).forEach(function (e) { e.addEventListener("change", sexSync) }); sexSync();
    bf.addEventListener("submit", function (e) {
      e.preventDefault();
      var sex = val(bf, "sex"), h = toCm(bf, n(bf.height.value)), nk = toCm(bf, n(bf.neck.value)), w = toCm(bf, n(bf.waist.value)), hp = toCm(bf, n(bf.hip.value)), kg = toKg(bf, n(bf.weight.value));
      var out = $("#bfOut"), pct;
      if (sex === "f") { if (!(w + hp - nk > 0)) return bad(); pct = 495 / (1.29579 - 0.35004 * Math.log10(w + hp - nk) + 0.22100 * Math.log10(h)) - 450; }
      else { if (!(w - nk > 0)) return bad(); pct = 495 / (1.0324 - 0.19077 * Math.log10(w - nk) + 0.15456 * Math.log10(h)) - 450; }
      if (!isFinite(pct) || pct < 2 || pct > 60) return bad();
      pct = r1(pct);
      var cats = sex === "f" ? [[13, "Essential fat"], [20, "Athletic"], [24, "Fitness"], [31, "Average"], [99, "Above average"]] : [[5, "Essential fat"], [13, "Athletic"], [17, "Fitness"], [24, "Average"], [99, "Above average"]];
      var cat = cats.filter(function (c) { return pct <= c[0]; })[0][1];
      var st = absStatus(sex, pct);
      var mass = isFinite(kg) && kg > 0 ? '<div><b>' + wOut(bf, kg * pct / 100) + '</b><span>Fat mass</span></div><div><b>' + wOut(bf, kg * (1 - pct / 100)) + '</b><span>Lean mass</span></div>' : "";
      var link = "abs-timeline-calculator.html?sex=" + sex + "&bf=" + pct + (isFinite(kg) && kg > 0 ? "&kg=" + r1(kg) : "");
      out.innerHTML = '<div class="small muted">Estimated body fat</div><div class="big">' + pct + '%</div>' +
        '<div class="meter" aria-hidden="true"><i style="left:' + Math.min(98, pct / 40 * 100) + '%"></i></div><div class="small faint" style="display:flex;justify-content:space-between"><span>0%</span><span>20%</span><span>40%+</span></div>' +
        '<div class="kv"><div><b>' + cat + '</b><span>Category (ACE ranges)</span></div><div><b>' + st[0] + '</b><span>Ab visibility</span></div>' + mass + '</div>' +
        '<p style="margin-top:14px">' + st[1] + '</p><div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-primary btn-sm" href="' + link + '">How long until my abs show? →</a><a class="btn btn-ghost btn-sm" href="macro-calculator.html">Get my calorie target</a></div>';
      out.hidden = false;
      function bad() { out.hidden = false; out.innerHTML = '<p class="form-msg err">Please check your measurements — waist must be larger than neck, and values must be in the selected units.</p>'; }
    });
  }

  /* ======================= Calorie & macro calculator ======================= */
  var mc = $("#macroCalc");
  if (mc) mc.addEventListener("submit", function (e) {
    e.preventDefault();
    var sex = val(mc, "sex"), age = n(mc.age.value), h = toCm(mc, n(mc.height.value)), kg = toKg(mc, n(mc.weight.value)), act = n(mc.activity.value), goal = n(mc.goal.value), bfp = n(mc.bodyfat.value);
    var bmr, method;
    if (isFinite(bfp) && bfp > 3 && bfp < 60) { bmr = 370 + 21.6 * kg * (1 - bfp / 100); method = "Katch-McArdle (uses your body fat)"; }
    else { bmr = 10 * kg + 6.25 * h - 5 * age + (sex === "f" ? -161 : 5); method = "Mifflin-St Jeor"; }
    var tdee = bmr * act, target = tdee * (1 + goal), floor = sex === "f" ? 1200 : 1500, floored = false;
    if (target < Math.max(floor, bmr * 0.95) && goal < 0) { target = Math.max(floor, bmr * 0.95); floored = true; }
    var pG = Math.round(kg * (goal < 0 ? 2.0 : 1.8)), fG = Math.round(Math.max(target * 0.25 / 9, kg * 0.6)), cG = Math.max(0, Math.round((target - pG * 4 - fG * 9) / 4));
    var out = $("#macroOut");
    out.innerHTML = '<div class="small muted">Daily calorie target</div><div class="big">' + Math.round(target) + ' kcal</div>' +
      '<div class="kv"><div><b>' + pG + ' g</b><span>Protein</span></div><div><b>' + cG + ' g</b><span>Carbs</span></div><div><b>' + fG + ' g</b><span>Fat</span></div><div><b>' + Math.round(target / 1000 * 14) + ' g</b><span>Fibre (14 g / 1,000 kcal)</span></div></div>' +
      '<div class="kv"><div><b>' + Math.round(bmr) + '</b><span>BMR — ' + method + '</span></div><div><b>' + Math.round(tdee) + '</b><span>Maintenance (TDEE)</span></div><div><b>' + (goal ? Math.round(goal * 100) + "%" : "0%") + '</b><span>Adjustment</span></div></div>' +
      (floored ? '<p class="callout" style="margin-top:14px">We raised your target to a safer floor. Very low intakes make it hard to keep muscle — the muscle you want to show.</p>' : "") +
      '<p style="margin-top:14px" class="small muted">Weigh yourself 3–4 mornings a week and use the weekly average. If it hasn\'t moved in 2–3 weeks, lower intake by ~100–150 kcal or add 2,000 daily steps.</p>' +
      '<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-primary btn-sm" href="abs-quiz.html">Build my free abs plan →</a><a class="btn btn-ghost btn-sm" href="nutrition.html">Abs nutrition guide</a></div>';
    out.hidden = false;
  });

  /* ======================= Abs timeline calculator ======================= */
  var tl = $("#timelineCalc");
  if (tl) {
    if (qs.get("sex")) $$('[name="sex"]', tl).forEach(function (r) { r.checked = r.value === qs.get("sex"); });
    if (qs.get("bf")) tl.current.value = qs.get("bf");
    if (qs.get("kg")) tl.weight.value = qs.get("kg");
    function defTarget() { if (!tl.target.dataset.touched) tl.target.value = val(tl, "sex") === "f" ? 18 : 11; }
    tl.target.addEventListener("input", function () { tl.target.dataset.touched = 1; });
    $$('[name="sex"]', tl).forEach(function (e) { e.addEventListener("change", defTarget); }); defTarget();
    tl.addEventListener("submit", function (e) {
      e.preventDefault();
      var w0 = n(tl.weight.value), cur = n(tl.current.value) / 100, tgt = n(tl.target.value) / 100, rate = n(tl.rate.value) / 100, out = $("#tlOut");
      out.hidden = false;
      if (!(cur > 0 && tgt > 0 && w0 > 0)) { out.innerHTML = '<p class="form-msg err">Please fill in all fields.</p>'; return; }
      if (cur <= tgt) { out.innerHTML = '<div class="big">You\'re there.</div><p>At ' + r1(cur * 100) + '% you\'re already at or below your target. Shift focus to building ab thickness: weighted crunches, hanging leg raises and ab-wheel work, 3×/week.</p><a class="btn btn-primary btn-sm" href="workout-generator.html">Generate an advanced workout →</a>'; return; }
      var lbm = w0 * (1 - cur), wt = lbm / (1 - tgt), w = w0, pts = [w0], weeks = 0;
      while (w > wt && weeks < 260) { w -= w * rate; weeks++; pts.push(Math.max(w, wt)); }
      var unit = imperial(tl) ? " lb" : " kg", end = new Date(Date.now() + weeks * 7 * 864e5);
      var W = 600, H = 200, mx = pts.length - 1 || 1, lo = Math.min.apply(null, pts), hi = Math.max.apply(null, pts), span = (hi - lo) || 1;
      var poly = pts.map(function (p, i) { return (i / mx * (W - 40) + 30).toFixed(1) + "," + (H - 30 - (p - lo) / span * (H - 60)).toFixed(1); }).join(" ");
      out.innerHTML = '<div class="small muted">Estimated time to ' + r1(tgt * 100) + '% body fat</div><div class="big">' + weeks + ' weeks</div>' +
        '<div class="kv"><div><b>' + fmtDate(end) + '</b><span>Target date</span></div><div><b>' + r1(wt) + unit + '</b><span>Goal weight (muscle kept)</span></div><div><b>' + r1(w0 - wt) + unit + '</b><span>Fat to lose</span></div><div><b>' + r1(w0 * rate) + unit + '</b><span>First-week loss</span></div></div>' +
        '<svg viewBox="0 0 ' + W + ' ' + H + '" style="width:100%;margin-top:16px" role="img" aria-label="Projected weight curve"><line x1="30" y1="' + (H - 30) + '" x2="' + (W - 10) + '" y2="' + (H - 30) + '" stroke="currentColor" opacity=".2"/><polyline fill="none" stroke="#c4ff3d" stroke-width="4" stroke-linecap="round" points="' + poly + '"/><text x="30" y="20" fill="currentColor" font-size="13" opacity=".7">' + r1(w0) + unit + '</text><text x="' + (W - 10) + '" y="' + (H - 8) + '" fill="currentColor" font-size="13" opacity=".7" text-anchor="end">Week ' + weeks + ' · ' + r1(wt) + unit + '</text></svg>' +
        '<p class="small muted">Assumes you keep your lean mass (lift + eat enough protein). Real progress is not linear — expect plateaus, water swings and diet breaks. Treat this as a planning range, not a promise.</p>' +
        '<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-primary btn-sm" href="coaching.html">Hit it faster with a coach →</a><a class="btn btn-ghost btn-sm" href="challenge.html">Start the 6-week challenge</a></div>';
    });
  }

  /* ======================= Exercise helpers ======================= */
  function pick(list, k, seed) {
    var a = list.slice(), s = seed || Math.random() * 1e9;
    for (var i = a.length - 1; i > 0; i--) { s = (s * 9301 + 49297) % 233280; var j = Math.floor(s / 233280 * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a.slice(0, k);
  }
  function pool(level, eqs, focus) {
    return EX.filter(function (x) { return x.level <= level && (x.eq === "none" || x.eq === "mat" || eqs.indexOf(x.eq) > -1); })
      .sort(function (a, b) { return (focus && b.area.indexOf(focus) > -1 ? 1 : 0) - (focus && a.area.indexOf(focus) > -1 ? 1 : 0); });
  }
  function balanced(level, eqs, focus, count, seed) {
    var p = pool(level, eqs, focus), out = [], used = {};
    var order = focus && focus !== "balanced" ? [focus, focus, "deep", "obliques", "lower", "upper", focus, "back"] : ["lower", "obliques", "deep", "upper", "obliques", "deep", "lower", "back"];
    order.forEach(function (ar) {
      if (out.length >= count) return;
      var c = pick(p.filter(function (x) { return x.area.indexOf(ar) > -1 && !used[x.id]; }), 1, seed ? seed + out.length * 7 : 0)[0];
      if (c) { used[c.id] = 1; out.push(c); }
    });
    pick(p.filter(function (x) { return !used[x.id]; }), count - out.length, seed).forEach(function (x) { out.push(x); });
    return out.slice(0, count);
  }
  function ytSearch(name) { return "https://www.youtube.com/results?search_query=" + encodeURIComponent(name + " exercise form tutorial"); }

  /* ======================= Exercise library + interactive core map ======================= */
  var lib = $("#library");
  if (lib) {
    var fArea = $("#fArea"), fLevel = $("#fLevel"), fEq = $("#fEq"), fQ = $("#fQ"), cnt = $("#libCount");
    var picks = JSON.parse(store("ab6-picks") || "[]");
    function render() {
      var a = fArea.value, l = +fLevel.value || 0, q2 = fQ.value.toLowerCase().trim(), eq = fEq.value;
      var list = EX.filter(function (x) { return (!a || x.area.indexOf(a) > -1) && (!l || x.level === l) && (!eq || x.eq === eq) && (!q2 || (x.name + " " + x.cue).toLowerCase().indexOf(q2) > -1); });
      cnt.textContent = list.length + " exercise" + (list.length === 1 ? "" : "s");
      lib.innerHTML = list.map(function (x) {
        var on = picks.indexOf(x.id) > -1;
        return '<article class="card ex-card" id="ex-' + x.id + '"><h3>' + x.name + '</h3><div>' + x.area.map(function (z) { return '<span class="tag">' + AREAS[z] + '</span>'; }).join("") +
          '<span class="tag l' + x.level + '">' + ["", "Beginner", "Intermediate", "Advanced"][x.level] + '</span><span class="tag">' + EQ[x.eq] + '</span></div><ol>' + x.steps.map(function (s) { return "<li>" + s + "</li>"; }).join("") + '</ol>' +
          '<div class="cue"><b class="accent">Coach cue:</b> ' + x.cue + '<br><b style="color:var(--danger)">Avoid:</b> ' + x.mistake + '</div>' +
          '<div class="acts"><a class="btn btn-dark btn-sm" target="_blank" rel="noopener" href="' + ytSearch(x.name) + '">▶ Watch demos</a><button class="btn btn-sm ' + (on ? "btn-primary" : "btn-ghost") + '" data-pick="' + x.id + '">' + (on ? "✓ In my workout" : "+ Add to my workout") + '</button></div></article>';
      }).join("") || '<p class="muted">No exercises match those filters.</p>';
      $$(".coremap .zone").forEach(function (z) { z.classList.toggle("on", z.getAttribute("data-area") === a); });
      $$(".legend button").forEach(function (b) { b.classList.toggle("on", b.getAttribute("data-area") === a); });
      var pc = $("#pickCount"); if (pc) pc.textContent = picks.length;
    }
    [fArea, fLevel, fEq].forEach(function (s) { s.addEventListener("change", render); });
    fQ.addEventListener("input", render);
    lib.addEventListener("click", function (e) {
      var b = e.target.closest("[data-pick]"); if (!b) return;
      var id = b.getAttribute("data-pick"), i = picks.indexOf(id);
      if (i > -1) picks.splice(i, 1); else picks.push(id);
      store("ab6-picks", JSON.stringify(picks)); render();
    });
    function setArea(ar) { fArea.value = fArea.value === ar ? "" : ar; render(); }
    $$(".coremap .zone").forEach(function (z) {
      z.addEventListener("click", function () { setArea(z.getAttribute("data-area")); });
      z.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); setArea(z.getAttribute("data-area")); } });
    });
    $$(".legend button").forEach(function (b) { b.addEventListener("click", function () { setArea(b.getAttribute("data-area")); }); });
    if (qs.get("area")) fArea.value = qs.get("area");
    render();
  }

  /* ======================= Interval timer engine ======================= */
  var actx;
  function beep(f, d) {
    try { actx = actx || new (window.AudioContext || window.webkitAudioContext)(); var o = actx.createOscillator(), g = actx.createGain(); o.frequency.value = f || 880; o.connect(g); g.connect(actx.destination); g.gain.setValueAtTime(.2, actx.currentTime); g.gain.exponentialRampToValueAtTime(.001, actx.currentTime + (d || .15)); o.start(); o.stop(actx.currentTime + (d || .15)); } catch (e) {}
  }
  function say(t) { try { if (window.speechSynthesis && store("ab6-voice") !== "off") { speechSynthesis.cancel(); speechSynthesis.speak(new SpeechSynthesisUtterance(t)); } } catch (e) {} }
  function Timer(box, list, onTick) {
    var i = 0, left = 0, iv = null, lock = null;
    function cur() { return list[i]; }
    function draw() {
      var c = cur(), nx = list[i + 1];
      box.className = "timer " + (c ? c.type : "");
      $(".clock", box).textContent = c ? left : "✓";
      $(".now", box).textContent = c ? c.label : "Workout complete — great work!";
      $(".next", box).textContent = nx ? "Next: " + nx.label : "";
      if (onTick) onTick(i);
    }
    function enter() { var c = cur(); if (!c) { stop(); beep(1200, .5); say("Workout complete"); draw(); return; } left = c.secs; if (c.type === "work") say(c.label); else if (c.type === "rest") say("Rest"); beep(c.type === "work" ? 1040 : 660, .25); draw(); }
    function tick() { left--; if (left <= 3 && left > 0) beep(760, .08); if (left <= 0) { i++; enter(); } else draw(); }
    function start() { if (iv) return; if (!cur()) { i = 0; enter(); } else if (!left) enter(); iv = setInterval(tick, 1000); try { navigator.wakeLock && navigator.wakeLock.request("screen").then(function (l) { lock = l; }); } catch (e) {} }
    function stop() { clearInterval(iv); iv = null; try { lock && lock.release(); } catch (e) {} }
    return { start: start, pause: stop, skip: function () { i++; enter(); }, reset: function () { stop(); i = 0; left = 0; draw(); $(".clock", box).textContent = "GO"; $(".now", box).textContent = "Press start"; }, running: function () { return !!iv; } };
  }

  /* ======================= Workout generator ======================= */
  var gen = $("#genForm");
  if (gen) {
    var gOut = $("#genOut"), timerBox = $("#timer"), T = null, steps = [];
    var vb = $("#voiceBtn"); function vSync() { vb.textContent = store("ab6-voice") === "off" ? "🔇 Voice off" : "🔊 Voice on"; }
    vb.addEventListener("click", function () { store("ab6-voice", store("ab6-voice") === "off" ? "on" : "off"); vSync(); }); vSync();
    function build(useP) {
      var mins = +val(gen, "minutes"), lvl = +val(gen, "level"), eqs = vals(gen, "eq"), focus = val(gen, "focus");
      var wr = { 1: [30, 20], 2: [40, 20], 3: [45, 15] }[lvl], list;
      if (useP) { var ids = JSON.parse(store("ab6-picks") || "[]"); list = EX.filter(function (x) { return ids.indexOf(x.id) > -1; }); if (!list.length) { alert("Your workout is empty — add exercises from the Exercise Library first."); return; } }
      else list = balanced(lvl, eqs, focus === "balanced" ? "" : focus, mins <= 5 ? 5 : 6);
      var per = list.length * (wr[0] + wr[1]), rounds = Math.max(1, Math.round((mins * 60 + 45) / (per + 45)));
      steps = [{ type: "rest", label: "Get ready", secs: 10 }];
      for (var r = 1; r <= rounds; r++) {
        list.forEach(function (x, k) {
          var side = /Side Plank|Suitcase|Pallof|Woodchop|Copenhagen/.test(x.name) ? " (switch sides halfway)" : "";
          steps.push({ type: "work", label: x.name + side, secs: wr[0], id: x.id, round: r });
          if (k < list.length - 1) steps.push({ type: "rest", label: "Rest", secs: wr[1] });
        });
        if (r < rounds) steps.push({ type: "rest", label: "Round " + r + " done — rest", secs: 45 });
      }
      var total = steps.reduce(function (a, s) { return a + s.secs; }, 0);
      gOut.innerHTML = '<div class="kv" style="margin:0 0 14px"><div><b>' + Math.round(total / 60) + ' min</b><span>Total time</span></div><div><b>' + rounds + '</b><span>Rounds</span></div><div><b>' + wr[0] + 's / ' + wr[1] + 's</b><span>Work / rest</span></div></div><ol class="plan-list">' +
        list.map(function (x) { return '<li data-id="' + x.id + '"><div><b>' + x.name + '</b><div class="small muted">' + x.area.map(function (z) { return AREAS[z]; }).join(" · ") + ' — ' + x.cue + '</div></div></li>'; }).join("") + '</ol>';
      timerBox.hidden = false;
      T = Timer(timerBox, steps, function (i) { var s = steps[i]; $$(".plan-list li", gOut).forEach(function (li) { li.classList.toggle("cur", !!s && li.getAttribute("data-id") === s.id); }); });
      T.reset();
      store("ab6-lastgen", JSON.stringify({ mins: mins, lvl: lvl }));
    }
    gen.addEventListener("submit", function (e) { e.preventDefault(); build(false); timerBox.scrollIntoView({ behavior: "smooth", block: "center" }); });
    var up = $("#usePicks"); if (up) up.addEventListener("click", function () { build(true); });
    $("#tStart").addEventListener("click", function () { if (T) (T.running() ? T.pause() : T.start()); this.textContent = T && T.running() ? "Pause" : "Start"; });
    $("#tSkip").addEventListener("click", function () { if (T) T.skip(); });
    $("#tReset").addEventListener("click", function () { if (T) { T.reset(); $("#tStart").textContent = "Start"; } });
    if (qs.get("wod")) { gen.minutes.value = "10"; build(false); setTimeout(function () { timerBox.scrollIntoView({ block: "center" }); }, 300); }
  }

  /* ======================= Workout of the day (seeded by date) ======================= */
  var wod = $("#wod");
  if (wod) {
    var d = new Date(), seed = d.getFullYear() * 1000 + d.getMonth() * 40 + d.getDate();
    var list = balanced(2, [], "", 5, seed);
    wod.innerHTML = '<ol class="plan-list">' + list.map(function (x) { return '<li><div><b>' + x.name + '</b> <span class="small muted">— 40s on / 20s off</span></div></li>'; }).join("") + '</ol><p class="small muted">3 rounds · ~15 minutes · no equipment · new workout every day</p>';
  }

  /* ======================= Core strength test ======================= */
  var ct = $("#coreTest");
  if (ct) {
    var TESTS = { plank: { n: "Forearm plank", b: [30, 60, 120] }, side: { n: "Side plank (weaker side)", b: [20, 45, 90] }, hollow: { n: "Hollow body hold", b: [15, 30, 60] } };
    var sw = null, t0 = 0, sel = "plank", disp = $("#ctClock"), res = $("#ctRes"), prs = JSON.parse(store("ab6-prs") || "{}");
    function grade(k, s) { var b = TESTS[k].b; return s < b[0] ? ["Building", "danger"] : s < b[1] ? ["Fair", "warn"] : s < b[2] ? ["Strong", "accent"] : ["Elite", "ok"]; }
    function table() {
      $("#ctPR").innerHTML = Object.keys(TESTS).map(function (k) { var p = prs[k]; return "<tr><td>" + TESTS[k].n + "</td><td>" + TESTS[k].b.join("s / ") + "s</td><td><b>" + (p ? p.s + "s" : "—") + "</b></td><td>" + (p ? grade(k, p.s)[0] + " · " + p.d : "") + "</td></tr>"; }).join("");
    }
    $$('[name="test"]', ct).forEach(function (r) { r.addEventListener("change", function () { sel = r.value; }); });
    $("#ctGo").addEventListener("click", function () {
      if (sw === -1) { clearInterval(this._cd); sw = null; this.textContent = "Start"; disp.textContent = "0"; return; }
      if (sw) {
        clearInterval(sw); sw = null; this.textContent = "Start"; var s = Math.floor((Date.now() - t0) / 1000), g = grade(sel, s);
        beep(1200, .4);
        var pr = !prs[sel] || s > prs[sel].s;
        if (pr) { prs[sel] = { s: s, d: fmtDate(new Date()) }; store("ab6-prs", JSON.stringify(prs)); }
        res.innerHTML = '<div class="big" style="color:var(--' + g[1] + ')">' + g[0] + '</div><p>' + TESTS[sel].n + ': <b>' + s + ' seconds</b>' + (pr ? " — new personal record! 🎉" : "") + '</p><a class="btn btn-primary btn-sm" href="workout-generator.html">Train to beat it →</a>';
        res.hidden = false; table();
      } else {
        var c = 3; this.textContent = "Stop"; disp.textContent = c; beep();
        var self = this, cd = setInterval(function () { c--; if (c > 0) { disp.textContent = c; beep(); } else { clearInterval(cd); beep(1200, .3); say("Go"); t0 = Date.now(); sw = setInterval(function () { disp.textContent = Math.floor((Date.now() - t0) / 1000); }, 200); } }, 1000);
        sw = -1; // guard while counting down
        self._cd = cd;
      }
    });
    table();
  }

  /* ======================= 6-week challenge tracker ======================= */
  var ch = $("#challenge");
  if (ch) {
    var THEMES = ["Foundation", "Control", "Anti-rotation", "Power", "Density", "Peak"];
    function dayPlan(day) {
      var w = Math.floor((day - 1) / 7), d = (day - 1) % 7, sets = 2 + Math.floor(w / 2), sec = 30 + w * 5, hold = 20 + w * 10;
      var A = ["Dead Bug", "Reverse Crunch", "Forearm Plank", "Bicycle Crunch"], B = ["Side Plank", "Pallof Press or Heel Taps", "Hollow Body Hold", "Mountain Climbers"], C = ["Lying Leg Raise", "Russian Twist", "Plank Shoulder Taps", "V-Up or Crunch Toe Reach"];
      var map = [
        { t: "Core A", rest: false, d: sets + " rounds: " + A.join(", ") + " — " + sec + "s each, 15s rest." },
        { t: "Steps + mobility", rest: false, d: (8000 + w * 500) + " steps, plus 10 min hip & thoracic mobility." },
        { t: "Core B", rest: false, d: sets + " rounds: " + B.join(", ") + " — " + sec + "s each (holds " + hold + "s)." },
        { t: "Rest", rest: true, d: "Full rest. Hit your protein target and sleep 7–9 hours." },
        { t: "Core C", rest: false, d: sets + " rounds: " + C.join(", ") + " — " + sec + "s each, 15s rest." },
        { t: "Full body + finisher", rest: false, d: "Any full-body strength session, then a 5-minute plank ladder finisher." },
        { t: w === 5 ? "Final test" : "Rest + check-in", rest: true, d: w === 5 ? "Retest plank & hollow hold, take final photos, submit your entry!" : "Log weight & waist, take progress photos, submit your weekly check-in." }
      ];
      return map[d];
    }
    var done = JSON.parse(store("ab6-ch") || "[]"), selDay = 1, cal = $("#chCal"), det = $("#chDay");
    var startEl = $("#chStart"); startEl.value = store("ab6-ch-start") || new Date().toISOString().slice(0, 10);
    startEl.addEventListener("change", function () { store("ab6-ch-start", startEl.value); draw(); });
    function draw() {
      var html = "";
      for (var i = 1; i <= 42; i++) { var p = dayPlan(i); html += '<button type="button" data-day="' + i + '" class="' + (done.indexOf(i) > -1 ? "done " : "") + (p.rest ? "rest" : "") + '" aria-label="Day ' + i + ': ' + p.t + '"><b>' + i + '</b><span>' + p.t + '</span></button>'; }
      cal.innerHTML = html;
      var pct = Math.round(done.length / 42 * 100), C = 2 * Math.PI * 62;
      $("#chRing").innerHTML = '<circle class="bg" cx="75" cy="75" r="62"/><circle class="fg" cx="75" cy="75" r="62" stroke-dasharray="' + C + '" stroke-dashoffset="' + (C * (1 - pct / 100)) + '"/><text x="75" y="86" text-anchor="middle">' + pct + '%</text>';
      var streak = 0; for (var k = 42; k >= 1; k--) { if (done.indexOf(k) > -1) streak++; else if (streak) break; }
      var entries = 0; for (var wk = 0; wk < 6; wk++) { var c = 0; for (var dd = 1; dd <= 7; dd++) if (done.indexOf(wk * 7 + dd) > -1) c++; if (c >= 5) entries++; }
      $("#chStats").innerHTML = '<div><b>' + done.length + '/42</b><span>Days done</span></div><div><b>' + streak + '</b><span>Current streak</span></div><div><b>' + entries + '</b><span>Prize-draw entries</span></div>';
      var today = Math.floor((new Date() - new Date(startEl.value)) / 864e5) + 1;
      $("#chToday").textContent = today >= 1 && today <= 42 ? "Today is Day " + today + " — " + dayPlan(today).t : today < 1 ? "Your challenge starts on " + fmtDate(new Date(startEl.value)) : "Challenge window complete — submit your final entry!";
      show(selDay);
      ch._entries = entries;
    }
    function show(day) {
      selDay = day; var p = dayPlan(day), w = Math.floor((day - 1) / 7), isDone = done.indexOf(day) > -1;
      det.innerHTML = '<div class="eyebrow">Week ' + (w + 1) + ' · ' + THEMES[w] + '</div><h3>Day ' + day + ': ' + p.t + '</h3><p class="muted">' + p.d + '</p><button class="btn ' + (isDone ? "btn-ghost" : "btn-primary") + ' btn-sm" data-toggle="' + day + '">' + (isDone ? "Mark as not done" : "✓ Mark Day " + day + " complete") + '</button> <a class="btn btn-dark btn-sm" href="workout-generator.html">Open timer</a>';
    }
    cal.addEventListener("click", function (e) { var b = e.target.closest("[data-day]"); if (b) show(+b.getAttribute("data-day")); });
    det.addEventListener("click", function (e) {
      var b = e.target.closest("[data-toggle]"); if (!b) return; var d2 = +b.getAttribute("data-toggle"), i = done.indexOf(d2);
      if (i > -1) done.splice(i, 1); else { done.push(d2); beep(1040, .2); }
      store("ab6-ch", JSON.stringify(done)); draw();
    });
    var rs = $("#chReset"); if (rs) rs.addEventListener("click", function () { if (confirm("Reset all challenge progress on this device?")) { done = []; store("ab6-ch", "[]"); draw(); } });
    var ci = $("#checkinForm"); if (ci) ci._extra = function () { return { days_completed: done.length + "/42", prize_entries: String(ch._entries || 0), start_date: startEl.value }; };
    draw();
  }

  /* ======================= Find-My-Abs-Plan quiz funnel ======================= */
  var qz = $("#absQuiz");
  if (qz) {
    var plan = null;
    var gate = $("#planGate");
    function makePlan() {
      var sex = val(qz, "sex"), goal = val(qz, "goal"), lvl = +val(qz, "level"), eqs = vals(qz, "eq"), mins = +val(qz, "minutes"), days = +val(qz, "days"), shape = val(qz, "shape");
      var names = { 1: "AB6 Foundation", 2: "AB6 Builder", 3: "AB6 Shred Pro" };
      var bfEst = { lean: [12, 20], athletic: [15, 23], average: [22, 30], above: [30, 38] }[shape][sex === "f" ? 1 : 0], tgt = sex === "f" ? 18 : 11;
      var weeks = bfEst <= tgt ? 0 : Math.ceil(Math.log((1 - bfEst / 100) / (1 - tgt / 100)) / Math.log(1 - 0.0075));
      var coreDays = Math.min(days, lvl === 1 ? 3 : 4), focus = goal === "perf" ? "deep" : "";
      var A = balanced(lvl, eqs, focus, 4, 11), B = balanced(lvl, eqs, focus || "obliques", 4, 29);
      var sets = { 1: "2–3 × 10–12 reps or 30s", 2: "3 × 12–15 reps or 40s", 3: "3–4 × 8–12 weighted reps or 45s" }[lvl];
      var C = [0, 2, 4, 5].slice(0, coreDays), extra = [1, 3, 5, 6].filter(function (x) { return C.indexOf(x) < 0; }).slice(0, Math.max(0, days - coreDays));
      var schedule = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].map(function (d, i) {
        var ci = C.indexOf(i);
        if (ci > -1) return [d, (ci % 2 ? "Core B" : "Core A") + " (" + Math.min(mins, 20) + " min)" + (mins > 20 ? " + full-body strength" : "")];
        return [d, extra.indexOf(i) > -1 ? "Full-body strength or cardio" : "Rest + 8–10k steps"];
      });
      var prog = [["1", "Learn form. " + sets.split("×")[0] + " sets, leave 3 reps in reserve.", "Plank " + (20 + lvl * 10) + "s"], ["2", "Add 1 set or 5s per exercise.", "Plank " + (30 + lvl * 10) + "s"], ["3", "Slow eccentrics (3-second lowering).", "Side plank " + (20 + lvl * 10) + "s/side"], ["4", "Deload: same exercises, 1 fewer set. Retest plank.", "Retest"], ["5", "Harder variations (see library) or add load.", "Hollow " + (15 + lvl * 10) + "s"], ["6", "Peak: max quality reps, then retest everything & photo check-in.", "Final test"]];
      plan = { name: names[lvl], weeks: weeks, bfEst: bfEst, tgt: tgt, A: A, B: B, sets: sets, schedule: schedule, prog: prog, goal: goal };
      var exList = function (L) { return '<ol class="plan-list">' + L.map(function (x) { return '<li><div><b>' + x.name + '</b><div class="small muted">' + sets + ' — ' + x.cue + '</div></div></li>'; }).join("") + "</ol>"; };
      $("#planName").textContent = plan.name;
      $("#planSummary").innerHTML = '<div class="kv"><div><b>' + coreDays + '×/week</b><span>Core sessions</span></div><div><b>' + Math.min(mins, 20) + ' min</b><span>Per core session</span></div><div><b>~' + bfEst + '%</b><span>Rough body-fat guess</span></div><div><b>' + (weeks ? weeks + " wks" : "Now") + '</b><span>Est. to ~' + tgt + '% (0.75%/wk)</span></div></div>' +
        '<h3 style="margin-top:22px">Your week</h3><div class="table-wrap"><table><tbody>' + schedule.map(function (r) { return "<tr><td><b>" + r[0] + "</b></td><td>" + r[1] + "</td></tr>"; }).join("") + '</tbody></table></div>' +
        '<h3 style="margin-top:22px">Core A — Week 1</h3>' + exList(A) +
        '<p class="small muted">Nutrition matters more than any crunch: get your exact calorie and protein targets with the <a href="macro-calculator.html">macro calculator</a>.</p>';
      $("#planFull").innerHTML = '<h3>Core B</h3>' + exList(B) + '<h3 style="margin-top:22px">6-week progression</h3><div class="table-wrap"><table><thead><tr><th>Week</th><th>Focus</th><th>Test</th></tr></thead><tbody>' + prog.map(function (r) { return "<tr><td>" + r[0] + "</td><td>" + r[1] + "</td><td>" + r[2] + "</td></tr>"; }).join("") + '</tbody></table></div>' +
        '<ul class="ticks" style="margin-top:20px"><li>Protein: ~1.6–2.2 g per kg of body weight daily.</li><li>Steps: 8,000–10,000 a day — the easiest fat-loss lever.</li><li>Sleep: 7–9 hours. Short sleep shifts weight loss away from fat.</li><li>Track waist at the navel weekly — it moves before the scale does.</li></ul>' +
        '<div style="display:flex;gap:10px;flex-wrap:wrap" class="no-print"><button class="btn btn-primary" onclick="window.print()">🖨 Print / save as PDF</button><a class="btn btn-ghost" href="challenge.html">Start the 6-week challenge</a><a class="btn btn-ghost" href="coaching.html">Get a coach</a></div>';
      $("#quizResult").hidden = false; $("#quizSteps").hidden = true;
      if (store("ab6-lead")) unlock();
      $("#quizResult").scrollIntoView({ behavior: "smooth" });
    }
    function unlock() { $("#planFull").hidden = false; gate.hidden = true; }
    $("#quizFinish").addEventListener("click", function () { var st = $(".step.on", qz); var ok = true; $$("input,select", st).forEach(function (el) { if (ok && !el.checkValidity()) { el.reportValidity(); ok = false; } }); if (ok) makePlan(); });
    var gf = $("#gateForm");
    gf._extra = function () {
      return { quiz_sex: val(qz, "sex"), quiz_goal: val(qz, "goal"), quiz_level: val(qz, "level"), quiz_equipment: vals(qz, "eq").join(", ") || "bodyweight", quiz_minutes: val(qz, "minutes"), quiz_days: val(qz, "days"), quiz_shape: val(qz, "shape"), plan: plan && plan.name, est_weeks: plan && String(plan.weeks) };
    };
    gf.addEventListener("ab6:sent", unlock);
    $("#quizRestart").addEventListener("click", function () { $("#quizResult").hidden = true; $("#quizSteps").hidden = false; });
  }
})();
