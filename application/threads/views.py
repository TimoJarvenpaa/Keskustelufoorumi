from application import app, db
from flask import redirect, render_template, request, url_for
from application.threads.models import Thread

@app.route("/threads", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads = Thread.query.all())

@app.route("/threads/new/")
def threads_form():
    return render_template("threads/new.html")

@app.route("/threads/", methods=["POST"])
def threads_create():
    t = Thread(request.form.get("title"))
    
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("threads_index"))