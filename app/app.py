from flask import Flask

# --- Routes ---
from routes.main_routes import main_bp  # Importamos el blueprint
from modules.user.routes.user_routes import user_bp


app = Flask(__name__)

# Registramos el blueprint
app.register_blueprint(main_bp)
app.register_blueprint(user_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)