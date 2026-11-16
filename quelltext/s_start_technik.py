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
        ("Neupreis", "ca. 45.400 DM", "23.205 €, ohne Extras"),
    ]
    daten_html = "".join(f"<div><dt>{k}</dt><dd>{v}<small>{z}</small></dd></div>" for k, v, z in kurz)
    seiten = [("geschichte.html", "Geschichte"), ("technik.html", "Technik"), ("fahrdaten.html", "Fahrdaten"),
              ("ausstattung.html", "Ausstattung"), ("wartung.html", "Wartung"), ("fakten.html", "Fakten")]
    inhalt = f"""
<div class="kurz">
  <section id="kurzdaten">
    <h2 class="start-titel">Kurzdaten</h2>
    <dl class="kurzdaten">{daten_html}</dl>
  </section>
  <div class="bild">{bild("t4-front", "VW T4 mit kurzem Vorderwagen, Ansicht von vorn links", (1600, 900), "(max-width: 860px) 92vw, 440px", lazy=False)}</div>
</div>
<h2 class="start-titel">Inhalt</h2>
<ul class="verzeichnis">{"".join(f'<li><a href="{d}">{n}</a></li>' for d, n in seiten)}</ul>
"""
    return dict(
        datei="index.html",
        titel="VW T4 Multivan 2.4 D, Baujahr 1994",
        beschreibung="Technik, Fahrdaten, Wartung, Ausstattung und Geschichte eines VW T4 Multivan 2.4 D (Motor AAB) von 1994.",
        kopf=kopf("", "VW T4 Multivan 2.4 D", None, ["Baujahr 1994", "Motor AAB", "Silbergrau Metallic", "Glasschiebedach"]),
        inhalt=inhalt,
    )


