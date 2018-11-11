from sqlalchemy import Column, ForeignKey, Integer

from .. import db
from .columns.suit import Suit


class Trick(db.Model):
    id = Column(Integer, nullable=False, primary_key=True)

    dealer_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id', ondelete='CASCADE'), nullable=False)
    trump_suit = Column(Suit)
