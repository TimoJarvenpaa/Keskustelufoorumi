from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.threads.models import Thread
from application.threads.forms import ThreadForm
from application.messages.models import Message

@app.route("/threads", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads = Thread.query.order_by(Thread.date_modified.desc()).all())

@app.route("/threads/new", methods=["GET", "POST"])
@login_required()
def threads_create():
    if request.method == "GET":
      return render_template("threads/new.html", form = ThreadForm())

    form = ThreadForm(request.form)

    if not form.validate():
      return render_template("threads/new.html", form = form)

    t = Thread(form.title.data)
    t.account_id = current_user.id
    
    db.session().add(t)
    db.session().flush()

    m = Message(form.content.data)
    m.thread_id = t.id
    m.account_id = current_user.id
    
    db.session().add(m)
    db.session().commit()

    return redirect(url_for("threads_index"))

@app.route("/threads/delete/<thread_id>", methods=["POST"])
@login_required()
def delete_thread(thread_id):
    thread = Thread.query.get(thread_id)

    if thread.account_id != current_user.id and current_user.role != "ADMIN":
      return login_manager.unauthorized()

    db.session().delete(thread)
    db.session().commit()

    return redirect(url_for("threads_index"))