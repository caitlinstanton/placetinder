from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html");

@app.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("login.html");

@app.route("/create", methods = ["GET", "POST"])
def create():
    return render_template("create.html");

@app.route("/settings")
def settings():
    return render_template("settings.html");

@app.route("/results")
def results():
    return render_template("results.html");

@app.route("/list")
def list():
    return render_template("list.html");

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
