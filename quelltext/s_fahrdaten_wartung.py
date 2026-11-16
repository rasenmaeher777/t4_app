"""Fahrdaten und Wartung."""
from helfer import *

ADAC_CARAVELLE = "https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/vw-nutzfahrzeuge/transporter/t4/961842/"
ADAC_MULTIVAN = "https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/vw-nutzfahrzeuge/transporter/t4/264156/"


def fahrdaten():
    leistung = abschnitt("fahrleistungen", "", "Fahrleistungen", kv([
        ("Höchstgeschwindigkeit", "137 km/h", "Automatik 133 km/h, syncro 135 km/h"),
        ("0–100 km/h", "24,7 s", None),
        ("Leistungsgewicht", "22,8 kg/PS", "1780 kg, 78 PS"),
        ("Reichweite", "ca. 860 km", "80 l Tank bei 9,3 l/100 km"),
    ]) + mehr("Vergleich mit den anderen Motoren bis 1995", tab(
        ["Motor", "Leistung", "Drehmoment", "Spitze", "0–100 km/h"],
        [
            ["1.9 D (1X)", "44 kW (60 PS)", "127 Nm", "128 km/h", "–"],
            ["1.9 TD (ABL)", "50 kW (68 PS)", "140 Nm", "132 km/h", "28,5 s"],
            ["2.4 D (AAB)", "57 kW (78 PS)", "164 Nm", "137 km/h", "24,7 s"],
            ["2.0 Benziner (AAC)", "62 kW (84 PS)", "159 Nm", "144 km/h", "21,7 s"],
            ["2.5 Benziner (AAF)", "81 kW (110 PS)", "190 Nm", "161 km/h", "17,7 s"],
        ], rechts=(1, 2, 3, 4), mein=(2,)) + f"""<p class="klein">{wiki("Motorkennbuchstabe", "Motorentabelle des T4-Wiki")}. Der {ext(ADAC_CARAVELLE, "ADAC-Autokatalog")} nennt für den Caravelle 2.4 D abweichend 14,8 s von 0 auf 100 km/h; für 78 PS ist das nicht plausibel.</p>"""))

    verbrauch = abschnitt("verbrauch", "", "Verbrauch", tab(["Messpunkt", "Verbrauch"], [
        ["Stadtverkehr", "10,1 l/100 km"],
        ["Konstant 90 km/h", "7,2 l/100 km"],
        ["Konstant 120 km/h", "10,6 l/100 km"],
        ["Gesamt (Drittelmix)", "9,3 l/100 km"],
    ], rechts=(1,), mein=(3,), stapel=False) + mehr("Zur Messung", f"""<p>Drittelmix (Stadt, 90 km/h, 120 km/h zu gleichen Teilen). Werte vom Caravelle kurz 2.4 D GL mit gleichem Antrieb; für den Multivan nennt der ADAC keinen Wert. Praxis laut Haltern: 8–9 l/100 km.</p>
<p class="klein">{ext(ADAC_CARAVELLE, "ADAC-Autokatalog, Caravelle kurz 2.4 D GL")}</p>"""))

    lasten = abschnitt("lasten", "", "Zuladung und Anhängelast", kv([
        ("Zuladung", "810 kg", "Basisausführung"),
        ("Anhängelast", "2000 kg gebremst, 700 kg ungebremst", "gebremst bis 12 % Steigung"),
    ]) + mehr("Weitere Lasten", kv([
        ("Stützlast", "100 kg", None),
        ("Dachlast", "100 kg", None),
        ("Zulässiges Zuggesamtgewicht", "4500 kg", None),
    ])) + f"""<p class="klein">{ext(ADAC_MULTIVAN, "ADAC-Autokatalog, Multivan 2.4 D")}</p>""")

    return dict(
        datei="fahrdaten.html",
        titel="Fahrdaten – T4 Multivan 2.4 D (AAB), Baujahr 1994",
        beschreibung="Höchstgeschwindigkeit, Beschleunigung, Verbrauch und Anhängelasten des VW T4 Multivan 2.4 D.",
        kopf=kopf("", "Fahrdaten"),
        sprungmarken=[("fahrleistungen", "Fahrleistungen"), ("verbrauch", "Verbrauch"), ("lasten", "Lasten")],
        inhalt=leistung + verbrauch + lasten,
    )


