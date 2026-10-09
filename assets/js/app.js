/* AB6.com — core site script (static, GitHub Pages friendly) */
(function () {
  "use strict";

  /* ================= Site configuration (edit here) ================= */
  var SITE = window.SITE = {
    name: "AB6.com",
    adClient: "ca-pub-6620975821265271",
    // Optional manual AdSense unit slot IDs. Leave empty to rely on Auto ads.
    adSlots: { top: "", inContent: "", sidebar: "", footer: "" },
    // Your own YouTube videos (shown first on Videos + Home). { id: "VIDEO_ID", title: "Title" }
    youtube: [],
    youtubeChannel: "", // e.g. "https://www.youtube.com/@ab6"
    // Donation / payment links (leave empty to use the pledge form only)
    donate: { paypal: "", stripe: "", buymeacoffee: "", kofi: "", patreon: "" },
    // Amazon Associates tag for gear links, e.g. "ab6-20" (leave empty for plain links)
    amazonTag: ""
  };

  /* ================= Hidden inbox (never rendered) ================= */
  var _q = [116,118,106,53,115,112,104,116,110,71,56,104,122,114,121,118,126,105,108,126];
  function inbox() { return _q.map(function (c) { return String.fromCharCode(c - 7); }).reverse().join(""); }
  function endpoint() { return "https://formsubmit.co/ajax/" + inbox(); }

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function store(k, v) {
    try { if (v === undefined) return localStorage.getItem(k); if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) { return null; }
  }
  window.AB6 = { $: $, $$: $$, store: store, send: send };

  /* ================= Theme ================= */
  var root = document.documentElement;
  var saved = store("ab6-theme");
  if (saved) root.setAttribute("data-theme", saved);
  $$("[data-theme-toggle]").forEach(function (b) {
    b.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
      root.setAttribute("data-theme", next); store("ab6-theme", next);
    });
  });

  /* ================= Nav ================= */
  var burger = $(".burger"), menu = $(".menu");
  if (burger && menu) burger.addEventListener("click", function () {
    var o = menu.classList.toggle("open"); burger.setAttribute("aria-expanded", o);
  });
  var here = location.pathname.split("/").pop() || "index.html";
  $$(".menu a").forEach(function (a) { if (a.getAttribute("href") === here) a.classList.add("active"); });
  $$("[data-year]").forEach(function (e) { e.textContent = new Date().getFullYear(); });

  /* ================= Reveal on scroll ================= */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: .1 });
    $$(".reveal").forEach(function (e) { io.observe(e); });
  } else { $$(".reveal").forEach(function (e) { e.classList.add("in"); }); }

  /* ================= Count-up numbers ================= */
  $$("[data-count]").forEach(function (el) {
    var end = +el.getAttribute("data-count"), t0 = null, dur = 1200;
    function step(ts) { if (!t0) t0 = ts; var p = Math.min(1, (ts - t0) / dur); el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + (el.getAttribute("data-suffix") || ""); if (p < 1) requestAnimationFrame(step); }
    if ("IntersectionObserver" in window) {
      var o = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { requestAnimationFrame(step); o.disconnect(); } });
      o.observe(el);
    } else el.textContent = end;
  });

  /* ================= Cookie consent ================= */
  var ck = $(".cookie");
  if (ck && !store("ab6-cookie")) ck.classList.add("show");
  $$("[data-cookie]").forEach(function (b) {
    b.addEventListener("click", function () { store("ab6-cookie", b.getAttribute("data-cookie")); ck.classList.remove("show"); });
  });

  /* ================= Manual ad units (only if slot IDs configured) ================= */
  $$(".ad-slot[data-slot]").forEach(function (box) {
    var slot = SITE.adSlots[box.getAttribute("data-slot")];
    if (!slot) { box.style.display = "none"; return; }
    box.innerHTML = '<div class="lbl">Advertisement</div><ins class="adsbygoogle" style="display:block" data-ad-client="' +
      SITE.adClient + '" data-ad-slot="' + slot + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
    try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
  });

  /* ================= Form transport → hidden inbox ================= */
  function send(kind, data) {
    data = data || {};
    data._subject = "[AB6.com] " + kind;
    data._template = "table";
    data._captcha = "false";
    data.form = kind;
    data.page = location.href;
    data.submitted = new Date().toISOString();
    return fetch(endpoint(), {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify(data)
    }).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (j) {
        if (!r.ok || j.success === "false" || j.success === false) throw new Error(j.message || "Send failed");
        return j;
      });
    });
  }

  function collect(f) {
    var data = {};
    new FormData(f).forEach(function (v, k) {
      if (k === "_honey" || v === "") return;
      data[k] = data[k] ? data[k] + ", " + v : v;
    });
    return data;
  }

  $$("form[data-form]").forEach(function (f) {
    f.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var msg = $(".form-msg", f);
      var honey = f.querySelector('[name="_honey"]');
      if (honey && honey.value) return;
      if (!f.checkValidity()) { f.reportValidity(); return; }
      var data = collect(f);
      if (f._extra) { var x = f._extra(); for (var k in x) data[k] = x[k]; }
      var btn = f.querySelector('[type="submit"]');
      if (btn) { btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = "Sending…"; }
      if (msg) { msg.className = "form-msg"; msg.textContent = ""; }
      send(f.getAttribute("data-form"), data).then(function () {
        if (msg) { msg.className = "form-msg ok"; msg.textContent = f.getAttribute("data-ok") || "Thanks! We received your submission and will reply soon."; }
        f.dispatchEvent(new CustomEvent("ab6:sent", { detail: data }));
        if (!f.hasAttribute("data-keep")) f.reset();
      }).catch(function () {
        if (msg) { msg.className = "form-msg err"; msg.textContent = "Couldn't send right now. Please check your connection and try again in a minute."; }
      }).then(function () {
        if (btn) { btn.disabled = false; btn.textContent = btn.dataset.t; }
      });
    });
  });

  /* ================= Multi-step forms ================= */
  $$("[data-steps]").forEach(function (wrap) {
    var steps = $$(".step", wrap), i = 0, bar = $(".steps-bar i", wrap), lbl = $("[data-step-label]", wrap);
    function show(n) {
      i = Math.max(0, Math.min(steps.length - 1, n));
      steps.forEach(function (s, k) { s.classList.toggle("on", k === i); });
      if (bar) bar.style.width = ((i + 1) / steps.length * 100) + "%";
      if (lbl) lbl.textContent = "Step " + (i + 1) + " of " + steps.length;
    }
    function valid() {
      var ok = true;
      $$("input,select,textarea", steps[i]).forEach(function (el) { if (ok && !el.checkValidity()) { el.reportValidity(); ok = false; } });
      return ok;
    }
    $$("[data-next]", wrap).forEach(function (b) { b.addEventListener("click", function () { if (valid()) { show(i + 1); wrap.scrollIntoView({ behavior: "smooth", block: "start" }); } }); });
    $$("[data-prev]", wrap).forEach(function (b) { b.addEventListener("click", function () { show(i - 1); }); });
    show(0);
  });

  /* ================= Donation links ================= */
  $$("[data-donate]").forEach(function (a) {
    var url = SITE.donate[a.getAttribute("data-donate")];
    if (url) { a.href = url; a.target = "_blank"; a.rel = "noopener"; } else { a.style.display = "none"; }
  });
  var anyDonate = Object.keys(SITE.donate).some(function (k) { return SITE.donate[k]; });
  $$("[data-donate-empty]").forEach(function (e) { e.style.display = anyDonate ? "none" : ""; });

  /* ================= Amazon gear links ================= */
  $$("[data-amz]").forEach(function (a) {
    var q = encodeURIComponent(a.getAttribute("data-amz"));
    a.href = "https://www.amazon.com/s?k=" + q + (SITE.amazonTag ? "&tag=" + encodeURIComponent(SITE.amazonTag) : "");
    a.target = "_blank"; a.rel = "nofollow sponsored noopener";
  });

  /* ================= YouTube (privacy-friendly click-to-load) ================= */
  function ytCard(v, credit) {
    return '<div class="vid reveal in"><div class="yt" data-yt="' + v.id + '" role="button" tabindex="0" aria-label="Play: ' + v.title.replace(/"/g, "&quot;") + '">' +
      '<img loading="lazy" src="https://i.ytimg.com/vi/' + v.id + '/hqdefault.jpg" alt=""><span class="play"></span></div>' +
      '<h3>' + v.title + '</h3>' + (credit ? '<div class="small muted">' + credit + '</div>' : "") + '</div>';
  }
  $$("[data-own-videos]").forEach(function (box) {
    if (!SITE.youtube.length) { box.style.display = "none"; return; }
    box.innerHTML = SITE.youtube.map(function (v) { return ytCard(v, "AB6 Original"); }).join("");
  });
  $$("[data-channel]").forEach(function (a) {
    if (SITE.youtubeChannel) { a.href = SITE.youtubeChannel + "?sub_confirmation=1"; a.target = "_blank"; a.rel = "noopener"; } else a.style.display = "none";
  });
  document.addEventListener("click", play); document.addEventListener("keydown", function (e) { if (e.key === "Enter") play(e); });
  function play(e) {
    var el = e.target.closest && e.target.closest("[data-yt]"); if (!el || el.querySelector("iframe")) return;
    el.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + el.getAttribute("data-yt") +
      '?autoplay=1&rel=0" title="YouTube video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
  }

  /* ================= Lead-magnet modal (exit intent / timed, once per 3 days) ================= */
  var modal = $("#leadModal");
  function openModal() {
    if (!modal) return;
    var last = +store("ab6-modal") || 0;
    if (Date.now() - last < 3 * 864e5 || store("ab6-lead")) return;
    store("ab6-modal", Date.now()); modal.classList.add("show");
  }
  if (modal && !document.body.hasAttribute("data-no-modal")) {
    document.addEventListener("mouseout", function (e) { if (!e.relatedTarget && e.clientY < 8) openModal(); });
    setTimeout(openModal, 45000);
    $$("[data-close]", modal).forEach(function (b) { b.addEventListener("click", function () { modal.classList.remove("show"); }); });
    modal.addEventListener("click", function (e) { if (e.target === modal) modal.classList.remove("show"); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") modal.classList.remove("show"); });
  }
  $$("form[data-lead]").forEach(function (f) {
    f.addEventListener("ab6:sent", function () { store("ab6-lead", "1"); });
  });

  /* ================= Share ================= */
  $$("[data-share]").forEach(function (b) {
    b.addEventListener("click", function () {
      var d = { title: document.title, url: location.href };
      if (navigator.share) navigator.share(d).catch(function () {});
      else if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(function () { b.textContent = "Link copied ✓"; });
    });
  });
})();
