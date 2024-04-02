import sqlite3


def create_database():
    con = sqlite3.connect('robot_base.db')
    c = con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS robot_base
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, start_time TEXT, duration REAL, start_number INTEGER)''')
    con.commit()
    con.close()


def add_database(start_time, duration, start_number):
    con = sqlite3.connect('robot_base.db')
    c = con.cursor()
    c.execute("INSERT INTO robot_base (start_time, duration, start_number) VALUES (?, ?, ?)",
              (start_time, duration, start_number))
    con.commit()
    con.close()


def start_database():
    con = sqlite3.connect('robot_base.db')
    c = con.cursor()
    c.execute("SELECT * FROM robot_base")
    runs = c.fetchall()
    con.close()
    return runs