"""Kapitel „Daten“: Fahrzeug, Antrieb, Fahrleistungen, Maße, Ausstattung, Wartung."""
from helfer import *

ADAC_MULTIVAN = "https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/vw-nutzfahrzeuge/transporter/t4/264156/"
ADAC_CARAVELLE = "https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/vw-nutzfahrzeuge/transporter/t4/961842/"

ADAC_LISTE = "https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/vw-nutzfahrzeuge/transporter/t4/"

# Listenpreise laut ADAC-Autokatalog (ADAC nennt Euro-Beträge), Schaltgetriebe, Frontantrieb
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


def daten_seite():
    td = daten("technische-daten.json")
    sich = td["sicherungen_hauptleiste"]["sicherungen"]
    m = {x["name"]: x for x in td["masse"]}

    # ---------- 1 Fahrzeug ----------
    fahrzeug = abschnitt("fahrzeug", "", "Fahrzeug", kv([
        ("Modell", "VW T4 Multivan 2.4 D", "Baujahr 1994, kurzer Radstand, kurzer Vorderwagen"),
        ("Kaufpreis", "52.710 DM", "beim Händler; Listenpreis Grundmodell 45.385 DM"),
        ("Lack", "Silbergrau Metallic", "Code D7V, Aufpreis 2.161 DM"),
        ("Polster", "Flachgewebe Hellgrau", None),
        ("Radio", "„alpha“ mit Kassettenteil", "Aufpreis 655 DM"),
        ("Außenspiegel", "elektrisch einstellbar und beheizbar", None),
        ("Nebelscheinwerfer", "ja", "Aufpreis 426 DM"),
        ("Glasschiebedach", "groß, elektrisch, über dem Fahrgastraum", None),
    ]) + mehr("Zusammensetzung des Kaufpreises", "<p>Grundmodell 45.385 DM + Metallic 2.161 DM + Radio 655 DM + Nebelscheinwerfer 426 DM = 48.627 DM. Die übrigen 4.083 DM entfallen auf Spiegel, Schiebedach und weitere Positionen ohne bekannten Einzelpreis.</p>")
      + mehr("Fahrzeugdatenträger", "<p>Aufkleber mit allen Angaben zu Motor, Getriebe, Lack und Ausstattung; im Serviceheft und im Fahrzeug nahe der Zentralelektrik.</p>" + tab(["Zeile", "Inhalt"], [
        ["1", "Fahrgestellnummer; 10. Stelle = Modelljahr (R = 1994, S = 1995)"],
        ["2", "Typ- und Verkaufskennnummer"],
        ["3–5", "Typ, Radstand, Leistung, Motor- und Getriebekennbuchstabe"],
        ["6", "Lacknummer hinter „L“, danach die Polsterfarbe"],
        ["ab 7", "PR-Nummern der Ausstattung (z. B. 3JG = Glasschiebedach)"],
      ], stapel=False))
      + f'<p class="klein">{wiki("Fahrzeugdatenträger")} · {wiki("Ausstattungsnummer", "PR-Nummern")} im T4-Wiki</p>')

    # ---------- 2 Motor und Antrieb ----------
    antrieb = abschnitt("antrieb", "", "Motor und Antrieb", kv([
        ("Motor", "2,4 l Diesel, 5 Zylinder", "Kennbuchstabe AAB, Saugdiesel ohne Turbo"),
        ("Leistung", "57 kW (78 PS)", "bei 3700 U/min"),
        ("Drehmoment", "164 Nm", "bei 1800–2200 U/min"),
        ("Einspritzung", "mechanisch", "keine Motorelektronik, kein Fehlerspeicher"),
        ("Antrieb", "Frontantrieb, 5-Gang-Schaltgetriebe", None),
        ("Tank", "80 l Diesel", None),
    ])
      + mehr("Weitere Motordaten", kv([
        ("Bohrung × Hub", "79,5 × 95,5 mm", None),
        ("Verdichtung", "23 : 1", "T4-Wiki-Motorentabelle: 22,5 : 1"),
        ("Zahnriemen", "zwei", "Nockenwelle und Einspritzpumpe; Wasserpumpe spannt den Riemen (Spannrolle erst ab 01/1995)"),
        ("Abgasreinigung", "keine", None),
        ("Bauzeit", "09/1990 bis 09/1998", "432.060 Stück"),
        ("Getriebeöl", "2,5 l SAE 75W-90", "API GL-4"),
      ]) + f'<p class="klein">{wiki("AAB", "AAB im T4-Wiki")} · {wiki("Getriebekennbuchstabe", "Getriebe im T4-Wiki")}</p>'))

    # ---------- 3 Fahrleistungen ----------
    fahr = abschnitt("fahrleistungen", "", "Fahrleistungen und Verbrauch", kv([
        ("Höchstgeschwindigkeit", "137 km/h", None),
        ("Beschleunigung 0–100 km/h", "24,7 s", None),
        ("Verbrauch", "9,3 l/100 km", "Normverbrauch; Praxis laut Haltern 8–9 l/100 km"),
        ("Reichweite", "ca. 860 km", "80 l Tank"),
    ]) + mehr("Verbrauch nach Fahrprofil", kv([
        ("Stadt", "10,1 l/100 km", None),
        ("Konstant 90 km/h", "7,2 l/100 km", None),
        ("Konstant 120 km/h", "10,6 l/100 km", None),
    ]) + f'<p>Drittelmix-Normwerte vom Caravelle kurz 2.4 D GL mit gleichem Antrieb; für den Multivan nennt der ADAC keinen Wert.</p><p class="klein">{ext(ADAC_CARAVELLE, "ADAC-Autokatalog")} (dort abweichend 14,8 s für 0–100 km/h, nicht plausibel; T4-Wiki: 24,7 s)</p>'))

    # ---------- 4 Maße, Gewichte, Fahrwerk ----------
    def mm(x):
        return f'{x["wert"]:,}'.replace(",", ".") + " mm"
    masse = abschnitt("masse", "", "Maße, Gewichte und Fahrwerk", kv([
        ("Länge × Breite × Höhe", f'{m["Länge"]["wert"]/1000:.2f} × {m["Breite"]["wert"]/1000:.2f} × {m["Höhe"]["wert"]/1000:.2f} m'.replace(".", ","), "Breite mit Außenspiegeln 2,18 m"),
        ("Leergewicht", "1780 kg", "zulässiges Gesamtgewicht 2590 kg, Zuladung 810 kg"),
        ("Anhängelast", "2000 kg gebremst", "ungebremst 700 kg, Stützlast 100 kg"),
        ("Bremsen", "Scheiben vorn, Trommeln hinten", "ABS nur als Sonderausstattung"),
        ("Reifen", "195/70 R15 97 S", "Luftdruck 2,6 bar vorn, 3,4 bar hinten (Aufkleber am Fahrzeug beachten)"),
    ]) + mehr("Weitere Angaben", kv([
        ("Radstand", "2920 mm", None),
        ("Wendekreis", "11,7 m", None),
        ("Dachlast", "100 kg", None),
        ("Zulässiges Zuggesamtgewicht", "4500 kg", None),
        ("Felgen", "Stahl 6J × 15", "Lochkreis 5 × 112 mm"),
        ("Radschrauben", "160 Nm", "nach ca. 50 km nachziehen"),
        ("Batterie", "12 V, 80 Ah", "Zweitbatterie serienmäßig"),
    ]) + f'<p class="klein">Basisausführung laut {ext(ADAC_MULTIVAN, "ADAC-Autokatalog")}; Sonderausstattung erhöht das Leergewicht.</p>')
      + mehr("Sicherungsbelegung", tab(
        ["Nr.", "Verbraucher", "Stärke"],
        [[f'{s["nr"]}', s["verbraucher"], f'{s["ampere"]} A' if s["ampere"] else "–"] for s in sich],
        rechts=(2,), stapel=False) + f'<p>Zentralelektrik links unter dem Armaturenbrett. Laut T4-Wiki; je nach Ausstattung abweichend.</p><p class="klein">{wiki("Sicherungsleiste")} · {wiki("Zentralelektrik")}</p>'))

    # ---------- 5 Ausstattung ----------

    motoren = [
        # Kennbuchstabe, Art, Hubraum/Zylinder, Leistung, Drehmoment, Vmax, 0-100, Bauzeit
        ["PD", "Benziner, Vergaser", "1,8 l / 4", "49 kW (67 PS)", "140 Nm", "–", "–", "09/1990–07/1992"],
        ["AAC", "Benziner, Einspritzung, Kat", "2,0 l / 4", "62 kW (84 PS)", "159 Nm", "144 km/h", "21,7 s", "09/1990–06/2003"],
        ["AAF", "Benziner, Einspritzung, Kat", "2,5 l / 5", "81 kW (110 PS)", "190 Nm", "161 km/h", "17,7 s", "09/1990–12/1993"],
        ["ACU", "Benziner, Einspritzung, Kat", "2,5 l / 5", "81 kW (110 PS)", "190 Nm", "161 km/h", "17,7 s", "08/1993–10/1996"],
        ["AES", "Benziner, VR6, Kat", "2,8 l / 6", "103 kW (140 PS)", "240 Nm", "174 km/h", "13,7 s", "01/1996–05/2000"],
        ["AET", "Benziner, Einspritzung, Kat", "2,5 l / 5", "85 kW (116 PS)", "200 Nm", "164 km/h", "17,7 s", "08/1996–06/2003"],
        ["1X", "Diesel, Saugdiesel", "1,9 l / 4", "44 kW (60 PS)", "127 Nm", "128 km/h", "–", "09/1990–12/1995"],
        ["ABL", "Diesel, Turbo", "1,9 l / 4", "50 kW (68 PS)", "140 Nm", "132 km/h", "28,5 s", "08/1992–06/2003"],
        ["<b>AAB</b>", "<b>Diesel, Saugdiesel</b>", "<b>2,4 l / 5</b>", "<b>57 kW (78 PS)</b>", "<b>164 Nm</b>", "<b>137 km/h</b>", "<b>24,7 s</b>", "<b>09/1990–09/1998</b>"],
        ["ACV", "Diesel, Turbo (TDI), Kat", "2,5 l / 5", "75 kW (102 PS)", "250 Nm", "157 km/h", "18,1 s", "09/1995–06/2003"],
    ]
    MOTORVERGLEICH = mehr("Motorenvergleich", tab(
        ["Motor", "Art", "Hubraum / Zylinder", "Leistung", "Drehmoment", "Höchstgeschw.", "0–100 km/h", "Bauzeit"],
        motoren, rechts=(3, 4, 5, 6), mein=(8,))
        + f'<p>Alle Motoren, die bis Modelljahr 1996 im T4 angeboten wurden; der Motor dieses Fahrzeugs ist hervorgehoben. Die VR6- (AES) und 116-PS-Motoren (AET) gab es nur mit langem Vorderwagen ab 1996. Die späteren Motoren (u. a. 2.5 TDI mit 111 kW, AJA, AJT) sind nicht aufgeführt. Fehlende Werte sind nicht überliefert.</p><p class="klein">{wiki("Motorkennbuchstabe", "Motorentabelle im T4-Wiki")} · Höchstgeschwindigkeit 1X: {ext(ADAC_LISTE, "ADAC-Autokatalog")} · {ext("https://de.wikipedia.org/wiki/VW_T4", "Wikipedia")}</p>')
    kopfzeile = ["Motor", "Leistung", "Multivan", "Allstar", "Classic", "Aufstelldach"]
    zeilen = [[mo, l] + [geld(x) for x in p] for mo, l, *p in PREISE]
    sonder_zeilen = [
        ["Metallic-Lack", "2.161 DM", "1.586 DM / 2.161 DM"],
        ["Klimaanlage", "3.393 DM", "3.393 DM"],
        ["ABS", "2.531 DM", "2.531 DM"],
        ["Leichtmetallräder", "1.956 DM", "Serie"],
        ["Zentralverriegelung", "833 DM", "Serie"],
        ["Elektrische Fensterheber vorn", "800 DM", "Serie"],
        ["Radio „alpha“ / „gamma“", "655 DM (alpha)", "Serie (gamma)"],
        ["Nebelscheinwerfer", "426 DM", "426 DM"],
        ["Außenspiegel elektrisch, beheizbar", "k. A.", "k. A."],
        ["Glasschiebedach, elektrisch", "k. A.", "k. A."],
        ["Airbag Fahrer / Beifahrer", "im Paket", "im Paket"],
        ["Automatikgetriebe", "3.204 DM", "3.202 DM"],
        ["Allradantrieb syncro", "6.456 DM", "6.456 DM"],
        ["Aufstelldach", "5.795 DM", "–"],
    ]
    mein = (0, 6, 7, 8, 9)
    f_items = "".join(
        f'<li{" class=mein" if c == "D7V" else ""}><span class="muster"{f" style=background:{h}" if h else ""}></span>'
        f'<div><b>{n}</b><span>{c} · {z}</span></div></li>' for c, n, z, h in FARBEN)
    ausst = abschnitt("ausstattung", "", "Serien- und Sonderausstattung", """
<ul class="liste-strich">
  <li>6 Sitzplätze (auf Wunsch 7), Rückbank zum Bett umklappbar</li>
  <li>Einzelsitz gegen die Fahrtrichtung mit Kühlbox, drehbarer Beifahrersitz</li>
  <li>Klapptisch, Vorhänge, ein Schiebefenster, Zweitbatterie, Servolenkung</li>
</ul>""" + mehr("Aufpreise (Sonderausstattung)", tab(["Position", "Multivan", "Allstar / Classic"], sonder_zeilen, rechts=(1, 2), mein=mein, stapel=False)
        + "<p>Hervorgehoben: im Fahrzeug vorhanden. k. A. = Preis nicht bekannt. Klimaanlage nur mit Motoren ab 2 l, Automatik nur mit Fünfzylindern.</p>")
      + mehr("Varianten und Grundpreise", klappliste([
        ("Multivan", "Grundmodell mit sechs Sitzen; Zentralverriegelung, Fensterheber, Radio und Leichtmetallräder gegen Aufpreis.", "ab 1991"),
        ("Allstar", "Sieben Sitze, silbergrau abgesetzte Schürze, Zentralverriegelung, Fensterheber, Radio „gamma“, Leichtmetallräder serienmäßig.", "ab 10/1992"),
        ("Classic", "Ausstattung wie Allstar, einfarbig lackiert, Stoßfänger in Wagenfarbe.", "ab 01/1994"),
        ("Aufstelldach", "Multivan mit Schlafdach, mit allen Motoren lieferbar.", "ab 02/1993"),
      ]) + tab(kopfzeile, zeilen, rechts=(2, 3, 4, 5), mein=(3,)) + "<p>Listenpreise 1991–1995, Schaltgetriebe, Frontantrieb.</p>")
      + MOTORVERGLEICH
      + mehr("Lackfarben bis 1995", f'<ul class="farben">{f_items}</ul><p style="margin-top:10px">N7P heißt ebenfalls Silbergrau Metallic, ist aber ein anderer Ton (ab 07/1995). Farbmuster sind Näherungen.</p>')
      + f'<p class="klein">Preise: {ext(ADAC_LISTE, "ADAC-Autokatalog")}, ADAC nennt Euro-Beträge, hier mit 1 € = 1,95583 DM in DM umgerechnet · {wiki("Multivan")} · {wiki("Farbnummern")} im T4-Wiki</p>')

    # ---------- 6 Wartung ----------
    wart = abschnitt("wartung", "", "Wartung", tab(["Arbeit", "Intervall"], [
        ["Motoröl und Ölfilter", "10.000 km oder jährlich"],
        ["Inspektion", "15.000 km oder jährlich"],
        ["Zahnriemen und Wasserpumpe", "120.000 km (bei hohem Alter früher)"],
        ["Bremsflüssigkeit", "alle 2 Jahre"],
    ], rechts=(1,), stapel=False) + kv([
        ("Motoröl", "10W-40", "5,5 l mit Filter, Norm VW 505 00"),
        ("Kühlmittel", "G11 (grün/blau)", "ca. 9 l"),
        ("Getriebeöl", "75W-90", "2,5 l"),
        ("Bremsflüssigkeit", "DOT 4", None),
    ])
      + mehr("Bekannte Schwachstellen", klappliste([
        ("Rost", "Baujahre 1994/95 gelten wegen der Lackumstellung als rostanfällig: A- und C-Säule, Radläufe, Schiebetür unten, Tankklappe, Scheibenrahmen."),
        ("Zahnriemen / Wasserpumpe", "Pumpe läuft im Riementrieb; Riemen und Pumpe gemeinsam wechseln."),
        ("Vorglühanlage", "Ausfall meist durch korrodierten Steckplatz 12 der Zentralelektrik (Startprobleme bei Kälte)."),
        ("Einspritzpumpe", "Altersbedingt undichte Dichtungen."),
        ("Schiebedach", "Verstopfte Abläufe oder verrutschter Blendrahmen führen zu Wasser im Innenraum; Abläufe jährlich prüfen, Schienen alle 30.000 km fetten."),
      ]))
      + f'<p class="klein">{wiki("Inspektion")} · {wiki("Gebrauchtwagen-Checkliste")} · {wiki("Motoröl")} im T4-Wiki</p>')

    return dict(
        datei="daten.html",
        titel="Daten – VW T4 Multivan 2.4 D, Baujahr 1994",
        beschreibung="Fahrzeugdaten, Technik, Fahrleistungen, Ausstattung und Wartungshinweise des VW T4 Multivan 2.4 D von 1994.",
        kopf=kopf("", "Daten"),
        sprungmarken=[("fahrzeug", "Fahrzeug"), ("antrieb", "Motor und Antrieb"), ("fahrleistungen", "Fahrleistungen"),
                      ("masse", "Maße und Fahrwerk"), ("ausstattung", "Ausstattung"), ("wartung", "Wartung")],
        inhalt=fahrzeug + antrieb + fahr + masse + ausst + wart,
    )
