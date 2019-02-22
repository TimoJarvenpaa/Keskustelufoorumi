from application import db
from application.models import Base

from sqlalchemy.sql import text

import bcrypt


class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(16), nullable=False)

    messages = db.relationship("Message", backref='account', lazy=True)

    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.password = password
        self.role = role

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_role(self):
      return self.role

    def password_is_correct(self, password):
      return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    @staticmethod
    def count_messages_for_all_users():
      stmt = text("SELECT Account.name AS name, COUNT(Message.id) AS count FROM Account"
                  " LEFT JOIN Message ON Message.account_id = Account.id"
                  " GROUP BY name"
                  " ORDER BY count DESC")
      res = db.engine.execute(stmt)

      response = []
      for row in res:
        response.append({"name":row[0], "messages":row[1]})

      return response

    @staticmethod
    def count_user_messages_by_user_id(u_id):
      stmt = text("SELECT Account.name AS name, COUNT(Message.id) AS count FROM Account"
                  " INNER JOIN Message ON Message.account_id = :id"
                  " GROUP BY name").params(id=u_id)
      res = db.engine.execute(stmt)

      response = []
      for row in res:
        response.append({"name":row[0], "messages":row[1]})

      return response