# -*- coding: utf-8 -*-
from lib import *


def home():
    # 1. HERO
    hero = f'''<section class="hero hero--home" data-wf="01 · Hero · full-viewport bg + H1 + byline + CTA">
  {ph_bg("תמונת / וידאו רקע · מסך מלא · 1920×1080 · מומלץ שהאלמנט הוויזואלי יישב בצד שמאל")}
  <div class="container"><div class="hero__content">
    <h1>Finext מייצרת מוצרים דיגיטליים שאלפי אנשים סומכים עליהם.</h1>
    <p class="hero__byline">אנחנו אנשי קוד. משלבים אפיון, עיצוב, פיתוח, דאטה ו‑AI כדי להפוך כל אתגר טכנולוגי לערך עסקי — בקנה מידה ארגוני.</p>
    {link_arrow("סיפורי הצלחה", "projects.html")}
  </div></div>
</section>'''

    # 2. WHAT WE DO — intro + 4 cards + link
    wwd = section(
        intro("מה אנחנו עושים", "אנחנו מפתחים פלטפורמות, פתרונות דאטה ו‑AI ותוכנה לארגונים, חנויות וסטארטאפים — מתוך מיקוד בערך עסקי.")
        + '<div class="grid grid--4 mt-l">' + "".join(card(t, "service.html") for t, _ in SERVICES) + '</div>'
        + '<div class="center link-row">' + link_arrow("כל השירותים שלנו", "services.html") + '</div>',
        "02 · What we do · eyebrow + H2 (centered) + 4 cards (7:9) + link")

    # 2b. ONGOING CARE
    care = section(
        f'''<div class="split split--wide-text">
  <div><span class="eyebrow">ליווי ותחזוקה</span>
    <h2>אנחנו לא נעלמים אחרי ההשקה. ליווי ותחזוקה שוטפים, בשותפות איתכם לאורך זמן.</h2>
    <p class="muted measure">שירות ותחזוקה הם לא תוספת אצלנו, אלא חלק מרכזי מהעבודה. את המוצר שבנינו ממשיכים לשמור, לשדרג ולפתח יחד.</p>
    <div class="mt-m">{link_arrow("תחזוקה ושירות", "service.html")}</div></div>
  {ph("4x3", "תמונה / איור ליווי ותחזוקה 4:3")}
</div>
<div class="mt-l">{care_points()}</div>''',
        "02b · Ongoing care & service · 2-col split + 3 points (Trello #5)", cls="section--surface")

    # 3. CLIENT LOGOS (dark band)
    logos = "".join(f'<div>{logo_ph(c)}</div>' for c in CLIENTS)
    clients = section(
        '<h2 style="max-width:18em">צוותי הפיתוח, הדאטה והמוצר שלנו עובדים בשיתוף פעולה עם חלק מהארגונים הנועזים והחדשניים בישראל.</h2>'
        f'<div class="logo-grid mt-l">{logos}</div>'
        '<div class="link-row">' + link_arrow("סיפורי ההצלחה שלנו", "projects.html") + '</div>',
        "03 · Client logos · dark band · H2 + logo grid ×18 + link", cls="section--dark")

    # (בלוק Waracle100 הוצא בכוונה — לא רלוונטי ל-Finext)

    # 4. INDUSTRIES
    ind = section(
        intro("תחומי פעילות", "אנחנו ממוקדים בארבעה תחומים מורכבים, שבהם הצוות שלנו יכול להשפיע הכי הרבה. " + EX)
        + '<div class="grid grid--4 mt-l">' + "".join(card(t, "industry.html", label="תמונת תחום 7:9", link="קראו עוד") for t, _ in INDUSTRIES) + '</div>'
        + '<div class="center link-row">' + link_arrow("התחומים שבחרנו", "industries.html") + '</div>',
        "04 · Industries · eyebrow + H2 + 4 cards (7:9) + link")

    # 5. CASE SLIDER (full width)
    slides = [
        ("Novidea", "אתר יציב ומאובטח לחברה חדשנית בביטוח"),
        ("חוות רום", "חנות אונליין ומערכת הזמנות לחווה אקולוגית דינמית"),
        ("Similari", "פלטפורמת תובנות מבוססת AI לעולם הפטנטים"),
    ]
    sl = "".join(f'''<div class="case-slide">
      {ph_bg("תמונת רקע של הפרויקט · 1920×1000")}
      <div class="container"><div class="case-slide__content">
        <span class="eyebrow">{c}</span><h2>{t}</h2>{link_arrow("לסיפור המלא", "project.html", "")}
      </div></div></div>''' for c, t in slides)
    slider = f'''<section class="case-slider" data-slider data-wf="05 · Case-study slider · full-width, 3 slides + dots">
  <div class="case-slider__track">{sl}</div>
  <div class="case-slider__dots" role="group" aria-label="שקופיות פרויקטים"></div>
</section>'''

    # 6. PROMO / WHITEPAPER
    promo = section(
        f'''<div class="promo">
  <div class="promo__media">{ph("3x4", "מוקאפ מכשיר + כריכת המדריך 3:4")}</div>
  <div>{logo_ph("לוגו / מותג המדריך")}
    <h2>קראו את המחקר שלנו על האופן שבו AI משנה את מחזור חיי פיתוח התוכנה. {EX}</h2>
    <a class="btn btn--light" href="not-included.html">להורדת המדריך החינמי</a></div>
</div>''',
        "06 · Promo / lead-magnet · dark band · device mock + H2 + download CTA", cls="section--dark2")

    # 7. CULTURE
    culture = section(
        f'''<div class="split">
  <div><span class="eyebrow">התרבות שלנו</span>
    <h2>פיתוח הוא התרבות שלנו. מאז 2010, לקוח מרוצה מספר לחבר — וכך גדלנו.</h2>
    {link_arrow("הכירו את הצוות", "about.html#team")}</div>
  {ph("4x5", "תמונת צוות / תרבות 4:5")}
</div>''',
        "07 · Culture · 2-col split (text + image)")

    # 8. INSIGHTS
    arts = [article_card(t) for t in ARTICLES[:4]]
    insights = f'''<div class="container"><hr class="rule"></div>
<section class="section" data-wf="08 · Insights · H2 + link + carousel ×4 article cards">
  <div class="container">{carousel(arts, f"<h2>תובנות מאנשי הקוד {EX}</h2>", link_arrow("כל התובנות", "insights.html"))}</div>
</section>'''

    return hero + wwd + care + clients + ind + slider + promo + culture + insights


