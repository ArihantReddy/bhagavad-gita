# Bhagavad Gita QR Quotes

## Overview

Bhagavad Gita QR Quotes is a FastAPI-based application that displays a random Bhagavad Gita quote whenever the application is opened.

The application is intended to be accessed through a QR code. Users scan the QR code using their mobile phone, which opens the web application and displays a randomly selected Bhagavad Gita verse.

Every new request generates a different quote.

---

## Features

- Random Bhagavad Gita quote generation
- Beautiful mobile-friendly UI
- 701 Bhagavad Gita quotes stored locally in JSON
- FastAPI backend
- Responsive design
- Ready for deployment

---

## Project Structure

```
BhagavadGita/
│
├── app/
│   ├── data/
│   │   └── gita_quotes.json
│   │
│   ├── services/
│   │   └── quote_service.py
│   │
│   ├── static/
│   │   ├── css/
│   │   └── images/
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── main.py
│
├── requirements.txt
├── generate_qr.py
├── scraper.py
└── README.md
```

---

## Installation

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

## QR Code

The QR code should point to the deployed production URL.

Example

```
https://your-domain.com
```

After deployment, update `generate_qr.py` with the production URL and generate the final QR code.

---

## Deployment

The application can be deployed on any platform capable of hosting a FastAPI application.

---

## Author

Developed as part of an internal Bhagavad Gita QR Quote project.