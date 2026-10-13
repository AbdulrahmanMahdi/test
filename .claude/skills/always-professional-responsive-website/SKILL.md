---
name: always-professional-responsive-website
description: Qualitätsstandard für jede Website-Arbeit. Sorgt dafür, dass Websites individuell, ruhig und professionell wirken, wie von einem erfahrenen Webdesigner und Frontend-Entwickler gebaut, und nie wie ein KI-Template, mit Desktop und Mobile als gleichwertigen Zielen. Verwende diesen Skill IMMER, wenn eine Website, Landingpage, Homepage, Unterseite oder Section gebaut, neu gestaltet, überarbeitet, erweitert oder geprüft wird. Das gilt auch für einzelne Teile wie Hero, Navigation, Mobile-Menü, Footer, Kontaktformular, Leistungsseite oder Preisbereich, in jedem Stack (HTML/CSS, Tailwind, React, Next.js, Vue, Svelte, Astro, WordPress-Theme). Er greift auch, wenn der Nutzer das Wort "Design" nicht nennt, etwa bei "bau mir eine Seite für meinen Betrieb", "mach die Website mobil besser", "füg eine Leistungen-Section hinzu", "redesign", "landing page", "build a website", "make it look professional", "responsive fix" oder "das sieht zu sehr nach KI aus".
---

# Always professional, responsive website

Dieser Skill ist ein Qualitätsstandard und kein Stil. Er gibt keinen Look vor. Er sorgt dafür, dass jede Gestaltungsentscheidung einen Grund hat, der sich aus dem konkreten Unternehmen, seinem Angebot und seinen Besuchern ableitet.

## Die Leitfrage

> Existiert dieses Element nur, weil KI-Website-Generatoren es oft verwenden? Dann muss es einen echten funktionalen oder gestalterischen Zweck nachweisen, sonst fliegt es raus.

Warum das so wichtig ist: Besucher haben inzwischen tausende generierte Landingpages gesehen. Sie erkennen Muster wie die kleine Linie vor dem Abschnittstitel, „01 / 02 / 03“, drei identische Icon-Cards oder Lila-Verläufe sofort und schließen daraus auf ein austauschbares, wenig sorgfältiges Unternehmen. Für einen Gutachter, eine Kanzlei oder einen Handwerksbetrieb kostet das Vertrauen und damit Anfragen.

**Professionell heißt: weniger unnötige Elemente und bessere Entscheidungen.** Die Qualität entsteht durch Typografie, Raster, Weißraum, Bildsprache und klare Hierarchie, nicht durch mehr Effekte, Farben, Cards, Icons oder Rundungen.

## Die Verbotsliste

Diese Dinge will der Nutzer auf keiner seiner Websites sehen. Sie sind die typischen Erkennungszeichen einer KI-erstellten Seite. Prüfe jede Section dagegen, bevor du sie baust, und noch einmal im Quality Gate. Details und Alternativen stehen in `references/anti-ai-patterns.md`.

**Aufbau und Layout**
- Jede Section nach demselben Schema: zentrierte Überschrift, ein Satz, drei Karten, fünf- bis sechsmal untereinander
- Karten für alles: abgerundete Boxen mit Schatten, Icon, Titel und zwei Zeilen Text, alles gleich gewichtet
- Standard-Hero: riesige Überschrift, Untertitel, zwei Buttons nebeneinander, rechts Laptop-Mockup oder Stockfoto
- Zahlenleiste wie „10+ Jahre · 500+ Kunden · 98 % Zufriedenheit“ ohne belegte Daten

**Typografie und Details**
- Überschriften, die nur groß sind, um „modern“ zu wirken
- Kleines Label über der Überschrift, oft mit Linie davor („— ÜBER UNS“, Versalien, weite Laufweite)
- Nummerierungen 01, 02, 03 vor Abschnitten, Leistungen oder Menüpunkten ohne echte Reihenfolge
- Bullet-Listen mit Häkchen statt erklärender Sätze
- Generische Icons (Schild, Blitz, Rakete, Häkchen) in farbigen Kreisen

