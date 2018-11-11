from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from euchre-game.app.models.columns import Suit

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    suit = Column(Suit, nullable=False)
