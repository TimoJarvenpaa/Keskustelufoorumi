from application import app, db
from application.auth.models import User
from datetime import datetime

@app.template_filter()
def get_username_from_account_id(id):
    user = User.query.filter_by(id=id).first()
    return user.name