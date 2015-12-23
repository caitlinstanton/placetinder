from pymongo import MongoClient
import hashlib

def encrypt(word):
    hashp = hashlib.md5()
    hashp.update(word)
    return hashp.hexdigest()

def addUser(username,password):
    connection = MongoClient()
    db = connection['data']
    db.users.insert({'name':username, 'password':encrypt(password)})

def userExists(username):
    connection = MongoClient()
    db = connection['data']
    res = db.users.find({'name':username})
    for doc in res:
        return True
    return False

def authenticate(username, password):
    connection = MongoClient()
    db = connection['data']
    res = db.users.find({'name':username})
    for doc in res:
        if encrypt(password) == doc['password']:
            return True
    return False
