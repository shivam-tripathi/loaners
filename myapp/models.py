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
		self.c.execute(self._getkarma,(username,))
		return self.c.fetchone()

	def inc_karma(self, username, inc):
		self.c.execute(self._getkarma,(username,))
		self.c.execute(self._inc_karma,(self.c.fetchone()+inc))



class PaymentSession(object):
	'''This database payments is managing the present things and not the previous transactions of the user. '''
	def __init__(self):
		self.bpaymentDATABASE = './borrowerpayments.db'
		self.conn = sqlite3.connect(self.bpaymentDATABASE)
		self.c = self.conn.cursor()
		#Use dictionary for outputs
		self.c.rowfactory = sqlite3.row
		self._getdetails = """SELECT * FROM payments WHERE username = ?"""
		self._adddetails = """INSERT INTO payments(accountno, Amount, interest, noofDays, remainingdays,
		remainingamount, username, complete) VALUES (?,?,?,?,?,?,?,?)"""
		self._renderfeed = """SELECT * FROM payments WHERE complete is null"""
		self._complete = """UPDATE payments SET complete =? WHERE username=?"""

	def return_details_for_payment(self,user):
		self.c.execute(self._getdetails, (user.username,))
		returnList = self.c.fetchall()
		#the return list is a list of dictionaries, this should be taken care of
		returnList = list(returnList[0])
		return returnList

	def add_bpayment(self, accountno, amount, interest, days, username):
		#remaining days and remaining amount has been set to none
		self.c.execute(self._adddetails,(accountno, amount, interest, days, None, None, username, None))
		self.commit()

	def render_feed(self):
		self.c.execute(self._renderfeed)
		x = c.fetchall()
		#return a list of dictionary of items
		return x

	def complete(self, username):
		self.c.execute(self._complete,(1,username))

	def time_over():
		#function to automatically complete the transactions when the time is over
		pass


class PreviousSessions(object):
	'''The database here manages and keeps a record of the previous databases being made'''
	def __init__(self):
		self.DATABASE = './prevdat'
	def get_loans():
		pass

class LendingSession(object):
	'''The database here manages details of lenders.'''
	def __init__(self):
		self.DATABASE = './lenders.db'
		self.conn = sqlite3.connect(self.bpaymentDATABASE)
		self.c = self.conn.cursor()
		#Use dictionary for outputs
		self.c.rowfactory = sqlite3.row
		self._getdetails = """SELECT * FROM lenders WHERE username = ?"""
		self._adddetails = """INSERT INTO lenders(accoutno, Amount, interest, username) VALUES(?,?,?,?)"""
		self._get_amount = """SELECT username FROM lenders WHERE amount > ?"""

	def render_lenders(self, amount):
		self.c.execute(self._get_amount,(amount,))
		return c.fetchall()

	def get_lender(self, username):
		self.c.execute(_getdetails,(username,))
