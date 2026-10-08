#!/usr/bin/env node
// Responsive- und Basis-Accessibility-Check mit Playwright.
//
// Aufruf:
//   node responsive_check.mjs <url> [<url> …] [--out <ordner>] [--widths 320,375,…] [--no-shots] [--json]
//
// Misst pro Breite: horizontales Overflow (mit Verursachern), Touch-Ziele < 44 px
// (unter 768 px), Text < 14 px bzw. Fließtext < 16 px auf Mobile, Bilder ohne alt oder
// ohne Maße (CLS), Anzahl der H1, übersprungene Überschriftenebenen. Speichert
// Ganzseiten-Screenshots. Die Screenshots danach selbst ansehen.
//
// Playwright wird zuerst im Projekt, dann global gesucht. Fehlt es:
//   npm i -D playwright && npx playwright install chromium

import { createRequire } from "node:module";
import { execSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";

const DEFAULT_WIDTHS = [320, 375, 390, 430, 768, 1024, 1280, 1440, 1920];

function parseArgs(argv) {
  const opts = { urls: [], out: "responsive-check", widths: DEFAULT_WIDTHS, shots: true, json: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--out") opts.out = argv[++i];
    else if (a === "--widths") opts.widths = argv[++i].split(",").map(Number).filter(Boolean);
    else if (a === "--no-shots") opts.shots = false;
    else if (a === "--json") opts.json = true;
    else if (a === "-h" || a === "--help") opts.help = true;
    else opts.urls.push(a);
  }
  return opts;
}

async function loadPlaywright() {
  const attempts = [() => import("playwright"), () => import("@playwright/test")];
  const req = createRequire(path.join(process.cwd(), "noop.js"));
  for (const name of ["playwright", "@playwright/test"]) attempts.push(() => import(req.resolve(name)));
  try {
    const globalRoot = execSync("npm root -g", { stdio: ["ignore", "pipe", "ignore"] }).toString().trim();
    for (const name of ["playwright", "@playwright/test"]) {
      attempts.push(() => import(createRequire(path.join(globalRoot, "noop.js")).resolve(name)));
    }
  } catch {}
  for (const tryImport of attempts) {
    try {
      const mod = await tryImport();
      const pw = mod.chromium ? mod : mod.default;
      if (pw?.chromium) return pw;
    } catch {}
  }
  return null;
}

// Läuft im Browser.
function measure({ mobile }) {
  const doc = document.documentElement;
  const vw = doc.clientWidth;
  const sel = (el) => {
    if (el.id) return `#${el.id}`;
    let s = el.tagName.toLowerCase();
    const cls = (el.getAttribute("class") || "").trim().split(/\s+/).filter(Boolean).slice(0, 3);
    if (cls.length) s += "." + cls.join(".");
    const p = el.parentElement;
    return p && p !== document.body ? `${p.tagName.toLowerCase()} > ${s}` : s;
  };
  const visible = (el) => {
    const st = getComputedStyle(el);
    if (st.display === "none" || st.visibility === "hidden" || Number(st.opacity) === 0) return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  };
  const clippedByAncestor = (el) => {
    for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) {
      const ox = getComputedStyle(p).overflowX;
      if (ox === "hidden" || ox === "auto" || ox === "scroll" || ox === "clip") return true;
    }
    return false;
  };

  const overflowPx = Math.max(doc.scrollWidth, document.body.scrollWidth) - vw;
  const offenders = [];
  if (overflowPx > 0) {
    for (const el of document.body.querySelectorAll("*")) {
      const r = el.getBoundingClientRect();
      if (r.width && (r.right > vw + 1 || r.left < -1) && visible(el) && !clippedByAncestor(el)) {
        offenders.push({ el: sel(el), left: Math.round(r.left), right: Math.round(r.right), width: Math.round(r.width) });
        if (offenders.length >= 8) break;
      }
    }
  }

  const smallTargets = [];
  if (mobile) {
    for (const el of document.querySelectorAll("a[href], button, input:not([type=hidden]), select, textarea, [role=button], summary")) {
      if (!visible(el)) continue;
      const r = el.getBoundingClientRect();
      const inline = getComputedStyle(el).display === "inline" && el.closest("p, li, dd, td");
      if (inline) continue; // Links im Fließtext sind ausgenommen (WCAG 2.5.8)
      if (r.width < 44 || r.height < 44) {
        smallTargets.push({ el: sel(el), text: (el.innerText || el.getAttribute("aria-label") || "").trim().slice(0, 40), w: Math.round(r.width), h: Math.round(r.height) });
      }
    }
  }

  const tinyText = [];
  const smallBody = [];
  const inputsUnder16 = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, { acceptNode: (n) => (n.textContent.trim().length > 2 ? 1 : 2) });
  const seen = new Set();
  for (let n = walker.nextNode(); n; n = walker.nextNode()) {
    const el = n.parentElement;
    if (!el || seen.has(el) || !visible(el)) continue;
    seen.add(el);
    const fs = parseFloat(getComputedStyle(el).fontSize);
    const txt = n.textContent.trim();
    if (fs < 12) tinyText.push({ el: sel(el), size: fs, text: txt.slice(0, 40) });
    else if (mobile && el.closest("p, li, dd") && txt.length > 60 && fs < 16) smallBody.push({ el: sel(el), size: fs, text: txt.slice(0, 40) });
  }
  if (mobile) {
    for (const el of document.querySelectorAll("input:not([type=hidden]):not([type=checkbox]):not([type=radio]), select, textarea")) {
      const fs = parseFloat(getComputedStyle(el).fontSize);
      if (visible(el) && fs < 16) inputsUnder16.push({ el: sel(el), size: fs });
    }
  }

  const imgs = [...document.images];
  const imgNoAlt = imgs.filter((i) => !i.hasAttribute("alt")).map((i) => i.currentSrc || i.src).slice(0, 8);
  const imgNoDims = imgs
    .filter((i) => !(i.getAttribute("width") && i.getAttribute("height")) && getComputedStyle(i).aspectRatio === "auto")
    .map((i) => i.currentSrc || i.src)
    .slice(0, 8);

  const heads = [...document.querySelectorAll("h1,h2,h3,h4,h5,h6")].filter(visible).map((h) => ({ l: +h.tagName[1], t: h.innerText.trim().slice(0, 60) }));
  const skips = [];
  for (let k = 1; k < heads.length; k++) if (heads[k].l > heads[k - 1].l + 1) skips.push(`${"h" + heads[k - 1].l} → h${heads[k].l} „${heads[k].t}“`);

  return {
    overflowPx: Math.max(0, overflowPx),
    offenders,
    smallTargets: smallTargets.slice(0, 12),
    smallTargetsCount: smallTargets.length,
    tinyText: tinyText.slice(0, 6),
    smallBody: smallBody.slice(0, 6),
    inputsUnder16,
    imgNoAlt,
    imgNoDims,
    h1Count: heads.filter((h) => h.l === 1).length,
    headingSkips: skips.slice(0, 6),
    hasMain: !!document.querySelector("main"),
    lang: doc.getAttribute("lang") || "",
  };
}

