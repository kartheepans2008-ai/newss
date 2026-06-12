import sqlite3


def create_db():

    conn = sqlite3.connect("news.db")

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS news(
        id INTEGER PRIMARY KEY,
        title TEXT,
        category TEXT,
        sentiment TEXT
    )
    """)

    conn.commit()
    conn.close()
