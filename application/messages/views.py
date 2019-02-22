from flask import redirect, render_template, request, url_for
from flask_login import current_user

from datetime import datetime

from application import app, db, login_manager, login_required
from application.messages.models import Message
from application.threads.models import Thread
from application.messages.forms import MessageForm

@app.route("/threads/<thread_id>", methods=["GET"])
def get_messages_from_thread_id(thread_id):
    thread = Thread.query.filter_by(id=thread_id).first()
    title = thread.title

    return render_template("messages/list.html",
      messages = Message.query.filter_by(thread_id=thread_id).order_by(Message.date_created),
      thread_id = thread_id,
      title = title,
      form = MessageForm())

@app.route("/threads/<thread_id>", methods=["POST"])
@login_required()
def messages_create(thread_id):
    form = MessageForm(request.form)

    if not form.validate():
      thread = Thread.query.filter_by(id=thread_id).first()
      title = thread.title

      return render_template("messages/list.html",
        messages = Message.query.filter_by(thread_id=thread_id).order_by(Message.date_created),
        thread_id = thread_id,
        title = title,
        form = form)

    m = Message(form.content.data)
    m.thread_id = thread_id
    m.account_id = current_user.id
    
    db.session().add(m)
    db.session().commit()

    t = Thread.query.filter_by(id=thread_id).first()
    t.date_modified = datetime.utcnow()
    db.session().commit()

    return redirect(url_for("get_messages_from_thread_id", thread_id=thread_id))

@app.route("/threads/<thread_id>/<message_id>", methods=["GET", "POST"])
@login_required()
def edit_message(thread_id, message_id):
    message = Message.query.get(message_id)

    if message.account_id != current_user.id and current_user.role != "ADMIN":
      return login_manager.unauthorized()

    if request.method == "GET":
        form = MessageForm()
        form.content.data = message.content
        return render_template("messages/edit.html", form = form, thread_id = thread_id, message_id = message_id)

    form = MessageForm(request.form)

    if not form.validate():
      return render_template("messages/edit.html", form = form, thread_id = thread_id, message_id = message_id)
    
    message.content = form.content.data
    db.session().commit()

    return redirect(url_for("get_messages_from_thread_id", thread_id=thread_id))
    
@app.route("/threads/<thread_id>/delete/<message_id>", methods=["POST"])
@login_required()
def delete_message(thread_id, message_id):
    message = Message.query.get(message_id)

    if message.account_id != current_user.id and current_user.role != "ADMIN":
      return login_manager.unauthorized()

    db.session().delete(message)
    db.session().commit()

    return redirect(url_for("get_messages_from_thread_id", thread_id=thread_id))
    