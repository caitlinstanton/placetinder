from flask import Flask, render_template, request, session, redirect
import query, stubhubapi, eventbriteapi, yelpapi

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
            try:
                eventsStubHub = stubhubapi.search(eventType, coordinates, radius, lowPrice, highPrice, dateRange[:dateRange.index("--")] + ";00:00", dateRange[dateRange.index("--")+2:] + ";00:00")
            except:
                eventsStubHub = []
            try:
                eventsEventbrite = eventbriteapi.search(eventType, coordinates, radius, eventbritePrice, dateRange[:dateRange.index("--")], dateRange[dateRange.index("--")+2:])
            except:
                eventsEventbrite = []
            try:
                eventsYelp = yelpapi.search(eventType, coordinates, radius)["businesses"]
            except:
                eventsYelp = []
            for i in eventsStubHub:
                i["APIWebsite"] = "http://www.stubhub.com/"
            for i in eventsEventbrite:
                i["price"] = eventbritePrice
            i = 0
            while i < len(eventsYelp):
                locDict = eventsYelp[i]["location"]
                if not (locDict.has_key("city") and locDict.has_key("state_code") and locDict.has_key("country_code")):
                    eventsYelp.pop(i)
                    i -= 1
                i += 1
            query.clearTempevents(session["username"])
            for i in eventsStubHub:
                query.addStubHubEvent(i, session["username"])
            for i in eventsEventbrite:
                query.addEventbriteEvent(i, session["username"])
            for i in eventsYelp:
                query.addYelpEvent(i, session["username"])
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
 
@app.route("/list", methods = ["GET", "POST"])
def list():
    if session.has_key("loggedIn") and session["loggedIn"]:
        if len(request.form) == 0:
            events = query.getSavedevents(session["username"])
            return render_template("list.html", events = events)
        elif len(request.form) == 1:
            query.removeEvent(session["username"], request.form.keys()[0])
            events = query.getSavedevents(session["username"])
            return render_template("list.html", events = events)
    else:
        return render_template("login.html")
 
@app.route("/logout")
def logout():
    if session.has_key("loggedIn") and session["loggedIn"]:
        session["username"] = ""
        session["searched"] = False
        session["eventCounter"] = 0
        session["loggedIn"] = False
        return redirect("")
 
app.secret_key = "secretsecret"
if __name__ == "__main__":
     app.debug = True
     app.run(host='0.0.0.0',port=8000)
