import sqlite3

conn = sqlite3.connect('lenders.db')
c = conn.cursor()

def createdb():
	c.execute("CREATE TABLE IF NOT EXISTS lenders(accountno TEXT, Amount REAL, interest REAL , username TEXT)")
createdb()