def technik():
    td = daten("technische-daten.json")
    sich = td["sicherungen_hauptleiste"]["sicherungen"]

    motor = abschnitt("motor", "", "Motor", kv([
        ("Bauart", "5-Zylinder-Reihenmotor, Diesel", "Saugdiesel mit Wirbelkammer, quer eingebaut"),
        ("Kennbuchstabe", "AAB", None),
        ("Hubraum", "2370 cm³", None),
        ("Leistung", "57 kW (78 PS) bei 3700 U/min", None),
        ("Drehmoment", "164 Nm bei 1800–2200 U/min", None),
        ("Einspritzung", "Bosch-Verteilerpumpe, mechanisch", "kein Motorsteuergerät"),
        ("Steuertrieb", "Zahnriemen", None),
    ]) + mehr("Weitere Motordaten", kv([
        ("Bohrung × Hub", "79,5 × 95,5 mm", None),
        ("Verdichtung", "23 : 1", "die Motorentabelle des T4-Wiki nennt 22,5 : 1"),
        ("Ventile", "2 je Zylinder, Hydrostößel", None),
        ("Abgasreinigung", "keine", "kein Katalysator, keine Abgasrückführung"),
        ("Zweiter Zahnriemen", "Nockenwelle → Einspritzpumpe", None),
        ("Bauzeit", "09/1990 bis 09/1998", "432.060 Stück, meistgebauter T4-Motor"),
    ]) + f"""<p>Kein Turbolader, keine Motorelektronik, kein Fehlerspeicher.</p>
<p class="klein">{wikibild("Motor_Leistungsdiagramm_AAB.jpg", "Leistungsdiagramm AAB (Bild)")} · {wiki("AAB", "AAB im T4-Wiki")}</p>""")
        + mehr("Einspritzung und Vorglühen", kv([
            ("Förderbeginn", "1,00 ± 0,02 mm Hub", "bei der Kontrolle sind 0,93–1,07 mm zulässig"),
            ("Einspritzdüsen", "Zapfendüsen, 130–138 bar", "Verschleißgrenze 120 bar"),
            ("Zahnrad an der Pumpe", "50 Nm", None),
            ("Antriebsrad an der Nockenwelle", "100 Nm", "mit 50 Nm voranziehen"),
            ("Glühkerzen", "5 Stück, M12 × 1,25", "je Kerze etwa 8–10 A, zusammen rund 50 A"),
            ("Vorglühsteuerung", "im Relais J52", "Dauer nach Motortemperatur; Nachglühen etwa 2 Minuten (Richtwert)"),
        ]) + f"""<p class="klein">{wiki("Förderbeginn (AAB)", "Förderbeginn prüfen und einstellen")} · {wikibild("Motor_Zahnriementrieb_ESP_5_Zylinder_AAB.jpg", "Zahnriementrieb der Einspritzpumpe (Bild)")} · {wikibild("Elektrik_Vorgluehanlage_Schaltbild_AAB_1991.jpg", "Schaltbild Vorglühanlage (Bild)")}</p>"""))

    grenzen = abschnitt("baujahr", "", "Besonderheiten Baujahr 1994", warnung("Motornummer prüfen", f"<p>Bis Motor-Nr. AAB 272 502 (ca. 05/1994) passt die spätere Vakuumpumpe nicht; das falsche Teil zerstört beim ersten Start das Pumpengehäuse. {wiki('Vakuumpumpe', 'T4-Wiki')}</p>") + mehr("Alle Änderungen rund um 1994", tab(
        ["Bauteil", "Bis", "Vorher", "Nachher"],
        [
            ["Vakuumpumpe, Zylinderkopf", "Motor-Nr. 272 502<small>ca. 05/1994</small>", "eigener Zylinderkopf", "Einheitspumpe der 5-Zylinder-Diesel"],
            ["Zahnriemenspannung", "Motor-Nr. 320 127<small>01/1995</small>", "über die Wasserpumpe (18 Zähne)", "Spannrolle, Wasserpumpe mit 20 Zähnen"],
            ["Zylinderkopfdichtung", "10/1993 oder 01/1995<small>Quellen uneinig</small>", "Weichstoff", "Metall, dazu neue Wirbelkammern"],
            ["Luftfilter", "Modelljahr 1995", "044 129 620", "074 129 620"],
            ["Zentralschraube Kurbelwelle", "Motor-Nr. 424 605<small>1997</small>", "M18 × 1,5 × 65", "M18 × 1,5 × 110"],
        ])))

    getriebe = abschnitt("getriebe", "", "Getriebe", kv([
        ("Bauart", "5-Gang-Schaltgetriebe, Typ 02B", "Frontantrieb"),
        ("Ölfüllung", "2,5 l SAE 75W-90", "API GL-4"),
        ("Alternativen ab Werk", "4-Gang-Automatik, Allrad (syncro)", None),
    ]) + mehr("Übersetzungen", kv([
        ("Achsübersetzung", "4,611 (CHP) oder 4,563 (CPW)", "zwei der Getriebe für den AAB von 1994"),
        ("1. / 2. / 3. Gang", "3,778 / 2,118 / 1,458", "Getriebe CHP"),
        ("4. / 5. Gang", "1,029 / 0,837", "Getriebe CHP"),
        ("Rückwärtsgang", "3,600", None),
    ]) + f"""<p>Verbautes Getriebe: Kennbuchstabe auf dem Fahrzeugdatenträger.</p>
<p class="klein">{wiki("Getriebekennbuchstabe", "Alle Getriebe im T4-Wiki")}</p>"""))

    fahrwerk = abschnitt("fahrwerk", "", "Fahrwerk und Bremsen", kv([
        ("Vorderachse", "Doppelquerlenker, Drehstabfedern", None),
        ("Hinterachse", "Schräglenker, Schraubenfedern", None),
        ("Lenkung", "Zahnstange mit Servo", "Wendekreis 11,7 m"),
        ("Bremse vorn", "Scheiben", None),
        ("Bremse hinten", "Trommeln", "bis Ende 1995"),
        ("ABS", "Sonderausstattung", None),
    ]) + mehr("Bremskraftverteilung", "<p>Ohne ABS regelt ein mechanischer Bremsdruckminderer die Hinterradbremse nach der Beladung. Er wird über Federn an der Hinterachse angesteuert; ein hinten tiefergelegtes Fahrwerk verfälscht die Regelung.</p>"))

    raeder = abschnitt("raeder", "", "Räder und Reifen", kv([
        ("Reifen", "195/70 R15 97 S", "verstärkt (reinforced)"),
        ("Reifendruck", "2,6 bar vorn, 3,4 bar hinten", "bei Achslast ab 1285 kg vorn 3,0 bar; maßgeblich ist der Aufkleber am Fahrzeug"),
        ("Radschrauben", "160 Nm", "nach etwa 50 km nachziehen"),
        ("Lochkreis", "5 × 112 mm", "Mittenzentrierung 57,1 mm"),
    ]) + mehr("Felgen und Alternativen", kv([
        ("Stahlfelge", "6J × 15 H2", None),
        ("Alternative ab Werk", "205/65 R15 auf 7J × 15", "98 S: gleicher Druck wie die Serienbereifung"),
    ]) + f"""<p class="klein">{wiki("Rad", "Räder und Reifendruck im T4-Wiki")}</p>"""))

    masse = abschnitt("masse", "", "Maße und Gewichte", f"""
{kv([(x["name"], f'{str(x["wert"]).replace(".", ",")} {x["einheit"]}', None) for x in td["masse"]])}
{mehr("Gewichte", kv([(x["name"], f'{tsd(x["wert"])} {x["einheit"]}', None) for x in td["gewichte"]]))}
<p class="klein">Basisausführung mit Schaltgetriebe laut {ext("https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/vw-nutzfahrzeuge/transporter/t4/264156/", "ADAC-Autokatalog")}. Sonderausstattung erhöht das Leergewicht.</p>
""")

    elektrik = abschnitt("elektrik", "", "Elektrik", kv([
        ("Bordnetz", "12 V", None),
        ("Batterie", "80 Ah", "95 Ah passt ebenfalls"),
        ("Sicherungen und Relais", "Zentralelektrik", "links unter dem Armaturenbrett, hinter dem Ablagefach"),
    ]) + mehr("Sicherungsbelegung", tab(
        ["Nr.", "Verbraucher", "Stärke"],
        [[f'{s["nr"]}', s["verbraucher"], f'{s["ampere"]} A' if s["ampere"] else "–"] for s in sich],
        rechts=(2,), stapel=False) + f"""<p>Laut T4-Wiki; je nach Ausstattung abweichend, Bordbuch geht vor.</p>
<p class="klein">{wiki("Sicherungsleiste")} · {wiki("Zentralelektrik")} · {wikibild("Elektrik_Sicherungen_Leiste_Haupt.jpg", "Hauptsicherungsleiste (Bild)")}</p>"""))

    return dict(
        datei="technik.html",
        titel="Technik – T4 Multivan 2.4 D (AAB), Baujahr 1994",
        beschreibung="Technische Daten des VW T4 Multivan 2.4 D von 1994: Motor AAB, Getriebe, Fahrwerk, Bremsen, Räder, Maße und Sicherungen.",
        kopf=kopf("", "Technik"),
        sprungmarken=[("motor", "Motor"), ("baujahr", "Baujahr 1994"), ("getriebe", "Getriebe"),
                      ("fahrwerk", "Fahrwerk"), ("raeder", "Räder"), ("masse", "Maße"), ("elektrik", "Elektrik")],
        inhalt=motor + grenzen + getriebe + fahrwerk + raeder + masse + elektrik,
    )
