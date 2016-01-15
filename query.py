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
