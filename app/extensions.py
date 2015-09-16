from flask.ext.cache import Cache
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.login import LoginManager
from flask_wtf.csrf import CsrfProtect
from flask_oauthlib.client import OAuth

from app.models import User

# Setup flask cache
cache = Cache()

debug_toolbar = DebugToolbarExtension()

csrf = CsrfProtect()

oauth = OAuth()

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message_category = "warning"

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
