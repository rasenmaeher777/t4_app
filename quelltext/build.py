#!/usr/bin/env python3
"""Baut die Website aus den Inhaltsdateien in diesem Ordner.

Aufruf (im Projektordner):   python3 quelltext/build.py

Die fertigen HTML-Dateien landen im Projektordner (index.html usw.).
Inhalte ändern: die Dateien s_*.py bearbeiten und das Skript erneut ausführen.
Gestaltung ändern: assets/css/stil.css (kein erneutes Bauen nötig).
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import helfer  # noqa: E402
import s_ausstattung  # noqa: E402
import s_fahrdaten_wartung  # noqa: E402
import s_geschichte_fakten  # noqa: E402
import s_start_technik  # noqa: E402

SEITEN = [
    s_start_technik.start,
    s_start_technik.technik,
    s_fahrdaten_wartung.fahrdaten,
    s_fahrdaten_wartung.wartung,
    s_ausstattung.ausstattung,
    s_geschichte_fakten.geschichte,
    s_geschichte_fakten.fakten,
    s_geschichte_fakten.quellen,
]

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#252525"/><text x="32" y="43" text-anchor="middle" font-family="Impact,Arial Narrow,sans-serif" font-size="34" fill="#F3F0F0" letter-spacing="-1">T4</text></svg>
"""


def schreibe(pfad, text):
    with open(os.path.join(helfer.WURZEL, pfad), "w", encoding="utf-8") as f:
        f.write(text)


def ohne_tags(text):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text))).strip()


def suchindex(seiten):
    """Sammelt Abschnitte, Datenzeilen und Tabellenzeilen aller Seiten für das Suchfeld."""
    namen = dict(helfer.NAVI)
    eintraege = []
    for s in seiten:
        seite = namen.get(s["datei"], "Quellen")
        for anker, titel, inhalt in re.findall(r'<section class="abschnitt" id="([^"]+)"><h2>(.*?)</h2>(.*?)</section>', s["inhalt"], flags=re.S):
            if anker == "inhalt-uebersicht":
                continue
            ziel, ort = f'{s["datei"]}#{anker}', f"{seite} › {ohne_tags(titel)}"
            eintraege.append({"k": ohne_tags(titel), "v": "", "o": seite, "z": ziel})
            for dt, dd in re.findall(r"<dt>(.*?)</dt><dd>(.*?)</dd>", inhalt, flags=re.S):
                eintraege.append({"k": ohne_tags(dt), "v": ohne_tags(dd), "o": ort, "z": ziel})
            for zeile in re.findall(r"<tr[^>]*>(.*?)</tr>", inhalt, flags=re.S):
                if 'scope="col"' in zeile or "<th>" in zeile:
                    continue
                zellen = [ohne_tags(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", zeile, flags=re.S)]
                if zellen and zellen[0]:
                    eintraege.append({"k": zellen[0], "v": " · ".join(c for c in zellen[1:] if c)[:220], "o": ort, "z": ziel})
            for titel2, text in re.findall(r'<li class="punkt"><div><b>(.*?)</b>.*?</div><p>(.*?)</p></li>', inhalt, flags=re.S):
                eintraege.append({"k": ohne_tags(titel2), "v": ohne_tags(text)[:220], "o": ort, "z": ziel})
            for titel2, text in re.findall(r'<details class="klapp"><summary><b>(.*?)</b>.*?</summary><p>(.*?)</p></details>', inhalt, flags=re.S):
                eintraege.append({"k": ohne_tags(titel2), "v": ohne_tags(text)[:220], "o": ort, "z": ziel})
            for zeit, was, text in re.findall(r"<li[^>]*><time>(.*?)</time><b>(.*?)</b><p>(.*?)</p></li>", inhalt, flags=re.S):
                eintraege.append({"k": f"{ohne_tags(zeit)}: {ohne_tags(was)}", "v": ohne_tags(text)[:220], "o": ort, "z": ziel})
    return eintraege


def main():
    seiten = [funktion() for funktion in SEITEN]
    uebersicht = '<ul class="inhalt-liste">' + "".join(
        f'<li><a href="{s["datei"]}">{dict(helfer.NAVI)[s["datei"]]}</a><span>'
        + " · ".join(f'<a href="{s["datei"]}#{a}">{t}</a>' for a, t in s["sprungmarken"]) + "</span></li>"
        for s in seiten if s.get("sprungmarken")) + "</ul>"  # nicht mehr verwendet
    for s in seiten:
        s["inhalt"] = s["inhalt"].replace("<!--INHALT-->", uebersicht)
        schreibe(s["datei"], helfer.rahmen(s["datei"], s["titel"], s["beschreibung"], s["kopf"], s["inhalt"], s.get("sprungmarken")))
        print("geschrieben:", s["datei"])
    schreibe("404.html", helfer.rahmen(
        "404.html", "Seite nicht gefunden", "Diese Seite gibt es nicht.",
        helfer.kopf("", "Seite nicht gefunden"),
        '<section class="abschnitt"><p>Diese Seite gibt es nicht. <a href="index.html">Zur Startseite</a></p></section>'))
    index = suchindex(seiten)
    schreibe(os.path.join("assets", "js", "suchindex.js"), "window.SUCHINDEX = " + json.dumps(index, ensure_ascii=False, separators=(",", ":")) + ";\n")
    print("Suchindex:", len(index), "Einträge")
    schreibe("manifest.webmanifest", json.dumps({
        "name": "VW T4 Multivan 2.4 D", "short_name": "T4 Multivan", "lang": "de",
        "start_url": "index.html", "scope": "./", "display": "standalone",
        "background_color": "#F3F0F0", "theme_color": "#252525",
        "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}],
    }, ensure_ascii=False, indent=2) + "\n")
    schreibe(".nojekyll", "")
    print("fertig.")


if __name__ == "__main__":
    main()
