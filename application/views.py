from flask import render_template
from application import app
from application.auth.models import User

@app.route("/")
def index():
	return render_template("index.html", count_messages=User.count_messages_for_all_users())
