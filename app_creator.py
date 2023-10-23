import logging

from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

from config import AppConfig
from error_handlers import register_error_handlers
from flask_session import Session
from membrane.client.flask import User


def create_app(config: AppConfig):
    """"""
    app = Flask(__name__)
    app.config.from_object(config)

    from routes import blueprint as main_blueprint

    app.register_blueprint(main_blueprint)

    CORS(
        app,
        origins=config.CORS_ALLOWED_ORIGINS,
        supports_credentials=True,
    )

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(config.LOGGING_FORMAT))
    handler.setLevel(getattr(logging, config.LOGGING_LEVEL))
    app.logger.addHandler(handler)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login_page"

    @login_manager.user_loader
    def load_user(email):
        """Load user for Flask-Login."""
        return User(email)

    Session(app)
    register_error_handlers(app)
    return app