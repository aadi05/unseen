import sqlite3

conn = sqlite3.connect('test.db')
conn.execute('''create table if not exists register
             (fname text,
              username text,
              password text)''')

conn.execute('''create table if not exists register2
             (name text,
              email text,
              seats text,
              subtotal integer)''')





