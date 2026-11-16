"""Ausstattung: eigene Ausstattung, Serienausstattung, Sonderausstattung (mit Preisen und Farben)."""
from helfer import *

ADAC_LISTE = "https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/vw-nutzfahrzeuge/transporter/t4/"

# Listenpreise laut ADAC-Autokatalog (in Euro umgerechnet), Schaltgetriebe, Frontantrieb
PREISE = [
    # Motor, Leistung, Multivan, Allstar, Classic, Aufstelldach
    ("1.9 D", "44 kW (60 PS)", 21509, 23575, 23575, 24472),
    ("1.9 TD", "50 kW (68 PS)", 22120, 24187, 24187, 25083),
    ("2.0 Benziner", "62 kW (84 PS)", 22220, 24287, 24287, 25184),
    ("2.4 D", "57 kW (78 PS)", 23205, 25272, 25272, 26168),
    ("2.5 Benziner", "81 kW (110 PS)", 23951, 26019, 26019, 26915),
]

# Farben bis 1995 laut T4-Wiki: Code, Name, Zeitraum, Farbmuster (soweit im Wiki hinterlegt)
FARBEN = [
    ("D7V", "Silbergrau Metallic", "09/1991 – 12/1995", "#9c9c9f"),
    ("007", "Grobsilber", "09/1990 – 05/1996", "#cdcdcd"),
    ("H7Z", "Mountaingrau Metallic", "09/1990 – 12/1995", "#685c68"),
    ("L7D", "Polargrau", "09/1990 – 12/1995", "#c3c0c0"),
    ("902", "Grauweiß", "09/1990 – 06/2003", None),
    ("114 / R10", "Elfenbein", "ab 09/1990", None),
    ("L1L", "Manilabeige", "09/1990 – 12/1995", "#ffecd5"),
    ("A1Z", "Sahara Metallic", "09/1990 – 12/1995", "#ccb29b"),
    ("L1G", "Cayennegelb", "09/1990 – 12/1995", "#fce071"),
    ("P2C", "Leuchtorange", "ab 09/1990", "#fb9c06"),
    ("H8M", "Pastellbraun", "09/1990 – 07/1992", "#ac715e"),
    ("B1V", "Terrabraun Metallic", "09/1990 – 07/1992", None),
    ("K3A", "Paprikarot", "09/1990 – 07/1992", None),
    ("H3D", "Marsalarot", "08/1992 – 12/1995", None),
    ("Y3D", "Tornadorot", "ab 08/1992", None),
    ("C3Y", "Bordeaux Perleffekt", "09/1990 – 12/1995", "#71424a"),
    ("H5G", "Mediumblau", "09/1991 – 12/1995", None),
    ("L5M", "Indienblau", "ab 09/1990", None),
    ("H5Y", "Rauchblau Metallic", "09/1991 – 12/1995", "#bcc3d5"),
    ("L5V", "Jamaikablau Metallic", "09/1990 – 12/1995", "#8dbdde"),
    ("H5Z", "Atlantisblau Metallic", "09/1990 – 12/1995", None),
    ("P6M", "Karibikgrün", "09/1990 – 12/1995", "#3e927d"),
    ("L6N", "Javagrün", "09/1990 – 12/1995", "#468b63"),
    ("H6S", "Scarabgreen", "ab 09/1990", None),
    ("A6U", "Caprigrün Metallic", "08/1992 – 12/1995", None),
]


