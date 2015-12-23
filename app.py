from flask import Flask, render_template, request, session, redirect
import query

app = Flask(__name__)

@app.route("/")
def home():
    if session.has_key("loggedIn") and session["loggedIn"]:
        loggedIn = session["loggedIn"]
    else:
        loggedIn = False
    return render_template("home.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.form.has_key("username") and request.form.has_key("password"):
        if query.authenticate(request.form["username"], request.form["password"]):
            session["loggedIn"] = True
            session["username"] = request.form["username"]
            return redirect("settings")
        else:
            return render_template("login.html", error = "Invalid username or password")
    else:
        if session.has_key("loggedIn") and session["loggedIn"]:
            return redirect("settings")
        else:
            return render_template("login.html")

@app.route("/create", methods = ["GET", "POST"])
def create():
    if session.has_key("loggedIn") and session["loggedIn"]:
        return redirect("settings")
    else:
        if request.form.has_key("username"):
            if request.form["password"] != request.form["confirmPassword"]:
                return render_template("create.html", error = "Password does not match confirm password")
            else:
                if not query.userExists(request.form["username"]):
                    query.addUser(request.form["username"], request.form["password"])
                    session["loggedIn"] = True
                    session["username"] = request.form["username"]
                    return redirect("settings")
                else:
                    return render_template("create.html", error = "Username already exists")
        else:
            return render_template("create.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/results")
def results():
    return render_template("results.html")

@app.route("/list")
def list():
    return render_template("list.html")

@app.route("/logout")
def logout():
    if session.has_key("loggedIn") and session["loggedIn"]:
        session["loggedIn"] = False
    return redirect("")

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "secret_key"
    app.run(host='0.0.0.0',port=8000)
