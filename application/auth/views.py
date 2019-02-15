from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

import bcrypt

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
      return render_template("auth/loginform.html", form = form)

    user = User.query.filter_by(username=form.username.data).first()

    if not user:
      form.username.errors.append("No such username")
      return render_template("auth/loginform.html", form = form)
    
    if not user.password_is_correct(form.password.data):
      form.password.errors.append("Wrong password")
      return render_template("auth/loginform.html", form = form)

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/signup", methods = ["GET", "POST"])
def auth_signup():
    if request.method == "GET":

        if current_user.is_authenticated:
          return redirect(url_for("index"))

        return render_template("auth/signupform.html", form = SignupForm())

    form = SignupForm(request.form)
    
    if not form.validate():
      return render_template("auth/signupform.html", form = form)

    existing_user = User.query.filter_by(username=form.username.data).first()

    if existing_user:
      form.username.errors.append("Username already taken")
      return render_template("auth/signupform.html", form = form)
    
    hashed_pw = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt(12)).decode('utf-8')

    u = User(form.name.data, form.username.data, hashed_pw, form.role.data)
    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))