def services():
    hero = f'''<section class="hero hero--small" data-wf="01 · Small hero · H1 + H2">
  <div class="container"><h1>שירותים</h1>
  <h2>אנחנו מאפיינים, מפתחים ומלווים מוצרים דיגיטליים — מהר יותר, חכם יותר, ביחד.</h2></div>
</section>'''
    rows = "".join(f'''<div class="alt-row">
  <div class="alt-row__text"><h2>{t}</h2><h3>{d}</h3>{link_arrow("גלו עוד", "service.html")}</div>
  {ph("4x3", "תמונת שירות 4:3")}
</div>''' for t, d in SERVICES)
    body = section(f'<div class="alt-rows">{rows}</div>', "02 · Alternating rows ×4 · text + image (flips each row)", cls="section--flush-top")
    care = section('<div class="section-title-row"><h2>בכל שירות: ליווי ותחזוקה שוטפים</h2></div><p class="muted measure">הליווי בשותפות לאורך זמן הוא חלק בלתי נפרד מכל שירות.</p><div class="mt-m">' + care_points() + '</div>',
                   "02b · Ongoing care callout · H2 + 3 points (Trello #5)")
    ind = section(
        '<div class="section-title-row"><h2>תחומי פעילות</h2></div>'
        '<div class="grid grid--4">' + "".join(card(t, "industry.html", label="תמונת תחום 7:9") for t, _ in INDUSTRIES) + '</div>',
        "03 · Industries · H2 + 4 cards", cls="section--surface")
    return hero + body + care + ind


