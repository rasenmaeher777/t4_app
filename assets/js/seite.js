/* T4 Multivan 1994 – Suche und Seitenleiste */
(function () {
  "use strict";

  var sauber = function (s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); };
  var norm = function (s) { return s.toLowerCase().replace(/ä/g, "ae").replace(/ö/g, "oe").replace(/ü/g, "ue").replace(/ß/g, "ss"); };

  /* ---------- Suche ---------- */
  var feld = document.getElementById("suchfeld");
  var box = document.getElementById("treffer");
  if (feld && box) {
    var suchen = function () {
      var index = window.SUCHINDEX || [];
      var worte = norm(feld.value.trim()).split(/\s+/).filter(Boolean);
      if (!worte.length) { box.hidden = true; box.innerHTML = ""; return; }
      var funde = [];
      index.forEach(function (e) {
        var k = norm(e.k), alles = k + " " + norm(e.v) + " " + norm(e.o);
        if (!worte.every(function (w) { return alles.indexOf(w) !== -1; })) { return; }
        var rang = worte.every(function (w) { return k.indexOf(w) !== -1; }) ? (k.indexOf(worte[0]) === 0 ? 0 : 1) : 2;
        funde.push({ rang: rang, e: e });
      });
      funde.sort(function (a, b) { return a.rang - b.rang; });
      if (!funde.length) { box.innerHTML = "<p>Nichts gefunden.</p>"; box.hidden = false; return; }
      box.innerHTML = funde.slice(0, 14).map(function (f) {
        return '<a href="' + f.e.z + '"><b>' + sauber(f.e.k) + "</b>" + (f.e.v ? " – " + sauber(f.e.v) : "") + "<small>" + sauber(f.e.o) + "</small></a>";
      }).join("");
      box.hidden = false;
    };
    /* iPhone: Die Tastatur verdeckt die untere Bildschirmhälfte, ohne die Seite zu verkleinern.
       Darum die Trefferliste nur so hoch machen, wie über der Tastatur Platz ist. */
    var passeHoehe = function () {
      if (box.hidden) { return; }
      var vv = window.visualViewport;
      var sichtbar = vv ? vv.height : window.innerHeight;
      var oben = box.getBoundingClientRect().top - (vv ? vv.offsetTop : 0);
      box.style.maxHeight = Math.max(150, Math.min(sichtbar - oben - 12, sichtbar * 0.7)) + "px";
    };
    var suchenUndPassen = function () { suchen(); passeHoehe(); };
    if (window.visualViewport) {
      window.visualViewport.addEventListener("resize", passeHoehe);
      window.visualViewport.addEventListener("scroll", passeHoehe);
    }
    feld.addEventListener("input", suchenUndPassen);
    feld.addEventListener("focus", suchenUndPassen);
    feld.addEventListener("keydown", function (ev) {
      if (ev.key === "Enter") { var erster = box.querySelector("a"); if (erster) { window.location.href = erster.getAttribute("href"); } }
      if (ev.key === "Escape") { box.hidden = true; feld.blur(); }
    });
    document.addEventListener("click", function (ev) {
      if (!ev.target.closest(".suche")) { box.hidden = true; }
      else if (ev.target.closest(".treffer a")) { try { sessionStorage.setItem("t4suche", ev.target.closest("a").querySelector("b").textContent); } catch (e) {} box.hidden = true; feld.value = ""; }
    });
  }

  /* Nach einem Suchtreffer: eingeklappten Bereich mit dem Treffer öffnen */
  var oeffneTreffer = function () {
    var wort; try { wort = sessionStorage.getItem("t4suche"); sessionStorage.removeItem("t4suche"); } catch (e) {}
    var ziel = location.hash ? document.getElementById(location.hash.slice(1)) : null;
    if (!wort || !ziel) { return; }
    var gefunden = null;
    ziel.querySelectorAll("details").forEach(function (d) {
      if (!gefunden && d.textContent.indexOf(wort) !== -1 && !d.classList.contains("quellen")) { d.open = true; gefunden = d; }
    });
    if (gefunden) { gefunden.scrollIntoView({ block: "center" }); }
  };
  oeffneTreffer();
  window.addEventListener("hashchange", oeffneTreffer);

  /* Aktuellen Abschnitt in der Seitenleiste markieren */
  var tocLinks = document.querySelectorAll(".toc a");
  if (tocLinks.length && "IntersectionObserver" in window) {
    var beobachter = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (ein) {
        if (!ein.isIntersecting) { return; }
        tocLinks.forEach(function (a) { a.classList.toggle("aktiv", a.getAttribute("href") === "#" + ein.target.id); });
      });
    }, { rootMargin: "-80px 0px -65% 0px" });
    document.querySelectorAll(".abschnitt[id]").forEach(function (s) { beobachter.observe(s); });
  }

})();
