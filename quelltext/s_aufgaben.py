"""Kapitel „Aufgaben“: Aufgabenliste und Notizen, gespeichert in Firestore (siehe assets/js/aufgaben.js)."""
from helfer import *


def aufgaben():
    liste = abschnitt("aufgaben", "", "Aufgaben", """
<button type="button" class="plus" id="aufgabe-plus" aria-expanded="false" aria-controls="aufgaben-form" aria-label="Neue Aufgabe" title="Neue Aufgabe"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button>
<form class="aufgaben-form neu" id="aufgaben-form" autocomplete="off" hidden>
  <label class="feld"><span>Aufgabe</span><input type="text" id="aufgabe-titel" maxlength="120" required placeholder="z. B. Ölwechsel"></label>
  <label class="feld"><span>Frist</span><input type="date" id="aufgabe-frist"></label>
  <label class="feld breit"><span>Details (optional)</span><textarea id="aufgabe-details" rows="2" maxlength="1000" placeholder="z. B. 5,5 l 10W-40, Filter und Dichtring"></textarea></label>
  <div class="knoepfe"><button type="submit" class="knopf">Hinzufügen</button><button type="button" class="knopf leise" id="aufgabe-abbrechen">Abbrechen</button></div>
</form>
<p class="status" id="aufgaben-status" role="status" aria-live="polite"></p>
<ul class="aufgaben-liste" id="aufgaben-liste"></ul>
""")
    notizen = abschnitt("notizen", "", "Notizen", """
<p>Ein freies Textfeld für alles, was man zum Bus festhalten will. Wird beim Tippen automatisch gespeichert.</p>
<textarea class="notizen" id="notizen-text" rows="12" maxlength="20000" aria-label="Notizen zum Bus" placeholder="Notizen zum Bus …"></textarea>
<p class="status" id="notizen-status" role="status" aria-live="polite"></p>
""")
    return dict(
        datei="aufgaben.html",
        titel="Aufgaben – VW T4 Multivan 2.4 D, Baujahr 1994",
        beschreibung="Aufgabenliste mit Fristen und Notizen zum VW T4 Multivan.",
        kopf=kopf("", "Aufgaben"),
        inhalt=liste + notizen,
        sprungmarken=[("aufgaben", "Aufgaben"), ("notizen", "Notizen")],
        skripte='<script type="module" src="assets/js/aufgaben.js"></script>',
    )
