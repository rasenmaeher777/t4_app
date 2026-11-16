"""Geschichte, Fakten, Quellen."""
import json
import os

from helfer import *

AMS = "https://www.auto-motor-und-sport.de/oldtimer/vw-t4-1990-2003-multivan-caravelle-staerken-schwaechen/"
WP = "https://de.wikipedia.org/wiki/VW_T4"

PRODUKTION = [(1990, 130370, "T3 und T4"), (1991, 137682, ""), (1992, 167830, ""), (1993, 129779, ""), (1994, 135144, ""),
              (1995, 141355, ""), (1996, 141454, ""), (1997, 155436, ""), (1998, 154982, ""), (1999, 148886, ""),
              (2000, 162699, ""), (2001, 151722, ""), (2002, 137913, ""), (2003, 154959, "T4 und T5")]


def _nachweise():
    with open(os.path.join(WURZEL, "assets", "img", "geschichte", "bildnachweise.json"), encoding="utf-8") as f:
        return json.load(f)


def foto(schluessel, titel, text):
    n = _nachweise()[schluessel]
    return (f'<figure class="foto"><img src="{n["datei"]}" width="{n["breite"]}" height="{n["hoehe"]}" alt="{e(titel)}" loading="lazy" decoding="async">'
            f'<figcaption><b>{titel}</b>{text} <span>Foto: {e(n["urheber"])}, {e(n["lizenz"])}</span></figcaption></figure>')


