# Rechnungs-Generator

Ein einfacher Rechnungs-Generator, der mit Flask und WeasyPrint entwickelt wurde. Diese Anwendung ermöglicht es Benutzern, Rechnungen für IT-Dienstleistungen zu erstellen und als PDF herunterzuladen.

## Funktionen

- Eingabe von Kundendaten (Name und Adresse)
- Auswahl mehrerer IT-Dienstleistungen
- Automatische Generierung einer Rechnungsnummer
- PDF-Generierung der Rechnung
- Download der Rechnung im PDF-Format

## Technologien

- Python
- Flask
- WeasyPrint
- HTML/CSS
- Google Places API

## Installation

### Voraussetzungen

Stelle sicher, dass du Python 3.x und pip installiert hast. 

### Schritt-für-Schritt-Anleitung

1. **Repository klonen:**

   ```bash
   git clone https://github.com/Lamboserker/PosServer.git
   cd PosServer
   ```

2. **Virtuelle Umgebung erstellen (optional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Auf macOS/Linux
   venv\Scripts\activate     # Auf Windows
   ```

3. **Abhängigkeiten installieren:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Flask-Anwendung ausführen:**

   ```bash
   python app.py
   ```

   Die Anwendung sollte nun auf `http://127.0.0.1:5000/` laufen.

## Verwendung

1. Öffne deinen Webbrowser und gehe zu `http://127.0.0.1:5000/`.
2. Gib die erforderlichen Informationen ein:
   - Name des Auftraggebers
   - Adresse des Auftraggebers
   - Art der IT-Dienstleistung (Mehrfachauswahl möglich)
   - Betrag (in Euro)
3. Klicke auf "Rechnung erstellen", um die Rechnung als PDF herunterzuladen.

## Google Places API

Um die Google Places API zu nutzen, musst du einen API-Schlüssel erstellen und ihn in den HTML-Dateien einfügen, wo die Google Maps Bibliothek eingebunden wird. Du kannst deinen API-Schlüssel hier anfordern: [Google Cloud Platform](https://cloud.google.com/maps-platform/).

Füge den API-Schlüssel in die folgende Zeile ein:
```html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places" async defer></script>
```

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die [LICENSE](LICENSE) Datei für Details.

## Autor

Lukas Oliver Lamberz  
[GitHub-Profil](https://github.com/Lamboserker)
