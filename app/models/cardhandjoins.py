from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .. import db

class CardHandJoin(db.Model):
    id = Column(Integer, nullable=False, primary_key=True)

    card_id = Column(Integer, ForeignKey('cards.id', ondelete='CASCADE'), nullable=False)
    hand_id = Column(Integer, ForeignKey('hands.id', ondelete='CASCADE'), nullable=False)
