import sqlite3

CONN = sqlite3.connect("db/classroom.db")
CURSOR = CONN.cursor()