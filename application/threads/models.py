from application import db
from application.models import Base

class Thread(Base):

    __tablename__ = "thread"

    title = db.Column(db.String(255), nullable=False)

    messages = db.relationship("Message", backref='thread', cascade="save-update, merge, delete", lazy=True)

    def __init__(self, title):
        self.title = title