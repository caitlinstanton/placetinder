from flask import Flask, render_template, request, session, redirect
import query, stubhubapi

app = Flask(__name__)

@app.route("/")
def home():
    print session["events"]
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
            elif request.form["email"] != request.form["confirmEmail"]:
                return render_template("create.html", error = "Email does not match confirm email")
            else:
                if not query.userExists(request.form["username"]):
                    query.addUser(request.form["username"], request.form["password"], request.form["email"])
                    session["loggedIn"] = True
                    session["username"] = request.form["username"]
                    return redirect("settings")
                else:
                    return render_template("create.html", error = "Username already exists")
        else:
            return render_template("create.html")

@app.route("/settings", methods = ["GET", "POST"])
def settings():
    if request.form.has_key("submit"):
        eventType = request.form["type"]
        dateRange = request.form["date"]
        radius = request.form["radius"]
        coordinates = request.form["coordinates"].replace(" ", "")
        coordinates = coordinates[1:len(coordinates)-1]
        highPrice = -1;
        lowPrice = -1;
        if request.form.has_key("$"):
            highPrice = 25
        if request.form.has_key("$$"):
            highPrice = 50
        if request.form.has_key("$$$"):
            highPrice = 100
        if request.form.has_key("$$$$"):
            highPrice = 999999999
            lowPrice = 100
        if request.form.has_key("$$$"):
            lowPrice = 50
        if request.form.has_key("$$"):
            lowPrice = 25
        if request.form.has_key("$"):
            lowPrice = 0
        if highPrice == -1 or lowPrice == -1:
            return render_template("settings.html", error = "Specify a price range")
        else:
            eventsStubHub = stubhubapi.search(eventType, coordinates, radius, lowPrice, highPrice, dateRange[:dateRange.index("--")] + ";00:00", dateRange[dateRange.index("--")+2:] + ";00:00")
            for i in eventsStubHub:
                i["APIWebsite"] = "http://www.stubhub.com/"
            query.clearTable("events")
            numEvents = query.countEvents()
            for i in eventsStubHub:
                query.addEvent(i, numEvents)
                numEvents += 1
            session["searched"] = True
            return redirect("results")
    else:
        return render_template("settings.html")

@app.route("/results")
def results():
    if session.has_key("searched") and session["searched"]:
        events = query.getEvents()
        if len(events) > 0:
            return render_template("results.html", event = events[0])
        else:
            return render_template("results.html", message = "No events found")
    else:
        return redirect("settings")

@app.route("/list")
def list():
    return render_template("list.html")

@app.route("/logout")
def logout():
    if session.has_key("loggedIn") and session["loggedIn"]:
        session["username"] = ""
        session["searched"] = False
        session["loggedIn"] = False
    return redirect("")

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "secret_key"
    app.run(host='0.0.0.0',port=8000)
