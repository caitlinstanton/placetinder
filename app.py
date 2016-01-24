from flask import Flask, render_template, request, session, redirect
import query, stubhubapi, eventbriteapi

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

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
        freeEvents = False
        paidEvents = False
        if request.form.has_key("$"):
            highPrice = 25
            freeEvents = True
        if request.form.has_key("$$"):
            highPrice = 50
            paidEvents = True
        if request.form.has_key("$$$"):
            highPrice = 100
            paidEvents = True
        if request.form.has_key("$$$$"):
            highPrice = 999999999
            lowPrice = 100
            paidEvents = True
        if request.form.has_key("$$$"):
            lowPrice = 50
        if request.form.has_key("$$"):
            lowPrice = 25
        if request.form.has_key("$"):
            lowPrice = 0
        if highPrice == -1 or lowPrice == -1 or not (freeEvents or paidEvents):
            return render_template("settings.html", error = "Specify a price range")
        else:
            if freeEvents and paidEvents:
                eventbritePrice = ""
            elif freeEvents:
                eventbritePrice = "free"
            else:
                eventbritePrice = "paid"
            eventsStubHub = stubhubapi.search(eventType, coordinates, radius, lowPrice, highPrice, dateRange[:dateRange.index("--")] + ";00:00", dateRange[dateRange.index("--")+2:] + ";00:00")
            eventsEventbrite = eventbriteapi.search(eventType, coordinates, radius, eventbritePrice, dateRange[:dateRange.index("--")], dateRange[dateRange.index("--")+2:])
            for i in eventsStubHub:
                i["APIWebsite"] = "http://www.stubhub.com/"
            for i in eventsEventbrite:
                i["price"] = eventbritePrice
            query.clearTempevents(session["username"])
            for i in eventsStubHub:
                query.addStubHubEvent(i, session["username"])
            for i in eventsEventbrite:
                query.addEventbriteEvent(i, session["username"])
            session["searched"] = True
            session["eventCounter"] = 0
            return redirect("results")
    else:
        return render_template("settings.html")

@app.route("/results", methods = ["GET", "POST"])
def results():
    if session.has_key("searched") and session["searched"]:
        events = query.getTempevents(session["username"])
        if request.form.has_key("reject"):
            session["eventCounter"] += 1
            if len(events) > session["eventCounter"]:
                return render_template("results.html", event = events[session["eventCounter"]])
            else:
                return render_template("results.html", message = "No events remaining")
        elif request.form.has_key("accept"):
            query.addSavedevent(events[session["eventCounter"]], session["username"])
            session["eventCounter"] += 1
            if len(events) > session["eventCounter"]:
                return render_template("results.html", event = events[session["eventCounter"]])
            else:
                return render_template("results.html", message = "No events remaining")
        else:
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
        session["eventCounter"] = 0
        session["loggedIn"] = False
    return redirect("")

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "secret_key"
    app.run(host='0.0.0.0',port=8000)
