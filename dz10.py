import sqlite3


connection = sqlite3.connect("dz10.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE temp (name TEXT);")
connection.commit()

connection.close()