function slug(url) {
  return url.replace(/^https?:\/\//, "").replace(/[^a-z0-9]+/gi, "_").replace(/^_|_$/g, "").slice(0, 60) || "page";
}

async function main() {
  const opts = parseArgs(process.argv.slice(2));
  if (opts.help || !opts.urls.length) {
    console.log("Aufruf: node responsive_check.mjs <url> [<url> …] [--out <ordner>] [--widths 320,375,…] [--no-shots] [--json]");
    process.exit(opts.help ? 0 : 1);
  }
  const pw = await loadPlaywright();
  if (!pw) {
    console.error("Playwright nicht gefunden. Installieren mit:\n  npm i -D playwright && npx playwright install chromium\n" +
      "Ohne Playwright: Breiten manuell in den DevTools prüfen und im Bericht als „nicht automatisiert geprüft“ vermerken.");
    process.exit(2);
  }
  const launchOpts = {};
  if (process.env.CHROMIUM_PATH) launchOpts.executablePath = process.env.CHROMIUM_PATH;
  let browser;
  try {
    browser = await pw.chromium.launch(launchOpts);
  } catch (e) {
    if (fs.existsSync("/opt/pw-browsers/chromium")) browser = await pw.chromium.launch({ executablePath: "/opt/pw-browsers/chromium" });
    else throw e;
  }

  if (opts.shots) fs.mkdirSync(opts.out, { recursive: true });
  const report = [];
  let problems = 0;

  for (const url of opts.urls) {
    for (const width of opts.widths) {
      const mobile = width < 768;
      const ctx = await browser.newContext({
        viewport: { width, height: mobile ? 800 : 900 },
        deviceScaleFactor: 1,
        isMobile: mobile,
        hasTouch: mobile,
        reducedMotion: "reduce",
      });
      const page = await ctx.newPage();
      const entry = { url, width };
      try {
        await page.goto(url, { waitUntil: "networkidle", timeout: 45000 });
      } catch {
        try { await page.goto(url, { waitUntil: "load", timeout: 30000 }); } catch (e) { entry.error = String(e.message || e); }
      }
      if (!entry.error) {
        // Lazy-Inhalte laden
        await page.evaluate(async () => {
          for (let y = 0; y < document.body.scrollHeight; y += window.innerHeight) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 60)); }
          window.scrollTo(0, 0);
        });
        await page.waitForTimeout(300);
        Object.assign(entry, await page.evaluate(measure, { mobile }));
        if (opts.shots) {
          entry.screenshot = path.join(opts.out, `${slug(url)}_${width}.png`);
          await page.screenshot({ path: entry.screenshot, fullPage: true });
        }
      }
      const p = (entry.error ? 1 : 0) + (entry.overflowPx > 0 ? 1 : 0) + (entry.smallTargetsCount || 0) + (entry.inputsUnder16?.length || 0) +
        (entry.imgNoAlt?.length || 0) + (entry.h1Count === 1 || entry.error ? 0 : 1) + (entry.headingSkips?.length || 0);
      problems += p;
      report.push(entry);
      await ctx.close();
    }
  }
  await browser.close();

  if (opts.json) {
    console.log(JSON.stringify(report, null, 2));
  } else {
    for (const r of report) {
      const head = `${r.width}px`.padEnd(7);
      if (r.error) { console.log(`✗ ${head} ${r.url}  Ladefehler: ${r.error}`); continue; }
      const flags = [];
      if (r.overflowPx > 0) flags.push(`OVERFLOW +${r.overflowPx}px`);
      if (r.smallTargetsCount) flags.push(`${r.smallTargetsCount} Touch-Ziele <44px`);
      if (r.inputsUnder16.length) flags.push(`${r.inputsUnder16.length} Felder <16px`);
      if (r.smallBody.length) flags.push(`Fließtext <16px`);
      if (r.tinyText.length) flags.push(`Text <12px`);
      if (r.imgNoAlt.length) flags.push(`${r.imgNoAlt.length} img ohne alt`);
      if (r.imgNoDims.length) flags.push(`${r.imgNoDims.length} img ohne Maße`);
      if (r.h1Count !== 1) flags.push(`${r.h1Count}× H1`);
      if (r.headingSkips.length) flags.push(`Überschriften-Sprung`);
      console.log(`${flags.length ? "!" : "✓"} ${head} ${r.url}  ${flags.join(" · ") || "ok"}`);
      for (const o of r.offenders) console.log(`     overflow: ${o.el}  (left ${o.left}, right ${o.right}, width ${o.width})`);
      for (const t of r.smallTargets.slice(0, 5)) console.log(`     touch:    ${t.el} „${t.text}“ ${t.w}×${t.h}`);
      for (const t of r.inputsUnder16) console.log(`     input:    ${t.el} ${t.size}px`);
      for (const t of r.smallBody.slice(0, 3)) console.log(`     text:     ${t.el} ${t.size}px „${t.text}“`);
      for (const s of r.headingSkips) console.log(`     heading:  ${s}`);
      for (const s of r.imgNoAlt.slice(0, 3)) console.log(`     alt:      ${s}`);
      for (const s of r.imgNoDims.slice(0, 3)) console.log(`     maße:     ${s}`);
    }
    const first = report.find((r) => !r.error);
    if (first) {
      if (!first.hasMain) console.log("\n! Kein <main>-Element gefunden.");
      if (!first.lang) console.log("! <html> ohne lang-Attribut.");
    }
    if (opts.shots) console.log(`\nScreenshots: ${path.resolve(opts.out)}  (jetzt ansehen: mindestens 375, 768 und 1440)`);
    console.log(problems ? `\n${problems} messbare Auffälligkeiten.` : "\nKeine messbaren Auffälligkeiten. Visuelle Prüfung der Screenshots bleibt nötig.");
  }
}

main().catch((e) => { console.error(e); process.exit(1); });