**Farben und Effekte**
- Lila-Blau- oder Pink-Orange-Verläufe, verschwommene Farbflecken, Neon-Glow, Text mit Farbverlauf
- Alles stark abgerundet (Pillen-Buttons, große Radien, überall derselbe Wert)
- Schatten auf jedem Element
- Unveränderte Framework-Standardfarben (z. B. Tailwind-Palette) statt Markenfarben

**Texte und Inhalte**
- Austauschbare Floskeln („auf das nächste Level“, „Qualität, die überzeugt“, „innovative Lösungen“, „Ihr zuverlässiger Partner“)
- Erfundene Bewertungen, Kundennamen, Kundenlogos, Zertifikate, Garantien oder Zahlen
- Kontakt-Button in jeder Section („Jetzt Kontakt aufnehmen“, „Mehr erfahren“)

**Navigation und Footer**
- Mobile-Menü als nummerierte Liste mit Linien und Pfeilen vor jedem Punkt
- KI-Footer: Banner „Bereit für den nächsten Schritt?“, Newsletter, vier Linkspalten, Social-Icons für Kanäle, die es nicht gibt

**Bilder**
- Stockfotos ohne Bezug (Hände auf Tastatur, lächelndes Büroteam, Handschlag, Person mit Tablet) oder gar keine echten Bilder, nur Illustrationen und Icons

**Mobile**
- Desktop-Layout einfach untereinander gestapelt: endloses Scrollen durch Karten, zu kleine Buttons, Wörter, die über den Rand laufen

**Nicht auf der Liste: Animationen.** Hochwertige Bewegung ist erwünscht. Verboten ist nur die billige Ausführung (Unschärfe-Einflug, Endlos-Schweben, Pulsieren, halb transparente Texte), siehe Abschnitt „Animationen“.

**Der Kern:** Eine KI füllt Lücken mit dem Üblichen. Stelle bei jedem Element die Frage: „Warum genau so, für genau dieses Unternehmen?“ Gibt es keine Antwort, gehört es nicht auf die Seite.

## Prioritäten

Wenn sich Ziele widersprechen, gilt diese Reihenfolge:

1. Funktionalität: alles funktioniert, Kontaktaufnahme klappt
2. Professionalität: wirkt individuell und seriös
3. UX: Besucher verstehen sofort Angebot und nächsten Schritt
4. Responsive Design: Desktop und Mobile gleich hochwertig
5. Visuelle Qualität
6. Performance
7. Accessibility
8. SEO

Accessibility steht hier nicht für „optional“. Die Grundregeln weiter unten gelten immer. Die Reihenfolge entscheidet nur echte Zielkonflikte.

## Referenzdateien

Lies diese Dateien in dem Arbeitsschritt, in dem du sie brauchst:

| Datei | Wann lesen |
|---|---|
| `references/anti-ai-patterns.md` | Vor dem Gestalten von Sections, Navigation, Hero und Footer sowie beim Anti-AI-Check. Enthält zu jedem Muster Don't/Do-Code und die Ausnahmen. |
| `references/design-system.md` | Wenn du Tokens festlegst oder ein bestehendes System analysierst. Enthält Vorlage, Skalen, Schriftwahl je Branche und Beispiele für Tailwind v4 und CSS. |
| `references/checklists.md` | Im Quality Gate. Enthält die Checklisten für Responsive, Accessibility, Performance und SEO, den Anti-AI-Check und die Berichtsvorlage. |

## Hilfsskripte

Sie liefern Befunde, keine Urteile. Jeder Treffer ist eine Stelle, die du bewusst prüfst. Ist ein Muster begründet, bleibt es.

- `python3 <skill>/scripts/anti_ai_scan.py <projektordner>` durchsucht den Quellcode nach typischen KI-Mustern: Deko-Linien, „01/02“-Nummerierung, Pillen-Rundungen, Schattenflut, Lila-Verläufe, Floskeln, erfundene Zahlen, CTA-Häufung, Card-Raster, Animationen sowie Accessibility-Grundfehler.
- `node <skill>/scripts/responsive_check.mjs <url> [--out <ordner>]` lädt die Seite mit Playwright bei 320, 375, 390, 430, 768, 1024, 1280, 1440 und 1920 px. Es misst horizontales Overflow, zu kleine Touch-Ziele, zu kleine Schrift, Bilder ohne `alt` oder Maße und die Überschriftenstruktur, und es speichert Screenshots. **Sieh dir die Screenshots danach selbst an**, vor allem 375 px und 1440 px sowie das geöffnete Mobile-Menü. Viele Probleme sieht man nur im Bild.

