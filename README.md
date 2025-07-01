# 🚀 Portfolio Generator

> A simple, customizable Python + Flask web app that lets users generate their own portfolio websites in seconds, complete with themes, QR codes, and downloadable zips.

## ✨ Features

✅ **Multiple themes**  
Choose from `minimal`, `glass`, `vibrant`, or `default` to style your personal portfolio.

✅ **Dynamic HTML & CSS generation**  
Based on user input, the app generates a complete portfolio website.

✅ **QR Code generation**  
Automatically generates a QR code linking to your hosted portfolio (or a placeholder link).

✅ **Download as zip**  
Users can instantly download their generated site as a ZIP file.

✅ **Auto-clean**  
Old generated folders are cleaned up automatically to keep your server tidy.

✅ **Lightweight Flask server**  
Runs efficiently and is easy to deploy on any platform (Render, Railway, etc.).

## 🖥️ Tech Stack

- **Backend:** Python 3.10+, Flask
- **Frontend:** HTML5, CSS3 (generated dynamically)
- **Extras:** 
  - [`qrcode`](https://pypi.org/project/qrcode/) for QR image generation
  - [`Pillow`](https://pypi.org/project/Pillow/) for image processing
- **Packaging:** `zipfile` to create downloadable site archives

## 🚀 Quick Start

### ⚙️ Clone & Install

```bash
git clone https://github.com/DozKooki/portfolio-generator.git
cd portfolio-generator
python3 -m venv venv
source venv/bin/activate  # (Linux/macOS)
venv\Scripts\activate     # (Windows)
pip install -r requirements.txt
yaml
Copy
Edit

---

## 🔥 RUN LOCALLY

```markdown
### 🔥 Run Locally

```bash
python app.py
Then open your browser at:

arduino
http://localhost:5000

## 🗂️ Project Structure

portfolio-generator/
│
├── app.py # Main Flask app
├── app/
│ ├── routes.py # Routes & views
│ └── utils.py # Portfolio generation functions
│
├── templates/
│ ├── form.html # User form page
│ └── success.html # Download & QR page
│
├── static/
│ └── style.css # Sample base CSS
│
├── requirements.txt # Python dependencies
├── runtime.txt # Python version for deployment
├── .gitignore # Ignore venv, pycache, downloads etc
└── README.md # This file

C
