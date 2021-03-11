from flask import Flask, redirect, render_template, request, session, flash, Blueprint
from cs50 import SQL
from helpers import apology, login_required


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///bookDB.db")

cart = Blueprint('cart', __name__)

@cart.route("/cart", methods=["GET", "POST"])
@login_required
def postCart():
    return render_template("/cart.html")