`<skill>` steht für den Ordner dieser SKILL.md.

---

## Arbeitsablauf

Arbeite die Schritte der Reihe nach ab. Bei kleinen Aufgaben, etwa einer einzelnen Section, kürzt du Schritt 1 bis 4 auf das ab, was die Section braucht. Den Abgleich mit dem bestehenden System und das Quality Gate überspringst du nicht.

### 1. Bestehendes Projekt analysieren

Bevor du etwas baust:

- Stack, Framework-Version, CSS-Ansatz und vorhandene Komponenten ermitteln. Projekteigene Anweisungen wie `CLAUDE.md` oder `AGENTS.md` haben Vorrang.
- Vorhandene Tokens suchen: Tailwind-`@theme` oder `tailwind.config`, CSS-Variablen, Fonts, Logo, Bildmaterial.
- Inhalte sammeln: Was bietet das Unternehmen konkret an? Für wen? In welcher Region? Was ist der Hauptweg zur Kontaktaufnahme (Anruf, WhatsApp, Formular)? Welche echten Fakten gibt es, etwa Zertifikate, Gründungsjahr, Bewertungen?
- Die bestehende Seite, falls vorhanden, einmal mit `responsive_check.mjs` aufnehmen. So hast du einen Vorher-Stand.

### 2. Bestehendes Design respektieren

Ist bereits ein gutes oder brauchbares Design vorhanden, dann **verbessere es, statt es zu ersetzen**. Behalte Markenfarben, Logo, Schriften und funktionierende Muster bei und entferne gezielt, was nach Template aussieht. Neu baust du nur, wenn der Nutzer es verlangt oder das Bestehende grundlegend kaputt ist. Sag dann vorher, warum.

### 3. Design-System festlegen

Lege die Tokens **vor** der ersten Section schriftlich fest, als CSS-Variablen oder Tailwind-`@theme`. Vorlage und Herleitung findest du in `references/design-system.md`. Mindestens:

- **Farben:** Primär-, Sekundär- und Akzentfarbe, Hintergründe, Textfarben, Rahmen. Alle aus der Marke abgeleitet und mit geprüftem Kontrast.
- **Typografie:** eine, höchstens zwei Schriftfamilien, eine Größenskala mit 5 bis 7 Stufen, Gewichte, Zeilenhöhen, Laufweite für Überschriften und eine maximale Textbreite von etwa 60 bis 75 Zeichen.
- **Abstände:** eine Skala, zum Beispiel 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128. Nur Werte daraus verwenden.
- **Layout:** Containerbreite, Seitenränder pro Breakpoint und Raster.
- **Radius:** höchstens 2 bis 3 Werte. Bilder, Buttons und Flächen bekommen bewusst unterschiedliche oder bewusst gleiche Werte, aber nicht zufällig.
- **Schatten:** keiner oder genau eine Stufe für Elemente, die wirklich schweben, etwa Dropdowns oder ein Sticky-Header beim Scrollen.
- **Komponenten:** Buttons (primär, sekundär, Textlink), Formularfelder mit allen Zuständen, Navigation.
- **Breakpoints:** dort setzen, wo der Inhalt bricht, nicht blind die Framework-Defaults übernehmen.

Übernimm keine Framework-Defaults ungeprüft, weder die Tailwind-Palette noch `rounded-xl` überall oder `shadow-lg`. Ein Default ist in Ordnung, wenn du ihn bewusst gewählt hast.

### 4. Desktop und Mobile gemeinsam konzipieren

Plane jede Section für beide Formate zugleich, bevor du Code schreibst. Halte für jede Section kurz fest:

- **Zweck:** Was soll der Besucher hier verstehen oder tun?
- **Layoutform:** zum Beispiel Statement, Split-Layout, Bild/Text, Prozess, Tabelle, Galerie oder Fließtext. Wiederhole nicht dieselbe Form direkt hintereinander.
- **Desktop:** Anordnung und Raster.
- **Mobile:** eigene Lösung, nicht einfach das Desktop-Layout untereinander gestapelt. Was wird umsortiert, gekürzt, horizontal scrollbar gemacht (nur mit sichtbarem Hinweis) oder aufklappbar?