def service():
    hero = f'''<section class="hero hero--media" data-wf="01 · Media hero · bg image + dark overlay + H1 + H2">
  {ph_bg("תמונת רקע · 1920×900 · עם כיסוי כהה")}
  <div class="container"><div class="hero__content">
    <h1>פיתוח פלטפורמות</h1>
    <h2>פלטפורמות Custom code שנבנות סביב הבעיה העסקית שלכם — ולא נדחסות לתוך תבנית מדף.</h2>
  </div></div>
</section>'''
    intro_p = section(
        '<p class="lede" style="max-width:34em">העסק שלכם אינו זהה לשום עסק אחר, ולכן גם האתר או המערכת שלכם חייבים להיות שונים. אנחנו מתחילים מהסוף: איזו חוויית משתמש תהיה שונה, ייחודית, זכירה ומבדלת עבור הלקוחות שלכם — ובונים לשם כך את הקוד.</p>',
        "02 · Intro paragraph (large type)", cls="section--tight")
    blocks_data = [
        ("אתרי תדמית Custom made", "אתר תדמית הוא חלון הראווה שלכם ברשת, ואין הזדמנות שנייה לרושם דיגיטלי ראשוני.",
         "אנחנו עוטפים את WordPress ב‑Custom code עם שימוש מזערי בתוספים — כדי שתקבלו אתר מהיר, יציב ומאובטח במיוחד."),
        ("פתרונות Web מורכבים ופורטלים", "פורטל עסקי, אתר פנים‑ארגוני או אפליקציית סלולר — בפיתוח מותאם ובממשקים ידידותיים למשתמש.",
         "המערכת קולטת, מאחסנת ומעבדת מידע, מתממשקת לבסיסי נתונים ולמערכות צד שלישי, ומתקשרת ברמת אבטחה גבוהה."),
        ("דפי נחיתה", "לדף נחיתה יש מטרה אחת: להפוך מי שהקליק על מודעה לליד.",
         "דפים בנויים בקוד, מדויקים ברמת הפיקסל, עם כפתורים סטיקי, Click to call ומעקב המרות — בדסקטופ ובמובייל."),
        ("אינטגרציות בין מערכות", "האתר והפלטפורמה לא חיים לבד — הם צריכים לדבר עם שאר הארגון.",
         "אנחנו מחברים בין הפלטפורמה לבין Priority, Salesforce, Monday ומערכות צד שלישי, כך שהמידע זורם בדיוק לאן שצריך."),
    ]
    nb = "".join(f'''<div class="num-block">
  {icon_ph("אייקון")}
  <div><span class="num-block__no">0{i}</span><h2>{t}</h2></div>
  <div><p>{p1}</p><p class="muted">{p2}</p>{link_arrow("בואו נדבר", "contact.html")}</div>
</div>''' for i, (t, p1, p2) in enumerate(blocks_data, 1))
    blocks = section(f'<div class="num-blocks">{nb}</div>', "03 · Numbered capability blocks ×4 · icon + no. + H2 + text + link", cls="section--flush-top")
    care = section('<div class="section-title-row"><h2>ואחרי ההשקה — ליווי ותחזוקה שוטפים</h2></div><div class="mt-m">' + care_points() + '</div>',
                   "03b · Ongoing care callout · H2 + 3 points (Trello #5)")
    who = section(
        carousel([case_card("Novidea", "אתר יציב ומאובטח לחברה חדשנית בביטוח"),
                  case_card("חוות רום", "חנות אונליין ומערכת הזמנות לחווה אקולוגית"),
                  case_card("Similari", "פלטפורמת תובנות מבוססת AI לעולם הפטנטים")],
                 "<h2>עם מי אנחנו עובדים</h2>", link_arrow("כל הפרויקטים", "projects.html"), three=True),
        "04 · Who we work with · case-study carousel ×3 (4:3)", cls="section--surface")
    tm = section(
        testimonial("״פיינקסט תכנתו לנו אתר שמתרגם מעולה את האיפיון והעיצוב איתו הגענו: כל כפתור, כל שורה, כל צבע וכל עמוד קיבלו את הקוד הנכון — באתר יציב, אמין ומתקדם – כיאה לחברתנו.״",
                    "ג׳ולי שפיקי · מנהלת שיווק ראשית, Novidea", logo="לוגו Novidea"),
        "05 · Client testimonial · centered quote + logo")
    ins = section(carousel([article_card(t) for t in ARTICLES[:4]], f"<h2>תובנות מאנשי הקוד {EX}</h2>", link_arrow("כל התובנות", "insights.html")),
                  "06 · Insights · carousel ×4", cls="section--surface")
    return hero + intro_p + blocks + care + who + tm + ins


