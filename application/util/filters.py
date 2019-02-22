from application import app, db
from application.auth.models import User

@app.template_filter()
def get_username_from_account_id(id):
    user = User.query.filter_by(id=id).first()
    return user.name

@app.template_filter()
def count_total_messages_by_user_id(u_id):
    res = User.count_user_messages_by_user_id(u_id)
    return res[0]['messages']