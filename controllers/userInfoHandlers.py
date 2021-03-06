from flask import Flask, redirect, render_template, request, session, flash, Blueprint
from cs50 import SQL
from helpers import apology, login_required

db = SQL("sqlite:///bookDB.db")
userInfo = Blueprint(userInfo, __name__)


@app.route("/info")
@login_required
def show_info():
    return render_template("/userInfo.html")

@app.route("/bookmarked")
@login_required
def show_bookmark():
    return render_template("/bookmark.html")

@app.route("/transaction")
@login_required
def show_transactrion():
    return render_template("/transaction.html")

@app.route("/topup", methods=["GET", "POST"])
@login_required
def request_topup():
    if request.method == "POST":
        return redirect("user/info")
    else:
        return render_template("/topup.html")

@app.route("/reset-password", methods=["GET", "POST"])
@login_required
def resetPassword():
    if request.method == "POST":
        return redirect("/")
    else:
        return render_template("/reset-password.html")