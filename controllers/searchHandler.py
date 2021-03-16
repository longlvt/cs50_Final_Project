from flask import Flask, redirect, render_template, request, flash, Blueprint, jsonify, session
from cs50 import SQL
from helpers import apology, login_required


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///bookDB.db")

search = Blueprint('search', __name__)

@search.route("/", methods=["GET", "POST"])
@login_required
def searchBook():
    if request.method == "POST":
        if not request.form.get("title"):
            flash('You need to input Book title', category='error')
        else:
            book = db.execute("SELECT * FROM books WHERE \"Book-Title\" = ?", request.form.get("title"))
            if len(book) == 0:
                return apology("Sorry, can't find your book.")
            else:
                url = "/search/detail?isbn=" + str(book[0]['ISBN'])
                print(f"DETAIL URL: {url}")
                return redirect(url)
                # return render_template("/bookDetail.html", book=book[0])
    else:
        return render_template("/search.html")

@search.route("/auto")
@login_required
def searchAuto():
    title = request.args.get('title')
    if title:
        books = db.execute("SELECT * FROM books WHERE \"Book-Title\" LIKE ? LIMIT 5", title + "%")
        # print(f"FOUND: {books}")
    else:
        books = []
    return jsonify(books)

@search.route("/detail", methods=["GET", "POST"])
@login_required
def detail():
    if request.method == "GET":
        isbn = request.args.get('isbn')
        if isbn:
            book = db.execute("SELECT * FROM books WHERE ISBN = ?", isbn)
            if len(book) == 0:
                return apology("Sorry, can't find your book.")
            else:
                print(f"FOUND: {book}")
                return render_template("/bookDetail.html", book=book[0])
        else:
            return apology("Sorry, something is missing. We can proceed with your request. Please try again.")
    else:
        isbn = request.form.get('productId')
        print(f"ISBN TO ADD TO CART: {isbn}")

        """ Add book to Cart table """
        # First, check if user already has same book in cart
        book = db.execute("SELECT * FROM cart WHERE userId = ? AND bookId = ?", session["user_id"], isbn)
        if len(book) > 0:
            # Update quantity of book in 'cart' table
            db.execute("UPDATE cart SET quantity = ? WHERE userId = ? AND bookID = ?", book[0]["quantity"] + 1, session["user_id"], isbn)
        else:
            # Create new row in 'cart' table
            db.execute("INSERT INTO cart (userId, bookId, quantity) VALUES (?, ?, ?)", session["user_id"], isbn, 1)
        return redirect('/cart')