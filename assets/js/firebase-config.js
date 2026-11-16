/* Firebase-Zugangsdaten für „Aufgaben“ und „Notizen“.

   Diese Werte sind keine Geheimnisse: Sie stehen in jeder Firebase-Web-App im Klartext.
   Geschützt werden die Daten durch die Sicherheitsregeln in Firestore (siehe README.md).

   Eintragen: Firebase-Konsole → Projekteinstellungen (Zahnrad) → „Meine Apps“ → Web-App →
   „SDK-Einrichtung und -Konfiguration“ → Option „Konfiguration“. Die Werte hier ersetzen. */
export const firebaseConfig = {
  apiKey: "AIzaSyA_zDW_PfGX3M6znWzNXRAjR73WFcViVNc",
  authDomain: "t4app-ff7b9.firebaseapp.com",
  projectId: "t4app-ff7b9",
  storageBucket: "t4app-ff7b9.firebasestorage.app",
  messagingSenderId: "543568311604",
  appId: "1:543568311604:web:2b6a7f231046d35c53e161",
};

/* Der eine gemeinsame Zugang zur Website. Dieselbe E-Mail-Adresse muss in Firebase unter
   Authentication → Users angelegt werden (das Passwort legst du dort fest) und steht in den Firestore-Regeln.
   Die Adresse muss nicht echt sein; es wird nie eine E-Mail dorthin geschickt. Auf der Anmeldeseite
   gibst du nur das Passwort ein. */
export const zugangEmail = "zugang@t4-multivan.example";
