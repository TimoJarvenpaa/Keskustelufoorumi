from application import db

class Thread(db.Model):

    __tablename__ = "thread"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    title = db.Column(db.String(255), nullable=False)

    messages = db.relationship("Message", backref='thread', cascade="save-update, merge, delete", lazy=True)

    def __init__(self, title):
        self.title = title