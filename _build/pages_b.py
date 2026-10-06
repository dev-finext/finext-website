# -*- coding: utf-8 -*-
from lib import *

PROJECTS = {
    "Novidea": "אתר יציב ובטוח לחברה חדשנית בביטוח",
    "חוות רום": "אתר אפקטיבי לחווה אקולוגית: חנות אונליין ומערכת הזמנות",
    "Similari": "פלטפורמת תובנות ואנליטיקה מבוססת AI ו‑NLP לעולם הפטנטים",
    "מפה לשם": "פלטפורמה דיגיטלית מורכבת למשחק חוויתי דרך WhatsApp",
    "Verix": "פלטפורמת AI/ML לעולם הפארמה, עם אנימציות מותאמות בקוד",
    "Amai Proteins": "אתר לסטארט‑אפ שמייצר את החלבון הטבעי שעתיד להחליף את הסוכר",
    "InNegev": "אתר לחממה טכנולוגית, בשיתוף סטודיו ג׳ירף",
    "Twig Health": "אתר למוצר דיגיטלי שמרחיב את יכולות הצוות הקליני",
    "Gifted": "אתר מכירות WooCommerce לייבוא ושיווק אופנה ממותגי אירופה",
    "Heven Drones": "אתר לחברת רחפנים לנשיאת משאות כבדים",
    "PicUp": "אתר לפלטפורמה שמגדילה מכירות ומשפרת את חוויית הלקוח",
    "Wanda Fish": "אתר לסטארט‑אפ של דג מתורבת וברי קיימא",
    "NSO": "אתר החברה והבלוג הטכני",
}


def pcards(names, ratio="4x3"):
    r = ratio.replace("x", ":")
    return "".join(case_card(n, PROJECTS[n], ratio=ratio, label=f"תמונת פרויקט {r}") for n in names)


def projects():
    hero = '''<section class="hero hero--small" data-wf="01 · Small hero · H1 + H2">
  <div class="container"><h1>פרויקטים</h1>
  <h2>אנחנו נבחרים על ידי חברות חדשניות בתחומי המסחר, הביטוח, ההייטק והארגונים.</h2></div>
</section>'''
    quotes = [
        ("״כחברת חדשנות, פנינו לפיינקסט, כי העומק, הדיוק והיכולת להכיל אתר בסדר גודל שכזה — היה חייב להתבצע בידיים טובות. מרוצים וממליצים!!״", "אודי כהן · מנכ״ל, Similari"),
        ("״Finext בנתה את האתר החדש שלנו וממשיכה לתחזק אותו. הפרויקט התנהל בצורה חלקה והצוות היה מקצועי, בעל ידע ותענוג לעבוד איתו. ממליצים בחום!״", "ג׳ולי שפיקי · מנהלת שיווק ראשית, Novidea"),
        ("״יש לנו משחק דיגיטלי משוגע שמבוסס על טכנולוגיה. פנינו לפיינקסט שלקחו את העיצוב שלנו ונתנו לו מערכת דיגיטלית כוללת. וזה פשוט עובד. תודה רבה!״", "עופר לשם · מנכ״ל, בעלים ויזם, מפה לשם"),
    ]
    qs = [f'<div class="quote-card"><blockquote>{q}</blockquote><footer>{logo_ph("לוגו")}<span>{w}</span></footer></div>' for q, w in quotes]
    tm = section(carousel(qs, "<h2>מה הלקוחות אומרים</h2>", "", three=True),
                 "02 · Testimonial carousel ×3 · quote cards + logo", cls="section--surface")
    feat = section(
        '<div class="section-title-row"><h2>פרויקטים נבחרים</h2></div><div class="grid grid--2">'
        + pcards(["Novidea", "חוות רום", "Similari", "מפה לשם"], "16x9") + '</div>',
        "03 · Featured projects · 2×2 large cards (16:9)")

    def group(title, names, wf):
        return section('<div class="section-title-row"><h3>' + title + '</h3></div><div class="grid grid--3">' + pcards(names) + '</div>',
                       wf, cls="section--tight")
    groups = (
        group("eCommerce ומסחר " + EX, ["Gifted", "חוות רום"], "04 · Project group · H3 + grid ×3")
        + group("ביטוח ופינטק " + EX, ["Novidea"], "05 · Project group")
        + group("הייטק וסטארטאפים " + EX, ["Verix", "Similari", "Amai Proteins", "Twig Health", "PicUp", "Wanda Fish", "Heven Drones", "NSO"], "06 · Project group")
        + group("ארגונים ורשויות " + EX, ["InNegev", "מפה לשם"], "07 · Project group")
    )
    return hero + tm + feat + groups


