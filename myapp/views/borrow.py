from flask import Blueprint, render_template

borrow = Blueprint('borrow', __name__)

@borrow.route('/')
def index():
	return "hello"
