# Mein T4 – Website und Recherchedaten

VW T4 Multivan, Baujahr 1994, 2,4 l Diesel (Motorkennbuchstabe AAB), Silbergrau Metallic, großes elektrisches Glasschiebedach.

Dieser Ordner enthält die fertige Website (für GitHub Pages) und die Recherche, auf der sie beruht.

Stand: 15.11.2026

## Die Website

Statische Seiten ohne Build-Schritt beim Hosten: HTML, eine CSS-Datei, zwei kleine JavaScript-Dateien (Suche). Keine externen Schriften, keine Cookies, kein Tracking. Nur Hell-Modus.

Aufbau jeder Seite: dunkler Titelblock (Überschrift in Impact), Menü mit Suchfeld, links die Abschnitte der Seite, rechts der Inhalt. Auf den Inhaltsseiten stehen die wichtigsten Werte offen, Details sind ausklappbar (`mehr(...)` und `klappliste(...)` in `quelltext/helfer.py`). Das Suchfeld durchsucht alle Abschnitte, Datenzeilen und Tabellen (`assets/js/suchindex.js`, wird beim Bauen erzeugt).

| Seite | Inhalt |
|---|---|
| `index.html` | Start: Kurzdaten und Inhaltsverzeichnis |
| `technik.html` | Motor, Einspritzung, Baujahr-Grenzen 1994, Getriebe, Fahrwerk, Räder, Maße, Sicherungen |
| `fahrdaten.html` | Fahrleistungen, Verbrauch, Motorenvergleich, Lasten |
| `wartung.html` | Wartungshinweise, Betriebsstoffe, Teilenummern, Schwachstellen, Anleitungen |
| `ausstattung.html` | Eigene Ausstattung, Serienausstattung (Varianten, Grundpreise), Sonderausstattung (Aufpreise, PR-Nummern, Farben) |
| `geschichte.html` | Eckdaten, Zeitleiste, Vorderwagen, Produktion, Modelljahre |
| `fakten.html` | Wissenswertes und Kurioses |
| `quellen.html` | Quellen, Lizenzen, Bildnachweise, Datenschutz |
| `404.html` | Fehlerseite |

### Auf GitHub Pages veröffentlichen

Für die Website werden nur diese Dateien gebraucht:

```
index.html, technik.html, fahrdaten.html, wartung.html, ausstattung.html,
geschichte.html, fakten.html, quellen.html, 404.html
assets/            (CSS, JavaScript, Bilder – ca. 3,6 MB)
manifest.webmanifest   (Name und Icon für „Zum Home-Bildschirm“)
.nojekyll          (leere Datei; sagt GitHub, die Dateien unverändert auszuliefern)
```

1. Repository auf GitHub anlegen und die Dateien hochladen (der ganze Ordner geht auch).
2. Im Repository: **Settings → Pages → Build and deployment → Deploy from a branch**, Branch `main`, Ordner `/ (root)`.
3. Nach ein bis zwei Minuten ist die Seite unter `https://<benutzername>.github.io/<repository>/` erreichbar.

Die `.gitignore` schließt die Rohbilder aus dem T4-Wiki (`recherche/t4-wiki/bilder/`, ca. 110 MB) vom Hochladen per Git aus. Beim Hochladen über die GitHub-Weboberfläche gilt sie nicht – dort einfach nur die oben genannten Dateien auswählen.

### Inhalte ändern

Die HTML-Dateien werden aus den Dateien in `quelltext/` erzeugt:

```
quelltext/
├── build.py                  baut alle Seiten
├── helfer.py                 Seitenrahmen, Menü, Tabellen, Links
├── s_start_technik.py        Startseite, Technik
├── s_fahrdaten_wartung.py    Fahrdaten, Wartung
├── s_ausstattung.py          Ausstattung, Serien- und Sonderausstattung
└── s_geschichte_fakten.py    Geschichte, Fakten, Quellen
```

Text in einer `s_*.py`-Datei ändern, dann im Projektordner ausführen:

```bash
python3 quelltext/build.py
```

Das Skript braucht nur Python 3, keine weiteren Pakete. Farben, Abstände und Schrift stehen in `assets/css/stil.css` (Farbvariablen ganz oben); dafür ist kein erneutes Bauen nötig. Kleine Korrekturen gehen auch direkt in den HTML-Dateien, werden beim nächsten Bauen aber überschrieben.

Lokal ansehen:

```bash
python3 -m http.server 4173
```

Danach im Browser `http://localhost:4173` öffnen.

### Bilder

- `assets/img/t4-front-*.png`, `t4-heck-*.png`, `emblem-*.png`: verkleinerte Fassungen von `Bild01.PNG`, `Bild03.PNG`, `Bild04.PNG`. Der Hintergrund ist exakt `#F3F0F0`, die Ränder wurden beschnitten.
- `assets/img/geschichte/`: sieben Fotos von Wikimedia Commons mit `bildnachweise.json` (Urheber, Lizenz, Link). Die Nachweise stehen auf `quellen.html`.
- Bilder zu Reparaturen sind nicht eingebettet; die Seiten verlinken auf das T4-Wiki.

## Die Recherche

```
daten/                  Aufbereitete Daten (JSON) mit Quellenverweisen
├── fahrzeug.json           Steckbrief + was am Fahrzeug zu prüfen ist
├── motor-aab.json          Motor: Kenndaten, Einspritzung, Vorglühen, Baujahr-Grenzen
├── technische-daten.json   Maße, Gewichte, Getriebe, Fahrwerk, Räder, Sicherungen
├── wartung.json            Intervalle, Betriebsstoffe, Teilenummern
├── schwachstellen.json     Bekannte Probleme für Bj. 1994 / AAB
├── schiebedach.json        Glasschiebedach (dünne Quellenlage)
├── modell-und-lack.json    Modellgeschichte, Modelljahre, Lack
├── literatur.json          Bücher, Herstellerdokumentation, Foren
└── quellen.json            Quellenverzeichnis mit Lizenzen
recherche/              Rohmaterial
├── offene-punkte.md        Lücken, Widersprüche, To-dos
├── t4-wiki/                ca. 800 Wiki-Seiten als Markdown, Index, Teilenummern, Bilder
└── web/                    ADAC-Daten und -Preise, Forennotizen, Wikipedia-Texte
```

Die Website liest beim Bauen aus `daten/` unter anderem die Sicherungsbelegung, die Modelljahre, die Teilenummern und die Schwachstellen.

## Was noch offen ist

Siehe `recherche/offene-punkte.md`. Am meisten hilft ein Foto des Fahrzeugdatenträgers sowie die Motornummer: Damit lassen sich Modelljahr, Getriebe, Sondermodell und die Schiebedach-Variante auf der Website von „möglich“ auf „sicher“ stellen.

## Lizenzen

- T4-Wiki: CC BY 2.0 DE – Verwendung mit Namensnennung und Lizenzhinweis.
- Wikipedia: CC BY-SA 4.0. Wikimedia-Commons-Fotos: je nach Bild CC0, CC BY oder CC BY-SA (siehe `quellen.html`).
- ADAC, Forenbeiträge, Zeitschriftenartikel: nur Fakten in eigenen Worten, mit Link.