def industries():
    hero = f'''<section class="hero hero--small" data-wf="01 · Small hero · H1 + H2">
  <div class="container"><h1>תחומי פעילות</h1>
  <h2>צוותי הפיתוח שלנו ממוקדים בארבעה תחומים מורכבים ותובעניים. {EX}</h2></div>
</section>'''
    rows = "".join(f'''<div class="alt-row">
  <div class="alt-row__text"><h2>{t}</h2><h3>{d}</h3>{link_arrow("קראו עוד", "industry.html")}</div>
  {ph("4x3", "תמונת תחום 4:3")}
</div>''' for t, d in INDUSTRIES)
    body = section(f'<div class="alt-rows">{rows}</div>', "02 · Alternating rows ×4 · text + image (flips each row)", cls="section--flush-top")
    who = section(
        carousel([case_card("Novidea", "אתר יציב ומאובטח לחברה חדשנית בביטוח"),
                  case_card("חוות רום", "חנות אונליין ומערכת הזמנות לחווה אקולוגית"),
                  case_card("Similari", "פלטפורמת תובנות מבוססת AI לעולם הפטנטים")],
                 "<h2>עם מי אנחנו עובדים</h2>", link_arrow("כל הפרויקטים", "projects.html"), three=True),
        "03 · Who we work with · case-study carousel ×3", cls="section--surface")
    return hero + body + who


