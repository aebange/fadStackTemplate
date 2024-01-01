import logging.config
from flask import Flask
from controllers.main_controller import main_bp


def create_app():
    app = Flask(__name__)

    # Register the blueprint
    app.register_blueprint(main_bp)

    # Configure logging
    configure_logging()

    return app


def configure_logging():

    if not logging.getLogger().handlers:
        logging.config.fileConfig('../app/config/logging_config.ini')


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, use_reloader=False)
