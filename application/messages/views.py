from application import app, db
from flask import redirect, render_template, request, url_for
from application.messages.models import Message

#EI TOIMI VIELÄ

@app.route("/threads/<thread_id>/", methods=["GET"])
def messages_index():
    return render_template("messages/list.html", messages = Message.query.filter_by(thread_id=thread_id))

@app.route("/messages/new/")
def messages_form():
    return render_template("messages/new.html")

@app.route("/threads/<thread_id>/", methods=["POST"])
def messages_create():
    m = Message(request.form.get("content"))
    m.thread_id = thread_id
    
    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("messages_index"))