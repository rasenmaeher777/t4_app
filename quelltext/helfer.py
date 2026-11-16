"""Bausteine für die Seiten: Layout, Tabellen, Hinweise, Links."""
import html
import json
import os
import urllib.parse

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAND = "November 2026"

NAVI = [
    ("index.html", "Start"),
    ("technik.html", "Technik"),
    ("fahrdaten.html", "Fahrdaten"),
    ("wartung.html", "Wartung"),
    ("ausstattung.html", "Ausstattung"),
    ("geschichte.html", "Geschichte"),
    ("fakten.html", "Fakten"),
]


def daten(name):
    with open(os.path.join(WURZEL, "daten", name), encoding="utf-8") as f:
        return json.load(f)


def e(text):
    return html.escape(str(text), quote=True)


def geld(wert):
    return f"{wert:,.0f}".replace(",", ".") + " €"


def tsd(wert):
    return f"{wert:,.0f}".replace(",", ".")


# ---------- Links ----------
def ext(url, text):
    return f'<a href="{e(url)}" target="_blank" rel="noopener">{text}</a>'


def wiki(seite, text=None):
    """Textlink auf eine Seite des T4-Wiki."""
    url = "https://www.t4-wiki.de/wiki/" + urllib.parse.quote(seite.replace(" ", "_"))
    return ext(url, text or e(seite))


def wikibild(datei, text):
    """Textlink auf ein Bild im T4-Wiki (wird bewusst nicht eingebettet)."""
    url = "https://www.t4-wiki.de/wiki/Datei:" + urllib.parse.quote(datei)
    return ext(url, text)


# ---------- Inhaltsbausteine ----------
def kv(paare):
    """Schlüssel/Wert-Liste. paare: (Bezeichnung, Wert) oder (Bezeichnung, Wert, Zusatz)."""
    teile = []
    for p in paare:
        zusatz = f"<small>{p[2]}</small>" if len(p) > 2 and p[2] else ""
        teile.append(f"<dt>{p[0]}</dt><dd>{p[1]}{zusatz}</dd>")
    return '<dl class="kv">' + "".join(teile) + "</dl>"


def tab(kopf, zeilen, rechts=(), mein=(), stapel=True, titel=None, kopfspalte=False):
    """Tabelle, die auf dem iPhone zu Karten umbricht.
    rechts: Spaltennummern mit Zahlen (rechtsbündig); mein: Zeilennummern, die hervorgehoben werden."""
    k = "".join(f'<th scope="col"{" class=z" if i in rechts else ""}>{h}</th>' for i, h in enumerate(kopf))
    body = []
    for zi, z in enumerate(zeilen):
        zellen = []
        for i, zelle in enumerate(z):
            klassen = []
            if i in rechts:
                klassen.append("z")
            if zelle in ("", None, "–"):
                klassen.append("leer") if zelle in ("", None) else None
            kl = f' class="{" ".join(klassen)}"' if klassen else ""
            marke = "th" if (kopfspalte and i == 0) else "td"
            scope = ' scope="row"' if marke == "th" else ""
            zellen.append(f'<{marke}{scope}{kl} data-t="{e(_ohne_tags(kopf[i]))}">{"" if zelle is None else zelle}</{marke}>')
        body.append(f'<tr{" class=mein" if zi in mein else ""}>{"".join(zellen)}</tr>')
    cap = f"<caption>{titel}</caption>" if titel else ""
    return (f'<div class="tab-huelle"><table class="tab{" stapel" if stapel else ""}">{cap}'
            f'<thead><tr>{k}</tr></thead><tbody>{"".join(body)}</tbody></table></div>')


def _ohne_tags(text):
    import re
    return html.unescape(re.sub(r"<[^>]+>", " ", str(text))).strip()


def hinweis(titel, text):
    return f'<div class="hinweis"><b>{titel}</b>{text}</div>'


def warnung(titel, text):
    return f'<div class="warnung"><b>{titel}</b>{text}</div>'


def karte(titel, text, etikett=None, art=""):
    """Zeile einer Punktliste: Titel links, Text rechts."""
    klasse = {"voll": " wichtig", "signal": " offen"}.get(art, "")
    et = f'<span class="marke{klasse}">{etikett}</span>' if etikett else ""
    return f'<li class="punkt"><div><b>{titel}</b>{et}</div><p>{text}</p></li>'


def karten(*eintraege):
    return '<ul class="karten">' + "".join(eintraege) + "</ul>"


def mehr(titel, inhalt):
    """Ausklappbarer Bereich für Details."""
    return f'<details class="mehr"><summary>{titel}</summary><div class="mehr-inhalt">{inhalt}</div></details>'


def klappliste(eintraege):
    """Liste, bei der jeder Punkt aufklappbar ist. eintraege: (Titel, Text) oder (Titel, Text, Zusatz)."""
    teile = []
    for ein in eintraege:
        zusatz = f'<span class="marke">{ein[2]}</span>' if len(ein) > 2 and ein[2] else ""
        teile.append(f'<details class="klapp"><summary><b>{ein[0]}</b>{zusatz}</summary><p>{ein[1]}</p></details>')
    return '<div class="klappliste">' + "".join(teile) + "</div>"


