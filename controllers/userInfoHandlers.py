from flask import Flask, redirect, render_template, request, session, flash, Blueprint
from cs50 import SQL

from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required

db = SQL("sqlite:///bookDB.db")
userManagement = Blueprint('userManagement', __name__)

@userManagement.route("/info")
@login_required
def show_info():
    
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    return render_template("/accountInfo.html", user = user[0])

# @userManagement.route("/bookmarked")
# @login_required
# def show_bookmark():
#     return render_template("/bookmark.html")

@userManagement.route("/transaction")
@login_required
def show_transactrion():
    
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    transaction = db.execute("SELECT \"Book-Title\" AS bookTitle, quantity, price, purchaseAt\
        FROM books JOIN transactions WHERE books.ISBN == transactions.bookId AND userId = ?", session["user_id"])
    # transaction = db.execute("SELECT * FROM transactions WHERE userId = ?", session["user_id"])
    return render_template("/transactionInfo.html", history=transaction, user = user[0])

@userManagement.route("/topup", methods=["GET", "POST"])
@login_required
def request_topup():
    
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    if request.method == "POST":
        amount = request.form.get("amount")
        password = request.form.get("password")
        if not check_password_hash(user[0]["hash"], password):
            return render_template("topup.html", user = user[0], message='Invalid Password')
        elif not amount.isnumeric() or int(amount) < 0 or int(amount) > 10000:
            return render_template("topup.html", user = user[0], message='Invalid Amount')
        else:
            # UPDATE new balance
            db.execute("UPDATE users SET balance = ? WHERE id = ?", user[0]["balance"] + int(amount), session["user_id"])
            return redirect("/user/info")
    else:
        return render_template("topup.html", user = user[0])

@userManagement.route("/reset-password", methods=["GET", "POST"])
@login_required
def resetPassword():    
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    if request.method == "POST":
        current = request.form.get("current")
        new = request.form.get("new")
        confirm = request.form.get("confirmation")
        if not current or not new or not confirm or \
            (len(current) < 4 or len(current) > 20) or (len(new) < 4 or len(new) > 20) or not check_password_hash(user[0]["hash"], current):
            return render_template("resetPwd.html", user = user[0], message='Invalid Password')
        elif new != confirm:
            return render_template("resetPwd.html", user = user[0], message='Password not matched')
        else:
            # Update new Password to DB
            db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(new), session["user_id"])
            return redirect("/user/info")
    else:
        return render_template("resetPwd.html", user = user[0])