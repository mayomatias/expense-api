from flask import Blueprint, jsonify
from ..service.user_service import *

# Creamos un blueprint para el módulo "user"
user_bp = Blueprint('user', __name__, url_prefix='/api/users')

@user_bp.route('/', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify(users)