Prüfe gegen das Muster „Überschrift, Text, 3 Cards“ × n. Folgen zwei Sections dieselbe Struktur, gestalte eine anders, oder führe beide zusammen.

### 5. Komponenten entwickeln

- Wiederverwenden, was das Projekt schon hat.
- Nur abstrahieren, was mindestens zweimal gleich gebraucht wird. Keine Wrapper ohne Funktion, keine 20 Varianten einer Card.
- Jede interaktive Komponente bekommt Hover-, Focus-visible-, Active- und Disabled-Zustände sowie bei Formularen Fehler- und Erfolgszustände.

### 6. Implementieren

Halte dich dabei an die Regeln in den Abschnitten unten: Anti-AI, Texte, Responsive, Accessibility, Performance und SEO.

### 7. Quality Gate

Siehe unten. Erst danach ist die Arbeit fertig.

---

## Anti-AI-Regeln (Kurzfassung)

Vollständige Don't/Do-Beispiele und Ausnahmen stehen in `references/anti-ai-patterns.md`. Lies die Datei, bevor du Sections, Navigation, Hero oder Footer gestaltest.

| Muster | Stattdessen | Erlaubt, wenn … |
|---|---|---|
| **A** Kleine Linie vor Label oder Seitentitel („— ÜBER UNS“) | Hierarchie über Größe, Gewicht und Abstand. Ein Eyebrow-Label ist meist überflüssig. | Die Linie gehört zu einem durchgängig entwickelten visuellen System, das aus der Marke kommt. |
| **B** Alles als Bullet-Liste | Kurze Absätze, Definitionspaare, Tabelle, Gegenüberstellung oder ein typografisch abgesetzter Fließtext | Es ist wirklich eine Liste gleichartiger, kurzer, abzuhakender Punkte. |
| **C** Card-Raster (3/4/6/8 gleiche Karten) mit großem Radius und Schatten | Zeilen mit Trennlinie, Split-Layout, Tabelle, eine große Hauptleistung plus Nebenleistungen | Die Einträge sind eigenständig anklickbar und gleichrangig, etwa Artikel oder Produkte. |
| **D** Mobile-Menü als „01 Startseite / 02 …“ mit Linien und Pfeilen | Ruhige, große Links mit klarer Gruppierung und dem Kontaktweg prominent am Ende | – |
| **E** Nummerierung 01, 02, 03 | Weglassen | Die Reihenfolge ist inhaltlich relevant, etwa Ablauf oder Schritte. |
| **F** Pillen-Buttons und große Rundungen überall | 2 bis 3 Radius-Tokens, eher zurückhaltend | Die Marke ist bewusst weich und verspielt, und das ist konsistent umgesetzt. |
| **G** Schatten auf jedem Element | Flächen durch Hintergrundton, Rahmen oder Abstand trennen | Das Element schwebt wirklich: Dropdown, Modal, Sticky-Header. |
| **H** Lila/blau-, Pink/orange-Verläufe, Glow, Neon | Markenfarben, flächig. Ein ruhiger Ton-in-Ton-Verlauf nur mit Grund. | Die Markenidentität besteht nachweislich aus einem Verlauf. |
| **I** Standard-Hero (große Floskel, Untertitel, 2 Buttons, Mockup) | Hero aus dem Angebot entwickeln: was, für wen, wo, und der wichtigste nächste Schritt | – |
| **J** Riesige Headlines um ihrer selbst willen | Größe aus Hierarchie und Textlänge ableiten | Kurze, starke Aussage in einer bewusst editorialen Gestaltung |
| **K** Icon + Überschrift + Text als Standardblock | Icons nur mit Informationswert (Telefon, Download, Status) | Das Icon erkennt man schneller als das Wort. |
| **L** Erfundene Zahlen („500+ Kunden“, „98 %“) | Echte, belegte Fakten oder nichts. Fehlende Daten als `[Vom Kunden zu liefern: …]` markieren. | Der Kunde hat die Zahl geliefert. |
| **M** Floskeln („auf das nächste Level“, „Qualität, die überzeugt“) | Konkrete Aussagen zu Leistung, Ort, Ablauf, Dauer, Preis oder Garantie | – |
| **N** CTA in jeder Section | Ein klarer primärer CTA, sichtbar in Header oder Sticky-Bar, dazu wenige gezielte Stellen | – |
| **O** Billige Animationen (Unschärfe-Einflug, Endlos-Floating, Wackeln, Typewriter, Bewegung, die Lesbarkeit kostet) | Hochwertige, präzise Bewegung: kurze Scroll-Reveals, Zähler, Magnet- und Tilt-Effekte, Cursor-Spotlight, Fortschrittslinien, Foto-Zoom beim Hovern | Animationen sind **erwünscht**, wenn sie modern, ruhig und sauber umgesetzt sind. Entfernt wird nur die billige Ausführung, nicht die Animation an sich. |
| **Q** Stockfotos ohne Bezug, Laptop-Mockups, nur Illustrationen | Echte Fotos von Team, Ort, Arbeit, Produkt. Ohne echtes Material lieber typografisch gestalten und Fotos als Platzhalter für den Kunden markieren. | Das Stockfoto zeigt konkret das Angebot und ist als solches nicht austauschbar. |
| **P** KI-Footer („Bereit für den nächsten Schritt?“, Newsletter, 4 Spalten, Social-Icons) | Footer mit dem, was Besucher dort suchen: Kontakt, Adresse, Öffnungszeiten, Impressum, Datenschutz | Newsletter oder Social-Kanäle existieren wirklich und werden gepflegt. |

