from flask import redirect, render_template, request, url_for, abort
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.categories.models import Category
from application.categories.forms import AddCategoryForm, SelectCategoryForm


@app.route("/categories", methods=["GET"])
@login_required(role="ADMIN")
def categories_index():

    if current_user.role != "ADMIN":
        abort(401)

    categories = Category.count_threads_within_category()
    return render_template("categories/list.html", categories=categories)


@app.route("/categories/new", methods=["GET", "POST"])
@login_required(role="ADMIN")
def create_category():

    if current_user.role != "ADMIN":
        abort(401)

    if request.method == "GET":
        return render_template("categories/new.html", form=AddCategoryForm())

    form = AddCategoryForm(request.form)

    if not form.validate():
        return render_template("categories/new.html", form=form)

    category_exists = Category.query.filter_by(name=form.name.data).first()

    if category_exists:
        form.name.errors.append("Category already exists")
        return render_template("categories/new.html", form=form)

    c = Category(form.name.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("categories_index"))


@app.route("/categories/delete/<category_id>", methods=["POST"])
@login_required(role="ADMIN")
def delete_category(category_id):

    if current_user.role != "ADMIN":
        abort(401)
    category = Category.query.get(category_id)

    db.session().delete(category)
    db.session().commit()

    return redirect(url_for("categories_index"))


@app.route("/categories/edit/<category_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def edit_category(category_id):

    if current_user.role != "ADMIN":
        abort(401)

    category = Category.query.get(category_id)

    if request.method == "GET":
        form = AddCategoryForm()
        form.name.data = category.name
        return render_template("categories/edit.html", form=form, category_id=category_id)

    form = AddCategoryForm(request.form)

    if not form.validate():
        return render_template("categories/edit.html", form=form, category_id=category_id)

    category_exists = Category.query.filter_by(name=form.name.data).first()

    if category_exists:
        form.name.errors.append("Category already exists")
        return render_template("categories/edit.html", form=form, category_id=category_id)

    category.name = form.name.data
    db.session().commit()

    return redirect(url_for("categories_index"))
