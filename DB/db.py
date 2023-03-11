import sqlite3 as sq
import data_users
with sq.connect('saper.db') as con:
  cur = con.cursor()
  #cur.execute("DROP TABLE IF EXISTS users")
  cur.execute("""CREATE TABLE IF NOT EXISTS users (
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
sex INTEGER NOT NULL DEFAULT 1,
old INTEGER,
score INTEGER
)""")
  #cur.execute("INSERT INTO users VALUES (1, 'Алексей', 1, 22, 1000)")
  #cur.execute("INSERT INTO users VALUES (2, 'Аня', 1, 22, 1000)")
  #cur.execute("INSERT INTO users VALUES (3, 'Алексей Выходец', 1, 65, 1000)")
  cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", data_users.data_users)


