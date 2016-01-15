import sqlite3

conn = sqlite3.connect("data.db")

c = conn.cursor()

q = "CREATE TABLE users(name text, password text, email text)"
c.execute(q)

conn.commit()
