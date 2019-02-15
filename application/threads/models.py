from application import db
from application.models import Base

from sqlalchemy.sql import text

class Thread(Base):

    __tablename__ = "thread"

    title = db.Column(db.String(40), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    messages = db.relationship("Message", backref='thread', cascade="save-update, merge, delete", lazy=True)

    def __init__(self, title):
        self.title = title