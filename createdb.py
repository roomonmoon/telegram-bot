import sqlite3

db = sqlite3.connect('data.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY, 
    title TEXT,
    price BIGINT
)""")

db.commit()

tag_title = input("Кличка:")
tag_price = int(input("Стоимость клички:"))


sql.execute(f"INSERT INTO tags VALUES (?,?,?)", (None, tag_title, tag_price))
db.commit()

# sql.execute(f"DELETE FROM tags WHERE id=2;")
# db.commit()


def main():
    pass

if __name__ == "__main__":
    main()