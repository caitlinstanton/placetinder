from pymongo import MongoClient
import hashlib

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

def addUser(username,password):
    """
    Adds a user to the database.
    Args:
        username (str): The user's username.
        password (str): The user's password.
    """
    connection = MongoClient()
    db = connection['data']
    db.users.insert({'name':username, 'password':encrypt(password)})

def userExists(username):
    """
    Checks whether a user exists in the database.
    Args:
        username (str): The username to be checked.
    Returns:
        boolean: Whether the user exists.
    """
    connection = MongoClient()
    db = connection['data']
    res = db.users.find({'name':username})
    for doc in res:
        return True
    return False

def authenticate(username, password):
    """
    Checks whether a username and password combination exists in the database.
    Args:
        username (str): The username to be checked.
        password (str): The password to be checked.
    Returns:
        boolean: Whether the username and password combination exists.
    """
    connection = MongoClient()
    db = connection['data']
    res = db.users.find({'name':username})
    for doc in res:
        if encrypt(password) == doc['password']:
            return True
    return False
