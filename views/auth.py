from flask import redirect, url_for, request
from flask.blueprints import Blueprint
from flask_dance.contrib.github import make_github_blueprint, github
from flask import session
import os


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

gh_blueprint = make_github_blueprint(
    client_id=os.environ.get("GH_CLIENT_ID"),
    client_secret=os.environ.get("GH_CLIENT_SECRET_KEY"),
    redirect_url='/'    
)

auth = Blueprint("auth", __name__)
@auth.route("/authorize")
def authorize():
    if not github.authorized:
        return redirect(url_for("github.login"))
    else:      
        if session.get("user_id") is None:
            user_info = github.get("/user").json()
            session["user_id"] = user_info["id"]
            session["username"] = user_info["login"]
            session["email"] = user_info["email"]                
        return redirect('/')


@auth.route("/logout")
def callback():
    session.clear()
    return redirect('/')
