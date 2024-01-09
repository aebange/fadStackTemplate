# main_controller.py
from flask import Blueprint, jsonify, current_app
from services.data_service import get_data

main_bp = Blueprint('main', __name__)


@main_bp.route('/api/data', methods=['GET'])
def get_data_route():
    data = get_data()
    current_app.logger.debug("Successfully fetched data from get(data)")
    return jsonify(data)
