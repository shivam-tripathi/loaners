import sqlite3

conn = sqlite3.connect('borrowerpayments.db')
c = conn.cursor()

def createdb():
	c.execute("CREATE TABLE IF NOT EXISTS payments(accountno TEXT, Amount REAL, remainingAmount REAL, interest REAL , noOfDays INT, remainingdays INT, username TEXT, complete INT)")
def newuser(username, email, encryptpassword):
	c.execute("INSERT INTO users(users, password, email, details) VALUES (?,?,?)",(username, email, encryptpassword, "New User", 0))
	conn.commit()
createdb()
