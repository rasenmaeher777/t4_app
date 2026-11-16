/* T4 Website – Passwortabfrage (Firebase Authentication)
   Es gibt einen gemeinsamen Zugang: die feste Adresse zugangEmail (firebase-config.js) plus das Passwort,
   das in Firebase unter Authentication → Users gesetzt ist. Die Seite fragt nur das Passwort ab.
   Wichtig: Das hier schützt die Anzeige und, über die Firestore-Regeln, die Aufgaben und Notizen.
   Die HTML-Dateien selbst liegen auf GitHub Pages und bleiben öffentlich abrufbar. */
import { firebaseConfig, zugangEmail } from "./firebase-config.js";

const SDK = "https://www.gstatic.com/firebasejs/10.14.1/";
const wurzel = document.documentElement;
const form = document.getElementById("zugang-form");
const feld = document.getElementById("zugang-passwort");
const meldung = document.getElementById("zugang-meldung");
const knopf = document.getElementById("zugang-los");
const abmelden = document.getElementById("abmelden");
if (form && form.elements.username) { form.elements.username.value = zugangEmail; }

let freigabe;
/* Wird mit der Firebase-App erfüllt, sobald jemand angemeldet ist (aufgaben.js wartet darauf). */
export const angemeldet = new Promise((ok) => { freigabe = ok; });

const merke = (an) => {
  try { if (an) { localStorage.setItem("t4zugang", "1"); } else { localStorage.removeItem("t4zugang"); } } catch (e) {}
};
const zeigeMeldung = (text) => { meldung.textContent = text; };

const fehlerText = (err) => {
  const code = err && err.code ? err.code : "";
  if (code === "auth/invalid-credential" || code === "auth/wrong-password" || code === "auth/user-not-found") { return "Falsches Passwort."; }
  if (code === "auth/too-many-requests") { return "Zu viele Versuche. Bitte später noch einmal probieren."; }
  if (code === "auth/network-request-failed") { return "Keine Verbindung. Bitte Internetverbindung prüfen."; }
  if (code === "auth/configuration-not-found") { return "In Firebase ist Authentication noch nicht eingerichtet (Anleitung in der README)."; }
  if (code === "auth/operation-not-allowed") { return "In Firebase ist die Anmeldung mit E-Mail und Passwort noch nicht aktiviert."; }
  return "Anmeldung nicht möglich (" + (code || (err && err.message) || "unbekannter Fehler") + ").";
};

async function start() {
  if (!firebaseConfig.projectId || firebaseConfig.projectId.indexOf("HIER") === 0) {
    /* Firebase noch nicht eingerichtet: nichts sperren, sonst käme niemand mehr auf die Seite */
    wurzel.classList.remove("gesperrt");
    return;
  }

  let app, au;
  try {
    const geladen = await Promise.all([import(SDK + "firebase-app.js"), import(SDK + "firebase-auth.js")]);
    app = geladen[0].initializeApp(firebaseConfig);
    au = geladen[1];
  } catch (err) {
    zeigeMeldung("Die Anmeldung konnte nicht geladen werden. Bitte Internetverbindung prüfen.");
    return;
  }
  const auth = au.getAuth(app);

  au.onAuthStateChanged(auth, (nutzer) => {
    if (nutzer) {
      merke(true);
      wurzel.classList.remove("gesperrt");
      if (abmelden) { abmelden.parentElement.hidden = false; }
      freigabe(app);
    } else {
      merke(false);
      wurzel.classList.add("gesperrt");
      if (abmelden) { abmelden.parentElement.hidden = true; }
      if (feld) { feld.focus(); }
    }
  });

  form.addEventListener("submit", async (ev) => {
    ev.preventDefault();
    if (!feld.value) { feld.focus(); return; }
    knopf.disabled = true;
    zeigeMeldung("");
    try {
      await au.signInWithEmailAndPassword(auth, zugangEmail, feld.value);
      feld.value = "";
    } catch (err) {
      zeigeMeldung(fehlerText(err));
      feld.select();
    }
    knopf.disabled = false;
  });

  if (abmelden) {
    abmelden.addEventListener("click", async (ev) => {
      ev.preventDefault();
      try { await au.signOut(auth); } catch (err) { /* egal */ }
      merke(false);
      window.location.reload();
    });
  }
}

start();
