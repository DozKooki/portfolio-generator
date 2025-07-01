

# 🚀 Portfolio Generator

> A simple, customizable Python + Flask web app that lets users generate their own portfolio websites in seconds — complete with themes, QR codes, and downloadable ZIPs.

---

## ✨ Features

* ✅ **Multiple themes:** Choose from `minimal`, `glass`, `vibrant`, or `default`.
* ✅ **Dynamic HTML & CSS generation** based on user input.
* ✅ **QR Code generation** that links to your hosted portfolio or a placeholder.
* ✅ **Download as ZIP** for instant use or deployment.
* ✅ **Auto-clean** old generated folders to keep your server tidy.
* ✅ **Lightweight Flask server** easy to deploy on Render, Railway, or locally.

---

## 🖥️ Tech Stack

* **Backend:** Python 3.10+, Flask
* **Frontend:** HTML5, CSS3 (generated dynamically)
* **Extras:**

  * [`qrcode`](https://pypi.org/project/qrcode/) for QR generation
  * [`Pillow`](https://pypi.org/project/Pillow/) for image processing
  * `zipfile` for creating site downloads

---

## 🚀 Quick Start

### ⚙️ Clone & Install

```bash
git clone https://github.com/DozKooki/portfolio-generator.git
cd portfolio-generator
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

---

### 🔥 Run Locally

```bash
python app.py
```

Then open your browser at:

```
http://localhost:5000
```

---

## 🗂️ Project Structure

```
portfolio-generator/
│
├── app.py                # Main Flask app
├── app/
│   ├── routes.py         # Routes & views
│   └── utils.py          # Portfolio generation functions
│
├── templates/
│   ├── form.html         # User input form
│   └── success.html      # Download & QR code page
│
├── requirements.txt      # Python dependencies
├── runtime.txt           # Python version for deployment
├── .gitignore            # Ignore venv, pycache, downloads etc.
└── README.md             # This file
```

---

## ⚡ Deployment

### 🚀 Render or Railway

* Ensure your repo has `runtime.txt`:

```
python-3.10.12
```

* **Render Start Command:**

```
gunicorn app:app
```

* Or for very basic free instances:

```
python app.py
```

✅ Now your app is live — users can fill the form, download their portfolio ZIP, scan the QR, and host it wherever they like.

---

## 📜 License

This project is licensed under the **MIT License** — see [`LICENSE`](./LICENSE) for details.

---

## 🤝 Contributing

Pull requests are welcome!
Want to add new themes, improve QR linking, or add more export formats? Fork and make a PR.

---

## 🚀 Author

**DozKooki**

* 📧 [dishankshetty29@gmail.com](mailto:dishankshetty29@gmail.com)
* 💻 [GitHub](https://github.com/DozKooki)

> ⭐ Star this repo if you like it — it helps others discover it too!

---
