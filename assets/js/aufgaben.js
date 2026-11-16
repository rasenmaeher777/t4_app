/* T4 Multivan 1994 – Aufgaben und Notizen (Firestore)
   Sammlung „aufgaben“: ein Dokument je Aufgabe { titel, frist ("JJJJ-MM-TT" oder null), details, erstellt, geaendert }
   Dokument „notizen/bus“: { text, geaendert }
   Alle Texte werden nur mit textContent/value in die Seite geschrieben, nie als HTML. */
import { firebaseConfig } from "./firebase-config.js";
import { angemeldet } from "./zugang.js";

const SDK = "https://www.gstatic.com/firebasejs/10.14.1/";

const $ = (id) => document.getElementById(id);
const el = (tag, klasse, text) => {
  const n = document.createElement(tag);
  if (klasse) { n.className = klasse; }
  if (text !== undefined) { n.textContent = text; }
  return n;
};

const aufgabenStatus = $("aufgaben-status");
const notizenStatus = $("notizen-status");
const liste = $("aufgaben-liste");
const formular = $("aufgaben-form");
const notizFeld = $("notizen-text");

const pad = (n) => String(n).padStart(2, "0");
const heute = () => { const d = new Date(); return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate()); };
const fristText = (s) => {
  const t = s.split("-").map(Number);
  return new Date(t[0], t[1] - 1, t[2]).toLocaleDateString("de-DE", { weekday: "short", day: "2-digit", month: "2-digit", year: "numeric" });
};

const fehlerText = (err) => {
  var code = err && err.code ? err.code : "";
  if (code === "permission-denied") { return "Zugriff verweigert. Die Sicherheitsregeln in Firestore erlauben diese Aktion nicht."; }
  if (code === "unavailable") { return "Keine Verbindung zu Firestore. Bitte Internetverbindung prüfen."; }
  return "Fehler: " + (err && err.message ? err.message : err);
};

const zeigeStatus = (feld, text, fehler) => {
  feld.textContent = text;
  feld.classList.toggle("fehler", !!fehler);
};

/* Formular für neue Aufgaben: erst nach Klick auf „+“ sichtbar */
const plus = $("aufgabe-plus");
const formularOeffnen = (auf) => {
  formular.hidden = !auf;
  plus.setAttribute("aria-expanded", auf ? "true" : "false");
  plus.classList.toggle("offen", auf);
  plus.title = auf ? "Abbrechen" : "Neue Aufgabe";
  plus.setAttribute("aria-label", plus.title);
  if (auf) { $("aufgabe-titel").focus(); } else { formular.reset(); }
};
plus.addEventListener("click", () => formularOeffnen(formular.hidden));
$("aufgabe-abbrechen").addEventListener("click", () => formularOeffnen(false));
formular.addEventListener("keydown", (ev) => { if (ev.key === "Escape") { formularOeffnen(false); plus.focus(); } });

const sperren = (grund) => {
  zeigeStatus(aufgabenStatus, grund, true);
  zeigeStatus(notizenStatus, grund, true);
  plus.disabled = true;
  formular.querySelectorAll("input, textarea, button").forEach((n) => { n.disabled = true; });
  notizFeld.disabled = true;
};

