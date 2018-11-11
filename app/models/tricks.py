from sqlalchemy import Column, ForeignKey, Integer

from . import Base
from .columns.suit import Suit


class Trick(Base):
    __tablename__ = 'tricks'

    id = Column(Integer, nullable=False, primary_key=True)
    dealer_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    trump_suit = Column(Suit)
