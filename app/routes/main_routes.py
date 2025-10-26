from flask import Blueprint

# Creamos el blueprint
main_bp = Blueprint('main', __name__)

# Definimos la ruta principal
@main_bp.route('/')
def home():
    print("holaaa")
    return '¡Hola desde Flask en Raspberry Pi! 🐍'