def ausstattung():
    # ---------- Eigene Ausstattung ----------
    eigen = abschnitt("ausstattung", "", "Ausstattung", kv([
        ("Modell", "Multivan 2.4 D", "kurzer Radstand, Baujahr 1994, Grundpreis 23.205 €"),
        ("Lack", "Silbergrau Metallic (D7V)", "Aufpreis 1.105 €"),
        ("Polster", "Flachgewebe Hellgrau", None),
        ("Radio", "„alpha“ mit Kassettenteil", "PR 8AB, 2 × 20 W, 2 Lautsprecher; Aufpreis 335 €"),
        ("Außenspiegel", "elektrisch einstellbar und beheizbar", "PR 6XD; Aufpreis nicht bekannt"),
        ("Nebelscheinwerfer", "ja", "PR 8WD; Aufpreis 218 €"),
        ("Glasschiebedach", "groß, elektrisch, über dem Fahrgastraum", "PR 3JG; Aufpreis nicht bekannt"),
        ("Neupreis", "mind. 24.863 € (ca. 48.600 DM)", "Grundpreis plus bekannte Aufpreise"),
    ]) + mehr("Hinweise zur Ausstattung", klappliste([
        ("Radio „alpha“: SAFE-Code", "Nach Abklemmen der Batterie oder längerer Unterspannung zeigt das Radio „SAFE“ und muss mit dem vierstelligen Code entsperrt werden. Code mit der Fahrzeugkarte aufbewahren.", "Radio"),
        ("Spiegelheizung", "Die Spiegelheizung läuft zusammen mit der Heckscheibenheizung (Entlastungsrelais, Sicherung S41). Beheizbare Gläser sind mit zwei Steckern angeschlossen; die Polarität ist egal.", "Spiegel"),
        ("Glasschiebedach: Abläufe", "Wasser läuft über Rinnen im Rahmen und Schläuche in den Säulen ab. Abläufe jährlich prüfen (Wasser in die Rinne gießen), Schienen alle 30.000 km reinigen und fetten. Tropft es an den Leseleuchten, ist meist der Blendrahmen aus den Clips gesprungen.", "Dach"),
    ])) + mehr("Fahrzeugdatenträger", "<p>Aufkleber mit allen Angaben zu Motor, Getriebe, Lack und Ausstattung; im Serviceheft und im Fahrzeug nahe der Zentralelektrik.</p>" + tab(["Zeile", "Inhalt"], [
        ["1", "Fahrgestellnummer; 10. Stelle = Modelljahr (R = 1994, S = 1995)"],
        ["2", "Typ- und Verkaufskennnummer; „70…“ = T4 vor 1996"],
        ["3–4", "Typ, Radstand, Motorleistung, Getriebeart"],
        ["5", "Motorkennbuchstabe (AAB) und Getriebekennbuchstabe"],
        ["6", "Lacknummer hinter „L“ (D7V), danach die Polsterfarbe"],
        ["ab 7", "PR-Nummern der Ausstattung, z. B. 3JG für das Glasschiebedach"],
    ], stapel=False)) + f'<p class="klein">{wiki("Radio")} · {wiki("Außenspiegel")} · {wiki("Fahrzeugdatenträger")} · {wikibild("Aufbau_Datentraeger_Einbauort.jpg", "Einbauort Datenträger (Bild)")} · {ext("https://www.t4forum.de/forum/index.php?thread/235033-panoramadach-schiebedach-beim-multivan-undicht/", "Schiebedach im T4Forum")}</p>')

    # ---------- Serienausstattung ----------
    kopfzeile = ["Motor", "Leistung", "Multivan", "Allstar", "Classic", "Aufstelldach"]
    zeilen = [[m, l] + [geld(x) for x in p] for m, l, *p in PREISE]
    serie = abschnitt("serie", "", "Serienausstattung", """
<ul class="liste-strich">
  <li>6 Sitzplätze (auf Wunsch 7), Rückbank zum Bett umklappbar</li>
  <li>Einzelsitz gegen die Fahrtrichtung mit Kühlbox, drehbarer Beifahrersitz</li>
  <li>Klapptisch, Vorhänge, ein Schiebefenster</li>
  <li>Zweitbatterie, Servolenkung, Stahlräder 6J × 15</li>
</ul>""" + klappliste([
        ("Multivan", "Grundmodell mit sechs Sitzen. Zentralverriegelung, elektrische Fensterheber, Radio und Leichtmetallräder gegen Aufpreis.", "ab 1991 · 23.205 €"),
        ("Multivan Allstar", "Sieben Sitze, silbergrau abgesetzte Schürze. Zentralverriegelung, elektrische Fensterheber, Radio „gamma“ und Leichtmetallräder serienmäßig; eingeschränkte Farbauswahl.", "ab 10/1992 · 25.272 €"),
        ("Multivan Classic", "Ausstattung wie Allstar, einfarbig lackiert, Stoßfänger in Wagenfarbe, Polster Stoff hellgrau. PR E6Y.", "ab 01/1994 · 25.272 €"),
        ("Multivan mit Aufstelldach", "Multivan mit Schlafdach, mit allen fünf Motoren lieferbar.", "ab 02/1993 · 26.168 €"),
    ]) + mehr("Grundpreise aller Motoren", tab(kopfzeile, zeilen, rechts=(2, 3, 4, 5), mein=(3,))
        + "<p>Preise mit Schaltgetriebe und Frontantrieb. 23.205 € entsprechen rund 45.400 DM.</p>")
      + mehr("Unterschied zum Transporter", "<p>Nur kurzer Radstand und eine Schiebetür. Außen bis 1995 kaum vom Transporter zu unterscheiden; innen volle Verkleidung, bessere Schalldämmung, gepolstertes Armaturenbrett.</p>")
      + f'<p class="klein">{wiki("Multivan")} · {wiki("Modellübersicht")} · {ext("https://de.wikipedia.org/wiki/VW_T4", "Wikipedia")} · Preise: {ext(ADAC_LISTE, "ADAC-Autokatalog")} (1 € = 1,95583 DM)</p>')

    # ---------- Sonderausstattung ----------
    sonder_zeilen = [
        ["Metallic- / Perleffektlack", "–", "1.105 €", "811 € / 1.105 €"],
        ["Klimaanlage", "9AB", "1.735 €", "1.735 €"],
        ["ABS", "1AC", "1.294 €", "1.294 €"],
        ["Leichtmetallräder", "–", "1.000 €", "Serie"],
        ["Zentralverriegelung", "–", "426 €", "Serie"],
        ["Elektrische Fensterheber vorn", "4R1", "409 €", "Serie"],
        ["Radio „alpha“ / „gamma“", "8AB / 8AD", "335 € (alpha)", "Serie (gamma)"],
        ["Nebelscheinwerfer", "8WD", "218 €", "218 €"],
        ["Außenspiegel elektrisch, beheizbar", "6XD", "k. A.", "k. A."],
        ["Glasschiebedach Fahrgastraum, elektrisch", "3JG", "k. A.", "k. A."],
        ["Glasschiebedach Fahrerhaus mit Jalousie", "3EF", "k. A.", "k. A."],
        ["Airbag Fahrer / Beifahrer", "4UC / 4UE", "im Paket", "im Paket"],
        ["Automatikgetriebe (4 Gänge)", "G0E", "1.638 €", "1.637 €"],
        ["Allradantrieb syncro", "–", "3.301 €", "3.301 €"],
        ["Aufstelldach", "3R3", "2.963 €", "–"],
    ]
    mein = tuple(i for i, z in enumerate(sonder_zeilen) if z[0].split()[0] in ("Metallic-", "Radio", "Nebelscheinwerfer", "Außenspiegel") or z[1] == "3JG")
    f_items = "".join(
        f'<li{" class=mein" if c == "D7V" else ""}><span class="muster"{f" style=background:{h}" if h else ""}></span>'
        f'<div><b>{n}</b><span>{c} · {z}</span></div></li>' for c, n, z, h in FARBEN)
    sonder = abschnitt("sonder", "", "Sonderausstattung", tab(["Position", "PR-Nr.", "Multivan", "Allstar / Classic"], sonder_zeilen, rechts=(2, 3), mein=mein)
        + "<p>Hervorgehoben: an diesem Fahrzeug vorhanden. Klimaanlage nur mit Motoren ab 2 Litern, Automatik nur mit den Fünfzylindern. Aufpreise für Automatik, syncro und Aufstelldach aus der Differenz der Listenpreise.</p>"
        + mehr("Lackfarben bis 1995", f'<ul class="farben">{f_items}</ul><p style="margin-top:10px">Uni-Lacke ohne Aufpreis. Nicht verwechseln: N7P heißt ebenfalls Silbergrau Metallic, ist aber ein anderer Ton (ab 07/1995). Farbmuster sind Näherungen; schraffiert = kein Muster im T4-Wiki.</p>')
        + mehr("Weitere Positionen (PR-Nummern)", tab(["Position", "PR-Nr."], [
            ["Standheizung / Zusatzheizung", "9M3, 7VE"],
            ["Anhängerkupplung abnehmbar", "1D2"],
            ["Sitzheizung vorn", "4A3"],
            ["Geschwindigkeitsregelanlage", "8T1"],
            ["Scheinwerferreinigung", "8X1"],
            ["Heckscheibenwischer", "8M1"],
            ["Beheizbare Scheibenwaschdüsen", "9T1"],
            ["Wärmeschutzverglasung", "W01, W02"],
            ["Lackkonservierung (Wachs)", "5K1"],
        ], stapel=False) + "<p>Aus der PR-Nummernliste des T4-Wiki ohne Preisangabe; ob jede Position 1994 für den Multivan bestellbar war, ist nicht belegt.</p>")
        + f'<p class="klein">Aufpreise: {ext(ADAC_LISTE, "ADAC-Autokatalog")} · {wiki("Ausstattungsnummer", "PR-Nummern")} und {wiki("Farbnummern")} im T4-Wiki</p>')

    return dict(
        datei="ausstattung.html",
        titel="Ausstattung – T4 Multivan 2.4 D, Baujahr 1994",
        beschreibung="Ausstattung des Fahrzeugs, Serien- und Sonderausstattung des VW T4 Multivan bis 1995 mit Preisen, PR-Nummern und Farben.",
        kopf=kopf("", "Ausstattung"),
        sprungmarken=[("ausstattung", "Ausstattung"), ("serie", "Serienausstattung"), ("sonder", "Sonderausstattung")],
        inhalt=eigen + serie + sonder,
    )
