# Design-System festlegen

Das Design-System steht fest, **bevor** die erste Section gebaut wird. Es verhindert die zufällige Mischung aus Werten wie `py-20`, `py-24`, `py-28`, `gap-7` und `text-[17px]`, die eine Seite unruhig macht.

## Inhalt

- [1. Herleitung](#1-herleitung)
- [2. Farben](#2-farben)
- [3. Typografie](#3-typografie)
- [4. Abstände und Layout](#4-abstände-und-layout)
- [5. Radius, Linien, Schatten](#5-radius-linien-schatten)
- [6. Komponenten](#6-komponenten)
- [7. Vorlage: Tailwind v4](#7-vorlage-tailwind-v4)
- [8. Vorlage: reines CSS](#8-vorlage-reines-css)

---

## 1. Herleitung

Bevor du Werte festlegst, beantworte vier Fragen in jeweils einem Satz:

1. **Branche und Tonalität:** sachlich, vertrauenswürdig, technisch, warm, handwerklich, exklusiv oder verspielt?
2. **Besucher:** in welcher Situation kommen sie? Beispiel: nach einem Unfall, gestresst und am Handy. Daraus folgt: Mobile zuerst, Telefonnummer sofort sichtbar, ruhige Gestaltung.
3. **Vorhandene Marke:** Logo-Farben, bestehende Schriften, Fotos. Diese haben Vorrang vor neuen Ideen.
4. **Wichtigste Handlung:** anrufen, Formular, Termin buchen oder kaufen?

Gibt es bereits Tokens, zum Beispiel in `@theme`, `tailwind.config` oder `:root`, dann **erweitere** sie und erfinde kein paralleles System.

## 2. Farben

Rollen statt Farbnamen, damit die Bedeutung klar ist:

| Token | Rolle | Hinweis |
|---|---|---|
| `--color-bg` | Seitenhintergrund | Selten reines `#fff`. Ein leicht getöntes Weiß wirkt ruhiger. |
| `--color-surface` | abgesetzte Flächen | 2 bis 4 % dunkler bzw. heller als bg |
| `--color-text` | Fließtext | Selten reines `#000`. Dunkles, leicht getöntes Grau oder Markenfarbe. |
| `--color-muted` | Sekundärtext | Kontrast ≥ 4,5 : 1 auf bg prüfen |
| `--color-line` | Rahmen, Trenner | dezent, Kontrast etwa 1,3 bis 1,6 : 1 |
| `--color-primary` | Marke, primärer Button | aus Logo oder Bestand |
| `--color-primary-ink` | Text auf primary | Kontrast ≥ 4,5 : 1 |
| `--color-accent` | sparsame Hervorhebung | höchstens für 1 bis 2 Elementtypen |
| `--color-danger` / `--color-success` | Formularzustände | nicht als Deko verwenden |

Regeln:
- **Eine** Markenfarbe trägt, die anderen ordnen sich unter. Etwa 70 bis 80 % der Fläche sind neutrale Töne.
- Neutraltöne leicht in Richtung der Markenfarbe tönen. Das ergibt eine harmonische Palette ohne Mühe.
- Kontrast für jede Text-Hintergrund-Paarung prüfen, auch für Text auf Bildern. Dort braucht es eine Abdunklung oder Fläche.
- Keine Lila- und Neon-Verläufe ohne Markenbezug, siehe Muster H.
- Dark Mode nur, wenn er gefordert ist oder schon existiert. Dann alle Rollen neu definieren und nicht einfach invertieren.

Kontrast schnell prüfen, ohne Tool:
```js
// Relative Luminanz nach WCAG
const L = h => { const c = h.match(/\w\w/g).map(x => parseInt(x, 16) / 255).map(v => v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; };
const ratio = (a, b) => { const [x, y] = [L(a), L(b)].sort((m, n) => n - m); return (x + 0.05) / (y + 0.05); };
ratio("1f2937", "f8f7f4"); // ≥ 4,5 für Fließtext
```

## 3. Typografie

### Schriftwahl nach Charakter

Die Schrift folgt der Marke, nicht der Mode. Gibt es eine Hausschrift, wird sie verwendet.

| Charakter | Passende Richtung | Beispiele |
|---|---|---|
| Sachlich, technisch, Gutachter, Ingenieure, B2B | Neo-Grotesk oder humanistische Grotesk | IBM Plex Sans, Inter, Source Sans 3, Public Sans |
| Modern, freundlich, Dienstleister, Praxis | Geometrisch-humanistisch | Manrope, DM Sans, Plus Jakarta Sans, Figtree |
| Klassisch, Kanzlei, Steuerberater, Hotel | Serif für Überschriften, Grotesk für Text | Source Serif 4, Fraunces (ruhig gesetzt), Newsreader, dazu Source Sans 3 oder Inter |
| Handwerk, regional, bodenständig | Kräftige Grotesk, eventuell Slab für Akzente | Work Sans, Archivo, Roboto Slab (sparsam) |
| Exklusiv, Mode, Architektur | Kontrastreiche Serif oder sehr reduzierte Grotesk | Cormorant (nur groß), Instrument Serif, Neue-Haas-artige Grotesk |

Regeln:
- Höchstens 2 Familien. Eine einzige Familie mit guter Gewichtsabstufung reicht oft.
- Höchstens 3 Gewichte laden, zum Beispiel 400, 500 und 600 oder 700.
- Space Grotesk, Poppins und Montserrat sind kein Verbot, wirken aber schnell nach Template. Setze sie nur bewusst ein.

### Größenskala

Nutze eine Skala mit 5 bis 7 Stufen und fließenden Größen per `clamp()`:

| Stufe | Mobile → Desktop | Zeilenhöhe | Verwendung |
|---|---|---|---|
| `--text-sm` | 14 → 14 px | 1,5 | Meta, Hinweise (nie für Fließtext) |
| `--text-base` | 16 → 17/18 px | 1,6 bis 1,7 | Fließtext |
| `--text-lg` | 18 → 20 px | 1,5 | Lead-Absatz, H4 |
| `--text-xl` | 20 → 24 px | 1,35 | H3 |
| `--text-2xl` | 26 → 36 px | 1,2 | H2 |
| `--text-3xl` | 32 → 52 px | 1,1 | H1 |

```css
--text-3xl: clamp(2rem, 1.2rem + 3.2vw, 3.25rem);
```

- Textbreite: `max-width: 65ch` für Fließtext, Überschriften etwa 20 bis 25 ch.
- Laufweite: ab etwa 32 px leicht negativ (`-0.01em` bis `-0.02em`), Großbuchstaben-Labels `+0.04em` bis `+0.08em` und nicht `0.3em`.
- Deutsch: `lang="de"` und `hyphens: auto` für Fließtext. In Überschriften lieber manuell `&shy;` setzen oder die Größe anpassen.
- `text-wrap: balance` für Überschriften, `text-wrap: pretty` für Absätze.

## 4. Abstände und Layout

**Abstandsskala** auf 4-px-Basis, mit Auswahl:
`4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128`

| Anwendung | Mobile | Desktop |
|---|---|---|
| Innerhalb von Komponenten | 8 bis 16 | 12 bis 24 |
| Zwischen Überschrift und Text | 12 bis 16 | 16 bis 24 |
| Zwischen Blöcken in einer Section | 24 bis 32 | 32 bis 48 |
| Section-Abstand vertikal | 64 | 96 bis 128 |

Section-Abstände als **eine** Variable (`--section-y`), damit alle Sections den gleichen Rhythmus haben. Bewusst abweichen darfst du, zum Beispiel enger bei zusammengehörigen Sections, aber nicht zufällig.

**Layout:**
- Container: `max-width` 1120 bis 1280 px für Inhalt, schmale Textspalte 680 bis 760 px.
- Seitenrand: 16 bis 20 px bei 320 bis 430 px, 24 bis 32 px bei Tablet, ab 1280 px automatisch.
- Raster: 12 Spalten auf Desktop, 4 bis 6 auf Mobile, oder einfache `grid-template-columns` je nach Inhalt.

## 5. Radius, Linien, Schatten

```css
--radius-sm: 4px;   /* Inputs, Buttons, Tags */
--radius-md: 8px;   /* Bilder, Flächen, Dropdowns */
/* Sections und Seitenbereiche: kein Radius */

--border: 1px solid var(--color-line);
--shadow-float: 0 8px 24px -12px rgb(0 0 0 / 0.25); /* nur Dropdown, Modal, Sticky-Header */
```

## 6. Komponenten

**Buttons:** höchstens drei Varianten.
- Primär: gefüllt mit `primary`, Mindesthöhe 44 px (Mobile 48 px), Padding etwa 12 × 20 px, Gewicht 600.
- Sekundär: Rahmen oder getönte Fläche.
- Textlink: unterstrichen oder mit klarer Farbe, bei Hover Unterstrich.
- Zustände: `:hover` (leicht dunkler), `:focus-visible` (2 px Outline mit Offset in Kontrastfarbe), `:active`, `:disabled` (Kontrast bleibt lesbar, `cursor: not-allowed`).

**Formulare:**
- Label sichtbar über dem Feld, nicht nur als Platzhalter.
- Feldhöhe mindestens 44 px, Schrift mindestens 16 px.
- `autocomplete`, `type`, `inputmode` setzen, zum Beispiel `tel`, `email` oder `postal-code`.
- Fehler unter dem Feld in Klartext, `aria-invalid`, `aria-describedby`.
- Erfolg: deutliche Bestätigung, die sagt, was als Nächstes passiert.

**Navigation:**
- Desktop: höchstens 5 bis 6 Hauptpunkte. Leistungen als Dropdown oder Mega-Menü nur bei vielen Leistungen. Primärer CTA rechts.
- Mobile: siehe Muster D in `anti-ai-patterns.md`.
- Ein Sticky-Header bleibt schlank, etwa 56 bis 64 px Mobile und 64 bis 80 px Desktop.

**Breakpoints:** am Inhalt ausrichten. Typische Startwerte sind 640, 768, 1024 und 1280 px. Prüfe aber, wo Navigation, Raster und Hero tatsächlich brechen, und verschiebe die Werte bei Bedarf.

## 7. Vorlage: Tailwind v4

```css
/* app/globals.css */
@import "tailwindcss";

@theme {
  --color-bg: #f8f7f4;
  --color-surface: #efede8;
  --color-text: #1c2430;
  --color-muted: #5a6472;
  --color-line: #dcd9d2;
  --color-primary: #0f3b5f;
  --color-primary-ink: #ffffff;
  --color-accent: #c8102e;

  --font-sans: "IBM Plex Sans", ui-sans-serif, system-ui, sans-serif;

  --text-base: clamp(1rem, 0.96rem + 0.2vw, 1.0625rem);
  --text-base--line-height: 1.65;
  --text-2xl: clamp(1.625rem, 1.3rem + 1.4vw, 2.25rem);
  --text-2xl--line-height: 1.2;
  --text-3xl: clamp(2rem, 1.2rem + 3.2vw, 3.25rem);
  --text-3xl--line-height: 1.1;

  --radius-sm: 4px;
  --radius-md: 8px;
}

:root { --section-y: 4rem; }
@media (min-width: 1024px) { :root { --section-y: 7rem; } }
```

Tailwind v4 setzt mit dem Namespace `--color-*` die Klassen `bg-primary`, `text-muted`, `border-line` usw. Überschreibst du vorher `--color-*: initial;`, entfernst du die Default-Palette ganz. Das verhindert, dass versehentlich `violet-500` auftaucht.

## 8. Vorlage: reines CSS

```css
:root {
  --color-bg: #f8f7f4; --color-surface: #efede8; --color-text: #1c2430;
  --color-muted: #5a6472; --color-line: #dcd9d2;
  --color-primary: #0f3b5f; --color-primary-ink: #fff; --color-accent: #c8102e;

  --font-sans: "IBM Plex Sans", system-ui, sans-serif;
  --text-base: clamp(1rem, 0.96rem + 0.2vw, 1.0625rem);
  --text-2xl: clamp(1.625rem, 1.3rem + 1.4vw, 2.25rem);
  --text-3xl: clamp(2rem, 1.2rem + 3.2vw, 3.25rem);

  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px; --space-5: 24px;
  --space-6: 32px; --space-7: 48px; --space-8: 64px; --space-9: 96px; --space-10: 128px;
  --section-y: var(--space-8);
  --container: 1200px; --gutter: 20px;
  --radius-sm: 4px; --radius-md: 8px;
}
@media (min-width: 768px)  { :root { --gutter: 32px; } }
@media (min-width: 1024px) { :root { --section-y: var(--space-9); } }

html { -webkit-text-size-adjust: 100%; }
body { background: var(--color-bg); color: var(--color-text); font: 400 var(--text-base)/1.65 var(--font-sans); }
.container { width: min(100% - 2 * var(--gutter), var(--container)); margin-inline: auto; }
:focus-visible { outline: 2px solid var(--color-primary); outline-offset: 3px; }
```

Die Beispielwerte sind ein Startpunkt für ein sachliches Dienstleister-Profil. Leite die tatsächlichen Werte aus der jeweiligen Marke ab.