def project():
    hero = '''<section class="hero hero--cream" data-wf="01 · Case hero · H1 (client × Finext) + H2 tagline">
  <div class="container"><h1>Novidea × Finext</h1>
  <h2 style="font-weight:400;margin-block-start:20px;max-width:24em">אתר יציב ובטוח לחברה חדשנית בביטוח</h2></div>
</section>
<section class="section--flush-top" data-wf="02 · Hero image · full-width 21:9">
  <div class="container" style="padding-block-start:var(--gap-lg)">''' + ph("21x9", "תמונת פתיחה של הפרויקט · 21:9") + '''</div>
</section>'''
    b1 = section(f'''<div class="case-body"><h3>הרקע</h3><div>
  <h2>חברה פורצת דרך שמציעה אוטומציה לחברות ביטוח, ואתר שצריך להתאים לה</h2>
  <p>נובידאה היא חברה פורצת דרך המציעה אפשרויות אוטומציה לחברות ביטוח. היא הגיעה אלינו עם איפיון ועיצוב מוכנים — ועם צורך באתר שמתרגם אותם במדויק.</p>
</div></div>''', "03 · Case body · label (H3) + H2 + text", cls="section--tight")
    b2 = section(f'''<div class="case-body"><h3>האתגר</h3><div>
  <h2>אתר וורדפרס שמתאים לדרך של החברה: מלא בידע, יעיל ואפקטיבי — ובעיקר בטוח</h2>
  <p>לנובידאה דרישות ייחודיות: גיבוי כפול בשני מקורות חיצוניים, עמידות גבוהה מול סיכוני פריצה, וסטנדרטים מחמירים בנושאי אבטחת האתר, אחסון התשתיות וניטור.</p>
  <p>מבחינה טכנולוגית נדרשו Custom post types, טקסונומיות, מבנה אדמין ומערכת ניהול מותאמים, Multisite והתאמת תוכן לגולש לפי זיהוי IP.</p>
</div></div>''', "04 · Case body · The challenge", cls="section--tight")
    img1 = '<section class="section--tight" data-wf="05 · Inline image · 16:9"><div class="container">' + ph("16x9", "תמונה מתוך הפרויקט · 16:9") + '</div></section>'
    b3 = section(f'''<div class="case-body"><h3>הפתרון</h3><div>
  <h2>בנינו את האתר בקוד Custom, בשלבים, עם אישור הלקוח לאורך הדרך</h2>
  <ol class="process-list">
    <li><strong>תכנות</strong>בנינו את האתר בוורדפרס לפי התרשים, האיפיון והעיצוב. התחלנו בעמודים הראשיים, ולאחר אישור המשכנו לקטגוריות ולשאר העמודים.</li>
    <li><strong>העברת התוכן</strong>דאגנו להעברה מסודרת של כל תכני האתר הישן לחדש.</li>
    <li><strong>QA כפול</strong>צוות ה‑QA שלנו סרק את האתר ותיקן, ואחריו הלקוח בדק ועלו שינויים ודיוקים.</li>
    <li><strong>שינויים תוך כדי תנועה</strong>נובידאה חברה דינמית, ולכן עלו דרישות חדשות שנפגשו עם המענה האג׳ילי והגמיש שלנו.</li>
    <li><strong>הדרכה וליווי</strong>הכנו מצגת הדרכה ייעודית לצוות, כי הזנת תוכן היא פעולה יומיומית באתר בסדר גודל כזה.</li>
  </ol>
</div></div>''', "06 · Case body · The solution + numbered process", cls="section--tight")
    img2 = '<section class="section--tight" data-wf="07 · Inline image · 16:9"><div class="container">' + ph("16x9", "תמונה מתוך הפרויקט · 16:9") + '</div></section>'
    b4 = section(f'''<div class="case-body"><h3>התוצאה</h3><div>
  <h2>אתר יציב, מאובטח וקל לתפעול — שהצוות של נובידאה מעדכן בעצמו</h2>
  <p>צוות החברה מעדכן ומתפעל את האתר בקלות תוך כדי ליווי שלנו, ולאתר גולשים רבים בפעילות ענפה.</p>
  <p>לפני כל השקה בדקנו שהאתר נטען במהירות, נגיש, קל לתפעול, קל לעריכה, מדויק עיצובית ומותאם לדפדפנים ולרזולוציות שונות.</p>
</div></div>''', "08 · Case body · The impact", cls="section--tight")
    stats = section('''<div class="stats stats--2">
  <div><span class="stat__num">2</span><span class="stat__label">מקורות גיבוי חיצוניים</span></div>
  <div><span class="stat__num">6</span><span class="stat__label">בדיקות איכות לפני כל השקה</span></div>
</div>''', "09 · Impact stats ×2 · big number + caption", cls="section--surface")
    band = '<section class="image-block" data-wf="10 · Full-width image band · dark overlay">' + ph_bg("תמונת רוחב מלא · 1920×600") + '</section>'
    tm = section(testimonial("״פיינקסט תכנתו לנו אתר שמתרגם מעולה את האיפיון והעיצוב איתו הגענו: כל כפתור, כל שורה, כל צבע וכל עמוד קיבלו את הקוד הנכון באתר יציב, אמין ומתקדם – כיאה לחברתנו.״",
                             "ג׳ולי שפיקי · מנהלת שיווק ראשית, Novidea", logo="לוגו Novidea"),
                 "11 · Client testimonial · dark band", cls="section--dark")
    more = section(carousel([case_card("חוות רום", PROJECTS["חוות רום"]), case_card("Similari", PROJECTS["Similari"]), case_card("מפה לשם", PROJECTS["מפה לשם"])],
                            "<h2>עוד פרויקטים</h2>", link_arrow("כל הפרויקטים", "projects.html"), three=True),
                   "12 · More projects · carousel ×3")
    return hero + b1 + b2 + img1 + b3 + img2 + b4 + stats + band + tm + more


