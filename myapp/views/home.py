from flask import Blueprint, render_template
from ..models import User, PaymentSession
home = Blueprint('home', __name__)


@home.route('/<username>')
def hindex(username):
	paymentdb = PaymentSession()
	feedlists = paymentdb.render_feed()
	for i in range(len(feedlists)):
		feedlists[i] = list(feedlists[i])
		feedlists[i][0] = str(feedlists[i][0])
		feedlists[i][6] = str(feedlists[i][6])
	return render_template('home/feed.html', username = username,feedlists = feedlists)




