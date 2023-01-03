import sys
import Card
import sqlite3 as db

connection = db.connect("card.db") 
cursor = connection.cursor()

def init_db():
  cursor.execute("""
  CREATE TABLE cards(
    front TEXT,
    back TEXT,
    created DATETIME,
    last_reviewed DATETIME
  )""")
  connection.commit()
  

if __name__ == "__main__":
  init_db()

connection.close()