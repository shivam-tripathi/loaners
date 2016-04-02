import sqlite3
class User(object):
	"""User Yo"""
	def __init__(self, username, password, email, karma=0):
		self.username = username
		self.password = password
		self.email = email
		self.karma = karma


class Usersession(object):
	def __init__(self):
		self.userDATABASE = './users.db'
		self.conn = sqlite3.connect(self.userDATABASE)
		self.c = self.conn.cursor()
		self._getuser = """SELECT * FROM users WHERE users = ?"""
		_getkarma =  """SELECT karma FROM users WHERE users = ?"""
		_getpassword = """SELECT password FROM users WHERE users = ?"""
		_adduser = """INSERT INTO users(users, email, password, karma) VALUES (?,?,?,?)"""
		_updateKarma = """UPDATE users SET karma = ? WHERE users=?"""
	def check_user(self, user):
		x = self.c.execute(self._getuser,(user.username,))
		a = (x.fetchall())
		if a == [(None,)]:
			return False
		else:
			return True
	def insert_user(self, user):
		x = self.c.execute(self._adduser,(user.username, user.email, user.password))
		self.c.commit()
	def update_user(self, username, karma):
		x = self.c.execute(self._updateKarma,(karma,username)
		self.c.commit()
	def return_karma(self, username, karma):
		x = self.c.execute(self._getkarma(username))
		self.c.commit()
		
		