## Texte

Texte wirken oft stärker „nach KI“ als das Layout.

- **Konkret statt generisch.** Nicht „Innovative Lösungen für Ihre Zukunft“, sondern „Unfallgutachten in Berlin, Termin meist innerhalb von 24 Stunden, auf Wunsch direkt am Unfallort“.
- **Keine erfundenen Fakten.** Gilt für Zahlen, Bewertungen, Kundennamen, Zertifikate, Jahreszahlen und Garantien. Fehlt etwas, setze einen sichtbaren Platzhalter wie `[Vom Kunden zu liefern: Anzahl Gutachten pro Jahr]` und nenne ihn im Abschlussbericht.
- **Branchensprache treffen:** sachlich für Gutachter und Kanzleien, nahbar für Handwerk und Gastronomie. Duzen oder Siezen wie im Bestand.
- **Kurze Überschriften, die etwas aussagen.** „Was wir prüfen“ ist besser als „Unsere Expertise für Sie“.
- **Kein Keyword-Stuffing.** Den Ort einmal natürlich in H1 und Title zu nennen reicht.

## Animationen

Animationen sind ausdrücklich erwünscht, wenn sie modern, interessant **und** hochwertig wirken. Das Ziel ist nicht eine statische Seite, sondern Bewegung, die sich präzise und gewollt anfühlt. Was KI-typisch wirkt, sind meist Gestaltungsmuster (riesige Überschriften, Nummern im Menü, Deko-Linien, Bullet-Listen), nicht die Animation selbst.

**Bestehende Animationen nicht entfernen**, nur verbessern: Wenn ein Projekt bereits Animationen hat, behalte sie und korrigiere nur die Ausführung (zu langsam, Unschärfe, Lesbarkeit). Frage nach, bevor du einen Effekt komplett streichst.

**Gute Beispiele:** einmalige Scroll-Reveals (0,3 bis 0,4 s, 12 bis 20 px, ohne Unschärfe), gestaffelte Listen, Zähler bzw. Odometer für echte Zahlen, magnetische Buttons, leichtes 3D-Tilt bei Siegeln oder Karten, Cursor-Spotlight auf Flächen, Lesefortschritt, Linien, die sich beim Scrollen füllen, Foto-Zoom beim Hovern, gleitende Aktiv-Indikatoren, kurze Seitenübergänge, Stempel-Effekt für Siegel und Zertifikate, Bild-Enthüllung per `clip-path`, zeilenweise Masken-Reveals für die Hero-Headline, gleitende Link-Unterstreichung.

