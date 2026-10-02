# -*- coding: utf-8 -*-
"""בונה את כל עמודי ה-wireframe לתיקיית השורש של הפרויקט. הרצה: python _build/build.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from lib import page
import pages_a as A
import pages_b as B
from pages_map import wf_map

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

EX_NOTE = "חלק גדול מהתוכן בעמוד זה נוצר לדוגמה"

PAGES = [
    ("index.html", "דף הבית", A.home, None, None),
    ("services.html", "שירותים", A.services, "services.html", None),
    ("service.html", "פיתוח פלטפורמות", A.service, "services.html", None),
    ("industries.html", "תחומי פעילות", A.industries, "industries.html", "התחומים עצמם הוצעו לצורך ה-wireframe"),
    ("industry.html", "eCommerce ומסחר", A.industry, "industries.html", None),
    ("projects.html", "פרויקטים", B.projects, "projects.html", None),
    ("project.html", "Novidea × Finext", B.project, "projects.html", None),
    ("insights.html", "תובנות", B.insights, "insights.html", "כל התוכן בעמוד זה לדוגמה (אין בלוג כרגע)"),
    ("article.html", "מאמר", B.article, "insights.html", "המאמר לדוגמה; הפסקאות על תמחור מבוססות על ה-FAQ באתר הישן"),
    ("about.html", "אודות", B.about, "about.html", None),
    ("careers.html", "קריירה", B.careers, "careers.html", "כל תוכן הקריירה לדוגמה"),
    ("contact.html", "צור קשר", B.contact, "contact.html", None),
    ("not-included.html", "עמוד לא כלול", B.not_included, None, None),
    ("wireframe-map.html", "מפת wireframe", wf_map, None, None),
]

for fname, title, fn, active, note in PAGES:
    html = page(title, fn(), active=active, note=note)
    with open(os.path.join(ROOT, fname), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("wrote", fname, len(html))
