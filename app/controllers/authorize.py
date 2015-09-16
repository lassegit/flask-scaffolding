from flask import Blueprint, Flask, flash, render_template, redirect, url_for, session, request, jsonify, current_app
from flask.ext.login import login_user, logout_user, login_required, current_user
from flask_oauthlib.client import OAuth, OAuthException
import shortuuid, json

from app.models import db, User, Authorize

authorize = Blueprint("authorize", __name__)

oauth = OAuth()

"""Google authenticating"""
google = oauth.remote_app("google",
    consumer_key = "<YOUR_KEY>.apps.googleusercontent.com",
    consumer_secret = "<YOUR_SECRET>",
    request_token_params = {
        "scope": "email"
    },
    base_url = "https://www.googleapis.com/oauth2/v1/",
    request_token_url = None,
    access_token_method = "POST",
    access_token_url = "https://accounts.google.com/o/oauth2/token",
    authorize_url = "https://accounts.google.com/o/oauth2/auth",
)

@authorize.route("/oauth2/google")
def google_info():
    callback = url_for('.google_auth', _external = True)
    return google.authorize(callback)

@google.tokengetter
def google_token():
    return session.get('google_token')

@authorize.route("/oauth2/google/callback")
def google_auth():
    resp = google.authorized_response()

    if resp is None:
        flash("An error occurred.", "danger")
        return redirect("/login")
        
    session['google_token'] = (resp['access_token'], '')
    google_user = google.get('userinfo')
    google_user = google_user.data

    authorize = Authorize.query.filter_by(oauth_id = google_user.get("id"), network = "google").first()
    
    if authorize is None:
        user = User.query.filter_by(email = google_user.get("email")).first()

        if user:
            """No authorize, but a user exists"""
            authorize = Authorize(google_user.get("id"), google_user.get("email"), "google", user.id)
            db.session.add(authorize)
            db.session.commit()
        else:
            """No user and no authorize"""
            username = google_user.get("name").replace(" ", "") + "-" + shortuuid.ShortUUID().random(length=5)
            user = User(username, google_user.get("email"), "")
            db.session.add(user)
            db.session.commit()

            authorize = Authorize(google_user.get("id"), google_user.get("email"), "google", user.id)
            db.session.add(authorize)
            db.session.commit()

        login_user(user, remember=True)

        flash("You are now signed up.", "success")

        return redirect(request.args.get("next") or "/user")
    else:
        """Authorize is found and therefore also user"""
        user = User.query.get(authorize.user_id)

        login_user(user, remember=True)
        
        flash("You are now signed in.", "success")

        return redirect(request.args.get("next") or "/user")

"""Facebook authenticating https://developers.facebook.com/apps"""
facebook = oauth.remote_app("facebook",
    consumer_key = "<KEY>", # APP ID
    consumer_secret = "<SECRET>", # APP SECRET
    request_token_params = {
        "scope": "email"
    },
    base_url = "https://graph.facebook.com/",
    request_token_url = None,
    access_token_url = "/oauth/access_token",
    access_token_method = "GET",
    authorize_url = "https://www.facebook.com/dialog/oauth",
)

@authorize.route("/oauth2/facebook")
def facebook_info():
    callback = url_for('.facebook_auth', _external = True, next=request.args.get('next') or None)
    return facebook.authorize(callback)

@facebook.tokengetter
def facebook_token():
    return session.get('oauth_token')

@authorize.route("/oauth2/facebook/callback")
def facebook_auth():
    resp = facebook.authorized_response()

    if resp is None or isinstance(resp, OAuthException):
        flash("An error occurred.", "danger")

        return redirect("/user")
        
    session['oauth_token'] = (resp['access_token'], '')

    facebook_user = facebook.get('/me')
    facebook_user = facebook_user.data

    authorize = Authorize.query.filter_by(oauth_id = facebook_user.get("id"), network = "facebook").first()
    
    if authorize is None:
        """No user and no authorize"""
        username = facebook_user.get("name").replace(" ", "") + "-" + shortuuid.ShortUUID().random(length=5)
        user = User(username, None, "")
        db.session.add(user)
        db.session.commit()

        authorize = Authorize(facebook_user.get("id"), None, "facebook", user.id)
        db.session.add(authorize)
        db.session.commit()

        login_user(user, remember=True)

        flash("You are now signed up.", "success")

        return redirect(request.args.get("next") or "/user")

    """Authorize is found and therefore also user"""
    user = User.query.get(authorize.user_id)

    login_user(user, remember=True)
    
    flash("You are now signed in.", "success")
    
    return redirect(request.args.get("next") or "/user")

