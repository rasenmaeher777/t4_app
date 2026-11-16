/* Wird im <head> vor allem anderen geladen: Merkt sich auf diesem Gerät, dass das Passwort schon
   eingegeben wurde. Fehlt der Merker, bleibt die Seite hinter der Passwortabfrage verborgen,
   bis zugang.js die Anmeldung geprüft hat. Sicherheit gibt das nicht, nur Ruhe beim Laden. */
(function () {
  var an = true;
  try { an = localStorage.getItem("t4zugang") !== "1"; } catch (e) {}
  if (an) { document.documentElement.className += " gesperrt"; }
})();
