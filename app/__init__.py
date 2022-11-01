from flask import Flask

from config import config_object

def create_app(config: str) -> Flask:

    app = Flask(__name__)

    app.config.from_object(config_object[config])

    config_object[config].init_app(app)


    # register blueprints if required

    from .main import main_blueprint

    app.register_blueprint(main_blueprint)

    return app