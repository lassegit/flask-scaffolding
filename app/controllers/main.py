from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app
from flask.ext.login import login_user, logout_user, login_required, current_user

from app.extensions import cache
from app.forms import LoginForm
from app.models import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
# @cache.cached(timeout=300, unless=lambda: current_user.is_authenticated())
def home():
    return render_template('index.html')

















