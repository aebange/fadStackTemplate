import logging
from flask import Flask
from controllers.main_controller import main_bp
from services.data_service import get_data


def create_app():
    app = Flask(__name__)

    # Register the blueprint
    app.register_blueprint(main_bp)

    # Configure logging
    configure_logging()

    return app


def configure_logging():
    pass
    #log = logging.getLogger('werkzeug')
    # Change this if you want to see ALL requests
    #log.setLevel(logging.ERROR)


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, use_reloader=False, host='0.0.0.0')
