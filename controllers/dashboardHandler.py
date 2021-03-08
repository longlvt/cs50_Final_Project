from flask import Flask, redirect, render_template, request, session, flash, Blueprint
from cs50 import SQL
from helpers import apology, login_required

db = SQL("sqlite:///bookDB.db")
dashboard = Blueprint('dashboard', __name__)

@dashboard.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show Search box, and 5 Top rating books"""

    if request.method == "POST":
        return redirect("/search/detail")
    else:
        return render_template("index.html")