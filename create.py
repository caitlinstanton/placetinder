import sqlite3

conn = sqlite3.connect("data.db")

c = conn.cursor()

q = "CREATE TABLE users(name text, password text, email text)"
c.execute(q)

q = "CREATE TABLE tempevents(user test, description text, url text, location text, datetime text, price text)"
c.execute(q)

q = "CREATE TABLE savedevents(user text, description text, url text, location text, datetime text, price text)"
c.execute(q)

conn.commit()
