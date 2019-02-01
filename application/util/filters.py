from application import app, db
from application.auth.models import User

@app.template_filter()
def getUserNameFromId(id):
    user = User.query.filter_by(id=id).first()
    return user.name