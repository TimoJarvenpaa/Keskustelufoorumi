from application import db
from application.models import Base

from sqlalchemy.sql import text

class Category(Base):

    __tablename__ = "category"

    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def count_threads_within_category():
      stmt = text("SELECT Category.id as id, Category.name AS name, COUNT(thread_category.thread_id) AS count FROM Category"
                  " LEFT JOIN thread_category ON Category.id = thread_category.category_id"
                  " GROUP BY id ORDER BY count DESC")
      res = db.engine.execute(stmt)

      response = []
      for row in res:
        response.append({"id":row[0], "name":row[1], "count":row[2]})

      return response
