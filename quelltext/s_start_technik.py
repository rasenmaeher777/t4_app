"""Startseite und Technik."""
from helfer import *


def start():
    kurz = [
        ("Baujahr", "1994", "gebaut 1990 bis 2003"),
        ("Motor", "2,4 l Diesel", "5 Zylinder, Kennbuchstabe AAB"),
        ("Leistung", "78 PS", "57 kW, 164 Nm"),
        ("Höchstgeschwindigkeit", "137 km/h", "0–100 km/h in 24,7 s"),
        ("Verbrauch", "9,3 l/100 km", "Tank 80 l"),
        ("Getriebe", "5-Gang", "Frontantrieb"),
        ("Sitzplätze", "6 bis 7", "Rückbank als Bett"),
        ("Länge", "4,71 m", "1,84 m breit, 1,92 m hoch"),
        ("Leergewicht", "1780 kg", "zulässig 2590 kg"),
        ("Anhängelast", "2000 kg", "gebremst"),
        ("Farbe", "Silbergrau Metallic", "Lackcode D7V"),
        ("Kaufpreis", "52.710 DM", "neu beim Händler, mit Extras"),
    ]
    daten_html = "".join(f"<div><dt>{k}</dt><dd>{v}<small>{z}</small></dd></div>" for k, v, z in kurz)
    inhalt = f"""
<div class="kurz">
  <section id="kurzdaten">
    <h2 class="start-titel">Kurzdaten</h2>
    <dl class="kurzdaten">{daten_html}</dl>
  </section>
  <div class="bild">{bild("t4-front", "VW T4 mit kurzem Vorderwagen, Ansicht von vorn links", (1600, 900), "(max-width: 860px) 92vw, 440px", lazy=False)}</div>
</div>
<figure class="zitat">
  <blockquote><p>„Dieser T4 ist das schönste und tollste, was einem Mensch in seinem Leben passieren kann“</p></blockquote>
  <figcaption>Wolfgang Johannes Göethe</figcaption>
</figure>
"""
    return dict(
        datei="index.html",
        titel="VW T4 Multivan 2.4 D, Baujahr 1994",
        beschreibung="Daten, Geschichte und Fakten zu einem VW T4 Multivan 2.4 D (Motor AAB) von 1994.",
        kopf=kopf("", "VW T4 Multivan 2.4 D", None, ["Baujahr 1994", "Motor AAB", "Silbergrau Metallic", "Glasschiebedach"]),
        inhalt=inhalt,
    )
