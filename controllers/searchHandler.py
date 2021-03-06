from flask import Flask, redirect, render_template, request, session, flash, Blueprint
from cs50 import SQL
from helpers import apology, login_required

db = SQL("sqlite:///bookDB.db")
search = Blueprint(search, __name__)


@search.route("/search/detail", methods=["GET", "POST"])
@login_required
def search():
    if request.method == "POST":
        return redirect("/")
    else:
        return render_template("/search.html")
