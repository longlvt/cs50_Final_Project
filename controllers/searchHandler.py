from flask import Flask, redirect, render_template, request, session, flash, Blueprint
from cs50 import SQL
from helpers import apology, login_required


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///bookDB.db")

search = Blueprint('search', __name__)

@search.route("/", methods=["GET", "POST"])
@login_required
def searchDetail():
    return render_template("/bookDetail.html")
