#!/usr/bin/env python3
"""Heuristischer Scan auf typische KI-Website-Muster im Quellcode.

Aufruf:
    python3 anti_ai_scan.py <projektordner> [--max-hits 8] [--json]

Jeder Treffer ist ein Prüfauftrag, kein Fehler. Ist ein Muster begründet
(z. B. nummerierter Ablauf), bleibt es. Der Exit-Code ist immer 0.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict

SOURCE_EXT = {
    ".html", ".htm", ".jsx", ".tsx", ".js", ".ts", ".mjs", ".vue", ".svelte",
    ".astro", ".css", ".scss", ".sass", ".less", ".php", ".twig", ".liquid",
    ".njk", ".hbs", ".erb", ".md", ".mdx", ".json", ".yaml", ".yml",
}
SKIP_DIRS = {
    "node_modules", ".git", ".next", ".nuxt", ".svelte-kit", ".astro", "dist",
    "build", "out", ".output", ".vercel", ".turbo", ".cache", "coverage",
    "vendor", ".claude",
}
SKIP_FILES = {"package-lock.json", "pnpm-lock.yaml", "yarn.lock", "package.json", "tsconfig.json"}
TEXT_ONLY_EXT = {".md", ".mdx", ".json", ".yaml", ".yml"}  # nur auf Texte prüfen
SMALL_DOT_RE = re.compile(r"\b(h|size)-(0\.5|1|1\.5|2|2\.5|3|3\.5|4)\b")
MAX_LINE = 600  # längere Zeilen sind meist minifiziert

I = re.IGNORECASE

# (kategorie, muster-id, regex, hinweis, nur_in_erweiterungen | None)
RULES: list[tuple[str, str, re.Pattern, str, set[str] | None]] = [
    # A Deko-Linien
    ("A Deko-Linie", "tw-line", re.compile(r"\b(h-px|h-\[(1|2)px\]|h-0\.5)\b[^\"'`]*\bw-(\d{1,2}|\[\d+px\])\b|\bw-(\d{1,2}|\[\d+px\])\b[^\"'`]*\b(h-px|h-\[(1|2)px\]|h-0\.5)\b"),
     "Kleine horizontale Linie, oft vor Eyebrow-Labels. Teil eines echten Systems?", None),
    ("A Deko-Linie", "text-dash", re.compile(r"(>|[\"'`])\s*(—|–|--+)\s+[A-ZÄÖÜ][A-ZÄÖÜa-zäöüß ]{2,}"),
     "Gedankenstrich vor Label/Titel („— ÜBER UNS“).", None),
    ("A Deko-Linie", "eyebrow", re.compile(r"\buppercase\b[^\"'`]*\btracking-(\[0\.[2-9]|widest)|\btracking-(\[0\.[2-9]|widest)[^\"'`]*\buppercase\b"),
     "Eyebrow-Label in Versalien mit sehr weiter Laufweite. Braucht es das Label?", None),
    # E Nummerierung
    ("E Nummerierung", "pad", re.compile(r"padStart\(\s*2\s*,\s*[\"']0[\"']\s*\)"),
     "Automatische 01/02/03-Nummerierung. Ist die Reihenfolge inhaltlich relevant?", None),
    ("E Nummerierung", "literal", re.compile(r"(>|[\"'`])\s*0[1-9]\s*(\.|/)?\s*(<|[\"'`])"),
     "Literal „01“, „02“ … als Text.", None),
    # F Rundungen
    ("F Rundungen", "tw-round", re.compile(r"\brounded-(full|3xl|\[(2[4-9]|[3-9]\d|\d{3,})px\])"),
     "Pille oder sehr großer Radius. Bewusst und konsistent?", None),
    ("F Rundungen", "css-round", re.compile(r"border-radius\s*:\s*(9{3,}|[3-9]\d|[1-9]\d{2,})(px|rem)?|border-radius\s*:\s*(2|3)(\.\d+)?rem", I),
     "Sehr großer border-radius.", {".css", ".scss", ".sass", ".less", ".vue", ".svelte", ".astro", ".html", ".htm"}),
    # G Schatten
    ("G Schatten", "tw-shadow", re.compile(r"\bshadow-(md|lg|xl|2xl|\[)"),
     "Schatten. Schwebt das Element wirklich (Dropdown, Modal, Sticky)?", None),
    ("G Schatten", "css-shadow", re.compile(r"box-shadow\s*:(?!\s*none)", I),
     "box-shadow. Schwebt das Element wirklich?", {".css", ".scss", ".sass", ".less", ".vue", ".svelte", ".astro", ".html", ".htm"}),
    # H Verläufe / Glow
    ("H Verlauf/Glow", "tw-gradient", re.compile(r"\bbg-(gradient-to|linear-to|radial|conic)-"),
     "Verlauf. Kommt er aus der Marke?", None),
    ("H Verlauf/Glow", "ai-colors", re.compile(r"\b(from|via|to)-(violet|purple|fuchsia|indigo|pink)-\d{2,3}"),
     "Lila/Pink-Verlaufsfarbe, das typische KI-Farbschema.", None),
    ("H Verlauf/Glow", "css-gradient", re.compile(r"(linear|radial|conic)-gradient\(", I),
     "CSS-Verlauf. Markenbezug? (Bild-Overlays zur Lesbarkeit sind ok.)", None),
    ("H Verlauf/Glow", "glow", re.compile(r"\bblur-(2xl|3xl|\[\d{2,}px\])\b|\bbg-clip-text\b|\bdrop-shadow-\[0_0"),
     "Glow-Blob, Verlaufstext oder Neon-Effekt.", None),
    # K Icons
    ("K Icons", "icon-badge", re.compile(r"\b(rounded-(full|xl|2xl|lg))\b[^\"'`]*\b(h|size)-(1[0-6]|\d)\b[^\"'`]*\bw-(1[0-6]|\d)\b[^\"'`]*\b(bg-[a-z]+-(50|100)|bg-\w+/(5|10|15|20))\b"),
     "Icon in getönter Kreis- oder Quadrat-Plakette, das Standard-Feature-Muster.", None),
    # O Animationen
    ("O Animation", "inview", re.compile(r"\bwhileInView\b|data-aos=|\bScrollTrigger\b|\buseInView\b"),
     "Scroll-Einblendung. Hochwertig umgesetzt (kurz, ohne Unschärfe, Inhalt lesbar)?", None),
    ("O Animation", "loop", re.compile(r"\banimate-(bounce|pulse|ping|spin|float)\b|repeat\s*:\s*Infinity|animation[^;]*\binfinite\b"),
     "Endlos-Animation. Billig wirkend? Besser einmalig abspielen.", None),
    ("O Animation", "parallax", re.compile(r"parallax|useScroll\(|useTransform\(", I),
     "Scroll-gekoppelte Bewegung. Ruckelfrei und Inhalt lesbar?", None),
    # C Cards
    ("C Card-Raster", "grid", re.compile(r"\b(sm:|md:|lg:|xl:)?grid-cols-(3|4|6)\b"),
     "Raster mit 3/4/6 Spalten. Wären Zeilen, Split oder Tabelle besser?", None),
    # A11y-Grundfehler
    ("A11y", "outline-none", re.compile(r"\boutline-none\b|outline\s*:\s*(none|0)\b"),
     "Fokus-Outline entfernt. Gibt es einen :focus-visible-Ersatz?", None),
    ("A11y", "img-no-alt", re.compile(r"<img\b(?![^>]*\balt=)[^>]*>", I),
     "<img> ohne alt-Attribut.", None),
    ("A11y", "div-click", re.compile(r"<(div|span)\b[^>]*\bonClick=", I),
     "Klick-Handler auf div/span. button oder a verwenden.", None),
]

PHRASES = [
    r"(auf|aufs) (das|ein) nächste[ns]? level", r"next level", r"ihre zukunft beginnt",
    r"qualität,? die überzeugt", r"innovative lösungen", r"gemeinsam gestalten wir",
    r"wir sind die zukunft", r"bereit für den nächsten schritt", r"kontaktieren sie uns noch heute",
    r"ihr (zuverlässiger|kompetenter|starker) partner", r"maßgeschneiderte lösungen",
    r"ganzheitliche[nr]? ansatz", r"mit leidenschaft", r"lösungen, die begeistern",
    r"wir bringen ihr", r"vision (wird|in die) realität", r"digitale zukunft",
    r"\belevate\b", r"\bunlock\b", r"\bseamless(ly)?\b", r"cutting[- ]edge", r"\bempower",
    r"\bsupercharge", r"your journey (starts|begins)", r"take your .{1,30} to the next",
    r"\bgame[- ]chang", r"\brevolutioni[sz]e", r"world[- ]class", r"state[- ]of[- ]the[- ]art",
]
PHRASE_RE = re.compile("|".join(PHRASES), I)

STAT_RE = re.compile(
    r"\b\d{1,4}(\.\d{3})?\s?\+\s*(<[^>]+>\s*)*[\"'`]?\s*(jahre|kunden|projekte|gutachten|mitarbeiter|years|clients|customers|projects)"
    r"|\b(9\d|100)\s?%\s*(<[^>]+>\s*)*[\"'`]?\s*(zufrieden|kundenzufriedenheit|satisfaction|weiterempfehlung)",
    I,
)
CTA_RE = re.compile(
    r"mehr erfahren|jetzt (kontakt|anfragen|starten|loslegen|termin)|termin vereinbaren|kontakt aufnehmen"
    r"|learn more|get started|book a (call|demo)|contact us",
    I,
)
UL_RE = re.compile(r"<ul\b", I)
REDUCED_MOTION_RE = re.compile(r"prefers-reduced-motion|motion-reduce|useReducedMotion|MotionConfig[^>]*reducedMotion")


def iter_files(root: str):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for name in filenames:
            if name in SKIP_FILES or name.endswith((".min.js", ".min.css", ".d.ts", ".map")):
                continue
            ext = os.path.splitext(name)[1].lower()
            if ext in SOURCE_EXT:
                yield os.path.join(dirpath, name), ext


def scan(root: str, max_hits: int):
    hits: dict[str, list[dict]] = defaultdict(list)
    counts: dict[str, int] = defaultdict(int)
    hints: dict[str, str] = {}
    ul_per_file: dict[str, int] = {}
    cta_total = 0
    cta_files: dict[str, int] = {}
    has_reduced_motion = False
    has_animation = False
    files_scanned = 0

    def add(cat, rel, lineno, line, hint):
        counts[cat] += 1
        hints.setdefault(cat, hint)
        if len(hits[cat]) < max_hits:
            hits[cat].append({"file": rel, "line": lineno, "text": line.strip()[:160], "hint": hint})

    for path, ext in iter_files(root):
        try:
            with open(path, encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
        except OSError:
            continue
        files_scanned += 1
        rel = os.path.relpath(path, root)
        if REDUCED_MOTION_RE.search(content):
            has_reduced_motion = True
        n_ul = len(UL_RE.findall(content))
        if n_ul:
            ul_per_file[rel] = n_ul
        n_cta = 0
        for lineno, line in enumerate(content.splitlines(), 1):
            if len(line) > MAX_LINE:
                continue
            for cat, rid, rx, hint, exts in RULES:
                if ext in TEXT_ONLY_EXT or (exts is not None and ext not in exts):
                    continue
                if rid == "tw-round" and SMALL_DOT_RE.search(line):
                    continue  # kleine runde Punkte/Indikatoren sind keine Pillen
                if rx.search(line):
                    add(cat, rel, lineno, line, hint)
                    if cat.startswith("O "):
                        has_animation = True
            if ext in {".json", ".yaml", ".yml"} and not re.search(r"[A-Za-zÄÖÜäöü]{4,} [a-zäöü]", line):
                continue
            if PHRASE_RE.search(line):
                add("M Floskel", rel, lineno, line, "Austauschbarer Marketing-Satz. Konkret umschreiben.")
            if STAT_RE.search(line):
                add("L Zahl prüfen", rel, lineno, line, "Statistik/Zahl. Vom Kunden belegt? Sonst Platzhalter.")
            m = len(CTA_RE.findall(line))
            if m:
                n_cta += m
                add("N CTA", rel, lineno, line, "Generischer CTA-Text. Konkreter formulieren, Anzahl begrenzen.")
        if n_cta:
            cta_total += n_cta
            cta_files[rel] = n_cta

    notes = []
    heavy_ul = {f: n for f, n in ul_per_file.items() if n >= 3}
    if heavy_ul:
        top = ", ".join(f"{f} ({n})" for f, n in sorted(heavy_ul.items(), key=lambda x: -x[1])[:5])
        notes.append(f"B Bullet-Flut: Dateien mit ≥3 <ul>: {top}. Ist jede davon wirklich eine Liste?")
    if cta_total >= 6:
        notes.append(f"N CTA: insgesamt {cta_total} generische CTA-Texte gefunden. Primären CTA festlegen und den Rest reduzieren.")
    if has_animation and not has_reduced_motion:
        notes.append("O Animation / A11y: Animationen gefunden, aber kein prefers-reduced-motion bzw. motion-reduce.")
    if counts.get("C Card-Raster", 0) >= 3:
        notes.append(f"C Card-Raster: {counts['C Card-Raster']} Raster mit 3/4/6 Spalten. Sehen mehrere Sections gleich aus?")

    return {
        "root": os.path.abspath(root),
        "files_scanned": files_scanned,
        "counts": dict(sorted(counts.items())),
        "hits": {k: hits[k] for k in sorted(hits)},
        "notes": notes,
    }


def print_report(res: dict):
    print(f"Anti-AI-Scan: {res['root']}  ({res['files_scanned']} Dateien)\n")
    if not res["counts"] and not res["notes"]:
        print("Keine Auffälligkeiten gefunden. Der visuelle Check bleibt trotzdem nötig.")
        return
    print("Übersicht (Treffer = zu prüfen, nicht automatisch falsch):")
    for cat, n in res["counts"].items():
        print(f"  {cat:<16} {n:>4}")
    print()
    for cat, items in res["hits"].items():
        print(f"## {cat}  ({res['counts'][cat]} Treffer)  {items[0]['hint']}")
        for h in items:
            print(f"   {h['file']}:{h['line']}  {h['text']}")
        if res["counts"][cat] > len(items):
            print(f"   … {res['counts'][cat] - len(items)} weitere")
        print()
    if res["notes"]:
        print("## Hinweise")
        for n in res["notes"]:
            print(f"   - {n}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--max-hits", type=int, default=8, help="Beispiele pro Kategorie (Standard 8)")
    ap.add_argument("--json", action="store_true", help="Ausgabe als JSON")
    args = ap.parse_args()
    if not os.path.isdir(args.root):
        print(f"Ordner nicht gefunden: {args.root}", file=sys.stderr)
        return 0
    res = scan(args.root, args.max_hits)
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print_report(res)
    return 0


if __name__ == "__main__":
    sys.exit(main())
