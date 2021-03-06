from flask import Flask, redirect, render_template, request, session, flash, Blueprint
from cs50 import SQL
from helpers import apology, login_required

db = SQL("sqlite:///bookDB.db")

@buy.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        return redirect("user/transaction")
    else:
        return render_template("/buy.html")