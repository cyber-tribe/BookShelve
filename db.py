import sqlite3

def get_book():
    """
    dbからデータを取得し、辞書型として返す関数
    """
    dbpath = "books.db"
    connection = sqlite3.connect(dbpath)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books ORDER BY id")
    res = cursor.fetchall()

    keys = ["id","name","url"]
    res = [dict(zip(keys,value)) for value in res]
    return res