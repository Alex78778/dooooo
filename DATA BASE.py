import sqlite3 as sq

connection = sq.connect('your_database_name.db')
cursor = connection.cursor()