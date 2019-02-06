from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.threads.models import Thread
from application.threads.forms import ThreadForm
from application.messages.models import Message

@app.route("/threads", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads = Thread.query.all())

@app.route("/threads/new/")
@login_required
def threads_form():
    return render_template("threads/new.html", form = ThreadForm())

@app.route("/threads/", methods=["POST"])
@login_required
def threads_create():
    form = ThreadForm(request.form)

    if not form.validate():
      return render_template("threads/new.html", form = form)

    t = Thread(form.title.data)
    
    db.session().add(t)
    db.session().commit()

    t = Thread.query.filter_by(title=t.title).first()

    m = Message(form.content.data)
    m.thread_id = t.id
    m.account_id = current_user.id
    
    db.session().add(m)
    db.session().commit()

    return redirect(url_for("threads_index"))