async function start() {
  if (!firebaseConfig.projectId || firebaseConfig.projectId.indexOf("HIER") === 0) {
    sperren("Noch nicht eingerichtet: In assets/js/firebase-config.js fehlen die Firebase-Zugangsdaten (Anleitung in der README.md).");
    return;
  }

  /* Erst nach der Anmeldung (zugang.js) auf die Datenbank zugreifen; die Firestore-Regeln verlangen sie */
  var app, fs;
  try {
    app = await angemeldet;
    fs = await import(SDK + "firebase-firestore.js");
  } catch (err) {
    sperren("Firestore konnte nicht geladen werden. Bitte Internetverbindung prüfen.");
    return;
  }
  var db = fs.getFirestore(app);

  /* ---------- Aufgaben ---------- */
  var alle = [];
  var bearbeiteId = null;
  var nachgezeichnet = false;

  var sortiere = function (a, b) {
    /* Frist: spätestes Datum zuerst; Aufgaben ohne Frist ganz unten */
    if (a.frist && b.frist && a.frist !== b.frist) { return a.frist < b.frist ? 1 : -1; }
    if (!!a.frist !== !!b.frist) { return a.frist ? -1 : 1; }
    return b.erstellt - a.erstellt;
  };

  var feldMitLabel = function (text, feld) {
    var l = el("label", "feld");
    l.appendChild(el("span", "", text));
    l.appendChild(feld);
    return l;
  };

  /* Symbole (feste Zeichenketten, keine Nutzerdaten) */
  var ICON_STIFT = '<path d="M17 3a2.83 2.83 0 0 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"/>';
  var ICON_PAPIERKORB = '<path d="M3 6h18"/><path d="M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2"/><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/><path d="M10 11v6M14 11v6"/>';
  var iconKnopf = function (pfade, beschriftung, klasse) {
    var b = el("button", "icon " + klasse);
    b.type = "button";
    b.title = beschriftung;
    b.setAttribute("aria-label", beschriftung);
    b.innerHTML = '<svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + pfade + "</svg>";
    return b;
  };

  var zeileAnzeigen = function (a) {
    var li = el("li", "aufgabe");
    var text = el("div", "aufgabe-text");
    text.appendChild(el("b", "", a.titel));
    if (a.details) { text.appendChild(el("p", "aufgabe-details", a.details)); }
    li.appendChild(text);
    var seite = el("div", "aufgabe-seite");
    if (a.frist) {
      var f = el("span", "frist", fristText(a.frist));
      if (a.frist < heute()) { f.classList.add("ueberfaellig"); f.textContent += " · überfällig"; }
      else if (a.frist === heute()) { f.classList.add("heute"); f.textContent += " · heute"; }
      seite.appendChild(f);
    } else {
      seite.appendChild(el("span", "frist ohne", "ohne Frist"));
    }
    var knoepfe = el("div", "icons");
    var bearb = iconKnopf(ICON_STIFT, "Aufgabe bearbeiten", "");
    bearb.addEventListener("click", function () { bearbeiteId = a.id; zeichne(); });
    var weg = iconKnopf(ICON_PAPIERKORB, "Aufgabe löschen", "gefahr");
    weg.addEventListener("click", async function () {
      if (!window.confirm("Aufgabe „" + a.titel + "“ löschen?")) { return; }
      try { await fs.deleteDoc(fs.doc(db, "aufgaben", a.id)); }
      catch (err) { zeigeStatus(aufgabenStatus, fehlerText(err), true); }
    });
    knoepfe.appendChild(bearb);
    knoepfe.appendChild(weg);
    seite.appendChild(knoepfe);
    li.appendChild(seite);
    return li;
  };

  var zeileBearbeiten = function (a) {
    var li = el("li", "aufgabe bearbeiten");
    var form = el("form", "aufgaben-form");
    var titel = el("input"); titel.type = "text"; titel.maxLength = 120; titel.required = true; titel.value = a.titel;
    var frist = el("input"); frist.type = "date"; frist.value = a.frist || "";
    var details = el("textarea"); details.rows = 2; details.maxLength = 1000; details.value = a.details || "";
    form.appendChild(feldMitLabel("Aufgabe", titel));
    form.appendChild(feldMitLabel("Frist", frist));
    var detailsFeld = feldMitLabel("Details (optional)", details);
    detailsFeld.classList.add("breit");
    form.appendChild(detailsFeld);
    var knoepfe = el("div", "knoepfe");
    var ok = el("button", "knopf", "Speichern"); ok.type = "submit";
    var nein = el("button", "knopf leise", "Abbrechen"); nein.type = "button";
    nein.addEventListener("click", function () { bearbeiteId = null; zeichne(); });
    knoepfe.appendChild(ok);
    knoepfe.appendChild(nein);
    form.appendChild(knoepfe);
    form.addEventListener("submit", async function (ev) {
      ev.preventDefault();
      var t = titel.value.trim();
      if (!t) { titel.focus(); return; }
      ok.disabled = true;
      try {
        await fs.updateDoc(fs.doc(db, "aufgaben", a.id), {
          titel: t, frist: frist.value || null, details: details.value.trim(), geaendert: fs.serverTimestamp(),
        });
        bearbeiteId = null;
        zeichne();
      } catch (err) {
        ok.disabled = false;
        zeigeStatus(aufgabenStatus, fehlerText(err), true);
      }
    });
    li.appendChild(form);
    return li;
  };

  var zeichne = function () {
    liste.textContent = "";
    if (!nachgezeichnet) { return; }
    if (!alle.length) {
      liste.appendChild(el("li", "leer-hinweis", "Noch keine Aufgaben. Oben eine hinzufügen, z. B. „Ölwechsel“ oder „Reifenwechsel“."));
      return;
    }
    alle.slice().sort(sortiere).forEach(function (a) {
      liste.appendChild(a.id === bearbeiteId ? zeileBearbeiten(a) : zeileAnzeigen(a));
    });
  };

  formular.addEventListener("submit", async function (ev) {
    ev.preventDefault();
    var titel = $("aufgabe-titel"), frist = $("aufgabe-frist"), details = $("aufgabe-details");
    var t = titel.value.trim();
    if (!t) { titel.focus(); return; }
    var knopf = formular.querySelector("button[type=submit]");
    knopf.disabled = true;
    try {
      await fs.addDoc(fs.collection(db, "aufgaben"), {
        titel: t, frist: frist.value || null, details: details.value.trim(),
        erstellt: fs.serverTimestamp(), geaendert: fs.serverTimestamp(),
      });
      formularOeffnen(false);
      zeigeStatus(aufgabenStatus, "", false);
    } catch (err) {
      zeigeStatus(aufgabenStatus, fehlerText(err), true);
    }
    knopf.disabled = false;
  });

  zeigeStatus(aufgabenStatus, "Lädt …", false);
  fs.onSnapshot(fs.collection(db, "aufgaben"), function (snap) {
    alle = snap.docs.map(function (d) {
      var x = d.data({ serverTimestamps: "estimate" });
      return {
        id: d.id, titel: x.titel || "", frist: x.frist || null, details: x.details || "",
        erstellt: x.erstellt && x.erstellt.toMillis ? x.erstellt.toMillis() : 0,
      };
    });
    nachgezeichnet = true;
    zeigeStatus(aufgabenStatus, "", false);
    /* Während der Bearbeitung nicht neu zeichnen, sonst gehen Eingaben verloren */
    if (bearbeiteId === null) { zeichne(); }
  }, function (err) {
    zeigeStatus(aufgabenStatus, fehlerText(err), true);
  });

  /* ---------- Notizen ---------- */
  var notizRef = fs.doc(db, "notizen", "bus");
  var geaendert = false;      /* Eingabe noch nicht gespeichert */
  var timer = null;

  var speichern = async function () {
    clearTimeout(timer);
    if (!geaendert) { return; }
    geaendert = false;
    zeigeStatus(notizenStatus, "Speichert …", false);
    try {
      await fs.setDoc(notizRef, { text: notizFeld.value, geaendert: fs.serverTimestamp() });
      if (!geaendert) { zeigeStatus(notizenStatus, "Gespeichert", false); }
    } catch (err) {
      geaendert = true;
      zeigeStatus(notizenStatus, fehlerText(err), true);
    }
  };

  notizFeld.addEventListener("input", function () {
    geaendert = true;
    zeigeStatus(notizenStatus, "Nicht gespeichert …", false);
    clearTimeout(timer);
    timer = setTimeout(speichern, 800);
  });
  notizFeld.addEventListener("blur", speichern);
  document.addEventListener("visibilitychange", function () { if (document.hidden) { speichern(); } });
  window.addEventListener("pagehide", speichern);

  zeigeStatus(notizenStatus, "Lädt …", false);
  notizFeld.disabled = true;
  fs.onSnapshot(notizRef, function (snap) {
    notizFeld.disabled = false;
    /* Eigene, noch nicht bestätigte Änderungen und laufende Eingabe nicht überschreiben */
    if (!snap.metadata.hasPendingWrites && !geaendert) {
      var neu = snap.exists() ? (snap.data().text || "") : "";
      if (neu !== notizFeld.value) { notizFeld.value = neu; }
    }
    if (!geaendert) { zeigeStatus(notizenStatus, snap.exists() ? "Gespeichert" : "Noch leer", false); }
  }, function (err) {
    notizFeld.disabled = true;
    zeigeStatus(notizenStatus, fehlerText(err), true);
  });
}

start();
