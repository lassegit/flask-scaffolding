#! ../env/bin/python

from flask import Flask

from app.models import db
from app.controllers.main import main
from app.controllers.auth import auth
from app.controllers.profile import profile
from app.controllers.authorize import authorize

from app.tpl_filter import tpl_filter

from app.extensions import (
    cache,
    debug_toolbar,
    login_manager,
    csrf,
    oauth,
)


def create_app(object_name, env="prod"):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. app.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """
    app = Flask(__name__, static_url_path='')

    app.config.from_object(object_name)
    app.config['ENV'] = env

    # templates and statics
    app.template_folder = app.config['TEMPLATE_FOLDER']
    app.static_folder = app.config['STATIC_FOLDER']

    # initialize the cache
    cache.init_app(app)

    # initialize the debug tool bar
    debug_toolbar.init_app(app)

    # CSRF protection
    csrf.init_app(app)

    # Oauthlib
    oauth.init_app(app)
    
    # initialize SQLAlchemy
    db.init_app(app)

    login_manager.init_app(app)

    # register our blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(profile)
    app.register_blueprint(authorize)

    # Import custom template filters
    app.register_blueprint(tpl_filter)

    if app.config["ENV"] == "prod":   
        import logging
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler('app.log', maxBytes=1024 * 1024 * 100, backupCount=20)
        formatter = logging.Formatter( "%(asctime)s | %(pathname)s:%(lineno)d | %(funcName)s | %(levelname)s | %(message)s ")
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)

    return app
