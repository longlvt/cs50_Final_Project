from flask import Flask, redirect, render_template, request, session, flash, Blueprint, jsonify
from cs50 import SQL
from helpers import apology, login_required

from datetime import datetime


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///bookDB.db")

cart = Blueprint('cart', __name__)

@cart.route("/cart", methods=["GET"])
@login_required
def getCart():
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
    # Get information from 'cart' table
    cart = db.execute("SELECT * FROM cart WHERE userId = ?", session["user_id"])

    # Update 'transactions' table
    totalPrice = 0
    for each in cart:
        db.execute("INSERT INTO transactions (userId, bookId, quantity, price, purchaseAt) VALUES (?, ?, ?, ?, ?)",
                    each["userId"], each["bookId"], each["quantity"], 10 * each["quantity"], datetime.now())
        totalPrice += 10 * each["quantity"]

    # Get User balance before purchasing
    balance = db.execute("SELECT balance FROM users WHERE id = ?", session["user_id"])
    
    # Update new balance for user
    db.execute("UPDATE users SET balance = ? WHERE id = ?", balance[0]["balance"] - totalPrice, session["user_id"])

    # Remove current items in cart
    db.execute("DELETE FROM cart WHERE userId = ?", session["user_id"])

    return redirect("/")