**Qualitätskriterien:**
- Inhalt bleibt jederzeit voll lesbar; Text wird nie dauerhaft transparent oder unscharf.
- Kurz und präzise: Reveals 0,3 bis 0,4 s, Hover 0,2 bis 0,9 s, `ease-out`, nur `transform` und `opacity`.
- Einmalig statt endlos: nichts pulsiert, wackelt oder schwebt dauerhaft.
- Maus-Effekte (Magnet, Tilt, Spotlight) nur bei `pointer: fine`; Touch bleibt ruhig.
- `prefers-reduced-motion` schaltet Bewegung ab, Inhalte bleiben sichtbar.
- Kein Layout-Shift, kein Ruckeln, kein Effekt, der Klicks verzögert.
- Scroll-Trigger nie auf das Element legen, das selbst per `clip-path` oder `opacity: 0` versteckt ist: Der IntersectionObserver hält es für unsichtbar und löst nie aus. Beobachte einen unverdeckten Wrapper.
- Nach dem Einbau mit Animationen testen (nicht nur mit „Bewegung reduzieren“): Seite komplett durchscrollen und prüfen, dass alle Bilder und Texte sichtbar sind. `responsive_check.mjs` macht das standardmäßig und meldet dauerhaft verdeckte Bilder.

## Desktop und Mobile

Beide Formate sind gleichwertige Ziele. Typische Fehler und die Gegenmittel:

- **Navigation:** Mobile braucht ein eigenes Konzept. Wichtigster Kontaktweg ohne Menü erreichbar, zum Beispiel ein Anruf-Button im Header oder eine schlanke Sticky-Bar. Menüpunkte groß und ruhig, Scroll-Lock beim offenen Menü, mit Escape und Fokus-Falle schließbar.
- **Hero:** Auf Mobile passt die Kernaussage plus primärer CTA in den ersten Bildschirm (etwa 375 × 667). Bilder werden neu zugeschnitten und nicht einfach verkleinert.
- **Überschriften:** Mit `clamp()` skalieren. Lange deutsche Komposita brechen sauber mit `hyphens: auto` und `lang="de"` sowie `overflow-wrap: break-word`.
- **Tabellen:** Auf Mobile in Zeilenpaare umbauen oder in einem scrollbaren Container mit sichtbarem Hinweis zeigen.
- **Formulare:** Felder in voller Breite, passende `type`/`inputmode`/`autocomplete`-Attribute, Schriftgröße mindestens 16 px, damit iOS nicht zoomt.
- **Telefon und E-Mail:** als `tel:` und `mailto:` verlinken, umbruchsicher.
- **Touch-Ziele:** mindestens 44 × 44 px mit genug Abstand zueinander.
- **Overflow:** Keine horizontale Scrollbar bei 320 px. Häufige Ursachen sind feste Breiten, `100vw` zusammen mit einer Scrollbar, lange URLs und negative Margins.

## Responsive-Regeln

- Prüfe bei 320, 375, 390, 430, 768, 1024, 1280, 1440 und 1920 px. Bei jeder Breite gilt es, Ausrichtung, Abstände, Typografie, Navigation, Bilder, Container, Raster, CTA und Footer anzusehen.
- Breakpoints setzt du dort, wo der Inhalt bricht. Container Queries sind sinnvoll für Komponenten, die in verschiedenen Spaltenbreiten vorkommen.
- Zwischenbreiten wie 900 px oder 1100 px sind die häufigste Fehlerquelle. Ein kurzer Blick dort lohnt sich.
- Auf großen Bildschirmen darf der Inhalt nicht endlos breit laufen: Container begrenzen, Textbreite begrenzen.

## Accessibility (immer)

- Semantisches HTML: `header`, `nav`, `main`, `footer`, `section` mit Überschrift; `button` für Aktionen, `a` für Navigation.
- Genau eine H1 pro Seite und keine übersprungenen Ebenen.
- Alt-Texte: beschreibend bei inhaltlichen Bildern, `alt=""` bei rein dekorativen.
- Volle Tastaturbedienung. Sichtbare `:focus-visible`-Stile; nie `outline: none` ohne Ersatz.
- Kontrast mindestens 4,5 : 1 für Text und 3 : 1 für große Schrift und UI-Elemente.
- Formulare mit `<label>`, Fehlermeldungen per `aria-describedby` verknüpft und in Klartext.
- `prefers-reduced-motion: reduce` schaltet nicht notwendige Animationen ab.
- Ein Skip-Link zum Hauptinhalt.

