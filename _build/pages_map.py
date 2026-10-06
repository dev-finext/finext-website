# -*- coding: utf-8 -*-
from lib import *

ROWS = [
    ("index.html", "דף הבית", "waracle.com/", "Hero מסך מלא · מה אנחנו עושים (4 כרטיסים) · לוגואים בבלוק כהה · תחומי פעילות (4 כרטיסים) · סליידר פרויקטים · פרומו למדריך · תרבות · קרוסלת תובנות · פוטר"),
    ("services.html", "שירותים (רשימה)", "waracle.com/what-we-do/", "Hero קטן · 4 שורות מתחלפות (טקסט+תמונה) · תחומי פעילות"),
    ("service.html", "דף שירות", "waracle.com/what-we-do/strategy-innovation/", "Hero מדיה · פסקת פתיחה · 4 בלוקים ממוספרים · קרוסלת פרויקטים · המלצה · תובנות"),
    ("industries.html", "תחומי פעילות (רשימה)", "waracle.com/industries/", "Hero קטן · 4 שורות מתחלפות · קרוסלת פרויקטים"),
    ("industry.html", "דף תחום", "waracle.com/industries/financial-services/", "Hero מדיה + CTA · סטריפ לוגואים · פתיחה · 5 בלוקים ממוספרים · פרויקטים · טופס ליד · המלצה · תובנות"),
    ("projects.html", "פרויקטים (רשימה)", "waracle.com/our-work/", "Hero קטן · קרוסלת המלצות · פרויקטים נבחרים (2×2) · קבוצות לפי תחום"),
    ("project.html", "דף פרויקט", "waracle.com/our-work/mylo-aegon/", "Hero · תמונה · רקע / אתגר / פתרון / תוצאה · מספרים · פס תמונה · המלצה · עוד פרויקטים"),
    ("insights.html", "תובנות (רשימה)", "waracle.com/insights/", "Hero · קרוסלת תובנות אחרונות · שורות לפי קטגוריה · צ׳יפים של קטגוריות"),
    ("article.html", "מאמר", "waracle.com/insights/…/ (פוסט)", "עמודה ראשית + Aside דביק (שיתוף, כותבים, קשור) · כרטיס ״הבא״"),
    ("about.html", "אודות", "waracle.com/about-us/ + about-us/people/", "Hero + 3 תמונות · סיפור · ערכים · לוגואים · מספרים · צוות"),
    ("careers.html", "קריירה", "waracle.com/careers/", "Hero + CTA · החיים אצלנו · פיד חברתי · ערכים (אקורדיון) · המלצות עובדים · שאלות נפוצות · מאגר מועמדים"),
    ("contact.html", "צור קשר + משרד", "waracle.com/contact/ + contact/london/", "טופס עם נושא · מצב ״נשלח״ · בלוק משרד עם מפה"),
]

NOT = [
    ("תתי-שירות / תתי-תחום (דפי נחיתה עם טופס)", "waracle.com/what-we-do/…/product-discovery/ · industries/…/retail-banking/"),
    ("משרות פתוחות + דף משרה", "waracle.com/careers/open-roles/…"),
    ("דפי משנה של אודות: ערכים, אנשים", "waracle.com/about-us/our-values/ · about-us/people/ (הערכים והצוות נכנסו בתוך דף האודות)"),
    ("עמוד קטגוריית תובנות", "waracle.com/insights/artificial-intelligence/"),
    ("אירועים", "waracle.com/events/"),
    ("דפי משרד נפרדים", "waracle.com/contact/london/ (נכנס בתוך צור קשר, כי ל‑Finext משרד אחד)"),
    ("דפי מדיניות: פרטיות, עוגיות, נגישות, תנאי שימוש", "waracle.com/privacy-policy/ ועוד"),
]


def wf_map():
    rows = "".join(f'<tr><td><a href="{h}">{t}</a></td><td dir="ltr" style="text-align:start">{w}</td><td>{c}</td></tr>' for h, t, w, c in ROWS)
    nots = "".join(f'<tr><td>{a}</td><td dir="ltr" style="text-align:start">{b}</td></tr>' for a, b in NOT)
    return f'''<section class="section" style="padding-block-start:150px">
  <div class="container">
    <span class="eyebrow">Finext · Wireframe</span>
    <h1>מפת ה‑wireframe</h1>
    <p class="lede muted mt-s measure">מבנה האתר החדש של Finext, בנוי על המבנה של waracle.com. אפור בלבד, בלי תמונות, בעברית RTL ורספונסיבי. המעצב מוסיף צבעים, טיפוגרפיה ותמונות.</p>

    <h2 class="mt-l">איך עובדים עם זה</h2>
    <div class="grid grid--3 mt-m">
      <div class="stack"><h3>צבעים וטיפוגרפיה</h3><p class="muted">כל המשתנים ב‑<code dir="ltr">assets/css/tokens.css</code>: צבעים, פונטים, גדלי כותרות, רוחב קונטיינר ומרווחים. החלפה שם משנה את כל האתר.</p></div>
      <div class="stack"><h3>תמונות</h3><p class="muted">כל משבצת אפורה עם X היא תמונה. הטקסט שעליה הוא יחס הגובה‑רוחב והרמז למעצב. מחליפים את ה‑<code dir="ltr">div.ph</code> ב‑<code dir="ltr">img</code> או ברקע. ל‑<code dir="ltr">.ph--bg</code> (רקעי hero) יש יחס חופשי.</p></div>
      <div class="stack"><h3>הערות wireframe</h3><p class="muted">הכפתור הצף <code dir="ltr">NOTES</code> מדליק ומכבה שתי שכבות: תוויות רכיב (למשל <code dir="ltr">03 · Client logos</code>) ותגיות <span class="ex-tag" style="display:inline-block">דוגמה</span> על תוכן שנוצר לצורך ה‑wireframe. את הבלוק הזה אפשר למחוק מ‑CSS במעבר לפרודקשן.</p></div>
    </div>

    <h2 class="mt-l">העמודים</h2>
    <div style="overflow-x:auto" class="mt-m"><table class="map-table"><thead><tr><th>עמוד</th><th>מקור ב‑Waracle</th><th>רכיבים לפי סדר</th></tr></thead><tbody>{rows}</tbody></table></div>

    <h2 class="mt-l">סוגי עמודים של Waracle שלא נבנו</h2>
    <p class="muted mt-s">קישורים אליהם מובילים ל‑<a href="not-included.html">not-included.html</a>.</p>
    <div style="overflow-x:auto" class="mt-m"><table class="map-table"><thead><tr><th>סוג עמוד</th><th>מקור ב‑Waracle</th></tr></thead><tbody>{nots}</tbody></table></div>

    <h2 class="mt-l">התנהגויות שנכללו</h2>
    <ul class="stack muted mt-s" style="list-style:disc;padding-inline-start:20px">
      <li>תפריט המבורגר במסך מלא, עם רשימה גדולה וארבע קבוצות קישורים (נפתח מהעיגול בפינה, נסגר ב‑Esc).</li>
      <li>קרוסלות עם חצים (גלילה אופקית), סליידר פרויקטים במסך מלא עם נקודות.</li>
      <li>אקורדיון (ערכים, שאלות נפוצות), טפסים עם מצב ״נשלח״ (לא נשלח דבר בפועל), באנר עוגיות.</li>
      <li>אנימציות הכניסה של Waracle (fade‑in של כותרות, אנימציית קו מתחת לקישורים) לא נבנו. ההחלטה עליהן בשלב העיצוב.</li>
    </ul>
  </div>
</section>'''
