import sqlite3


def create_user_table(firstname: str, lastname: str, email: str, password: str, age: int):
   with sqlite3.connect("db.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
            CREATE TABLE user (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               firstname VARCHAR,
               lastname VARCHAR,
               email VARCHAR,
               password VARCHAR,
               age INTEGER,
               datetime DATETIME
            );
           """,
       )
       session.commit()
