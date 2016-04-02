import sqlite3
class User(object):
	"""User Yo!!!!!"""
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
		self._getkarma =  """SELECT karma FROM users WHERE users = ?"""
		self._getpassword = """SELECT password FROM users WHERE users = ?"""
		self._adduser = """INSERT INTO users(users, email, password, karma) VALUES (?,?,?,?)"""
		self_updateKarma = """UPDATE users SET karma = ? WHERE users=?"""
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
		x = self.c.execute(self._updateKarma,(karma,username))
		self.c.commit()
	def return_karma(self, username, karma):
		self.c.execute(self._getkarma(username,))
		return self.c.fetchone()

class PaymentSession(object):
	'''This database payments is managing the present things and not the previous transactions of the user. '''
	def __init__(self):
		self.bpaymentDATABASE = './borrowerpayments.db'
		self.conn = sqlite3.connect(self.bpaymentDATABASE)
		self.c = self.conn.cursor()
		self._getdetails = """SELECT * FROM payments WHERE username = ?"""
		self._adddetails = """INSERT INTO payments(accountno, Amount, userinterest, payinterest, noofDays, remainingdays,
		remainingamount, username) VALUES (?,?,?,?,?,?,?,?)"""
		self._renderfeed = """SELECT * FROM payments WHERE payinterest in null"""
	
	def returndetailsforpayment(self,user):
		self.c.execute(self._getdetails, (user.username,))
		returnList = self.c.fetchall()
		#the return list is a list of tuples, this should be taken care of
		returnList = list(returnList[0])
		return returnList

	def addbpayment(self,accountno, amount, userinterest, days, username):
		self.c.execute(self._adddetails,(accountno, amount, userinterest, None, days, None, None, username))
		self.commit()
	def renderfeed(self):
		self.c.execute(self._renderfeed)
		x = c.fetchall()
		return x
class PreviousSessions(object):
	'''The database here manages and keeps a record of the previous databases being made'''
	def __init__(self):
		self.DATABASE = './prevdat'