def industry():
    hero = f'''<section class="hero hero--media" data-wf="01 · Media hero · bg + overlay + H1 + H2 + consultation CTA">
  {ph_bg("תמונת רקע · 1920×900 · עם כיסוי כהה")}
  <div class="container"><div class="hero__content">
    <h1>eCommerce ומסחר</h1>
    <h2>חנויות ומערכות מסחר מותאמות — מהרכישה הראשונה ועד אינטגרציות ERP וסליקה.</h2>
    <a class="btn btn--light" href="#contactForm">לתיאום שיחת ייעוץ ראשונית</a>
  </div></div>
</section>
<div class="logo-strip" data-wf="02 · Client logo strip · overlaps hero bottom">
  <div class="container"><div class="logo-strip__inner">{logo_ph("Gifted")}{logo_ph("חוות רום")}{logo_ph("לוגו לקוח")}{logo_ph("לוגו לקוח")}</div></div>
</div>'''
    intro_p = section(
        '<p class="lede" style="max-width:34em">מסחר אלקטרוני הוא לעיתים הזרוע השיווקית היחידה של העסק, ולכן הוא חייב להציע חוויית לקוח מושלמת בדסקטופ ובמובייל, מערכת ידידותית לניהול מלאי ומבצעים, כלי סליקה והפקת חשבוניות — ומעל הכול, אבטחת מידע ללא פשרות.</p>',
        "03 · Intro paragraph (large type)", cls="section--tight")
    data = [
        ("חנויות WooCommerce Custom", "חנויות B2B, B2C ו‑C2C מבוססות WooCommerce, מותאמות לצרכים המסחריים שלכם עד לרמת הפיקסל.",
         "שילוב קפדני של תוספים נבחרים בלבד, כדי לשמור על חנות מהירה ומאובטחת."),
        ("מערכות הזמנות ורישום", "מעבר לחנות: הזמנת אירועים, מקומות אירוח ורישום לפעילויות — בתוך אותה פלטפורמה.",
         "כך בנינו עבור חוות רום חנות אונליין ומערכת הזמנות שצוות החווה מתפעל בעצמו."),
        ("סליקה, חשבוניות ו‑ERP", "חיבור לכלי סליקה, הפקת חשבוניות ואינטגרציה למערכות כמו Priority.", "המידע זורם בין החנות למלאי ולהנהלת החשבונות — בלי עבודה ידנית."),
        ("ניהול מלאי ומבצעים", "ממשק ידידותי לניהול מלאי, החלפות מוצרים, עדכון מחירים ויצירת מבצעים.", "הצוות שלכם שולט בחנות, בלי להיות תלוי בנו לכל שינוי."),
        ("מהירות, SEO והמרה", "חנות שנטענת מהר ונגישה בכל מכשיר ממירה יותר ומדורגת גבוה יותר.", "אנחנו בודקים טעינה, נגישות והתאמה לדפדפנים לפני כל השקה."),
    ]
    nb = "".join(f'''<div class="num-block">
  {icon_ph("אייקון")}
  <div><span class="num-block__no">0{i}</span><h2>{t}</h2></div>
  <div><p>{a}</p><p class="muted">{b}</p>{link_arrow("גלו עוד", "not-included.html")}</div>
</div>''' for i, (t, a, b) in enumerate(data, 1))
    blocks = section(f'<div class="num-blocks">{nb}</div>', "04 · Numbered sub-topic blocks ×5 · icon + no. + H2 + text + link", cls="section--flush-top")
    who = section(
        carousel([case_card("Gifted", "אתר מכירות WooCommerce לייבוא ושיווק אופנה ממותגי אירופה"),
                  case_card("חוות רום", "חנות אונליין ומערכת הזמנות לחווה אקולוגית"),
                  case_card("PicUp", "אתר לפלטפורמה שמגדילה מכירות ומשפרת את חוויית הלקוח")],
                 "<h2>עם מי אנחנו עובדים</h2>", link_arrow("כל הפרויקטים", "projects.html"), three=True),
        "05 · Who we work with · case-study carousel ×3", cls="section--surface")
    form = section(f'''<div class="form-card" id="contactForm">
  <h2>בואו נעבוד יחד</h2>
  <p>נגדיר את הצוות הנכון לפיתוח המוצר הדיגיטלי שלכם. השאירו פרטים ונחזור אליכם בהקדם.</p>
  <form class="form" data-wf-form action="#">
    <div class="form__row"><div class="field"><label for="f-name">שם מלא*</label><input id="f-name" type="text" required></div>
      <div class="field"><label for="f-title">תפקיד*</label><input id="f-title" type="text" required></div></div>
    <div class="form__row"><div class="field"><label for="f-co">שם החברה*</label><input id="f-co" type="text" required></div>
      <div class="field"><label for="f-mail">אימייל*</label><input id="f-mail" type="email" required></div></div>
    <div class="field"><label for="f-msg">פרטים נוספים</label><textarea id="f-msg"></textarea></div>
    <button class="btn btn--light" type="submit">שלחו את הבקשה</button>
  </form>
  <div class="form-success"><h3>תודה, הבקשה נשלחה!</h3><p class="muted">העברנו אותה לצוות שלנו ונחזור אליכם בקרוב.</p></div>
</div>''', "06 · Lead form · dark card · 5 fields + success state", cls="section--flush-top")
    tm = section(
        testimonial("״השקענו המון בעיצוב והבנו מהר מאוד שכדי לממש את העיצוב אנחנו צריכים חברת קוד שתדע את העבודה. פנינו לפיינקסט ומצאנו אנשים שדואגים להכל: לתוצאה מעולה ולליווי מקצועי שדואג שנוכל לממש את הכוח של האתר לאורך זמן. תודה!״",
                    "יסמין אלון · מנהלת דיגיטל, חוות רום", logo="לוגו חוות רום"),
        "07 · Client testimonial · centered quote + logo")
    ins = section(carousel([article_card(t) for t in ARTICLES[:4]], f"<h2>תובנות מאנשי הקוד {EX}</h2>", link_arrow("כל התובנות", "insights.html")),
                  "08 · Insights · carousel ×4", cls="section--surface")
    return hero + intro_p + blocks + who + form + tm + ins
