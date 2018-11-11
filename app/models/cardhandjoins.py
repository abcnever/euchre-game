from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from . import Base

class CardHandJoin(Base):
    __tablename__ = "cardhandjoins"

    id = Column(Integer, primary_key=True)

    card_id = Column(Integer, ForeignKey('cards.id', ondelete='CASCADE'), nullable=False)
    hand_id = Column(Integer, ForeignKey('hands.id', ondelete='CASCADE'), nullable=False)
