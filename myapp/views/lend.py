from flask import Blueprint, render_template

lend = Blueprint('lend', __name__)

@lend.route('/')
def lindex():
	return "lendpage"
