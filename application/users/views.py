from flask import redirect, render_template, request, url_for, abort
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.auth.models import User

@app.route("/users", methods=["GET"])
@login_required(role="ADMIN")
def users_index():

    if current_user.role != "ADMIN":
        abort(401)

    users = User.query.all()
    return render_template("users/list.html", users=users)


@app.route("/users/delete/<user_id>", methods=["POST"])
@login_required(role="ADMIN")
def delete_user(user_id):

    if current_user.role != "ADMIN":
        abort(401)

    user = User.query.filter_by(id=user_id).first()

    if current_user.id == user.id:
      db.session().delete(user)
      db.session().commit()

      return redirect(url_for("index"))

    db.session().delete(user)
    db.session().commit()

    return redirect(url_for("users_index"))
