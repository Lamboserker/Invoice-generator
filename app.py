from flask import Flask, render_template, request, send_file
from weasyprint import HTML
from datetime import datetime
import io
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    # Userdaten eingeben
    client_name = request.form['client_name']
    client_address = request.form['client_address']
    service_types = request.form.getlist('service_type[]')  # Mehrfachauswahl

    amount = request.form['amount']

    # Rechnungsnummer automatisch erstellen basierend auf IT-Art und Datum
    it_services = {
        'Wix_Website': 'WX',
        'Web_Programmierung': 'WP',
        'App_Programmierung': 'AP',
        'Google_Ads_Kampagne': 'GA',
        'Content_Creation': 'CC',
        'Social_Media_Post': 'SM'
    }

    # Kürzel für die Rechnungsnummer basierend auf den ausgewählten Dienstleistungen
    it_short_list = [it_services.get(service_type, 'IT') for service_type in service_types]
    it_short = "-".join(it_short_list)  # Kürzel aller ausgewählten Dienstleistungen

    date = datetime.now().strftime("%Y%m%d")  # Aktuelles Datum
    random_number = random.randint(100, 999)  # Zufallszahl für Eindeutigkeit
    invoice_number = f"{date}-{it_short}-LUK{random_number}"  # Rechnungsnummer mit IT-Art, Datum, Kürzel und Zufallszahl

    # Daten für die Rechnung sammeln
    invoice_data = {
        'client_name': client_name,
        'client_address': client_address,
        'service_types': ", ".join(service_types),  # Alle ausgewählten Dienstleistungen in einem String
        'amount': amount,
        'invoice_number': invoice_number,
        'invoice_date': datetime.now().strftime("%d.%m.%Y"),
        'my_name': 'Lukas Oliver Lamberz',
        'my_address': 'Am Steinberg 68, 51643 Gummersbach',
        'my_iban': 'DE55384500001000135630',
        'my_bank': 'Sparkasse Gummersbach'
    }
    print(service_types)
    # Rechnung als HTML rendern
    html = render_template('invoice_template.html', data=invoice_data)

    # PDF generieren
    pdf = HTML(string=html).write_pdf()

    # PDF als Download zur Verfügung stellen
    return send_file(
        io.BytesIO(pdf),
        download_name=f"Rechnung_{invoice_number}.pdf",
        as_attachment=True
    )


if __name__ == '__main__':
    app.run(debug=True)

("Ausgewählte Dienstleistungen:", service_types)  # Überprüfe die ausgewählten Dienstleistungen