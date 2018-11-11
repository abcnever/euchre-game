from sqlalchemy import Column, Integer

from .. import db

class Room(db.Model):
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Room(id={})>".format(self.id)
