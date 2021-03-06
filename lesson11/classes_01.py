import sqlite3

from datetime import datetime

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


def create_user(
    firstname: str, lastname: str, email: str, password: str, age: int, created_at: datetime):
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (firstname, lastname, email, password, age, datetime)
            VALUES (?, ?, ?, ?, ?, ?);
            """,
            (firstname, lastname, email, password, age, created_at),
        )
        session.commit()


create_user("Alexander", "Chaika", "manti.by@gmail.com", "TestPass", 44, datetime.now())
