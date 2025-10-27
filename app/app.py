from flask import Flask
from configuration.extensions import db
from configuration.config import Config
# --- Routes ---
from routes.main_routes import main_bp  # Importamos el blueprint
from modules.user.routes.user_routes import user_bp


app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializamos SQLAlchemy
    db.init_app(app)

    # Registramos blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)