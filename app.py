from flask import Flask, render_template, request, send_file, redirect, url_for
from weasyprint import HTML
from datetime import datetime
import os
import io
import random


app = Flask(__name__)

# Basisverzeichnis für Rechnungen
INVOICE_DIR = "invoices"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    # Userdaten eingeben
    client_name = request.form['client_name']
    client_address = request.form['client_address']
    service_types = request.form.getlist('service_type[]')
    amount = request.form['amount']

    # Rechnungsnummer automatisch erstellen
    it_services = {
        'Wix_Website': 'WX',
        'Web_Programmierung': 'WP',
        'App_Programmierung': 'AP',
        'Google_Ads_Kampagne': 'GA',
        'Content_Creation': 'CC',
        'Social_Media_Post': 'SM'
    }
    it_short_list = [it_services.get(service_type, 'IT') for service_type in service_types]
    it_short = "-".join(it_short_list)
    date = datetime.now().strftime("%Y%m%d")
    random_number = random.randint(100, 999)
    invoice_number = f"{date}-{it_short}-LUK{random_number}"

    invoice_data = {
        'client_name': client_name,
        'client_address': client_address,
        'service_types': ", ".join(service_types),
        'amount': amount,
        'invoice_number': invoice_number,
        'invoice_date': datetime.now().strftime("%d.%m.%Y"),
        'my_name': 'Max Mustermann',
        'my_address': 'Musterstraße 20, 12345 Berlin',
        'my_iban': 'DEXX XXXX XXXX XXXX XXXX XX',
        'my_bank': 'Volksbank Berlin'
    }

    # Rechnung als HTML rendern
    html = render_template('invoice_template.html', data=invoice_data)

    # PDF generieren
    pdf = HTML(string=html).write_pdf()

    # Ordnerstruktur nach Jahr und Monat erstellen
    year_folder = datetime.now().strftime("%Y")
    month_folder = datetime.now().strftime("%m")
    save_path = os.path.join(INVOICE_DIR, year_folder, month_folder)
    os.makedirs(save_path, exist_ok=True)

    # PDF speichern
    pdf_filename = f"Rechnung_{invoice_number}.pdf"
    pdf_path = os.path.join(save_path, pdf_filename)
    with open(pdf_path, 'wb') as pdf_file:
        pdf_file.write(pdf)

    # PDF zur Vorschau bereitstellen oder als Download
    return send_file(io.BytesIO(pdf), download_name=pdf_filename, as_attachment=True)


@app.route('/invoices')
def list_invoices(amount=None):
    invoice_files = []
    if not os.path.exists(INVOICE_DIR):
        return render_template('invoices.html', invoices=invoice_files)  # Kein Verzeichnis

    for year in os.listdir(INVOICE_DIR):
        year_path = os.path.join(INVOICE_DIR, year)
        for month in os.listdir(year_path):
            month_path = os.path.join(year_path, month)
            for invoice in os.listdir(month_path):
                invoice_number = invoice.split('.')[0]  # Rechnungsnummer ohne Dateiendung
                # Hier das Datumsteil extrahieren, indem du zuerst das erste '_' trennst
                date_str = invoice_number.split('_')[1]  # '20240925-IT-IT-LUK773'
                # Dann nur das erste Teil bis zum '-' nehmen
                date_str = date_str.split('-')[0]  # '20240925'

                invoice_date = datetime.strptime(date_str, '%Y%m%d').strftime('%d.%m.%Y')

                invoice_files.append({
                    'path': os.path.join(year, month, invoice),  # Hier wird der relative Pfad zur Datei verwendet
                    'name': invoice,
                    'invoice_number': invoice_number,  # Rechnungsnummer hinzufügen
                    'invoice_date': invoice_date,  # Datum hinzufügen
                    'amount': amount  # Hier kannst du den Betrag hinzufügen, falls er benötigt wird
                })

    # Rechnungen nach Datum sortieren
    invoice_files.sort(key=lambda x: x['invoice_date'], reverse=True)

    return render_template('invoices.html', invoices=invoice_files)


@app.route('/download_invoice/<path:filename>')
def download_invoice(filename):
    file_path = os.path.join(INVOICE_DIR, filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
