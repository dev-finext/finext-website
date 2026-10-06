# -*- coding: utf-8 -*-
"""
מחולל ה-wireframe של Finext: רכיבים משותפים (header / footer / כרטיסים / קרוסלות).
הפלט הוא HTML סטטי. אחרי המסירה למעצב עורכים ישירות את קבצי ה-HTML.
"""

# ---------- תוכן משותף ----------
EX = '<span class="ex-tag" title="תוכן לדוגמה שנוצר עבור ה-wireframe — להחלפה">דוגמה</span>'

NAV = [
    ("שירותים", "services.html"),
    ("תחומי פעילות", "industries.html"),
    ("פרויקטים", "projects.html"),
    ("תובנות", "insights.html"),
    ("הכירו את הצוות", "about.html#team"),
    ("בואו נדבר", "contact.html"),
]

CLIENTS = ["Novidea", "Similari", "Verix", "Gifted", "חוות רום", "מפה לשם",
           "מדנס", "Elsight", "Prodalim", "Aerotour", "Summit", "We Ankor",
           "משינה", "Immopi", "Trifolium", "InNegev", "Amai Proteins", "Twig Health"]

TECH_GROUPS = [
    ("CMS ופלטפורמות אתרים", ["WordPress", "WooCommerce", "Laravel", "Shopify"]),
    ("תוספים ובילדרים של WordPress", ["ACF", "Elementor", "WPML", "LearnDash"]),
    ("Frontend", ["HTML/CSS/JS", "Bootstrap", "Tailwind"]),
    ("Backend, שפות ודאטה", ["PHP", "MySQL", "Python", "Node", "git"]),
    ("אחסון ותשתיות", ["Cloudways", "Nginx", "Apache", "Imunify"]),
    ("CDN, DNS ואבטחה", ["Cloudflare"]),
    ("גיבויים ואחסון קבצים", ["SnapShooter", "Backblaze B2"]),
    ("דיוור ושיווק", ["Mailchimp (סנכרון קמפיינים)", "Mailgun"]),
    ("SEO, פרסום ואנליטיקס", ["Semrush", "Google Search Console", "Google Analytics"]),
    ("עיצוב", ["Figma"]),
]

SERVICES = [
    ("פיתוח פלטפורמות", "פלטפורמות Custom code בקנה מידה ארגוני — מאתרי תדמית ועד פורטלים ומערכות Web מורכבות."),
    ("eCommerce ומסחר", "חנויות WooCommerce ומערכות מסחר מותאמות — מהרכישה הראשונה ועד אינטגרציות ERP וסליקה."),
    ("דאטה ו‑AI", "בינה מלאכותית, NLP ואוטומציה כשכבה פונקציונלית בתוך המוצר הדיגיטלי — לא כגימיק."),
    ("ניהול ארגוני ותחזוקה", "פורטלים פנים‑ארגוניים, אינטגרציות בין מערכות, אחסון ותחזוקה שוטפת עם ליווי אנושי 24/7."),
]

INDUSTRIES = [
    ("eCommerce ומסחר", "חנויות ומערכות הזמנות מותאמות מקצה לקצה — WooCommerce, סליקה ואינטגרציות."),
    ("ביטוח ופינטק", "פלטפורמות יציבות ומאובטחות לחברות שבהן אמינות ואבטחת מידע הן תנאי סף."),
    ("הייטק וסטארטאפים", "מוצרי AI, ביו ופארמה — אתרים ופלטפורמות שמסבירים טכנולוגיה מורכבת בפשטות."),
    ("ארגונים ורשויות", "פורטלים ארגוניים, חממות ומערכות מרובות הרשאות לגופים עסקיים וציבוריים."),
]

ARTICLES = [
    "למה אנחנו כמעט לא משתמשים בתוספים ב‑WordPress",
    "כמה עולה פיתוח אתר? (רמז: כמה עולה מכונית?)",
    "AI בתוך המוצר ולא כגימיק: ארבע דוגמאות שעובדות",
    "מה בודקים ב‑QA לפני השקה — ורשימת הבדיקות שלנו",
    "אתר Custom או תבנית מדף? מדריך החלטה למנהלי דיגיטל",
    "אבטחה כברירת מחדל: מה חייב להיות מהיום הראשון",
]


