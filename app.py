from flask import Flask
from app.routes import main as main_blueprint

def create_app():
    app = Flask(__name__, template_folder="app/templates", static_folder="static")
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.register_blueprint(main_blueprint)
    return app

if __name__ == "__main__":
    from app import create_app
    app = create_app()
    app.run(host='0.0.0.0', port=10000)

