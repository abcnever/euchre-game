from sqlalchemy import Column, String, Integer

from .. import db
from .columns.suit import Suit

class Card(db.Model):
    id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    suit = Column(Suit, nullable=False)