def geschichte():
    mj = daten("modell-und-lack.json")["modelljahre"]["tabelle"]

    t4 = abschnitt("t4", "", "Der T4", kv([
        ("Bauzeit", "08/1990 – 06/2003", "Vorgänger T3, Nachfolger T5"),
        ("Stückzahl", "rund 1,9 Millionen", "1994: 135.144"),
        ("Interne Bezeichnung", "Typ 70", "ab 1996 auch 7D"),
        ("Konzept", "Frontmotor quer, Frontantrieb", "erster VW-Bus ohne Heckmotor"),
        ("Radstände", "2920 und 3320 mm", "Multivan nur kurz"),
        ("Auszeichnung", "Van of the Year 1992", "cw-Wert 0,36"),
    ]) + mehr("Vorgänger und Neuanfang", f"""<p>T1 bis T3 hatten Heckmotor und Heckantrieb. Der T4 war eine vollständige Neukonstruktion mit Frontantrieb und tiefem, durchgehendem Ladeboden; Entwicklungskosten laut {ext(AMS, "auto motor und sport")} rund zwei Milliarden Mark.</p>
<div class="galerie drei">
  {foto("t1", "T1 · 1950–1967", "")}
  {foto("t2", "T2 · 1967–1979", "")}
  {foto("t3", "T3 · 1979–1992", "")}
</div>
<div class="galerie zwei" style="margin-top:14px">
  {foto("t4-1993", "T4 Caravelle, 1993", "Kurzer Vorderwagen.")}
  {foto("t4-allstar", "Multivan Allstar", "Silbergrau abgesetzte Schürze.")}
</div>"""))

    zeit = abschnitt("zeitleiste", "", "Zeitleiste", klappliste([
        ("Produktionsstart", "Der T4 löst in Hannover den T3 ab. Zum Start drei Benziner und zwei Diesel, darunter der 2.4 D (AAB).", "08/1990"),
        ("Multivan 2.4 D im Katalog", "Grundpreis umgerechnet 23.205 €. Im Herbst kommt Silbergrau Metallic (D7V).", "1991"),
        ("Van of the Year, 1.9 TD, Allstar", "August: 1.9 TD. Oktober: Sondermodell Allstar. In Nordamerika als EuroVan verkauft.", "1992"),
        ("syncro und Aufstelldach", "Allrad erst jetzt, weil bis dahin der T3 syncro lief. 1993/94 entstehen 9.667 T4 in Emden.", "1993"),
        ("Classic, Wasserlack, neue Vakuumpumpe", "Januar: Multivan Classic. Umstellung auf Wasserbasislack. Mai: geänderter Zylinderkopf mit neuer Vakuumpumpe am AAB. 135.144 Transporter gebaut.", "1994"),
        ("Spannrolle am AAB, VW Nutzfahrzeuge eigenständig", "Ab Februar spannt eine Spannrolle den Zahnriemen statt der Wasserpumpe. Im Herbst Beginn der 2.5-TDI-Fertigung.", "1995"),
        ("Große Produktaufwertung", "Multivan und Caravelle mit 8 cm längerem Vorderwagen, Scheibenbremsen hinten, Airbags, TDI und VR6.", "01/1996"),
        ("AJA löst AAB ab", "Nachfolger AJA mit 75 PS und Oxidationskatalysator. Letzter AAB im September 1998.", "1997–1998"),
        ("Multivan II", "Sitze der zweiten Reihe in Schienen verschieb- und drehbar; Kühlbox im Sitz entfällt.", "1999"),
        ("Produktionsende", "Nach rund 1,9 Millionen Fahrzeugen folgt der T5.", "06/2003"),
    ]))

    nase = abschnitt("vorderwagen", "", "Kurzer und langer Vorderwagen", kv([
        ("Kurz (T4a)", "bis 12/1995", "gerade Haube, rechteckige Scheinwerfer, gelbe Blinker"),
        ("Lang (T4b)", "ab 01/1996", "Multivan und Caravelle, 8 cm länger, schräge Scheinwerfer"),
        ("Dieses Fahrzeug", "kurzer Vorderwagen", None),
    ]) + "<p>Kotflügel, Stoßfänger, Grill, Scheinwerfer und viele Fahrwerksteile unterscheiden sich.</p>"
      + mehr("Bilder", f"""<div class="galerie zwei">
  {foto("t4-1993", "Kurzer Vorderwagen", "")}
  {foto("t4-langer-vorderwagen", "Langer Vorderwagen", "")}
</div>"""))

    maxi = max(p[1] for p in PRODUKTION)
    bal = "".join(
        f'<li{" class=mein" if j == 1994 else ""}><span class="jahr">{j}</span><span class="spur"><i style="width:{w / maxi * 100:.1f}%"></i></span>'
        f'<span class="wert">{tsd(w)}</span></li>' for j, w, _ in PRODUKTION)
    prod = abschnitt("produktion", "", "Produktion", kv([
        ("Hannover", "rund 1,7 Millionen", "Stammwerk; alle syncro"),
        ("Emden", "9.667", "1993/94"),
        ("Weitere", "Poznań, Brasilien", None),
        ("Häufigster Motor", "2.4 D (AAB)", "432.060 Stück"),
    ]) + mehr("Fertigung pro Jahr", f'<ul class="balken">{bal}</ul><p>1990 einschl. T3, 2003 einschl. T5. Quelle: Volkswagen Chronik, nach {wiki("Produktionszahl", "T4-Wiki")}.</p>')
      + mehr("Stückzahlen nach Motor", tab(["Motor", "Stückzahl"], [
        ["2.4 D (AAB)", "432.060"],
        ["2.5 TDI 102 PS (ACV)", "391.850"],
        ["1.9 D (1X)", "144.720"],
        ["2.0 Benziner (AAC)", "ca. 110.000"],
        ["2.4 D mit Kat (AJA)", "74.460"],
        ["1.8 Vergaser (PD)", "2.020"],
    ], rechts=(1,), mein=(0,), stapel=False))
      + f'<p class="klein">{ext(WP, "Wikipedia")} und T4-Wiki</p>')

    mj_tab = abschnitt("modelljahre", "", "Modelljahre", "<p>Modelljahr beginnt nach den Werksferien im Sommer; Kennzeichen ist die 10. Stelle der Fahrgestellnummer. Baujahr 1994 = Modelljahr 1994 (R) oder 1995 (S).</p>"
      + mehr("Tabelle", tab(["Modelljahr", "Gebaut", "Zeichen"],
           [[str(m["modelljahr"]), m["zeitraum"], f'<b class="mono">{m["zeichen"]}</b>'] for m in mj],
           rechts=(2,), mein=tuple(i for i, m in enumerate(mj) if m.get("mein_bus")), stapel=False))
      + f'<p class="klein">{wiki("Modelljahr")} im T4-Wiki</p>')

    return dict(
        datei="geschichte.html",
        titel="Geschichte des VW T4",
        beschreibung="Geschichte des VW T4: Zeitleiste 1990 bis 2003, Vorderwagen, Produktion und Modelljahre.",
        kopf=kopf("", "Geschichte"),
        sprungmarken=[("t4", "Der T4"), ("zeitleiste", "Zeitleiste"), ("vorderwagen", "Vorderwagen"),
                      ("produktion", "Produktion"), ("modelljahre", "Modelljahre")],
        inhalt=t4 + zeit + nase + prod + mj_tab,
    )


