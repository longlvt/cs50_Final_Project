from flask import Flask, redirect, render_template, request, session, flash, Blueprint
from cs50 import SQL
from helpers import apology, login_required

db = SQL("sqlite:///bookDB.db")
dashboard = Blueprint('dashboard', __name__)

@dashboard.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show Search box, and 5 Top rating books"""
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    # top5Books = db.execute("SELECT ISBN FROM ratings ORDER BY \"Book-Rating\" DESC LIMIT 5")
    # # print(f"BOOKS FOUND: {top5Books}")

    # bookDetails = []
    # for id in top5Books:
    #     detail = db.execute("SELECT * FROM books WHERE ISBN = ?", id["ISBN"])
    #     # print(f"DETAIL: {detail}")
    #     if len(detail) != 0:
    #         bookDetails.append(detail[0])

    bookDetails =db.execute("SELECT * FROM books WHERE ISBN IN (SELECT ISBN FROM ratings ORDER BY \"Book-Rating\" DESC LIMIT 5)")
    # print(f"DETAILS: {bookDetails}")
    if len(user) != 0:
        return render_template("index.html", amount=user[0]["balance"], topBooks = bookDetails)
        