def insights():
    hero = f'''<section class="hero hero--small" data-wf="01 · Landing hero · eyebrow + H1">
  <div class="container"><span class="eyebrow">תובנות</span><h1>רעיונות שמעוררים מחשבה, מאנשי הקוד {EX}</h1></div>
</section>'''
    latest = [article_card(t) for t in ARTICLES]
    s1 = section(carousel(latest, "<h3>התובנות האחרונות</h3>", ""), "02 · Latest insights · carousel ×6", cls="section--tight")

    def row(title, titles, wf):
        return section(carousel([article_card(t) for t in titles], f"<h3>{title}</h3>", link_arrow("הצגת הכול", "not-included.html")), wf, cls="section--tight")
    rows = (
        row("AI ודאטה", [ARTICLES[2], "NLP בפועל: איך מפיקים תובנות ממסמכים ופניות", "עוזרים חכמים שמחוברים לדאטה של הארגון", "אוטומציה של תהליכים: איפה כדאי להתחיל"], "03 · Category row · H3 + link + carousel ×4")
        + row("פיתוח ו‑WordPress", [ARTICLES[0], ARTICLES[3], ARTICLES[4], "Laravel או WordPress? איך בוחרים פלטפורמה"], "04 · Category row")
        + row("eCommerce", [ARTICLES[1], "חנות WooCommerce מהירה: חמש נקודות לבדיקה", "אינטגרציית ERP לחנות: מה חשוב לדעת", "סליקה והפקת חשבוניות בלי כאבי ראש"], "05 · Category row")
    )
    cats = section('<div class="section-title-row"><h3>כל הקטגוריות</h3></div><div class="chips">'
                   + "".join(f'<a href="not-included.html">{c}</a>' for c in ["AI ודאטה", "פיתוח", "WordPress", "eCommerce", "אבטחה", "ניהול ארגוני", "תחזוקה ואחסון", "חדשות Finext", "הכירו את הצוות"])
                   + '</div>', "06 · Category chips", cls="section--tight section--surface")
    return hero + s1 + rows + cats


