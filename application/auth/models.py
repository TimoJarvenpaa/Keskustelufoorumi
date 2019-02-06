from application import db
from application.models import Base

from sqlalchemy.sql import text


class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    messages = db.relationship("Message", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def count_messages_by_user():
      stmt = text("SELECT Account.name AS name, COUNT(Message.id) AS count FROM Account"
                  " LEFT JOIN Message ON Message.account_id = Account.id"
                  " GROUP BY name"
                  " ORDER BY count DESC")
      res = db.engine.execute(stmt)

      response = []
      for row in res:
        response.append({"name":row[0], "messages":row[1]})

      return response