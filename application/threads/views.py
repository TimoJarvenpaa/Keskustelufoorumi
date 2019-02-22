from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.threads.models import Thread
from application.threads.forms import ThreadForm, EditThreadForm
from application.messages.models import Message
from application.categories.models import Category
from application.categories.forms import SelectCategoryForm


@app.route("/threads", methods=["GET", "POST"])
def threads_index():

    categories = [(c.id, c.name) for c in Category.query.all()]

    if request.method == "GET":
      form = SelectCategoryForm()
      form.category.choices = categories
      return render_template("threads/list.html", threads=Thread.query.order_by(Thread.date_modified.desc()).all(), form=form)
    
    form = SelectCategoryForm(request.form)
    form.category.choices = categories
    category_id = form.category.data

    thread_ids = Thread.get_list_of_threads_by_category_id(category_id)
    return render_template("threads/list.html", threads=Thread.query.filter(Thread.id.in_(thread_ids)).order_by(Thread.date_modified.desc()).all(),
    form = form)

@app.route("/threads/new", methods=["GET", "POST"])
@login_required()
def threads_create():

    categories = [(c.id, c.name) for c in Category.query.all()]

    if request.method == "GET":
        form = ThreadForm()
        form.categories.choices = categories
        return render_template("threads/new.html", form=form)

    form = ThreadForm(request.form)
    form.categories.choices = categories

    if not form.validate():
        return render_template("threads/new.html", form=form)

    t = Thread(form.title.data)
    t.account_id = current_user.id

    categories = form.categories.data
    for c_id in categories:
        c = Category.query.get(c_id)
        t.categories.append(c)

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


@app.route("/threads/edit/<thread_id>", methods=["GET", "POST"])
@login_required()
def edit_thread(thread_id):

    thread = Thread.query.get(thread_id)

    if thread.account_id != current_user.id and current_user.role != "ADMIN":
        return login_manager.unauthorized()

    categories = [(c.id, c.name) for c in Category.query.all()]

    if request.method == "GET":
        form = EditThreadForm()
        form.title.data = thread.title
        form.categories.choices = categories
        return render_template("threads/edit.html", form=form, thread_id=thread_id)

    form = EditThreadForm(request.form)
    form.categories.choices = categories

    if not form.validate():
        return render_template("threads/edit.html", form=form, thread_id=thread_id)

    thread.title = form.title.data
    thread.categories.clear()

    categories = form.categories.data
    for c_id in categories:
        c = Category.query.get(c_id)
        thread.categories.append(c)

    db.session().commit()

    return redirect(url_for("threads_index"))
