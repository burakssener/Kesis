import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
# app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///social.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():



@app.route("/history")
@login_required



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 400)
        else:
            username = request.form.get("username")
            if not request.form.get("password") or not request.form.get("confirmation"):
                return apology("must provide password", 400)
            else:
                password = request.form.get("password")
                crpassword = request.form.get("confirmation")
                users = db.execute("SELECT username FROM users WHERE username= ? ", username)
                if  password != crpassword:
                    return apology("must provide password", 400)
                for user in users:
                    if username == user["username"]:
                     return apology("This username is taken", 400)
                db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
                return render_template("login.html")




@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Buy shares of stock"""
    if request.method == "GET":
        user_data = db.execute("SELECT stock_num AS Shares, stock_name AS Name FROM users_balance WHERE user_id = ?", session['user_id'])
        return render_template("sell.html", user_data = user_data)

    elif request.method == "POST":
        symbol = lookup(request.form.get("symbol"))
        stock_data = db.execute("SELECT stock_num, stock_name FROM users_balance WHERE user_id = ? ", session['user_id'])
        status = False
        for stock in stock_data:
            if symbol["symbol"] == stock["stock_name"]:
                status = True
                real_stock_num = stock["stock_num"]
        if status == True:
            stock_name = symbol["symbol"]
            stock_num = int(request.form.get("shares"))
            user_data = db.execute("SELECT id, cash FROM users WHERE id = ?", session['user_id'])[0]
            for stock in stock_data:
                if stock_name == stock["stock_name"] and real_stock_num < stock_num:
                    return apology("You don't have enough stock")
                if stock_name == stock["stock_name"] and real_stock_num != stock_num:
                    db.execute("UPDATE users_balance SET stock_num = ? WHERE user_id = ? AND stock_name = ?", real_stock_num - stock_num, session['user_id'], stock_name )
                elif stock_name == stock["stock_name"] and real_stock_num == stock_num:
                    db.execute("DELETE FROM users_balance WHERE user_id = ? AND stock_name = ?", session['user_id'], stock_name)
            db.execute("UPDATE users SET cash = ? WHERE id = ?", user_data["cash"] + symbol["price"] * stock_num, session['user_id'] )
            user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session['user_id'])
            user_data = db.execute("SELECT stock_num AS Shares, stock_name AS Name FROM users_balance WHERE user_id = ?", session['user_id'])

            db.execute("INSERT INTO history (hstock_num, hstock_name, hstock_price, user_id) VALUES (?, ?, ?, ?)", -1*stock_num, stock_name, symbol["price"], session['user_id'] )
            total_money = 0
            for stock_data in user_data:
                stock_data["stock_price"] = lookup(stock_data["Name"])["price"]
                stock_data["total"] = stock_data["stock_price"] * int(stock_data["Shares"])
                stock_data["stock_price"] = usd(stock_data["stock_price"])
                total_money += stock_data["total"]
                stock_data["total"] = usd(stock_data["total"])
                total_money += user_cash[0]["cash"]
            return render_template("basket.html", user_data=user_data, user_cash= usd(user_cash[0]["cash"]), total_money = usd(total_money))
        else:
            return apology("Not enough balance", 403)