def wartung():
    w = daten("wartung.json")
    s = daten("schwachstellen.json")

    plan_voll = [
        ["Motoröl und Ölfilter", "10.000 km", "1 Jahr"],
        ["Inspektion", "15.000 km", "1 Jahr"],
        ["Frostschutz prüfen (−25 °C)", "15.000 km", "1 Jahr"],
        ["Staub- und Pollenfilter (falls vorhanden)", "20.000 km", "–"],
        ["Zahnriemen prüfen", "30.000 km", "–"],
        ["Kraftstofffilter entwässern", "30.000 km", "–"],
        ["Ölstand Getriebe und Servolenkung", "30.000 km", "–"],
        ["Schiebedach: Schienen reinigen und fetten", "30.000 km", "–"],
        ["Kraftstofffilter ersetzen", "60.000 km", "–"],
        ["Luftfilter ersetzen", "60.000 km", "–"],
        ["Zahnriemen und Wasserpumpe", "120.000 km", "–"],
        ["Bremsflüssigkeit", "–", "2 Jahre"],
    ]
    plan = abschnitt("intervalle", "", "Wartungshinweise", tab(["Arbeit", "Intervall"], [
        ["Motoröl und Ölfilter", "10.000 km oder jährlich"],
        ["Inspektion", "15.000 km oder jährlich"],
        ["Zahnriemen und Wasserpumpe", "120.000 km"],
        ["Bremsflüssigkeit", "alle 2 Jahre"],
    ], rechts=(1,), stapel=False) + mehr("Alle Intervalle", tab(["Arbeit", "Kilometer", "Zeit"], plan_voll, rechts=(1, 2), stapel=False)
        + "<p>Es gilt, was zuerst erreicht ist. Keine Service-Anzeige im Tacho. Pollenfilter vorn vermutlich erst ab Modelljahr 1996. Zahnriemen bei hohem Alter unabhängig von der Laufleistung tauschen.</p>")
        + f"""<p class="klein">{wiki("Inspektion", "Inspektionsplan")} und {wiki("Motoröl")} im T4-Wiki</p>""")

    stoffe = abschnitt("betriebsstoffe", "", "Betriebsstoffe", kv([
        ("Motoröl", "10W-40", "5,0 l, mit Filter 5,5 l; Norm VW 505 00"),
        ("Kühlmittel", "ca. 9 l, G11", "grün/blau; entspricht G48"),
        ("Getriebeöl", "2,5 l SAE 75W-90", "API GL-4"),
        ("Bremsflüssigkeit", "DOT 4", "ca. 1,5 l für den Wechsel"),
        ("Kraftstoff", "Diesel, 80 l", None),
    ]) + warnung("Nicht verwenden", "<p>Kein LongLife-Öl (VW 506 00 / 506 01): laut VW drohen Motorschäden. Kühlmittel G11 nie mit G12 (rot) mischen.</p>")
        + mehr("Details und Drehmomente", kv([
            ("Weitere Ölnormen", "VW 501 01, 500 00, 505 01, 502 00", "oder ACEA B3/B4"),
            ("Ölablassschraube", "50 Nm", "mit neuem Dichtring"),
            ("Ölfilter", "nur handfest", None),
            ("Frostschutzanteil", "40–60 %", "zum Nachfüllen im Zweifel G12++ oder G13"),
        ]) + f"""<p class="klein">{wiki("Motoröl", "Ölwechsel")} · {wiki("Kühlsystem (Kühlmittel ablassen/auffüllen)", "Kühlmittel wechseln")} · {wiki("Getriebeöl", "Getriebeöl prüfen und wechseln")}</p>"""))

    teile = abschnitt("teile", "", "Teilenummern", mehr("Teilenummern anzeigen", tab(
        ["Teil", "VW-Teilenummer"],
        [[t["teil"], f'<span class="mono">{t["teilenummer"]}</span>'] for t in w["verschleissteile_teilenummern"]],
        stapel=True) + f"""<p>Nummern aus dem T4-Wiki (Stand 2010 bis 2016). Vor dem Kauf anhand der Fahrgestellnummer prüfen lassen, etwa bei {ext("https://volkswagen-classic-parts.com/", "VW Classic Parts")}.</p>"""))

    def liste(eintraege):
        aus = []
        for x in eintraege:
            if x["titel"] == "Fahrleistungen":
                continue
            zusatz = "unbestätigt" if x.get("bestaetigt") is False else ("Bj. 1994" if x["relevanz"] == "hoch" else "")
            aus.append((e(x["titel"]), e(x["beschreibung"].replace("Siehe schiebedach.json – ", "")), zusatz))
        return klappliste(aus)

    schwach = abschnitt("schwachstellen", "", "Bekannte Schwachstellen", f"""
{mehr("Motor und Elektrik", liste(s["motor"]))}
{mehr("Karosserie und Rost", liste(s["karosserie_rost"]))}
{mehr("Innenraum", liste(s["innenraum_ausstattung"]))}
<p class="klein">{wiki("Gebrauchtwagen-Checkliste")} im T4-Wiki · {wikibild("Maengelliste_Verschweissungen_Uebersicht.jpg", "Übersicht der Schweißnähte (Bild)")} · {wikibild("Maengelliste_Verschweissungen_Rost_C_Saeule.jpg", "Rost an der C-Säule (Bild)")}</p>
""")

    links = [
        wiki("Förderbeginn (AAB)", "Förderbeginn prüfen und einstellen"),
        wiki("Einspritzpumpe", "Einspritzpumpe aus- und einbauen, abdichten"),
        wiki("Wasserpumpe", "Wasserpumpe wechseln"),
        wiki("Glühkerzen (Prüfen)", "Glühkerzen prüfen") + " und " + wiki("Glühkerzenwechsel (Motor)", "wechseln") + " (" + wikibild("Elektrik_Gluehkerze_Einbauort_AAB.jpg", "Bild Einbauort") + ")",
        wiki("Zentralelektrik", "Zentralelektrik reparieren (Steckplatz Vorglührelais)"),
        wiki("Kompressionsdruck", "Kompression messen") + " – neu 34 bar, Verschleißgrenze 26 bar",
        wiki("Kühlmittelregler", "Thermostat wechseln"),
        wiki("Vakuumpumpe", "Vakuumpumpe prüfen und wechseln") + " (" + wikibild("Motor_Vakuumpumpe_Einbaulage_Bild.jpg", "Bild Einbaulage") + ")",
        wiki("Hydrostößel", "Hydrostößel prüfen"),
        wiki("Trommelbremse", "Trommelbremse hinten zerlegen und einstellen"),
        wiki("Startprobleme", "Startprobleme eingrenzen"),
    ]
    anleit = abschnitt("anleitungen", "", "Reparaturanleitungen", mehr("Anleitungen im T4-Wiki", "<ul>" + "".join(f"<li>{a}</li>" for a in links) + "</ul>"
        "<p>Eine Anleitung zum Zahnriemenwechsel am AAB gibt es dort nicht; dafür braucht es ein Reparaturbuch oder den VW-Reparaturleitfaden.</p>"))

    return dict(
        datei="wartung.html",
        titel="Wartung und Reparaturen – T4 Multivan 2.4 D (AAB), Baujahr 1994",
        beschreibung="Wartungshinweise, Betriebsstoffe, Teilenummern, bekannte Schwachstellen und Reparaturanleitungen für den VW T4 2.4 D von 1994.",
        kopf=kopf("", "Wartung"),
        sprungmarken=[("intervalle", "Wartungshinweise"), ("betriebsstoffe", "Betriebsstoffe"), ("teile", "Teilenummern"),
                      ("schwachstellen", "Schwachstellen"), ("anleitungen", "Anleitungen")],
        inhalt=plan + stoffe + teile + schwach + anleit,
    )
