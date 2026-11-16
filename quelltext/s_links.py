"""Kapitel „Links“: Foren und Wiki zum T4, dazu die Betriebsanleitung als PDF zum Herunterladen."""
from helfer import *

PDF_DATEI = "assets/dokumente/1991_VWT4_Transporter_Betriebsanleitung.pdf"


def links():
    websites = abschnitt("websites", "", "Foren und Wiki", karten(
        karte(ext("https://www.t4-wiki.de/", "T4-Wiki"),
              "Wiki rund um den VW T4: Reparaturanleitungen, Technik, Teilenummern und Erklärungen zu Schaltern, Relais und Steuergeräten.",
              "t4-wiki.de"),
        karte(ext("https://www.t4forum.de/", "T4Forum"),
              "Forum für T4-Fahrer: Fragen zu Technik, Reparatur und Kauf.",
              "t4forum.de"),
        karte(ext("https://vwbuswelt.de/", "VWBuswelt"),
              "Forum rund um VW Busse mit eigenem T4-Bereich.",
              "vwbuswelt.de"),
    ))
    anleitung = abschnitt("anleitung", "", "Betriebsanleitung", f"""
<p>Betriebsanleitung für den VW Transporter T4 von 1991, 164 Seiten, PDF, 9,4 MB.</p>
<div class="knoepfe"><a class="knopf" href="{PDF_DATEI}" download target="_blank" rel="noopener">PDF herunterladen</a></div>
<p class="klein">Quelle: {ext("https://westfaliat4.info/html/vw_westfalia_t4_transporter_do.html", "westfaliat4.info – VW Westfalia T4 Transporter Downloads")}</p>
""")
    return dict(
        datei="links.html",
        titel="Links – VW T4 Multivan 2.4 D, Baujahr 1994",
        beschreibung="Links zu T4-Wiki, T4Forum und VWBuswelt sowie die Betriebsanleitung als PDF.",
        kopf=kopf("", "Links"),
        inhalt=websites + anleitung,
        sprungmarken=[("websites", "Foren und Wiki"), ("anleitung", "Betriebsanleitung")],
    )
