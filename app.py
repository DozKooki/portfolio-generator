from flask import Flask
from app.routes import main as main_blueprint

def create_app():
    app = Flask(__name__, template_folder="app/templates", static_folder="static")
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.register_blueprint(main_blueprint)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
