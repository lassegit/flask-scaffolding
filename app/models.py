from datetime import datetime
import shortuuid
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.String(22), primary_key=True)
    username = db.Column(db.String(50), default=None)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100), default=None, nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime(), default=None)

    def __init__(self, username, email, password):
        self.id = shortuuid.uuid()
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username

class Authorize(db.Model):
    id = db.Column(db.String(22), primary_key=True)
    oauth_id = db.Column(db.String(100), default=None, nullable=True, index=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120))
    network = db.Column(db.String(30), index=True)
    user_id = db.Column(db.String(22), db.ForeignKey("user.id"), default=None, nullable=False)

    def __init__(self, oauth_id, email, network, user_id):
        self.id = shortuuid.uuid()
        self.oauth_id = oauth_id
        self.email = email
        self.network = network,
        self.user_id = user_id

class Password_reset(db.Model):
    token = db.Column(db.String(44), primary_key=True)
    email = db.Column(db.String(120))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, token, email):
        self.token = token
        self.email = email
