from flask import Flask, redirect, render_template, request, session, flash, Blueprint, jsonify
from cs50 import SQL
from helpers import apology, login_required


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///bookDB.db")

cart = Blueprint('cart', __name__)

@cart.route("/cart", methods=["GET", "POST"])
@login_required
def getCart():
    # cartInfo = db.execute("SELECT * FROM cart WHERE userId = ?", session["user_id"])
    # print(f"CART INFO: {cartInfo}")
    # product_details = []
    # for prod in cartInfo:
    #     detail = db.execute("SELECT * FROM books WHERE ISBN = ?", prod["bookId"])
    #     print(f"DETAIL: {detail}")
    #     if len(detail) != 0:
    #         product_details.append(detail[0])
    product_details = db.execute("SELECT ISBN, \"Book-Title\", quantity\
        FROM books JOIN cart WHERE books.ISBN == cart.bookId AND userId = ?", session["user_id"])
    return render_template("/cart.html", products=product_details)

@cart.route("/cart-delete-item", methods=["POST"])
@login_required
def deleteItem():
    isbn = request.form.get('productId')
    db.execute("DELETE FROM cart WHERE bookId = ? AND userId = ?", isbn, session["user_id"])
    return redirect("/cart")

@cart.route("/buy", methods=["POST"])
@login_required
def buyBook():
    # isbn = request.form.get('productId')
    # db.execute("DELETE FROM cart WHERE bookId = ? AND userId = ?", isbn, session["user_id"])
    # return redirect("/cart")
    pass