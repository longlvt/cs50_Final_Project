from flask import Flask, redirect, render_template, request, session, flash, Blueprint
from cs50 import SQL

from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///bookDB.db")

userAuth = Blueprint('userAuth', __name__)

@userAuth.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # user = db.execute("SELECT id FROM users WHERE username = ? AND hash = ?", username, pwdHash)
        # session["user_id"] = user[0]["id"]
        userName = request.form.get("username")
        password = request.form.get("password")
        confirmPwd = request.form.get("confirmation")
        validInput = userName and len(userName) <= 25 and password and len(password) <= 20 and confirmPwd == password
        # print(f"VALID: {validInput}")
        if validInput == True:
            # Ensure that Username hasn't been taken in DB
            user = db.execute("SELECT * FROM users WHERE username = ?", userName)
            if len(user) > 0:
                flash("Invalid Username/Password", category='error')
                return render_template("register.html")
            else:
                # If input userName not found in DB, proceed to add new user to DB
                db.execute("INSERT INTO users (userName, hash) VALUES (?, ?)", userName, generate_password_hash(password))
                return redirect("/login")
        else:
            if not userName or len(userName) > 25:
                # nameMsg = ['Username can not be blank.', 'Maximum 25 characters.']
                # errMsg.append('Username is missing!')
                flash('Username is missing!', category='error')
            elif len(userName) > 25:
                flash('Username too long (maximum 25 characters)', category='error')
            elif not password:
                # pwdMsg = ['Password can not be blank', 'Maximum 20 characters.']
                # errMsg.append('Password is missing!')
                flash('Password is missing!', category='error')
            elif len(password) > 20:
                # errMsg.append('Password too long (maximum 20 characters).')
                flash('Password too long (maximum 20 characters)', category='error')
            elif password != confirmPwd:
                # errMsg.append('Password too long (maximum 20 characters).')
                flash('Password not matched', category='error')
            return render_template("register.html")
    if request.method == "POST":
        return redirect("/login.html")
    else:
        return render_template("register.html")


@userAuth.route("/login", methods=["GET", "POST"])
def login():
    """ Login user """
    # Forget any user_id
    session.clear()

    if request.method == "POST":
        # user = db.execute("SELECT id FROM users WHERE username = ? AND hash = ?", username, pwdHash)
        # session["user_id"] = user[0]["id"]
        userName = request.form.get("username")
        password = request.form.get("password")
        user = db.execute("SELECT * FROM users WHERE userName = ?", userName)
        if not userName or len(userName) > 25: # If userName = blank
            flash('Username is missing!', category='error')
            return render_template("login.html")
        elif not password: # If no password = blankt
            flash('Password is missing!', category='error')
            return render_template("login.html")
        elif len(user) != 1 or len(password) > 20 or not check_password_hash(user[0]["hash"], password):
            flash('Invalid Username/Password', category='error')
            return render_template("login.html")
        else: # Valid user found
            session["user_id"] = user[0]["id"]
            return redirect("/") 
    else:
        return render_template("login.html")

@userAuth.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@userAuth.route("/reset-password", methods=["GET", "POST"])
def resetPwd():
    pass
