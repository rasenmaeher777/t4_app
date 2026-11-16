# Mein T4 – Website und Recherchedaten

VW T4 Multivan, Baujahr 1994, 2,4 l Diesel (Motorkennbuchstabe AAB), Silbergrau Metallic, großes elektrisches Glasschiebedach.

Dieser Ordner enthält die fertige Website (für GitHub Pages) und die Recherche, auf der sie beruht.

Stand: 15.11.2026

## Die Website

Statische Seiten ohne Build-Schritt beim Hosten: HTML, eine CSS-Datei, kleine JavaScript-Dateien (Suche, Passwortabfrage, Aufgaben). Keine externen Schriften, keine Cookies, kein Tracking. Zum Anmelden lädt jede Seite Skripte von Google (Firebase), und die Seite „Aufgaben“ verbindet sich mit Google Firestore. Nur Hell-Modus.

Aufbau jeder Seite: dunkler Titelblock (Überschrift in Impact), Menü mit Suchfeld, links die Abschnitte der Seite, rechts der Inhalt. Auf den Inhaltsseiten stehen die wichtigsten Werte offen, Details sind ausklappbar (`mehr(...)` und `klappliste(...)` in `quelltext/helfer.py`). Das Suchfeld durchsucht alle Abschnitte, Datenzeilen und Tabellen (`assets/js/suchindex.js`, wird beim Bauen erzeugt).

| Seite | Inhalt |
|---|---|
| `index.html` | Start: Kurzdaten und Inhaltsverzeichnis |
| `daten.html` | Fahrzeug (Ausstattung, Kaufpreis), Motor und Antrieb, Fahrleistungen, Maße und Fahrwerk, Serien-/Sonderausstattung, Wartung |
| `geschichte.html` | Eckdaten, Zeitleiste, Vorderwagen, Produktion, Modelljahre |
| `fakten.html` | Wissenswertes und Kurioses |
| `aufgaben.html` | Aufgabenliste mit Fristen und ein Notizfeld, gespeichert in Firestore (Einrichtung siehe unten) |
| `quellen.html` | Quellen, Lizenzen, Bildnachweise, Datenschutz |
| `404.html` | Fehlerseite |

### Auf GitHub Pages veröffentlichen

Für die Website werden nur diese Dateien gebraucht:

```
index.html, daten.html,
geschichte.html, fakten.html, aufgaben.html, quellen.html, 404.html
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
├── s_start_technik.py        Startseite
├── s_daten.py                Kapitel „Daten“
├── s_aufgaben.py             Kapitel „Aufgaben“ (Seitenaufbau)
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

### Aufgaben und Notizen einrichten (Firestore)

Die Seite `aufgaben.html` speichert (nach der Anmeldung) Aufgaben (Sammlung `aufgaben`) und das Notizfeld (Dokument `notizen/bus`) in Google Cloud Firestore. Die Logik steht in `assets/js/aufgaben.js`, die Zugangsdaten in `assets/js/firebase-config.js`. Solange dort noch `HIER-EINTRAGEN` steht, zeigt die Seite einen Hinweis und ist gesperrt.

1. **Projekt anlegen:** [console.firebase.google.com](https://console.firebase.google.com) → „Projekt hinzufügen“ → Name z. B. `t4-multivan` → Google Analytics ausschalten.
2. **Datenbank anlegen:** links *Build → Firestore Database* → „Datenbank erstellen“ → Standort `eur3 (europe-west)` → Modus **Produktionsmodus** (nicht Testmodus; der läuft nach 30 Tagen ab). Der kostenlose Tarif „Spark“ reicht; es wird keine Zahlungsart verlangt.
3. **Sicherheitsregeln setzen:** Firestore → Reiter *Regeln* → Inhalt ersetzen durch den Block unten → *Veröffentlichen*.
4. **Web-App registrieren:** Projektübersicht → Zahnrad → *Projekteinstellungen* → *Meine Apps* → Web-Symbol `</>` → Name `t4-website`, „Firebase Hosting“ nicht ankreuzen → *App registrieren*. Es erscheint ein Block `firebaseConfig = { … }`.
5. **Werte eintragen:** Die Werte in `assets/js/firebase-config.js` übernehmen.
6. **Hochladen:** `assets/js/firebase-config.js` und `aufgaben.html` mit auf GitHub Pages hochladen. Fertig.

Die Werte in `firebase-config.js` sind keine Geheimnisse (jede Firebase-Web-App enthält sie öffentlich im Quelltext). Schützen kann die Daten nur die Regel in Schritt 3.

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // Nur der eine Zugang mit dieser E-Mail-Adresse darf lesen und schreiben
    // (dieselbe Adresse wie `zugangEmail` in assets/js/firebase-config.js).
    function erlaubt() {
      return request.auth != null
        && request.auth.token.email == 'zugang@t4-multivan.example';
    }

    match /aufgaben/{id} {
      allow read, delete: if erlaubt();
      allow create, update: if erlaubt()
        && request.resource.data.keys().hasOnly(['titel', 'frist', 'details', 'erstellt', 'geaendert'])
        && request.resource.data.titel is string
        && request.resource.data.titel.size() > 0
        && request.resource.data.titel.size() <= 120
        && (request.resource.data.frist == null || request.resource.data.frist is string)
        && (!('details' in request.resource.data) || request.resource.data.details.size() <= 1000);
    }

    match /notizen/{id} {
      allow read: if erlaubt();
      allow write: if erlaubt()
        && request.resource.data.text is string
        && request.resource.data.text.size() <= 20000;
    }

    match /{rest=**} {
      allow read, write: if false;
    }
  }
}
```

