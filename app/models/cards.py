from app import db
from .columns.suit import Suit
from .columns.card_name import CardName

class Card(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(CardName, nullable=False)
    suit = db.Column(Suit, nullable=False)
