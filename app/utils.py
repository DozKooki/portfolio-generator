import os
import zipfile
import qrcode


def create_portfolio_site(folder, data):
    theme = data.get('theme', 'default')

    html_content = f"""
    <html>
    <head>
        <title>{data.get('name', 'My Portfolio')}</title>
        <link rel="stylesheet" href="./style.css">
    </head>
    <body>
        <h1>{data.get('name', '')}</h1>
        <p>{data.get('about', '')}</p>
        <h3>Skills</h3>
        <p>{data.get('skills', '')}</p>
        <h3>Projects</h3>
        <ul>
            <li>{data.get('project1', '')}</li>
            <li>{data.get('project2', '')}</li>
        </ul>
    </body>
    </html>
    """
    with open(os.path.join(folder, "index.html"), "w") as f:
        f.write(html_content)

    # Write themed CSS directly as style.css
    css_content = ""
    if theme == "glass":
        css_content = """
        body {
            background: url('https://images.unsplash.com/photo-1612831663830-cfb05e4bc674?auto=format&fit=crop&w=1950&q=80') no-repeat center center fixed;
            background-size: cover;
            color: #fff;
            font-family: 'Segoe UI', sans-serif;
            padding: 2rem;
        }
        h1 {
            background: rgba(255,255,255,0.2);
            backdrop-filter: blur(8px);
            border-radius: 10px;
            padding: 1rem;
        }
        """
    elif theme == "minimal":
        css_content = """
        body {
            background: #f9f9f9;
            color: #222;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            line-height: 1.8;
            max-width: 800px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            color: #333;
        }
        h3 {
            margin-top: 2rem;
            color: #555;
        }
        ul li {
            margin: 0.5rem 0;
        }
        """
    elif theme == "vibrant":
        css_content = """
        body {
            background: linear-gradient(135deg, #ff4081, #7a2a8a);
            color: #fff;
            font-family: 'Poppins', sans-serif;
            padding: 2rem;
        }
        h1 {
            color: #fff;
            font-size: 3rem;
            animation: slideIn 1s ease forwards;
        }
        h3 {
            color: #ffe57f;
        }
        ul li {
            margin: 0.5rem 0;
        }
        @keyframes slideIn {
            from { transform: translateY(-20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        """
    else:  # default
        css_content = """
        body {
            font-family: sans-serif;
            background: #111;
            color: #eee;
            padding: 2rem;
        }
        h1 {
            color: #ff4081;
        }
        h3 {
            color: #90ee90;
        }
        """

    with open(os.path.join(folder, "style.css"), "w") as f:
        f.write(css_content)

    # QR Code
    portfolio_url = f"https://myportfolio-host.com/{os.path.basename(folder)}/"
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(portfolio_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(os.path.join(folder, "qr.png"))

    # README.html
    readme_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Your Portfolio Instructions</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f9f9f9;
            color: #333;
            padding: 2rem;
            max-width: 700px;
            margin: auto;
            line-height: 1.6;
        }}
        h1, h2 {{ color: #4b0082; }}
        code {{
            background: #eee;
            padding: 0.2rem 0.4rem;
            border-radius: 4px;
        }}
        .qr {{
            text-align: center;
            margin: 2rem 0;
        }}
        .qr img {{
            max-width: 200px;
        }}
    </style>
</head>
<body>
    <h1>✅ Your Personal Portfolio is Ready!</h1>
    <p>Files:</p>
    <ul>
        <li><strong>index.html</strong> – Homepage</li>
        <li><strong>style.css</strong> – Design</li>
        <li><strong>qr.png</strong> – Your QR code</li>
    </ul>

    <div class="qr">
        <img src="qr.png" alt="QR Code" />
    </div>

    <h2>🚀 How to Deploy</h2>
    <p>1. Upload files to GitHub or Vercel.</p>
    <p>2. Your portfolio will be live!</p>

    <h2>📱 QR Code</h2>
    <p>This QR links to:</p>
    <code>{portfolio_url}</code>

    <h2>🔥 You’re all set!</h2>
</body>
</html>
"""
    with open(os.path.join(folder, "README.html"), "w") as f:
        f.write(readme_content)


def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))