### Passwort für die ganze Seite (Firebase Authentication)

Beim Öffnen jeder Seite erscheint zuerst die Passwortabfrage („T4 Website“). Es gibt genau ein Passwort. Es wird nicht in der Website gespeichert, sondern in Firebase: ein gemeinsamer Benutzer mit fester E-Mail-Adresse (`zugangEmail` in `assets/js/firebase-config.js`), dessen Passwort du in Firebase festlegst. Die Seite fragt nur das Passwort ab und meldet damit diesen Benutzer an. Die Anmeldung bleibt auf dem Gerät erhalten, bis man unten im Fuß „Abmelden“ klickt. Die Logik steht in `assets/js/zugang.js`.

Einrichtung in Firebase:

1. **Authentication aktivieren:** *Build → Authentication → Los geht's → Sign-in method → E-Mail/Passwort* einschalten (nur den ersten Schalter, nicht „E-Mail-Link“) → Speichern.
2. **Benutzer anlegen:** Reiter *Users → Nutzer hinzufügen*. E-Mail genau `zugang@t4-multivan.example` (die Adresse muss nicht echt sein), Passwort = dein Passwort (mindestens 6 Zeichen).
3. **Regeln ersetzen:** *Firestore Database → Regeln* → den Block aus dem Abschnitt oben (mit `erlaubt()`) einfügen → *Veröffentlichen*. Danach kommt nur noch dieser eine Benutzer an Aufgaben und Notizen.
4. **Neue Registrierungen sperren (empfohlen):** *Authentication → Einstellungen → Nutzeraktionen* → „Erstellen (Registrierung) aktivieren“ ausschalten. Die Regel in Schritt 3 lässt fremde Konten ohnehin nicht an die Daten.
5. **Hochladen:** Alle Seiten (`*.html`), `assets/js/` und `assets/css/` neu hochladen.

Passwort ändern: In Firebase den Benutzer unter *Authentication → Users* löschen und mit derselben E-Mail und dem neuen Passwort neu anlegen. Die Funktion „Passwort zurücksetzen“ in der Konsole würde nur eine E-Mail an die (nicht vorhandene) Adresse schicken.

**Grenzen:** GitHub Pages liefert die HTML-Dateien aus, bevor jemand ein Passwort eingibt. Die Passwortabfrage verbirgt die Seiten im Browser, ein technisch versierter Besucher kann die Dateien aber direkt abrufen (sie enthalten nur die Fahrzeugdaten aus öffentlichen Quellen). Wirklich geschützt sind die Aufgaben und Notizen, weil Firestore sie nur nach der Anmeldung herausgibt. Etwas Privates gehört daher nur in „Aufgaben“ und „Notizen“, nie in die HTML-Dateien.

#### Sortierung ändern

Aufgaben stehen nach Frist sortiert, das späteste Datum oben, Aufgaben ohne Frist unten. Soll das früheste Datum oben stehen, in `assets/js/aufgaben.js` in der Funktion `sortiere` die Zeile `return a.frist < b.frist ? 1 : -1;` zu `? -1 : 1` ändern.

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
