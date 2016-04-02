from flask import Flask, render_template, request 
from .views.borrow import borrow
from .views.circle import circle
from .views.home import home
from views.lend import lend
from .views.user import user
from forms import RegisterForm
from models import User, db_sessiorcle.route('/')
from models import Users, Usersession
app = Flask(__name__)


app.register_blueprint(borrow, url_prefix='/borrow')
app.register_blueprint(lend, url_prefix='/lend')
app.register_blueprint(circle, url_prefix='/circle')
app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(user, url_prefix='/user')

userdb = Usersession()

@app.route('/register', methods=['POST','GET'])
def register():
	from createuserdb import *
	form = RegisterForm(request.form)
	if(request.method == 'POST' and form.validate()):
		user = User(form.username.data, form.email.data, form.password.data)
		userdb.insert_user(user)
		flash("Thanks for registering")
		return render_template('user/login.html')
	return render_template('user/register.html')

@app.route('/login')
def login():
	render_template('Hi')

if __name__ == '__main__':
	app.run()
