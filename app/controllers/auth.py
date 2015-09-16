from flask import Blueprint, render_template, flash, request, redirect, url_for, session
from flask.ext.login import login_user, logout_user, login_required, current_user

from app.extensions import cache
from app.forms import LoginForm, SignupForm
from app.models import db, User

auth = Blueprint('auth', __name__)

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated():
        return redirect("/user")

    form = SignupForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user, remember=True)
        
        flash("You are now signed up. Enjoy.", "success")

        return redirect(request.args.get("next") or "/user")

    return render_template("signup.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated():
        return redirect("/user")

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one()

        login_user(user, remember=True)

        flash("You are now logged in. Enjoy.", "success")
        
        return redirect(request.args.get("next") or "/user")

    return render_template("login.html", form=form)


@auth.route("/logout")
def logout():
    session.pop('google_token', None)
    session.pop('facebook_token', None)

    logout_user()

    flash("You have been logged out.", "success")
    
    return redirect("/login")
