import sqlite3


connection = sqlite3.connect("p10test.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE weather (дата й час TEXT);")
connection.commit()

connection.close()
