from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms import validators
from flask.ext.login import current_user

from .models import db, User

class SignupForm(Form):
    email = TextField(u'email', validators=[validators.required(), validators.Email()])
    username = TextField(u'Username', validators=[validators.required()])
    password = PasswordField(u'Password', validators=[validators.required()])

    def validate(self):
        check_validate = super(SignupForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email is already taken.")
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Username is already taken.")
            return False

        return True

class LoginForm(Form):
    email = TextField(u'email', validators=[validators.required()])
    # username = TextField(u'Username', validators=[validators.required()])
    password = PasswordField(u'Password', validators=[validators.required()])

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False
        
        # Does our the exist
        user = User.query.filter_by(email=self.email.data).first()
        if not user:
            self.email.errors.append("Invalid email or password")
            return False

        # Do the passwords match
        if not user.check_password(self.password.data):
            self.email.errors.append("Invalid email or password")
            return False

        return True

class UserForm(Form):
    email = TextField(u'email', validators=[validators.required()])
    username = TextField(u'Username', validators=[validators.required()])
    password = PasswordField(u'Password', validators=[validators.required()])

    def validate(self):
        check_validate = super(UserForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        user = User.query.filter(User.id != current_user.get_id(), User.username == self.username.data).first()
        if user:
            self.username.errors.append("Username is already taken.")
            return False

        user = User.query.filter(User.id != current_user.get_id(), User.email == self.email.data).first()
        if user:
            self.email.errors.append("Email is already taken.")
            return False

        return True
