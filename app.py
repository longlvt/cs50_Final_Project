import os

from cs50 import SQL
from flask import Blueprint, Flask, redirect, render_template, request, session, flash
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

from datetime import datetime
from controllers.userHandlers import userAuth
from controllers.userInfoHandlers import userManagement
from controllers.dashboardHandler import dashboard
from controllers.purchaseHandler import purchase
from controllers.searchHandler import search

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.register_blueprint(userAuth)
app.register_blueprint(userManagement, url_prefix="/user")
app.register_blueprint(dashboard)
app.register_blueprint(purchase)
app.register_blueprint(search, url_prefix="/search")
