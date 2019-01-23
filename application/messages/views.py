from application import app, db
from flask import redirect, render_template, request, url_for
from application.messages.models import Message
from application.threads.models import Thread

@app.route("/threads/<thread_id>/", methods=["GET"])
def messages_index(thread_id):
    thread = Thread.query.filter_by(id=thread_id).first()
    title = thread.title

    return render_template("messages/list.html",
      messages = Message.query.filter_by(thread_id=thread_id),
      thread_id = thread_id,
      title = title)

@app.route("/messages/new/")
def messages_form():
    return render_template("messages/new.html")

@app.route("/threads/<thread_id>/", methods=["POST"])
def messages_create(thread_id):
    m = Message(request.form.get("content"))
    m.thread_id = thread_id
    
    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("messages_index", thread_id=thread_id))