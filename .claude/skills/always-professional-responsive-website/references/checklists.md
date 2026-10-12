# Checklisten für das Quality Gate

Hake jede Checkliste im Quality Gate tatsächlich ab. Einen Punkt, den du in der Umgebung nicht prüfen kannst, markierst du als „nicht geprüft“ und begründest das.

## Inhalt

- [Anti-AI-Check (25 Fragen)](#anti-ai-check-25-fragen)
- [Responsive-Check pro Breite](#responsive-check-pro-breite)
- [Accessibility](#accessibility)
- [Performance](#performance)
- [SEO](#seo)
- [Abschlussbericht: Vorlage](#abschlussbericht-vorlage)

---

## Anti-AI-Check (25 Fragen)

Beantworte jede Frage mit „ok“ oder „Problem: <Stelle>“. **Zeigt mehr als eine Frage ein Problem, überarbeite die Stellen und gehe die Liste danach erneut durch.** Ein einzelnes Problem behebst du direkt.

1. Gibt es unnötige dekorative Striche, etwa vor Labels oder Überschriften?
2. Gibt es unnötige Nummerierungen (01, 02 …) ohne relevante Reihenfolge?
3. Gibt es zu viele Bullet-Listen? Wäre bei einer davon Fließtext, eine Tabelle oder Definitionspaare besser?
4. Gibt es zu viele Cards? Wäre bei einem Raster eine Zeilenliste oder ein Split-Layout besser?
5. Sehen mehrere Sections strukturell identisch aus?
6. Gibt es zu viele stark abgerundete Elemente (Pillen, `rounded-3xl`)?
7. Gibt es Schatten auf Elementen, die nicht schweben?
8. Gibt es generische Verläufe, Glow oder Neon?
9. Gibt es Icons ohne Informationswert?
10. Gibt es KI-typische Marketingsätze, also Sätze, die auf jede andere Firmenseite passen würden?
11. Gibt es zu viele CTAs, oder ist der primäre CTA unklar?
12. Sind die Animationen hochwertig (kurz, präzise, einmalig, Inhalt immer lesbar), oder wirken sie billig (Unschärfe, Endlos-Effekte, Wackeln)? Wurden bestehende Animationen ohne Rückfrage entfernt?
13. Wirkt die Desktop-Navigation wie ein Template?
14. Wirkt das Mobile-Menü hochwertig: gruppiert, ruhig, mit Kontaktweg?
15. Ist der Footer individuell und auf das Unternehmen zugeschnitten?
16. Wirkt die Seite insgesamt wie ein fertiges Template?
17. Gibt es Elemente ohne echten Zweck?
18. Sind Desktop und Mobile gleichermaßen hochwertig, und hat Mobile eigene Lösungen statt nur Stapeln?
19. Ist die Typografie professionell: Skala, Zeilenhöhe, Textbreite, Laufweite, Umbrüche?
20. Werden Farben konsistent und nur aus dem Token-Set verwendet?
21. Sind Abstände konsistent und nur aus der Skala genommen?
22. Gibt es visuelle Überladung, also zu viele Reize auf einem Bildschirm?
23. Gibt es zu viel leeren Raum, zum Beispiel Sections, die auf Mobile wie leere Bildschirme wirken?
24. Gibt es horizontales Scrollen auf Mobile (320 bis 430 px)?
25. Sind Buttons und Formulare auf Mobile gut bedienbar (≥ 44 px, 16-px-Schrift, passende Tastatur)?

Zusätzlich: Sind alle Zahlen, Bewertungen und Fakten belegt oder als Platzhalter markiert?

## Responsive-Check pro Breite

Breiten: **320 · 375 · 390 · 430 · 768 · 1024 · 1280 · 1440 · 1920**. Die Messwerte liefert `scripts/responsive_check.mjs`. Bei jeder Breite ansehen:

| Prüfpunkt | Worauf achten |
|---|---|
| Ausrichtung | Linke Kanten von Logo, Überschriften und Text auf einer Linie, Container einheitlich |
| Abstände | Section-Rhythmus gleichmäßig, nichts klebt am Rand, Seitenrand ≥ 16 px |
| Typografie | H1 bricht nicht in Einzelwörter, keine Silbentrennung mitten in Marken, Fließtext ≥ 16 px |
| Navigation | Desktop-Navigation passt ohne Umbruch, und der Wechsel zum Mobile-Menü liegt an der richtigen Breite |
| Bilder | Bildausschnitt sinnvoll, Motiv nicht abgeschnitten, keine Verzerrung |
| Container | Bei 1440 und 1920 px begrenzt, keine endlos langen Zeilen |
| Raster | Spaltenzahl passt zum Inhalt, keine verwaisten Einzelkarten in der letzten Reihe |
| CTA | Primärer CTA sichtbar, auf Mobile mit dem Daumen erreichbar |
| Footer | Lesbar, Adressblock nicht zerrissen, Links mit Abstand |
| Overflow | `scrollWidth` ≤ `clientWidth`, keine abgeschnittenen Inhalte |
| Sonderfälle | Lange Wörter, E-Mail-Adressen und Telefonnummern brechen sauber; Tabellen und horizontale Scroller zeigen einen Hinweis |

Zusätzlich das Mobile-Menü geöffnet bei 375 px prüfen und eine Zwischenbreite wie 900 px ansehen.

## Accessibility

- [ ] Landmarks: `header`, `nav` (mit `aria-label` bei mehreren), `main`, `footer`
- [ ] Genau eine H1 und keine übersprungenen Ebenen (H2 → H4)
- [ ] Inhaltsbilder mit beschreibendem `alt`, Deko-Bilder mit `alt=""`
- [ ] Alle Funktionen per Tastatur erreichbar, Reihenfolge logisch, kein Fokus-Verlust
- [ ] `:focus-visible` überall sichtbar, kein `outline: none` ohne Ersatz
- [ ] Skip-Link „Zum Inhalt springen“
- [ ] Kontrast Text ≥ 4,5 : 1, große Schrift und UI-Elemente ≥ 3 : 1, auch auf Bildern
- [ ] Touch-Ziele ≥ 44 × 44 px
- [ ] Formulare: sichtbare `<label>`, Fehler mit `aria-describedby`, `aria-invalid`, verständliche Texte
- [ ] Menü-Toggle: `aria-expanded`, `aria-controls`, Escape schließt, Fokus kehrt zurück
- [ ] `prefers-reduced-motion` respektiert
- [ ] `lang` am `<html>` gesetzt
- [ ] Links unterscheidbar, nicht nur über die Farbe, und Linktexte aussagekräftig (kein „hier“)

## Performance

- [ ] Bilder in AVIF oder WebP, responsive (`srcset`/`sizes` oder Framework-Komponente)
- [ ] `width`/`height` oder `aspect-ratio` an allen Bildern und Embeds, damit kein Layout-Shift entsteht
- [ ] Hero-Bild ohne Lazy Loading, mit `fetchpriority="high"`; Rest `loading="lazy"`
- [ ] Fonts selbst gehostet oder über das Framework geladen, höchstens 3 Gewichte, `font-display: swap`
- [ ] Keine unnötigen Libraries; jede neue Abhängigkeit begründet
- [ ] Client-JavaScript nur für echte Interaktion; statisch oder serverseitig rendern, wo möglich
- [ ] Animationen nur auf `transform` und `opacity`
- [ ] Embeds wie Karten oder Videos erst bei Interaktion oder Sichtbarkeit laden
- [ ] Build-Ausgabe auf auffällig große Bundles prüfen

## SEO

- [ ] `<title>` einzigartig, etwa 50 bis 60 Zeichen, Leistung und Ort natürlich enthalten
- [ ] Meta-Description 140 bis 160 Zeichen, konkret und ohne Keyword-Stuffing
- [ ] Eine H1, die zum Title passt
- [ ] Sprechende, kurze URLs in Kleinbuchstaben mit Bindestrichen
- [ ] Canonical gesetzt
- [ ] Open Graph: `og:title`, `og:description`, `og:image` (1200 × 630), `og:url`
- [ ] `robots`: Produktionsseiten indexierbar, Staging und Danke-Seiten `noindex`
- [ ] Sitemap bei mehreren Seiten
- [ ] Strukturierte Daten, wo passend (`LocalBusiness`, `Service`, `FAQPage`, `BreadcrumbList`, `Article`), nur mit echten Angaben
- [ ] Interne Verlinkung zwischen verwandten Seiten
- [ ] Impressum und Datenschutz erreichbar (in Deutschland Pflicht)

---

## Abschlussbericht: Vorlage

```markdown
## Ergebnis

**Geändert:** <2–5 Sätze, was gebaut oder überarbeitet wurde und warum>

**Design-System:** <Farben, Schrift, Skalen in einer Zeile, oder „bestehendes System übernommen, ergänzt um …“>

**Quality Gate**
| Prüfung | Status |
|---|---|
| Build / Lint | bestanden / Fehler: … |
| Anti-AI-Scan | x Treffer, y behoben, z bewusst beibehalten |
| Responsive (320–1920) | bestanden / offen: … |
| Screenshots gesichtet | 375 / 768 / 1440 / Mobile-Menü |
| Accessibility | bestanden / offen: … |
| Performance | bestanden / offen: … |
| SEO | bestanden / offen: … |
| Real-Designer-Test | ja / nein: was noch fehlt |

**Bewusst beibehalten:** <Muster + Begründung, z. B. „nummerierter Ablauf, weil Reihenfolge relevant“>

**Vom Kunden zu liefern:** <Liste aller Platzhalter: echte Zahlen, Fotos, Texte>

**Nicht geprüft:** <was in dieser Umgebung nicht möglich war und warum>
```