# ---------- אבני בניין ----------
def ph(ratio, label, extra_cls=""):
    """משבצת תמונה: ratio למשל '4x3'. הטקסט הוא רמז למעצב."""
    return (f'<div class="ph r-{ratio} {extra_cls}" role="img" aria-label="{label}">'
            f'<span class="ph__label">{label}</span></div>')


def ph_bg(label):
    return (f'<div class="ph ph--bg" role="img" aria-label="{label}">'
            f'<span class="ph__label">{label}</span></div>')


def logo_ph(text="לוגו לקוח"):
    return f'<span class="logo-ph">{text}</span>'


def icon_ph(text="אייקון"):
    return f'<span class="icon-ph" aria-hidden="true">{text}</span>'


def link_arrow(text, href, cls=""):
    return f'<a class="link-arrow {cls}" href="{href}">{text}</a>'


def card(title, href, ratio="7x9", label="תמונה 7:9", link="קראו עוד", center=True):
    c = "card card--center" if center else "card"
    return (f'<article class="{c}">{ph(ratio, label)}<h3>{title}</h3>'
            f'<a class="link-underline" href="{href}">{link}</a></article>')


def case_card(client, title, href="project.html", ratio="4x3", label="תמונת פרויקט 4:3"):
    return (f'<article class="card card--project"><a class="card__link" href="{href}">{ph(ratio, label)}</a>'
            f'<span class="meta">{client}</span>'
            f'<a class="card__link" href="{href}"><h3>{title}</h3></a></article>')


def article_card(title, href="article.html", label="תמונה 16:10", tag="מאמר"):
    return (f'<article class="card"><a class="card__link" href="{href}">{ph("16x10", label)}</a>'
            f'<h5>{tag}</h5><a class="card__link" href="{href}"><h3>{title}</h3></a></article>')


def carousel(items, head_html, link_html="", three=False):
    """קרוסלה אופקית (scroll-snap). head_html = כותרת הסקשן, link_html = קישור 'הכול'."""
    cls = "carousel carousel--3" if three else "carousel"
    lis = "".join(f'<div class="carousel__item">{i}</div>' for i in items)
    return (f'<div class="{cls}" data-carousel>'
            f'<div class="section-title-row">{head_html}'
            f'<div class="carousel__nav">{link_html}'
            f'<button type="button" class="carousel__btn" data-dir="-1" aria-label="הקודם">→</button>'
            f'<button type="button" class="carousel__btn" data-dir="1" aria-label="הבא">←</button></div></div>'
            f'<div class="carousel__track">{lis}</div></div>')


def section(inner, wf, cls="", container=True, sid=""):
    idattr = f' id="{sid}"' if sid else ""
    body = f'<div class="container">{inner}</div>' if container else inner
    return f'<section class="section {cls}" data-wf="{wf}"{idattr}>{body}</section>'


def intro(eyebrow, h2):
    return f'<div class="intro"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2></div>'


def testimonial(quote, who, logo="לוגו לקוח", ex=False, dark=False, heading="המלצת לקוח"):
    tag = f" {EX}" if ex else ""
    return (f'<div class="testimonial"><h3>{heading}</h3><blockquote>{quote}</blockquote>'
            f'<cite>{who}{tag}</cite>{logo_ph(logo)}</div>')


# ---------- Header / Overlay / Footer ----------
def header(active=None):
    items = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if active == h else ""}>{t}</a></li>' for t, h in NAV)
    return f'''<header class="site-header">
  <div class="container site-header__bar">
    <a class="logo" href="index.html" aria-label="Finext — לדף הבית">FINEXT <small>לוגו</small></a>
    <nav class="main-nav" aria-label="ניווט ראשי"><ul>{items}</ul></nav>
    <div class="site-header__actions">
      <button class="lang-switch" type="button" aria-label="Switch language to English" lang="en">EN</button>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-overlay" aria-label="פתיחת תפריט"><span></span><span></span></button>
    </div>
  </div>
</header>'''


