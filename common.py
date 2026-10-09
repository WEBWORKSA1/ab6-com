"""Shared HTML snippets for AB6.com page modules."""

HP = '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'
MSG = '<div class="form-msg" role="status" aria-live="polite"></div>'
CONSENT = ('<label class="check"><input type="checkbox" name="consent" value="yes" required> '
           'I agree to be contacted about my request and accept the <a href="privacy.html">Privacy Policy</a>.</label>')

ICON = {
    "quiz": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 01-2 2H6a2 2 0 01-2-2V5a2 2 0 012-2h9"/></svg>',
    "fat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 3v9l6 4"/></svg>',
    "fire": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22c4 0 7-3 7-7 0-5-5-7-5-12-3 2-4 5-4 7-1-1-2-2-2-4-2 2-3 5-3 9 0 4 3 7 7 7z"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l2 2M9 2h6"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></svg>',
    "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19V5a2 2 0 012-2h13v16H6a2 2 0 00-2 2zm0 0a2 2 0 002 2h13"/></svg>',
    "cal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
    "play": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="3"/><path d="M10 9l5 3-5 3z"/></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/></svg>',
    "trophy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 01-10 0zM17 5h3v2a3 3 0 01-3 3M7 5H4v2a3 3 0 003 3"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.8 4.6a5.5 5.5 0 00-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 00-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 000-7.8z"/></svg>',
    "grid": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="3" width="7" height="5" rx="1.5"/><rect x="13" y="3" width="7" height="5" rx="1.5"/><rect x="4" y="10" width="7" height="5" rx="1.5"/><rect x="13" y="10" width="7" height="5" rx="1.5"/><rect x="4" y="17" width="7" height="4" rx="1.5"/><rect x="13" y="17" width="7" height="4" rx="1.5"/></svg>',
    "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="6" cy="12" r="3"/><circle cx="18" cy="12" r="3"/><path d="M9 12h6"/></svg>',
    "mega": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 11v2a1 1 0 001 1h3l6 5V5L7 10H4a1 1 0 00-1 1zM17 8a5 5 0 010 8"/></svg>',
    "brief": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 012-2h2a2 2 0 012 2v2"/></svg>',
}


def crumb(*items):
    parts = ['<a href="index.html">Home</a>'] + [f'<a href="{h}">{t}</a>' if h else t for h, t in items]
    return '<nav class="crumbs" aria-label="Breadcrumb">' + " / ".join(parts) + "</nav>"


def phero(eyebrow, h1, lead, crumbs=(), extra=""):
    return (f'<section class="phero"><div class="wrap">{crumb(*crumbs) if crumbs else ""}'
            f'<div class="eyebrow">{eyebrow}</div><h1>{h1}</h1><p class="lead">{lead}</p>{extra}</div></section>')


def ad(slot="inContent"):
    return f'<div class="ad-slot" data-slot="{slot}"></div>'


def faq(items):
    html = "".join(f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in items)
    schema = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q,
                              "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return html, schema


def band(title, text, href, label):
    return (f'<section class="section-tight"><div class="wrap"><div class="band reveal"><div><h2>{title}</h2><p>{text}</p></div>'
            f'<a class="btn" href="{href}">{label}</a></div></div></section>')


def card(href, icon, title, text, tag=""):
    t = f'<span class="badge-new">{tag}</span>' if tag else ""
    return f'<a class="card reveal" href="{href}">{t}<div class="ico">{ICON[icon]}</div><h3>{title}</h3><p class="muted small" style="margin:0">{text}</p></a>'


COACH_SIDE = ('<div class="card" style="border-color:var(--accent)"><div class="eyebrow">1-on-1 coaching</div><h3>Want results faster?</h3>'
              '<p class="small muted">Get matched with a certified coach for a free 15-minute consult. No obligation.</p>'
              '<a class="btn btn-primary btn-block" href="coaching.html">Get matched free →</a></div>')

QUIZ_SIDE = ('<div class="card"><div class="ico">' + ICON["quiz"] + '</div><h3>Your plan in 60 seconds</h3>'
             '<p class="small muted">Answer 7 quick questions and get a personalised 6-week abs plan.</p>'
             '<a class="btn btn-dark btn-block" href="abs-quiz.html">Take the quiz</a></div>')


def sidebar(*extra):
    return '<aside class="sidebar"><div class="sticky">' + QUIZ_SIDE + COACH_SIDE + ad("sidebar") + "".join(extra) + "</div></aside>"


def article(eyebrow, h1, lead, crumbs, toc, body, faqs=None, updated="2026-10-09", reviewed="AB6 Editorial Team"):
    """Long-form article wrapper with TOC, byline, sidebar, FAQ + schema."""
    toc_html = '<nav class="toc" aria-label="Contents"><b>On this page</b><ol>' + "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in toc) + "</ol></nav>"
    fq_html, fq_schema = faq(faqs) if faqs else ("", None)
    by = (f'<div class="byline"><span>By {reviewed}</span><span>Updated {updated}</span><span>Sources cited inline</span>'
          '<button class="btn btn-ghost btn-sm" data-share>Share</button></div>')
    html = (phero(eyebrow, h1, lead, crumbs, by) +
            f'<section><div class="wrap layout"><article class="prose">{toc_html}{body}'
            + (f'<h2 id="faq">Frequently asked questions</h2>{fq_html}' if faqs else "") +
            '<div class="callout blue small" style="margin-top:28px"><b>Health note:</b> This article is general education, not medical advice. '
            'Check with a qualified professional before starting a new diet or training plan, especially if you are pregnant, postpartum, injured or have a medical condition.</div>'
            f'</article>{sidebar()}</div></section>')
    schema = [{"@context": "https://schema.org", "@type": "Article", "headline": h1, "dateModified": updated,
               "author": {"@type": "Organization", "name": "AB6.com"}, "publisher": {"@type": "Organization", "name": "AB6.com"}}]
    if fq_schema:
        schema.append(fq_schema)
    return html, schema


def pubmed(q, label):
    return f'<a href="https://pubmed.ncbi.nlm.nih.gov/?term={q}" target="_blank" rel="noopener">{label}</a>'


VIDEOS = [
    ("AnYl6Nk9GOA", "10 Min Ab Workout — No Equipment", "Pamela Reif"),
    ("1919eTCoESo", "10 Min Abs — Abdominal &amp; Oblique Exercises", "Fitness Blender"),
    ("DHD1-2P94DI", "Intense 7-Minute Ab Workout (Follow Along)", "ATHLEAN-X"),
    ("2pLT-olgUJs", "Get Abs in 2 Weeks — Abs Challenge", "Chloe Ting"),
    ("8AAmaSOSyIA", "20 Min Total Core / Ab Workout (At Home)", "MadFit"),
    ("3p8EBPVZ2Iw", "6 Pack Abs for Beginners — Anywhere", "THENX"),
    ("YEfsRDnj3iA", "10 Min Ab Workout — Dumbbells or No Equipment", "HASfit"),
    ("vkKCVCZe474", "8 Min Abs Workout", "P4P Workouts"),
]


def video_cards(items):
    return "".join(
        f'<div class="vid reveal"><div class="yt" data-yt="{i}" role="button" tabindex="0" aria-label="Play video: {t}">'
        f'<img loading="lazy" src="https://i.ytimg.com/vi/{i}/hqdefault.jpg" alt="Video thumbnail: {t}"><span class="play"></span></div>'
        f'<h3>{t}</h3><div class="small muted">Creator: {b} · embedded from YouTube</div></div>' for i, t, b in items)
