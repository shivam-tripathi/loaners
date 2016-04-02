from flask import Blueprint, render_template

circle = Blueprint('circle', __name__)

@circle.route('/')
def index():
	return "mycircle"
