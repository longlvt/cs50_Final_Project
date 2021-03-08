from flask import Flask, redirect, render_template, request, session, flash, Blueprint
from cs50 import SQL
from helpers import apology, login_required


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///bookDB.db")

purchase = Blueprint('purchase', __name__)

@purchase.route("/purchase", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        return redirect("user/transaction")
    else:
        return render_template("/buy.html")