# main_controller.py
from flask import Blueprint, jsonify
import logging
from backend.app.services.data_service import get_data

main_bp = Blueprint('main', __name__)


logger = logging.getLogger('flaskLogger')


@main_bp.route('/api/data', methods=['GET'])
def get_data_route():
    data = get_data()
    logger.debug('Hello again!')
    return jsonify(data)