def abschnitt(anker, nr, titel, inhalt, vorspann=None):
    """Abschnitt mit Überschrift. Kleingedruckte Quellenzeilen wandern in einen ausklappbaren Bereich am Ende."""
    import re
    quellen = re.findall(r'<p class="klein"[^>]*>(.*?)</p>', inhalt, flags=re.S)
    if quellen:
        inhalt = re.sub(r'<p class="klein"[^>]*>.*?</p>', "", inhalt, flags=re.S)
        inhalt += ('<details class="mehr quellen"><summary>Quellen und Links</summary><div class="mehr-inhalt">'
                   + "".join(f"<p>{q}</p>" for q in quellen) + "</div></details>")
    return f'<section class="abschnitt" id="{anker}"><h2>{titel}</h2>{inhalt}</section>'


def bild(name, alt, breiten, sizes, lazy=True, klasse=""):
    """Eigenes Bild aus assets/img in zwei Größen."""
    gross, klein = breiten
    masse = BILDMASSE[name]
    return (f'<img src="assets/img/{name}-{klein}.png" srcset="assets/img/{name}-{klein}.png {klein}w, '
            f'assets/img/{name}-{gross}.png {gross}w" sizes="{sizes}" width="{masse[0]}" height="{masse[1]}" '
            f'alt="{e(alt)}"{" loading=lazy" if lazy else " fetchpriority=high"} decoding="async"{f" class={klasse}" if klasse else ""}>')


BILDMASSE = {"t4-front": (1600, 1117), "t4-heck": (1600, 1033), "emblem": (720, 559)}


# ---------- Seitenrahmen ----------
SEITENNAME = "VW T4 Multivan 2.4 D"


def rahmen(datei, titel, beschreibung, kopf, inhalt, sprungmarken=None):
    nav = "".join(
        f'<li><a href="{d}"{" aria-current=page" if d == datei else ""}>{n}</a></li>' for d, n in NAVI
    )
    toc = ""
    if sprungmarken:
        toc = ('<aside class="toc"><b>Auf dieser Seite</b><ul>'
               + "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in sprungmarken) + "</ul></aside>")
    namen = [d for d, _ in NAVI]
    weiter = ""
    if datei in namen and datei != "index.html":
        pos = namen.index(datei)
        vor = NAVI[pos - 1]
        nach = NAVI[pos + 1] if pos < len(NAVI) - 1 else ("quellen.html", "Quellen")
        weiter = (f'<nav class="weiter" aria-label="Blättern"><a href="{vor[0]}">← {vor[1]}</a>'
                  f'<a href="{nach[0]}">{nach[1]} →</a></nav>')
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light only">
<meta name="theme-color" content="#252525">
<meta name="format-detection" content="telephone=no">
<title>{e(titel)}</title>
<meta name="description" content="{e(beschreibung)}">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="48x48" href="assets/img/favicon-48.png">
<link rel="apple-touch-icon" sizes="180x180" href="assets/img/apple-touch-icon.png">
<link rel="manifest" href="manifest.webmanifest">
<meta name="apple-mobile-web-app-title" content="T4 Multivan">
<meta name="application-name" content="T4 Multivan">
<link rel="stylesheet" href="assets/css/stil.css">
</head>
<body>
<header class="titel"><div class="innen"><div class="titel-text">{kopf}</div><img class="logo" src="assets/img/emblem-frei-120.png" srcset="assets/img/emblem-frei-120.png 1x, assets/img/emblem-frei-240.png 2x" width="119" height="120" alt="VW-Emblem"></div></header>
<nav class="navi" aria-label="Hauptmenü"><div class="innen">
  <ul class="menue">{nav}</ul>
  <div class="suche"><input type="search" id="suchfeld" placeholder="Suchen" aria-label="Seite durchsuchen" autocomplete="off"><div class="treffer" id="treffer" hidden></div></div>
</div></nav>
<div class="innen seite{"" if toc else " ohne-toc"}">
{toc}
<main id="inhalt">
{inhalt}
{weiter}
</main>
</div>
<footer class="fuss"><div class="innen">
  <p>Private, nicht kommerzielle Seite. Keine Verbindung zur Volkswagen AG; „Volkswagen“, „VW“ und „Multivan“ sind Marken der Volkswagen AG.</p>
  <p>Alle Angaben ohne Gewähr. Stand: {STAND}. <a href="quellen.html">Quellen und Bildnachweise</a></p>
</div></footer>
<script src="assets/js/suchindex.js" defer></script>
<script src="assets/js/seite.js" defer></script>
</body>
</html>
"""


def kopf(ueber, h1, unter=None, marken=None):
    """Titelblock. Auf Unterseiten steht darüber ein Link zur Startseite."""
    if marken:  # Startseite
        return f'<h1>{h1}</h1><p class="unter">{" · ".join(marken)}</p>'
    return f'<a class="heim" href="index.html">{SEITENNAME} · Baujahr 1994</a><h1>{h1}</h1>'