## Performance

- Bilder in AVIF oder WebP mit `srcset`/`sizes` bzw. der Framework-Bildkomponente, `width`/`height` oder `aspect-ratio` gesetzt, damit kein Layout-Shift entsteht, und `loading="lazy"` außer beim Hero-Bild. Das Hero-Bild bekommt `fetchpriority="high"`.
- Fonts selbst hosten oder über das Framework laden, nur benötigte Gewichte, `font-display: swap`, passende Fallback-Metriken.
- Keine neue Library für etwas, das CSS oder eine bereits vorhandene Library kann, etwa Accordions mit `<details>`. Prüfe vor jeder neuen Abhängigkeit, ob sie nötig ist. Vorhandene Animations-Libraries (z. B. framer-motion) dürfen für hochwertige Animationen genutzt werden.
- So viel wie möglich serverseitig oder statisch rendern, Client-JavaScript nur für echte Interaktion. In React keine unnötigen Re-Renders durch Inline-Objekte in Hot-Paths oder State für reine Ableitungen.

## SEO

Für jede Seite: einzigartiger `<title>` mit etwa 50 bis 60 Zeichen, Meta-Description mit 140 bis 160 Zeichen, eine H1, logische Überschriftenstruktur, sprechende URLs, Canonical, Open Graph (Titel, Beschreibung, Bild), `robots`, eine Sitemap bei mehreren Seiten und strukturierte Daten, wo sie passen. Das kann zum Beispiel `LocalBusiness`, `Service`, `FAQPage`, `BreadcrumbList` oder `Article` sein. Strukturierte Daten nur mit echten Angaben befüllen.

---

## Quality Gate

Eine Website oder Section gilt erst als fertig, wenn alle Schritte erledigt sind. Führe sie tatsächlich aus und hake sie nicht nur gedanklich ab.

1. **Build und Lint** des Projekts laufen fehlerfrei.
2. **`anti_ai_scan.py`** ausführen und jeden Treffer bewerten: entfernen oder begründen.
3. **`responsive_check.mjs`** gegen die laufende Seite ausführen, lokal per Dev-Server oder Preview. Overflow, Touch-Ziele und Überschriftenstruktur müssen sauber sein.
4. **Screenshots ansehen,** mindestens 375 px, 768 px und 1440 px, außerdem das geöffnete Mobile-Menü. Bewerte sie wie ein Art Director: Ruhe, Ausrichtung, Rhythmus, Hierarchie, Konsistenz.
5. **Anti-AI-Check:** die 29 Fragen aus `references/checklists.md`. Zeigen mehrere Antworten ein Problem, überarbeite die betroffenen Stellen und prüfe erneut.
6. **Accessibility-, Performance- und SEO-Checkliste** aus `references/checklists.md`.
7. **Real-Designer-Test:**
   > Wenn ich nicht wüsste, dass diese Website mit KI erstellt wurde: Würde ich sie für die individuelle Arbeit eines professionellen Webdesigners halten?

   Lautet die Antwort „nein“ oder „eher nein“, benenne konkret, woran es liegt (Layout, Typografie, Komponenten, Abstände, Texte oder Muster). Überarbeite das und prüfe erneut.
8. **Gegenprobe gegen Überdesign:** Sind Gestaltungselemente hinzugekommen, die nur Platz füllen (Deko-Linien, Icons, Cards, Badges)? Dann entfernen. Animationen fallen nicht pauschal darunter: Sie bleiben, wenn sie hochwertig sind (siehe Muster O).

Ist eine Prüfung in der Umgebung nicht möglich, weil zum Beispiel kein Browser oder kein Dev-Server verfügbar ist, sag das ausdrücklich im Bericht und behaupte nicht, dass sie bestanden ist.

## Abschlussbericht

Halte den Bericht kurz und nutze die Vorlage am Ende von `references/checklists.md`: was geändert wurde, Ergebnis der Prüfungen (bestanden, behoben, offen), bewusst beibehaltene Muster mit Begründung und die offenen Platzhalter, die der Kunde liefern muss.
