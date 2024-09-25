
# Invoice Generator

A simple invoice generator developed with Flask and WeasyPrint. This application allows users to create invoices for IT services and download them as PDFs.

## Features

- Input customer data (name and address)
- Select multiple IT services
- Automatic generation of an invoice number
- PDF generation of the invoice
- Download the invoice in PDF format

## Technologies

- Python
- Flask
- WeasyPrint
- HTML/CSS
- Google Places API

## Installation

### Prerequisites

Ensure you have Python 3.x and pip installed.

### Step-by-step Guide

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Lamboserker/PosServer.git
   cd PosServer
   ```

2. **Create a virtual environment (optional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**

   ```bash
   python app.py
   ```

   The application should now be running at `http://127.0.0.1:5000/`.

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Enter the required information:
   - Client's name
   - Client's address
   - Type of IT service (multiple selections possible)
   - Amount (in Euros)
3. Click on "Create Invoice" to download the invoice as a PDF.

## Google Places API

To use the Google Places API, you need to create an API key and insert it into the HTML files where the Google Maps library is included. You can request your API key here: [Google Cloud Platform](https://cloud.google.com/maps-platform/).

Insert the API key in the following line:
```html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places" async defer></script>
```

## Author

Lukas Oliver Lamberz  
[GitHub Profile](https://github.com/Lamboserker)