def fakten():
    zahlen = abschnitt("zahlen", "", "Zahlen", kv([
        ("432.060", "AAB-Motoren", "meistgebauter T4-Motor"),
        ("2.020", "1.8-Vergasermotoren (PD)", "seltenster Motor, 1990–1992"),
        ("2 Mrd. DM", "Entwicklungskosten", None),
        ("13 Jahre", "Bauzeit", "08/1990 – 06/2003"),
        ("9.667", "T4 aus Emden", "1993/94"),
        ("5.610", "T4 für die Bundeswehr", "ab 1995"),
    ]))

    motor = abschnitt("motor", "", "Motor", klappliste([
        ("Kein Steuergerät", "Einspritzpumpe rein mechanisch; Strom braucht der Motor im Betrieb nur für das Abstellventil, vorher zum Vorglühen."),
        ("Wasserpumpe spannt den Zahnriemen", "Bis 01/1995 keine Spannrolle: Die Wasserpumpe sitzt in Langlöchern und wird zum Spannen verschoben."),
        ("Zwei Zahnriemen", "Der zweite Riemen am anderen Ende der Nockenwelle treibt die Einspritzpumpe."),
        ("Mehr Drehmoment als der 2.0 Benziner", "164 Nm gegenüber 159 Nm. Bis Ende 1995 stärkster Diesel im T4."),
        ("„Schiffsdiesel“", "Spitzname für AAB und AJA."),
        ("Nie ein SDI", "Der T4 bekam keinen Saugdiesel mit Direkteinspritzung; der 2.4 D blieb Wirbelkammermotor."),
    ]))

    bus = abschnitt("bus", "", "Fahrzeug", klappliste([
        ("Zweimal Silbergrau Metallic", "D7V bis 12/1995, N7P ab 07/1995 – gleicher Name, anderer Ton. Nach Code bestellen."),
        ("Lack von 1994", "Umstellung auf Wasserbasislack Ende 1993; Jahrgänge 1994/95 gelten als rostanfälliger, Metallic weniger als Weiß."),
        ("Kühlbox im Sitz", "Im Einzelsitz gegen die Fahrtrichtung; Zweitbatterie serienmäßig."),
        ("Von vorn wie ein Transporter", "Bis 1995 gleiche Front für Transporter, Caravelle und Multivan."),
        ("Lastabhängige Bremse", "Ohne ABS regelt ein mechanischer Bremsdruckminderer die Hinterradbremse nach Beladung."),
        ("Fünfter Gang verlängerbar", "Beim 02B sind die Zahnräder des 5. Gangs unter einem Deckel zugänglich – beliebter Umbau."),
    ]))

    welt = abschnitt("welt", "", "Sonstiges", klappliste([
        ("EuroVan", "In die USA ging nur die Pkw-Version; Winnebago baute daraus Wohnmobile."),
        ("Teuerster Volkswagen", "Caravelle Business ab 1997, bis zum Phaeton."),
        ("Kamei ClubVan", "Rund 100 Stück, Konferenzraum auf Caravelle-Basis."),
        ("Kein „Tresor“ mehr", "Das abschließbare Fach unter der Ladefläche von T2/T3-Pritschen entfiel mit dem Frontmotor."),
        ("syncro nicht höhergelegt", "Anders als beim T3; Allrad erst ab 1993."),
        ("H-Kennzeichen", "Baujahr 1994 ist seit 2024 alt genug, wenn Zustand und Originalität passen."),
    ]))

    return dict(
        datei="fakten.html",
        titel="Fakten zum VW T4 und zum Motor AAB",
        beschreibung="Zahlen und Wissenswertes zum VW T4 Multivan und zum 2,4-Liter-Diesel AAB.",
        kopf=kopf("", "Fakten"),
        sprungmarken=[("zahlen", "Zahlen"), ("motor", "Motor"), ("bus", "Fahrzeug"), ("welt", "Sonstiges")],
        inhalt=zahlen + motor + bus + welt,
    )