def overlay():
    big = '<li><a href="index.html">דף הבית</a></li>' + "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in NAV)
    return f'''<div class="nav-overlay" id="nav-overlay" aria-hidden="true">
  <div class="nav-overlay__inner">
    <ul class="nav-overlay__list">{big}</ul>
    <div class="nav-overlay__groups">
      <div><strong>אודות</strong><ul><li><a href="about.html">הסיפור והערכים</a></li><li><a href="about.html#team">הכירו את הצוות</a></li></ul></div>
      <div><strong>תובנות</strong><ul><li><a href="insights.html">בלוג</a></li><li><a href="not-included.html">חדשות</a></li></ul></div>
      <div><strong>המשרד</strong><ul><li><a href="contact.html#office">הוד השרון</a></li><li><a href="tel:+97299556006"><bdi dir="ltr">09-9556006</bdi></a></li></ul></div>
    </div>
  </div>
</div>'''


def footer():
    return f'''<footer class="site-footer">
  <section class="footer-cta" data-wf="Footer CTA · headline + button + device image">
    <div class="container footer-cta__grid">
      <div>
        <h2>אנחנו עובדים עם מותגים ואנשים שאפתנים. אם זה אתם — בואו נדבר.</h2>
        <a class="btn" href="contact.html">צרו קשר</a>
      </div>
      {ph("4x3", "איור / מוקאפ מכשיר 4:3")}
    </div>
  </section>
  <div class="footer-main">
    <div class="container footer-main__grid">
      <div>
        <a class="logo" href="index.html" aria-label="Finext — לדף הבית">FINEXT <small>לוגו</small></a>
        <div class="badges" aria-label="תקנים ותעודות">{logo_ph("תו תקן / שותפות")}{logo_ph("תו תקן / שותפות")}{logo_ph("תו נגישות")} {EX}</div>
      </div>
      <div><h4>קישורים</h4><ul>
        <li><a href="services.html">שירותים</a></li><li><a href="industries.html">תחומי פעילות</a></li><li><a href="projects.html">פרויקטים</a></li>
        <li><a href="insights.html">תובנות</a></li><li><a href="about.html">אודות</a></li></ul></div>
      <div><h4>המשרד</h4><ul>
        <li><a href="tel:+97299556006"><bdi dir="ltr">09-9556006</bdi></a></li>
        <li><a href="mailto:hi@finext.co.il">hi@finext.co.il</a></li><li><a href="https://wa.me/97299556006">WhatsApp</a></li></ul></div>
    </div>
    <div class="footer-legal"><div class="container footer-legal__row">
      <span>© 2026 Finext · כל הזכויות שמורות</span>
      <ul><li><a href="not-included.html">מדיניות פרטיות</a></li><li><a href="not-included.html">עוגיות</a></li><li><a href="not-included.html">הצהרת נגישות</a></li><li><a href="not-included.html">תנאי שימוש</a></li></ul>
    </div></div>
  </div>
</footer>'''


def cookie():
    return '''<div class="cookie" role="dialog" aria-label="הסכמה לעוגיות">
  <strong>הפרטיות שלכם חשובה לנו</strong>
  <span>אנחנו משתמשים בעוגיות כדי לשפר את חוויית הגלישה, להציג תוכן מותאם ולנתח תנועה. בלחיצה על ״אישור הכול״ אתם מסכימים לשימוש בעוגיות.</span>
  <div class="cookie__btns"><button type="button">התאמה אישית</button><button type="button">דחיית הכול</button><button type="button" class="is-primary">אישור הכול</button></div>
</div>'''


def tools(note=None):
    n = f'<span class="wf-tools__note">{note}</span>' if note else ""
    return (f'<div class="wf-tools">{n}<a href="wireframe-map.html">WIREFRAME MAP</a>'
            f'<button type="button" data-wf-toggle aria-pressed="true">NOTES</button></div>')


def page(title, body, active=None, note=None):
    return f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title} · Finext (Wireframe)</title>
<link rel="stylesheet" href="assets/css/tokens.css">
<link rel="stylesheet" href="assets/css/wireframe.css">
</head>
<body class="wf-notes">
<a class="sr-only" href="#main">דלגו לתוכן הראשי</a>
{header(active)}
{overlay()}
<main id="main">
{body}
</main>
{footer()}
{cookie()}
{tools(note)}
<script src="assets/js/wireframe.js"></script>
</body>
</html>
'''