def article():
    body = f'''<div class="container article" data-wf="01 · Article layout · main column + sticky aside">
  <div>
    <div class="article__meta"><h5>מאמר · פיתוח אתרים · 15 בספטמבר 2026</h5></div>
    <h1>כמה עולה פיתוח אתר? (רמז: כמה עולה מכונית?)</h1>
    <p class="article__lede">אחת השאלות שאנחנו שומעים הכי הרבה היא גם הכי קשה לענות עליה במשפט אחד. הנה ההסבר שלנו, בלי מילים גדולות.</p>
    {ph("16x9", "תמונת פתיחה למאמר · 16:9")}
    <div class="article__body mt-m">
      <p>כמה עולה מכונית? תלוי ביצרן, בדגם, בביצועים, ברמת הבטיחות ובטכנולוגיות המוטמעות בה. באופן דומה, אנחנו מתמחרים פיתוח אתרים לפי האפיון, קבצי העיצוב, כמות התבניות, מורכבות העמודים ועוד.</p>
      <h2>מה משפיע על המחיר</h2>
      <p>אתר תדמית עם חמישה עמודים וחנות אונליין עם אינטגרציית ERP הם שני מוצרים שונים לגמרי, גם אם מבחוץ שניהם ״אתר״. ככל שיש יותר תבניות עיצוב, יותר לוגיקה עסקית ויותר מערכות לחבר — כך גדלה העבודה.</p>
      {ph("16x9", "תמונה / איור בתוך המאמר · 16:9")}
      <h2>איפיון קודם לכול</h2>
      <p>בפיתוח של מערכות מורכבות ו/או תהליכי אינטגרציה אנחנו מבצעים אפיון מלא שמתומחר בנפרד. הוא חוסך הפתעות: כולם יודעים מה נבנה, באיזה סדר ומה ייחשב ״גמור״.</p>
      <blockquote>הצעת מחיר טובה היא לא מספר. היא הסבר ברור של מה נכלל, מה לא, ומה קורה כשהדרישות משתנות באמצע.</blockquote>
      <h2>שקיפות לאורך הדרך</h2>
      <p>כל פרויקט מלווה במנהל פרויקטים שנמצא בקשר עם הלקוח ופועל בצמוד ללוח זמנים שנקבע בתחילת הפיתוח. כך תמיד אפשר לדעת איפה אנחנו עומדים.</p>
      <h2>ומה אחרי ההשקה?</h2>
      <p>מחיר הפיתוח הוא רק חלק מהתמונה. כדאי לחשוב מראש גם על אחסון, גיבויים, ניטור ותחזוקה שוטפת, כדי שהאתר יישאר מהיר, מאובטח ומעודכן.</p>
    </div>
    <article class="next-card">{ph("4x3", "תמונה 4:3", "ph--flat")}
      <div><h5>המאמר הבא</h5><h3><a href="article.html" style="text-decoration:none">למה אנחנו כמעט לא משתמשים בתוספים ב‑WordPress</a></h3>{link_arrow("קראו עוד", "article.html")}</div></article>
  </div>
  <aside class="article__aside" aria-label="מידע נוסף">
    <div><h2>שתפו את המאמר</h2><div class="share"><a href="#" aria-label="LinkedIn">in</a><a href="#" aria-label="Facebook">f</a><a href="#" aria-label="WhatsApp">wa</a><a href="#" aria-label="העתקת קישור">⧉</a></div></div>
    <div><h2>הכותבים</h2><div class="author">{ph("1x1", "תמונה", "ph--round")}<div><strong>שם הכותב</strong><span>תפקיד · Finext</span></div></div></div>
    <div><h2>קשור</h2><div class="related-list">{article_card(ARTICLES[0])}{article_card(ARTICLES[3])}</div></div>
  </aside>
</div>'''
    return body


