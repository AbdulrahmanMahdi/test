# Anti-AI-Patterns: Don't / Do

Jedes Muster hat vier Teile: woran man es erkennt, warum es schadet, was stattdessen geht und wann es doch in Ordnung ist. Die Beispiele sind in Tailwind geschrieben, gelten aber genauso für reines CSS und andere Frameworks.

## Inhalt

- [A Deko-Linie vor Labels](#a-deko-linie-vor-labels)
- [B Bullet-Flut](#b-bullet-flut)
- [C Card-Raster](#c-card-raster)
- [D Mobile-Navigation](#d-mobile-navigation)
- [E Nummerierung](#e-nummerierung)
- [F Rundungen](#f-rundungen)
- [G Schatten](#g-schatten)
- [H Verläufe und Glow](#h-verläufe-und-glow)
- [I Hero](#i-hero)
- [J Überdimensionierte Headlines](#j-überdimensionierte-headlines)
- [K Generische Icons](#k-generische-icons)
- [L Erfundene Zahlen](#l-erfundene-zahlen)
- [M Floskeln](#m-floskeln)
- [N CTA-Spam](#n-cta-spam)
- [O Animationen](#o-animationen)
- [P Footer](#p-footer)
- [Q Bilder](#q-bilder)
- [Gleichförmige Sections](#gleichförmige-sections)
- [Praxisbeispiel: Kfz-Gutachter](#praxisbeispiel-kfz-gutachter)

---

## A Deko-Linie vor Labels

**Erkennen:** eine kleine horizontale Linie mit 16 bis 48 px Breite und 1 bis 2 px Höhe vor einem Eyebrow-Label in Großbuchstaben mit weiter Laufweite. Varianten sind „— LEISTUNGEN“, „-- KONTAKT“, `::before`-Striche oder eine Linie, ein Punkt und ein Label.

**Warum es schadet:** Das ist derzeit das deutlichste Erkennungszeichen generierter Seiten. Es füllt Raum, ohne Information zu tragen, und das Label wiederholt meist nur, was die Überschrift ohnehin sagt.

```tsx
// Don't
<div className="flex items-center gap-3">
  <span className="h-px w-10 bg-accent" />
  <span className="text-xs uppercase tracking-[0.3em] text-accent">Über uns</span>
</div>
<h2 className="text-5xl font-bold">Erfahrung, der Sie vertrauen können</h2>

// Do: Die Überschrift trägt die Aussage, die Hierarchie entsteht über Größe und Abstand
<h2 className="text-3xl md:text-4xl font-semibold tracking-tight">
  Seit 2009 Kfz-Sachverständige in Berlin
</h2>
<p className="mt-4 max-w-[60ch] text-muted">…</p>
```

**Erlaubt, wenn** die Linie Teil eines Systems ist, das aus der Marke kommt, etwa ein Logo mit Linienelement, das in Raster, Bildrahmen und Navigation konsequent wiederkehrt, und nicht nur vor Überschriften steht. Ein schlichtes Label ohne Linie ist in Ordnung, wenn es echte Orientierung gibt, zum Beispiel eine Kategorie über einem Ratgeber-Artikel.

## B Bullet-Flut

**Erkennen:** jede Section enthält eine `<ul>`, Listenpunkte bestehen aus 2 bis 5 Wörtern, Häkchen-Icons stehen vor jedem Punkt.

**Warum es schadet:** Listen zerlegen Zusammenhänge in Schlagworte. Sie wirken wie ein Foliensatz und nicht wie eine Website, die etwas erklärt.

**Alternativen nach Inhaltsart:**

| Inhalt | Bessere Form |
|---|---|
| Begriffe mit kurzer Erklärung | Definitionspaare (`<dl>`) in 2 Spalten oder Zeilen mit Trennlinie |
| Vergleich von Optionen | Tabelle oder Gegenüberstellung |
| 3 bis 4 Kernaussagen | Kurze Absätze mit fetter Einstiegsphrase |
| Ablauf | Nummerierte Schritte (hier ist Nummerierung richtig) |
| Viele kleine Fakten | Kompakter Fließtext, eine Fakten-Zeile oder eine Tabelle |
| Echte Checkliste (Unterlagen mitbringen) | Liste, das ist korrekt |

```tsx
// Don't
<ul>
  {["Technik und Optik im Detail", "Wertbeeinflussende Faktoren", "Vorschäden", "Ausstattung"].map(i =>
    <li key={i} className="flex gap-2"><CheckIcon/>{i}</li>)}
</ul>

// Do: Definitionspaare, jeder Punkt bekommt seine Erklärung
<dl className="grid gap-x-12 gap-y-6 md:grid-cols-2">
  <div className="border-t border-line pt-4">
    <dt className="font-semibold">Technik und Optik</dt>
    <dd className="mt-1 text-muted">Motor, Fahrwerk, Lack, Innenraum, dokumentiert mit Fotos und Messwerten.</dd>
  </div>
  …
</dl>
```

## C Card-Raster

**Erkennen:** `grid-cols-3` oder `grid-cols-4` mit gleichen Boxen aus `rounded-2xl`, `shadow`, `border`, `p-8` und Icon, Titel und Text. Oft mehrfach pro Seite.

**Warum es schadet:** Alles wirkt gleich wichtig, die Seite liest sich wie ein UI-Kit. Karten mit Rahmen, Schatten und Rundung erzeugen visuelles Rauschen, ohne Inhalte zu ordnen.

**Alternativen:**
- **Zeilen statt Karten:** Leistung links, Kurzbeschreibung Mitte, Link rechts, getrennt durch `border-t`. Ruhig, gut scanbar und auf Mobile einfach zu stapeln.
- **Gewichtung:** eine Hauptleistung groß mit Bild, Nebenleistungen kompakt daneben oder darunter.
- **Split-Layout:** Text und Erklärung links, eine Liste der Leistungen als Links rechts.
- **Tabelle** bei vergleichbaren Attributen wie Preis, Dauer oder Anwendungsfall.

```tsx
// Don't
<div className="grid md:grid-cols-3 gap-8">
  {services.map(s => (
    <div className="rounded-3xl bg-white p-8 shadow-xl">
      <s.Icon className="h-10 w-10 text-violet-500" /><h3>{s.title}</h3><p>{s.text}</p>
    </div>))}
</div>

// Do: Zeilen-Layout mit Trennlinien, die ganze Zeile ist der Link
<ul className="divide-y divide-line border-y border-line">
  {services.map(s => (
    <li key={s.href}>
      <a href={s.href} className="group grid gap-2 py-6 md:grid-cols-[1fr_2fr_auto] md:items-baseline md:gap-8">
        <span className="text-lg font-semibold">{s.title}</span>
        <span className="text-muted">{s.summary}</span>
        <span className="text-sm text-primary group-hover:underline">Details</span>
      </a>
    </li>))}
</ul>
```

**Erlaubt, wenn** die Einträge eigenständige, gleichrangige und klickbare Objekte sind, etwa Ratgeber-Artikel, Referenzprojekte, Produkte oder Teammitglieder. Auch dann gilt: dezenter Radius, keine Schatten, und Bilder tragen die Karte.

## D Mobile-Navigation

**Erkennen:** Vollbild-Overlay mit „01 Startseite / 02 Leistungen …“, Linien vor jedem Punkt, Pfeil-Icons rechts an jeder Zeile, jeder Menüpunkt in einer eigenen Box, riesige Schrift ohne Gruppierung.

**Warum es schadet:** Das Menü ist auf Mobile oft das Erste, was angefasst wird. Wirkt es wie ein Template, ist der Eindruck sofort weg.

**So geht es besser:**
- Inhalte gruppieren, zum Beispiel „Leistungen“ (Unterpunkte), dann „Über uns · Ratgeber · Kontakt“.
- Hierarchie über Größe und Gewicht: Hauptpunkte etwa 20 bis 24 px, Unterpunkte 16 bis 17 px, normal gesetzt.
- Großzügige Touch-Höhen von mindestens 48 px, keine Rahmen um jeden Punkt.
- Den Kontaktweg ans Ende als echte Aktion setzen: Telefonnummer als Button, darunter Öffnungszeiten oder Erreichbarkeit.
- Die aktive Seite dezent markieren, etwa mit Farbe oder Gewicht.
- Technik: `aria-expanded` und `aria-controls` am Toggle, Fokus wandert ins Menü, Escape schließt, Scroll-Lock auf `body`, Fokus kehrt zum Toggle zurück.

```tsx
// Don't
{links.map((l, i) => (
  <a className="flex items-center justify-between border-b py-5 text-3xl">
    <span><span className="text-accent mr-4">0{i + 1}</span>— {l.label}</span><ArrowRight/>
  </a>))}

// Do
<nav aria-label="Hauptmenü" className="flex h-full flex-col px-6 pb-8 pt-4">
  <p className="text-sm text-muted">Leistungen</p>
  <ul className="mt-2">
    {services.map(s => <li key={s.href}><a href={s.href} className="block py-3 text-xl">{s.label}</a></li>)}
  </ul>
  <ul className="mt-6 border-t border-line pt-4">
    {pages.map(p => <li key={p.href}><a href={p.href} className="block py-3 text-lg">{p.label}</a></li>)}
  </ul>
  <div className="mt-auto">
    <a href="tel:+4930…" className="btn-primary w-full">030 … anrufen</a>
    <p className="mt-3 text-sm text-muted">Mo–Fr 8–18 Uhr, Notfälle rund um die Uhr</p>
  </div>
</nav>
```

## E Nummerierung

**Erkennen:** `01`, `02`, `03` vor Sections, Menüpunkten oder Leistungen; `String(i + 1).padStart(2, "0")`.

**Regel:** Nummeriere nur, wenn die Reihenfolge inhaltlich zählt, etwa im Ablauf „So läuft ein Gutachten ab“. Auch dort reichen oft „1, 2, 3“ ohne führende Null und ohne Riesengröße.

## F Rundungen

**Erkennen:** `rounded-full` an allen Buttons, `rounded-3xl` an Karten, Bildern und Sections, `border-radius: 999px` überall, und überall derselbe große Radius.

**Regel:** Lege 2 bis 3 Radius-Tokens fest, zum Beispiel `--radius-sm: 4px` für Felder und Buttons und `--radius-md: 8px` für Bilder und Flächen. Section-Container bekommen keinen Radius, denn eine Website ist keine App-Oberfläche. Pillen-Buttons nur bei einer bewusst weichen Marke und dann überall konsistent.

## G Schatten

**Regel:** Standard ist kein Schatten. Flächen trennst du über Hintergrundton (`--surface-2`), eine 1-px-Linie oder Abstand. Eine Schattenstufe ist für schwebende Ebenen reserviert: Dropdown, Modal, Sticky-Header nach dem Scrollen, Toast. Keine farbigen Glow-Schatten.

## H Verläufe und Glow

Auch: unveränderte Framework-Standardfarben (Tailwind-Blau, -Indigo, -Violett), die keinen Bezug zur Marke haben.

**Erkennen:** `from-violet-500 to-fuchsia-500`, `from-indigo-600 via-purple-600`, `bg-gradient-to-r` auf Text, unscharfe Farbkleckse (`blur-3xl`) im Hintergrund, Neon-Ränder, „Aurora“-Hintergründe.

**Regel:** Farben kommen aus der Marke. Flächige Farbe wirkt hochwertiger als ein Verlauf. Ein Verlauf ist zulässig, wenn er Teil der Markenidentität ist oder ganz subtil Ton in Ton bleibt, zum Beispiel ein dunkles Blau, das in ein etwas dunkleres Blau übergeht, um ein Bild zu überlagern und Text lesbar zu machen.

## I Hero

**Erkennen:** Floskel-Headline („Wir sind die Zukunft von …“), Untertitel, ein primärer und ein sekundärer Button, rechts ein Mockup oder Stockfoto, dahinter Glow-Blobs, darunter Logos „Trusted by“.

**So entwickelst du den Hero aus dem Unternehmen:**
1. Was genau? Leistung in Worten des Kunden, zum Beispiel „Unfallgutachten“.
2. Für wen und wo? „nach einem unverschuldeten Unfall in Berlin“.
3. Warum hier? Ein echter Vorteil, etwa „Termin innerhalb von 24 Stunden, auch vor Ort“.
4. Nächster Schritt: ein primärer CTA, der zum tatsächlichen Kontaktweg passt (Anruf, WhatsApp, Formular).
5. Bild: echtes Foto vom Unternehmen, Team, Fahrzeug oder Ort. Ohne echtes Bild lieber ein typografischer Hero als ein Stockfoto.

Optional kommt eine Vertrauenszeile mit echten Fakten dazu, zum Beispiel „DEKRA-zertifiziert · Google 4,9 aus 212 Bewertungen“, aber nur mit belegten Daten.

## J Überdimensionierte Headlines

**Regel:** Die H1 auf Desktop liegt typischerweise bei 40 bis 64 px, auf Mobile bei 30 bis 40 px, gesetzt mit `clamp()`. Je länger die Überschrift, desto kleiner. Über 80 px nur bei sehr kurzen, editorial gemeinten Aussagen. Zeilenhöhe 1,05 bis 1,2, leicht negative Laufweite ab etwa 32 px. Keine Headline, die auf Mobile in einzelne Wörter pro Zeile zerfällt.

## K Generische Icons

**Erkennen:** Jede Leistung, jeder Vorteil und jeder Schritt hat ein Linien-Icon aus derselben Bibliothek (Schild, Blitz, Rakete, Häkchen, Stern) in einem farbigen Kreis.

**Regel:** Ein Icon bleibt nur, wenn es schneller erkannt wird als das Wort oder eine Funktion zeigt: Telefon, E-Mail, WhatsApp, Download, extern, Menü, Schließen, Status. Ein „Qualität“-Icon neben dem Wort „Qualität“ trägt nichts bei.

## L Erfundene Zahlen

**Erkennen:** `10+ Jahre`, `500+ Kunden`, `98 % Zufriedenheit`, `24/7` ohne Beleg, Fake-Testimonials mit Vornamen und Stockfotos.

Dazu gehören auch erfundene Kundenlogos („Trusted by“), Zertifikats-Siegel, Auszeichnungen und Garantien.

**Regel:** Nur Zahlen und Stimmen verwenden, die der Kunde geliefert hat oder die öffentlich belegbar sind, etwa Google-Bewertungen über die API. Sonst einen Platzhalter setzen, zum Beispiel `[Vom Kunden zu liefern: Anzahl erstellter Gutachten]`, und ihn im Bericht auflisten. Es ist besser, keine Zahlenleiste zu haben als eine erfundene.

## M Floskeln

**Verboten, wenn nicht wirklich gemeint und belegt:**
„auf das nächste Level“, „Ihre Zukunft beginnt hier“, „Qualität, die überzeugt“, „Innovative Lösungen für eine erfolgreiche Zukunft“, „Gemeinsam gestalten wir die Zukunft“, „Ihr zuverlässiger Partner für …“, „maßgeschneiderte Lösungen“, „ganzheitlicher Ansatz“, „mit Leidenschaft“, „Wir sind die Zukunft von …“, „Bereit für den nächsten Schritt?“, „Kontaktieren Sie uns noch heute“. Englisch: „elevate“, „unlock“, „seamless“, „cutting-edge“, „next level“, „empower“, „supercharge“, „Your journey starts here“.

**Test:** Könnte der Satz unverändert auf der Website eines völlig anderen Unternehmens stehen? Dann umschreiben, mit Leistung, Ort, Ablauf, Dauer, Preis, Garantie oder einem echten Beispiel.

| Floskel | Konkret |
|---|---|
| „Qualität, die überzeugt.“ | „Unsere Gutachten erkennen alle Versicherer an, auch bei Streit über die Schadenhöhe.“ |
| „Ihr Partner für Mobilität.“ | „Wir begutachten Pkw, Motorräder und Transporter bis 7,5 t.“ |
| „Schnell und unkompliziert.“ | „Termin meist am selben oder nächsten Tag. Das Gutachten liegt nach 48 Stunden vor.“ |

## N CTA-Spam

**Regel:** Lege einen primären CTA fest, also die wichtigste Handlung. Er ist ständig erreichbar, im Header und auf Mobile als Sticky-Bar oder im Header-Icon. Zusätzlich setzt du ihn an 1 bis 2 Stellen, an denen die Entscheidung naheliegt, etwa nach dem Ablauf und am Seitenende. Sekundäre Links wie „Mehr zu Wertgutachten“ beschreiben konkret ihr Ziel. Keine „Mehr erfahren“-Buttons unter jeder Section.

## O Animationen

Animationen sind erwünscht. Hier geht es nur um die **billige Ausführung**, nicht um die Animation an sich. Bestehende Animationen werden verbessert, nicht gestrichen.

**Billig (vermeiden):** Elemente fliegen mit Unschärfe und großem Weg ein, Wort-für-Wort-Einflug bei jeder Überschrift, Endlos-Floating, Wackeln oder Pulsieren, Typewriter-Effekte, Text, der beim Scrollen halb transparent bleibt, Animationen über 0,6 s für einfache Reveals, Effekte, die auf Touch-Geräten stören.

**Hochwertig (gern einsetzen):**

| Effekt | Gute Umsetzung |
|---|---|
| Scroll-Reveal | einmalig, 0,3–0,4 s, 12–20 px nach oben, ohne Unschärfe, Listen leicht gestaffelt (50–80 ms) |
| Zähler / Odometer | nur echte Zahlen, einmal beim Sichtbarwerden, Wert für Screenreader und Suchmaschinen im DOM |
| Magnetische Buttons | Stärke 0,2–0,3, Federung, nur Maus/Stift |
| Tilt | max. 6–10°, für Siegel, Zertifikate, Bewertungskarten; nie für Formulare |
| Cursor-Spotlight | weicher Lichtkegel, optional Rahmen-Glühen in Markenfarbe, nur `pointer: fine` |
| Fortschritt | Lesefortschritt oben, Ablauf-Linie füllt sich beim Scrollen; Schritte bleiben voll lesbar |
| Foto-Zoom | Hover, ca. `scale(1.04)` über 0,8–0,9 s |
| Aktiv-Indikator | gleitet zwischen Tabs oder Menüpunkten (layout animation) |

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

## P Footer

**Erkennen:** große CTA-Banner-Section mit „Bereit für den nächsten Schritt?“, Newsletter-Feld, 4 Linkspalten, Social-Icons-Reihe, „Made with ♥“.

**Was Besucher im Footer suchen:** Kontakt (Telefon, E-Mail, Adresse), Öffnungszeiten oder Erreichbarkeit, eventuell eine Anfahrt, die wichtigsten Seiten, Impressum, Datenschutz, Cookie-Einstellungen. Für lokale Unternehmen wirkt ein kompakter Footer mit Adressblock, Öffnungszeiten und kurzer Seitenliste hochwertiger als ein Mega-Footer. Newsletter und Social-Icons nur, wenn es sie tatsächlich gibt und sie gepflegt werden.

---

## Q Bilder

**Erkennen:** Stockfotos ohne Bezug zum Unternehmen (Hände auf Laptop, lächelndes Team im Großraumbüro, Handschlag, Businessperson mit Tablet, Glühbirne, Puzzleteile), Laptop- oder Smartphone-Mockups im Hero, Bilder von Unsplash/Pexels/Picsum als Dauerlösung, oder eine Seite ganz ohne Fotos, nur mit Illustrationen und Icons.

**Warum es schadet:** Besucher erkennen Stockfotos sofort. Sie zeigen nicht dieses Unternehmen, also beweisen sie nichts, und die Seite wirkt austauschbar.

**Stattdessen:**
- Echte Fotos vom Team, vom Ort, von der Arbeit und vom Ergebnis, passend zugeschnitten (Desktop und Mobile getrennt).
- Fehlt echtes Material: Seite typografisch tragen lassen, Bildflächen als `[Vom Kunden zu liefern: Foto der Werkstatt]` markieren und im Bericht auflisten.
- Bildstil einheitlich halten (Licht, Farbton, Ausschnitt).

**Erlaubt, wenn** ein Stockfoto konkret das Angebot zeigt (z. B. ein bestimmtes Fahrzeugmodell) und kein generisches „Business“-Motiv ist.

## Gleichförmige Sections

**Erkennen:** Die Seite besteht aus 5 oder mehr Blöcken nach dem Schema zentrierte Überschrift, Untertitel, Raster. Alle haben dieselbe Breite, denselben Hintergrund und denselben Abstand.

**Gegenmittel:** Lege pro Section die Layoutform nach Zweck fest und variiere mit Maß:

| Zweck | Mögliche Form |
|---|---|
| Kernaussage oder Haltung | Statement: ein Satz groß, viel Weißraum |
| Leistungen | Zeilenliste oder eine Hauptleistung plus Nebenleistungen |
| Ablauf | Horizontale Schritte (Desktop) oder vertikale Timeline (Mobile) |
| Vertrauen | Echte Bewertungen, Zertifikat-Logos klein und ruhig, Foto des Teams |
| Erklären | Editorial: schmale Textspalte mit Zwischenüberschriften und Randnotizen |
| Vergleich | Tabelle |
| Ort | Karte und Adresse im Split-Layout |

Wechsle Ausrichtung (links/zentriert), Breite (schmaler Text/volle Breite) und Hintergrund nur so oft, dass ein Rhythmus entsteht und kein Flickenteppich.

---

## Praxisbeispiel: Kfz-Gutachter

### Menü

**Vorher:**
```
01 — Unfallgutachten        →
02 — Kurzgutachten          →
03 — Wertgutachten          →
04 — Reparaturbestätigung   →
05 — Beweissicherung        →
```

**Nachher (Desktop-Dropdown oder Mobile-Menü):**
```
Leistungen
  Unfallgutachten          nach unverschuldetem Unfall
  Kurzgutachten            für Bagatellschäden bis ca. 750 €
  Wertgutachten            für Kauf, Verkauf, Versicherung
  Reparaturbestätigung
  Beweissicherung
Über uns   Ratgeber   Kontakt

[ 030 … anrufen ]
```
Keine Nummern, keine Linien, keine Pfeile. Die Hierarchie entsteht über Gruppierung, Gewicht und eine kurze, konkrete Unterzeile, die bei der Wahl hilft. Die Unterzeilen zeigst du nur, wenn Platz ist. Den Betrag „ca. 750 €“ übernimmst du nur, wenn das Unternehmen ihn so angibt.

### „Was wir prüfen“

**Vorher:**
```
Was wir prüfen
• Technik und Optik im Detail
• Wertbeeinflussende Faktoren
• Vorschäden und Reparaturen
• Ausstattung und Zustand
```

**Nachher:** Definitionspaare in zwei Spalten (Desktop) bzw. untereinander (Mobile), jeweils mit feiner Linie oben:

```
Technik und Optik             Wertbeeinflussende Faktoren
Motor, Fahrwerk, Lack und      Laufleistung, Wartungshistorie,
Innenraum, dokumentiert mit    Marktlage und regionale
Fotos und Messwerten.          Vergleichsangebote.

Vorschäden                    Ausstattung
Lackschichtmessung zeigt       Sonderausstattung wird einzeln
nachlackierte Teile, auch      erfasst und bewertet.
bei fachgerechter Reparatur.
```
Jeder Punkt sagt jetzt, **was** geprüft wird und **wie**. Das schafft Vertrauen, während die Schlagwortliste beliebig wirkte.
