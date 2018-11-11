from sqlalchemy import Column, ForeignKey, Integer, String

from .. import db

class User(db.Model):
    id = Column(Integer, nullable=False, primary_key=True)

    username = Column(String, nullable=False)
    wins = Column(Integer, nullable=False, default=0)
    losses = Column(Integer, nullable=False, default=0)
