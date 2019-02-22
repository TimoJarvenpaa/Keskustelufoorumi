from application import db
from application.models import Base
from application.categories.models import Category

from sqlalchemy.sql import text

thread_category = db.Table('thread_category', db.Model.metadata,
    db.Column('thread_id', db.Integer, db.ForeignKey('thread.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)

class Thread(Base):

    __tablename__ = "thread"

    title = db.Column(db.String(100), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    messages = db.relationship("Message", backref='thread', cascade="save-update, merge, delete", lazy=True)
    categories = db.relationship("Category", secondary=thread_category, lazy='subquery',
        backref=db.backref('threads', lazy=True))

    def __init__(self, title):
        self.title = title

    @staticmethod
    def get_list_of_threads_by_category_id(c_id):
      stmt = text("SELECT Thread.id as id FROM Thread INNER JOIN thread_category tc ON"
                  " Thread.id = tc.thread_id WHERE tc.category_id = :id").params(id=c_id)
      res = db.engine.execute(stmt)

      response = []
      for row in res:
        response.append(row[0])

      return response
