from flask import Blueprint, render_template, flash, request, redirect, current_app
from flask.ext.login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash

from app.extensions import cache
from app.forms import UserForm
from app.models import db, User

profile = Blueprint("profile", __name__)

@profile.route("/user")
@login_required
def user():
    return render_template("user.html")

@profile.route("/user/edit", methods=["GET", "POST"])
@login_required
def user_edit():
    form = UserForm()

    if form.username.data is None:
        form.username.data = current_user.username
    if form.email.data is None:
        form.email.data = current_user.email

    if form.validate_on_submit():
        user = db.session.query(User).get(current_user.get_id())
        user.username = form.username.data
        user.email = form.email.data
        user.password = generate_password_hash(form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect("/user")
    
    return render_template("user_edit.html", form = form)
