import sqlite3

# com = sqlite3.connect('profile.db')
# cur = com.cursor()
#
# cur.execute('''''')
#
# com.close()

# with sqlite3.connect('profile.db') as com:
#     cur = com.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     date BLOB
#     )''')
#     cur.execute("DROP TABLE users")


# with sqlite3.connect('users.db') as com:
#     cur = com.cursor()
    # cur.execute('''CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT "+79094556789",
    # age INTEGER CHECK (age > 0 AND age < 100),
    # email TEXT UNIQUE)
    # ''')

    # cur.execute("""
    # ALTER TABLE person
    # ADD COLUMN address TEXT
    # """)


# with sqlite3.connect('db_3.db') as com:
#     cur = com.cursor()
#     cur.execute("""
#     select *
#     from T1
#     limit 2, 6
#     """)
#
#     # for res in cur:
#     #     print(res)
#
#     # res = cur.fetchall()
#     # print(res)
#
#     res = cur.fetchone()
#     print(res)
#
#     res2 = cur.fetchmany(3)
#     print(res2)

# with sqlite3.connect('car.db') as com:
#     cur = com.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )""")
#
#     cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000")
#     cur.execute("INSERT INTO cars VALUES(2, 'AUDI', 20000")
#     cur.execute("INSERT INTO cars VALUES(3, 'VAZ', 19000")
#     cur.execute("INSERT INTO cars VALUES(4, 'BMW', 34000")



"""hgdfgffd"""