def about():
    hero = f'''<section class="hero hero--md" data-wf="01 · Medium hero · eyebrow + H1 + 3 images">
  <div class="container"><div class="hero__top">
    <div><span class="eyebrow">התרבות שלנו</span><h1>מקום שבו אנשי הקוד הטובים בתעשייה בונים עבודה שאפשר להיות גאים בה.</h1></div>
    <div class="hero__imgs">{ph("4x5", "תמונת צוות 4:5")}{ph("4x3", "תמונה 4:3")}{ph("4x3", "תמונה 4:3")}</div>
  </div></div>
</section>'''
    story = section(f'''<div class="split">
  <div><span class="eyebrow">הסיפור שלנו</span><h2>שיתוף פעולה אמיתי</h2>
    <p>מאז 2010 אנחנו בונים אתרים ופלטפורמות מבוססי קוד עבור ארגונים, מעצבים ועסקים מכל הגדלים. מה שהתחיל בצוות קטן בהוד השרון הפך לבית תוכנה שליווה אלפי פרויקטים דיגיטליים.</p>
    <p class="mt-s">לקוח מרוצה מספר לחבר אחד או שניים — ככה גדלנו להיות מי שאנחנו. אנחנו אנשי קוד, אבל דווקא נחמד לדבר איתנו.</p></div>
  {ph("4x3", "תמונת מייסדים / צוות 4:3")}
</div>''', "02 · Our story · split (text + image)", cls="section--bordered")
    vals_head = section('<span class="eyebrow">החזון והערכים</span><h2 style="max-width:22em;font-weight:400;font-size:clamp(1.625rem,1.1rem + 2vw,2.5rem)">טכנולוגיה טובה נמדדת בערך העסקי שהיא מייצרת — לא במספר השורות.</h2>',
                        "03 · Vision & values · eyebrow + H2", cls="section--tight", sid="values")
    vals = [("אבטחה כברירת מחדל", "כל שורת קוד נכתבת מתוך הנחה שמישהו ינסה לשבור אותה — הצפנה, בקרת גישה וניטור מהיום הראשון."),
            ("אספקה מבוססת AI", "כלי בינה מלאכותית מאיצים אותנו לאורך הדרך — אבל ההחלטות, האיפיון והאחריות נשארים אנושיים."),
            ("קוד Custom, לא תבניות מדף", "כל מערכת נבנית סביב הבעיה העסקית האמיתית שלכם, ולא נדחסת לתוך תבנית קיימת."),
            ("ליווי אנושי, גם אחרי ההשקה", "אותם אנשים שבנו את המערכת נשארים אתכם — אותו מספר טלפון, תמיכה 24/7, לאורך כל חיי המוצר.")]
    rows = "".join(f'<div class="feature-row">{ph("4x3", "תמונה 4:3")}<div><h2>{t}</h2><p class="muted">{d}</p></div></div>' for t, d in vals)
    vrows = section(f'<div class="feature-rows">{rows}</div>', "04 · Values rows ×4 · image + H3 + text (flips each row)", cls="section--flush-top")
    stack = section('<div class="section-title-row"><h2>טכנולוגיות שאנחנו עובדים איתן</h2></div><div class="logo-grid">'
                    + "".join(f'<div>{logo_ph(t)}</div>' for t in TECH) + '</div>',
                    "05 · Recognition / partners grid · logos ×12 (Waracle: awards badges)", cls="section--surface")
    nums = section(f'''<div class="section-title-row"><h2>אנשים. ניסיון. זמינות.</h2></div>
<p class="muted measure">צוות ותיק של אנשי קוד שמלווה ארגונים, עסקים ומעצבים — מהאפיון הראשון ועד הרבה אחרי ההשקה.</p>
<div class="stats mt-m"><div><span class="stat__num">5,936</span><span class="stat__label">פרויקטים דיגיטליים</span></div>
<div><span class="stat__num">17</span><span class="stat__label">שנות ניסיון</span></div>
<div><span class="stat__num">24/7</span><span class="stat__label">תמיכה אנושית</span></div></div>''',
                   "06 · Numbers strip · H2 + text + 3 stats (Waracle: People page)")
    team = section('<div class="section-title-row"><h2>הכירו את הצוות ' + EX + '</h2></div><div class="grid grid--4">'
                   + "".join(f'<div class="person">{ph("1x1", "תמונה 1:1")}<strong>שם מלא</strong><span>תפקיד</span></div>' for _ in range(8))
                   + '</div>', "07 · Team grid ×8 · photo + name + role", cls="section--surface", sid="team")
    return hero + story + vals_head + vrows + stack + nums + team


