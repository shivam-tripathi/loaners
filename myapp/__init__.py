from flask import Flask, render_template, request, redirect, flash 
from .views.borrow import borrow
from .views.home import home
from views.lend import lend
from .views.user import user
from forms import RegisterForm
from models import User, Usersession
app = Flask(__name__)
app.secret_key = "fkjdasfh jsa"
app.register_blueprint(borrow, url_prefix='/borrow')
app.register_blueprint(lend, url_prefix='/lend')
app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(user, url_prefix='/user')

userdb = Usersession()

@app.route('/register', methods=['POST','GET'])
def register():
	form = RegisterForm(request.form)
	if(request.method == 'POST' and form.validate()):
		user = User(form.username.data, form.email.data, form.password.data)
		userdb.insert_user(user)
		flash("Thanks for registering")
		return render_template('user/login.html')
	return render_template('user/register.html')

@app.route('/',methods=['GET','POST'])
def index():
	if (request.method == 'POST'):
		username = request.form['username']
		password = request.form['password']
		if username == 'admin' and password == 'admin':
			return redirect('/home/{}'.format(username))
		else:
			flash("Incorrect username or password")
	return render_template('index.html')

@app.route('/check')
def check():
	return render_template('base.html')

if __name__ == '__main__':
	app.run(debug=True)