def quellen():
    n = _nachweise()
    bilder = "".join(
        f'<tr><td data-t="Bild">{e(v["titel"].replace("File:", ""))}</td><td data-t="Urheber">{e(v["urheber"])}</td>'
        f'<td data-t="Lizenz">{ext(v["lizenz_url"], e(v["lizenz"])) if v["lizenz_url"] else e(v["lizenz"])}</td>'
        f'<td data-t="Quelle">{ext(v["seite"], "Wikimedia Commons")}</td></tr>' for v in n.values())
    inhalt = abschnitt("quellen", "Quellen", "Quellen", f"""
<ul class="karten">
  {karte("T4-Wiki", f"Wichtigste Quelle für Technik, Wartung, Teilenummern, Farben und Modelljahre. Inhalte unter {ext('https://creativecommons.org/licenses/by/2.0/de/', 'CC BY 2.0 DE')}; hier in eigenen Worten zusammengefasst. {ext('https://www.t4-wiki.de/', 't4-wiki.de')}", "Technik")}
  {karte("ADAC-Autokatalog", f"Maße, Gewichte, Fahrleistungen, Normverbrauch und die Listenpreise aller Multivan-Varianten 1991 bis 1995. {ext('https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/vw-nutzfahrzeuge/transporter/t4/', 'adac.de')}", "Daten und Preise")}
  {karte("Wikipedia", f"Modellgeschichte, Ausstattungsvarianten und Stückzahlen der Motoren. {ext(WP, 'Artikel „VW T4“')}, Lizenz CC BY-SA 4.0.", "Geschichte")}
  {karte("auto motor und sport", f"Kaufberatung zum T4 mit Angaben zu Entwicklungskosten und Luftwiderstand. {ext(AMS, 'Zum Artikel')}", "Geschichte")}
  {karte("T4Forum.de", f"Erfahrungen von Haltern zum großen Glasschiebedach. {ext('https://www.t4forum.de/forum/index.php?thread/235033-panoramadach-schiebedach-beim-multivan-undicht/', 'Zum Thread')}", "Schiebedach")}
  {karte("Volkswagen Chronik", "Jährliche Produktionszahlen, zitiert nach dem T4-Wiki.", "Produktion")}
</ul>
{hinweis("Ohne Gewähr", "<p>Diese Seite ist ein privates Hobbyprojekt. Wo sich Quellen widersprechen, ist das im Text vermerkt. Verbindlich sind Fahrzeugpapiere, Bordbuch und der Reparaturleitfaden von Volkswagen.</p>")}
""") + abschnitt("bilder", "Bildnachweise", "Bildnachweise", f"""
<div class="tab-huelle"><table class="tab stapel"><thead><tr><th>Bild</th><th>Urheber</th><th>Lizenz</th><th>Quelle</th></tr></thead><tbody>{bilder}</tbody></table></div>
<p class="klein" style="margin-top:12px">Die Fotos stammen von Wikimedia Commons. Sie wurden verkleinert und werden auf dieser Seite in Graustufen dargestellt. Bilder unter CC BY-SA dürfen unter derselben Lizenz weiterverwendet werden.</p>
<p class="klein">Die freigestellten Schwarz-Weiß-Abbildungen (Frontansicht, Heckansicht, Emblem) wurden vom Betreiber dieser Seite bereitgestellt. Bilder zu Reparaturen sind nicht eingebettet, sondern als Links auf das T4-Wiki gesetzt.</p>
""") + abschnitt("technik-der-seite", "Zur Seite", "Datenschutz", """
<div class="text">
  <p>Die Seite besteht aus statischen Dateien. Sie setzt keine Cookies, bindet keine Schriften oder Skripte von fremden Servern ein und zählt keine Besucher. </p>
  <p>Beim Abruf verarbeitet der Hoster (GitHub Pages) technisch notwendige Daten wie die IP-Adresse.</p>
</div>
""")
    return dict(
        datei="quellen.html",
        titel="Quellen und Lizenzen – T4 Multivan 1994",
        beschreibung="Quellen, Lizenzen und Bildnachweise der Seite über den VW T4 Multivan 2.4 D von 1994.",
        kopf=kopf("", "Quellen"),
        inhalt=inhalt,
    )
