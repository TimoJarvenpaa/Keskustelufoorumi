from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.messages.models import Message
from application.threads.models import Thread
from application.messages.forms import MessageForm

@app.route("/threads/<thread_id>/", methods=["GET"])
def messages_index(thread_id):
    thread = Thread.query.filter_by(id=thread_id).first()
    title = thread.title

    return render_template("messages/list.html",
      messages = Message.query.filter_by(thread_id=thread_id),
      thread_id = thread_id,
      title = title,
      form = MessageForm())

@app.route("/messages/new/")
@login_required
def messages_form():
    return render_template("messages/new.html", form = MessageForm())

@app.route("/threads/<thread_id>/", methods=["POST"])
@login_required
def messages_create(thread_id):
    form = MessageForm(request.form)

    if not form.validate():
      thread = Thread.query.filter_by(id=thread_id).first()
      title = thread.title

      return render_template("messages/list.html",
        messages = Message.query.filter_by(thread_id=thread_id),
        thread_id = thread_id,
        title = title,
        form = form)

    m = Message(form.content.data)
    m.thread_id = thread_id
    m.account_id = current_user.id
    
    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("messages_index", thread_id=thread_id))