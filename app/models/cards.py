from sqlalchemy import Column, String, Integer 

from euchre-game.app.models.columns import Suit

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    suit = Column(Suit, nullable=False)
