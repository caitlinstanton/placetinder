import sqlite3, hashlib

def encrypt(word):
    """
    Encrypts a word using the sha256 hash algorithm.
    Args:
        word (str): The word to be encrypted.
    Returns:
        str: The encrypted word.
    """
    hashp = hashlib.sha256()
    hashp.update(word)
    return hashp.hexdigest()

def addUser(username, password, email):
    """
    Adds a user to the database.
    Args:
        username (str): The user's username.
        password (str): The user's password.
        email (str): The user's email address.
    """
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = "INSERT INTO users VALUES('" + username + "','" + encrypt(password) + "','" + email + "');"
    c.execute(q)
    conn.commit()
    conn.close()

def userExists(username):
    """
    Checks whether a user exists in the database.
    Args:
        username (str): The username to be checked.
    Returns:
        boolean: Whether the user exists.
    """
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = "SELECT name FROM users;"
    exists = False
    for i in c.execute(q):
        if i[0] == username:
            exists = True
            break
    conn.commit()
    conn.close()
    return exists

def authenticate(username, password):
    """
    Checks whether a username and password combination exists in the database.
    Args:
        username (str): The username to be checked.
        password (str): The password to be checked.
    Returns:
        boolean: Whether the username and password combination exists.
    """
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = "SELECT name, password FROM users;"
    valid = False
    for i in c.execute(q):
        if i[0] == username and i[1] == encrypt(password):
            valid = True
    conn.commit()
    conn.close()
    return valid
    
def addTempevent(eventDict, user):
    """
    Adds an temporary event to the database for a given user.
    Args:
        eventDict (dict): A dictionary of an event as returned from an API.
        user (str): The user to assign the event to.
    """
    description = eventDict["description"].replace("'", "&#146;")
    apiWebsite = eventDict["APIWebsite"]
    url = apiWebsite + eventDict["eventUrl"]
    venue = eventDict["venue"]
    location = venue["city"] + ", " + venue["state"] + ", " + venue["country"]
    datetime = eventDict["eventDateLocal"][:19].replace("T", ", ")
    minPrice = str(eventDict["ticketInfo"]["minPrice"])
    maxPrice = str(eventDict["ticketInfo"]["maxPrice"])
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = "INSERT INTO tempevents VALUES('" + user + "','" + description + "','" + url + "','" + location + "','" + datetime + "','" + minPrice + "','" + maxPrice + "');"
    c.execute(q)
    conn.commit()
    conn.close()
    
def clearTempevents(user):
    """
    Clears the temporary events for a given user.
    Args:
        user (str): The name of the user.
    """
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = "DELETE FROM tempevents WHERE user = '" + user + "';"
    c.execute(q)
    conn.commit()
    conn.close()

def getTempevents(user):
    """
    Returns the temporary events in the database for a given user.
    Args:
        user (str): The user to get events for.
    Returns:
        list: The events.
    """
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    events = []
    q = "SELECT * FROM tempevents WHERE user = '" + user + "';"
    for i in c.execute(q):
        events.append(i)
    conn.commit()
    conn.close()
    return events

def addSavedevent(event, user):
    """
    Adds an event to the user's list of saved events.
    Args:
        event (list): The necessary information from the event.
        user (str): The username.
    """
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = "INSERT INTO savedevents VALUES('" + event[0] + "','" + event[1] + "','" + event[2] + "','" + event[3] + "','" + event[4] + "','" + event[5] + "','" + event[6] + "');"
    c.execute(q)
    conn.commit()
    conn.close()
