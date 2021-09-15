#  Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
#  Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.


def create_user_table(name: str, price: int, quantity: int, comment: str):
   with sqlite3.connect("db.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
            CREATE TABLE user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                price INTEGER,
                quantity INTEGER,
                comment VARCHAR,
            );
            """,
        )
        session.commit()
