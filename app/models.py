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



