/* ==========================================================================
   FINEXT WIREFRAME — מינימום התנהגויות כדי שה-wireframe ירגיש כמו אתר חי.
   בלי ספריות. אפשר להחליף בכל מימוש בשלב הפיתוח.
   ========================================================================== */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  function store(key, val) {
    try { if (val === undefined) { return window.localStorage.getItem(key); } window.localStorage.setItem(key, val); } catch (e) { /* storage may be blocked */ }
    return null;
  }

  /* ---------- תפריט overlay (המבורגר) ---------- */
  var toggle = $(".nav-toggle");
  var overlay = $(".nav-overlay");
  function setNav(open) {
    document.body.classList.toggle("nav-open", open);
    if (toggle) { toggle.setAttribute("aria-expanded", String(open)); toggle.setAttribute("aria-label", open ? "סגירת תפריט" : "פתיחת תפריט"); }
    if (overlay) { overlay.setAttribute("aria-hidden", String(!open)); }
  }
  if (toggle) { toggle.addEventListener("click", function () { setNav(!document.body.classList.contains("nav-open")); }); }
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") { setNav(false); } });
  $$(".nav-overlay a").forEach(function (a) { a.addEventListener("click", function () { setNav(false); }); });

  /* ---------- קרוסלות (scroll-snap + חצים) ---------- */
  $$("[data-carousel]").forEach(function (root) {
    var track = $(".carousel__track", root);
    if (!track) { return; }
    function step(dir) {
      var rtl = getComputedStyle(track).direction === "rtl";
      var item = track.firstElementChild;
      var w = item ? item.getBoundingClientRect().width + 24 : track.clientWidth;
      track.scrollBy({ left: (rtl ? -1 : 1) * dir * w, behavior: "smooth" });
    }
    $$("[data-dir]", root).forEach(function (b) { b.addEventListener("click", function () { step(Number(b.getAttribute("data-dir"))); }); });
  });

  /* ---------- סליידר מסך מלא עם נקודות (שקופיות פרויקט) ---------- */
  $$("[data-slider]").forEach(function (root) {
    var track = $(".case-slider__track", root);
    var dotsWrap = $(".case-slider__dots", root);
    if (!track || !dotsWrap) { return; }
    var slides = $$(".case-slide", track);
    slides.forEach(function (_, i) {
      var d = document.createElement("button");
      d.type = "button"; d.setAttribute("aria-label", "שקופית " + (i + 1));
      d.addEventListener("click", function () { slides[i].scrollIntoView({ behavior: "smooth", inline: "start", block: "nearest" }); });
      dotsWrap.appendChild(d);
    });
    function sync() {
      var idx = Math.round(Math.abs(track.scrollLeft) / track.clientWidth);
      $$("button", dotsWrap).forEach(function (d, i) { d.setAttribute("aria-current", String(i === idx)); });
    }
    track.addEventListener("scroll", function () { window.requestAnimationFrame(sync); });
    sync();
  });

  /* ---------- טפסים: בלי שליחה אמיתית, רק מצב "נשלח" ---------- */
  $$("form[data-wf-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var box = form.parentElement;
      var ok = $(".form-success", box);
      form.classList.add("is-hidden");
      if (ok) { ok.classList.add("is-visible"); ok.scrollIntoView({ behavior: "smooth", block: "center" }); }
    });
  });

  /* ---------- באנר עוגיות ---------- */
  var cookie = $(".cookie");
  if (cookie) {
    if (store("finext-wf-cookie") === "1") { cookie.hidden = true; }
    $$("button", cookie).forEach(function (b) { b.addEventListener("click", function () { cookie.hidden = true; store("finext-wf-cookie", "1"); }); });
  }

  /* ---------- הערות wireframe ---------- */
  var notesBtn = $("[data-wf-toggle]");
  function setNotes(on) {
    document.body.classList.toggle("wf-notes", on);
    if (notesBtn) { notesBtn.setAttribute("aria-pressed", String(on)); }
    store("finext-wf-notes", on ? "1" : "0");
  }
  setNotes(store("finext-wf-notes") !== "0");
  if (notesBtn) { notesBtn.addEventListener("click", function () { setNotes(!document.body.classList.contains("wf-notes")); }); }
})();
