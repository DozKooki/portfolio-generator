from flask import Blueprint, render_template, request, redirect, url_for, send_file
import os
import shutil

from app.utils import create_portfolio_site, zip_folder

main = Blueprint('main', __name__)

@main.route('/')
def form():
    return render_template('form.html')

@main.route('/generate', methods=['POST'])
def generate():
    data = request.form.to_dict()
    user_id = os.urandom(4).hex()
    output_folder = f"generated_sites/{user_id}"
    os.makedirs(output_folder, exist_ok=True)

    create_portfolio_site(output_folder, data)
    zip_path = f"downloads/{user_id}.zip"
    zip_folder(output_folder, zip_path)

    return redirect(url_for('main.download', user_id=user_id))

@main.route('/download/<user_id>')
def download(user_id):
    zip_path = f"downloads/{user_id}.zip"
    folder_path = f"generated_sites/{user_id}"
    try:
        # Send the file to user
        response = send_file(zip_path, as_attachment=True)

        # Clean up after sending
        if os.path.exists(zip_path):
            os.remove(zip_path)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)

        return response
    except Exception as e:
        return f"Error: {str(e)}"