def contact():
    form = f'''<section class="section" style="padding-block-start:170px" data-wf="01 · Contact form · 5 fields + message + success state">
  <div class="container"><div style="max-width:760px;margin-inline:auto">
    <h1 style="font-size:var(--fs-h2)">ספרו לנו איך נוכל לעזור</h1>
    <div class="mt-m">
      <form class="form" data-wf-form action="#">
        <div class="form__row"><div class="field"><label for="c-first">שם פרטי*</label><input id="c-first" type="text" required></div>
          <div class="field"><label for="c-last">שם משפחה*</label><input id="c-last" type="text" required></div></div>
        <div class="form__row"><div class="field"><label for="c-co">חברה</label><input id="c-co" type="text"></div>
          <div class="field"><label for="c-mail">אימייל*</label><input id="c-mail" type="email" required></div></div>
        <div class="field"><label for="c-tel">טלפון*</label><input id="c-tel" type="tel" required></div>
        <div class="field"><label for="c-msg">איך נוכל לעזור?*</label><textarea id="c-msg" required></textarea></div>
        <p class="form__small">בשליחת הטופס אתם מסכימים ל<a href="not-included.html">מדיניות הפרטיות</a> שלנו.</p>
        <div><button class="btn" type="submit">שליחה</button></div>
      </form>
      <div class="form-success"><h3>ההודעה נשלחה</h3><p class="muted">תודה שפניתם! נחזור אליכם בהקדם. בינתיים אפשר להציץ ב<a href="projects.html">פרויקטים</a> שלנו וב<a href="insights.html">תובנות</a>.</p><div class="mt-m"><a class="btn btn--ghost" href="index.html">חזרה לדף הבית</a></div></div>
    </div>
  </div></div>
</section>'''
    office = f'''<section class="section section--dark" id="office" data-wf="02 · Office / location · address + map placeholder + photo carousel">
  <div class="container"><div class="location">
    <div><span class="eyebrow">המשרד שלנו</span><h2>Finext הוד השרון</h2>
      <dl><dt>טלפון</dt><dd><a href="tel:+97299556006"><bdi dir="ltr">09-9556006</bdi></a></dd>
        <dt>אימייל</dt><dd><a href="mailto:hi@finext.co.il">hi@finext.co.il</a></dd>
        <dt>WhatsApp</dt><dd><a href="https://wa.me/97299556006">שלחו הודעה</a></dd>
        <dt>שעות פעילות</dt><dd>א׳–ה׳ · 09:00–17:30 {EX}</dd></dl></div>
    <div>{ph("16x10", "מפה / תמונת המשרד · 16:10")}</div>
  </div></div>
</section>'''
    return form + office


def not_included():
    return '''<section class="hero hero--small" data-wf="Placeholder page">
  <div class="container" style="min-height:50vh"><h1>העמוד הזה לא נכלל בשלב ה-wireframe</h1>
  <h2 class="mt-s">סוג העמוד הזה (למשל מדיניות פרטיות, הצהרת נגישות או דף תת-שירות) לא נבנה בשלב הזה. הקישור נשמר כדי שהניווט יהיה שלם.</h2>
  <div class="mt-m"><a class="btn" href="index.html">חזרה לדף הבית</a> <a class="btn btn--ghost" href="wireframe-map.html">מפת ה-wireframe</a></div></div>
</section>'''
