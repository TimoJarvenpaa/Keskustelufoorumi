from application import db
from application.models import Base

class Message(Base):

    content = db.Column(db.String(500), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, content):
        self.content = content