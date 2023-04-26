import sqlite3 as sq
from info import info_fac
from info import info_dep
from info import info_spec
from info import info_items
from info import sub_form
from info import plan_info
from info import info_abitur
from info import card_student

with sq.connect('decanat.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS fac (
        id_fac INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR
        )""")

with sq.connect('decanat.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS dep (
        id_dep INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        fac_id INTEGER,
        FOREIGN KEY (fac_id) REFERENCES fac (id_fac)
        )""")

with sq.connect('decanat.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS spec (
        id_spec INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        dep_id INTEGER,
        FOREIGN KEY (dep_id) REFERENCES dep (id_dep)
        )""")

with sq.connect('decanat.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS items (
        id_item INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR
        )""")

with sq.connect('decanat.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS form (
        id_form INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR
        )""")

with sq.connect('decanat.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS plan (
        id_plan INTEGER PRIMARY KEY AUTOINCREMENT,
        id_spec INTEGER,
        id_item INTEGER,
        id_form INTEGER,
        amount_lec INTEGER,
        amount_prac INTEGER,
        amount_lab INTEGER,
        course_work BOOL,
        FOREIGN KEY (id_spec) REFERENCES spec (id_spec),
        FOREIGN KEY (id_item) REFERENCES items (id_item),
        FOREIGN KEY (id_form) REFERENCES form (id_form)
        )""")

with sq.connect('decanat.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS abitur (
                id_abit INTEGER PRIMARY KEY AUTOINCREMENT,
                last_name TEXT,
                name TEXT,
                fatherland TEXT,
                sex TEXT,
                date_b DATE,
                address TEXT,
                phone TEXT,
                email TEXT,
                date_i DATE,
                id_spec INTEGER,
                FOREIGN KEY (id_spec) REFERENCES spec (id_spec)
                )''')


with sq.connect('decanat.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS card_student(
                id_card INTEGER PRIMARY KEY AUTOINCREMENT,
                FIO_s TEXT,
                group_st TEXT,
                id_spec INTEGER,
                id_item INTEGER,
                id_form INTEGER,
                rating INTEGER,
                FOREIGN KEY (id_spec) REFERENCES spec (id_spec),
                FOREIGN KEY (id_item) REFERENCES items (id_item),
                FOREIGN KEY (id_form) REFERENCES form (id_form)
                )''')

with sq.connect('decanat.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO fac (id_fac, name) VALUES (?, ?)", info_fac)
    cur.executemany("INSERT INTO dep VALUES (?, ?, ?)", info_dep)
    cur.executemany("INSERT INTO spec VALUES (?, ?,?)", info_spec)
    cur.executemany("INSERT INTO items VALUES (?, ?)", info_items)
    cur.executemany("INSERT INTO form VALUES (?, ?)", sub_form)
    cur.executemany("INSERT INTO plan VALUES (?, ?, ?, ?, ?, ?, ?, ?)", plan_info)
    cur.executemany("INSERT INTO abitur VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", info_abitur)
    cur.executemany("INSERT INTO card_student VALUES (?, ?, ?, ?, ?, ?, ?)", card_student)
    con.commit()

# with sq.connect('decanat.db') as con:
#     cur = con.cursor()
#     cur.execute('SELECT FIO_s FROM card_student WHERE')