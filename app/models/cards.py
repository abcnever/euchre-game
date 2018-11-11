from . import db
from .columns.suit import Suit

class Card(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String, nullable=False)
    suit = db.Column(db.String, nullable=False)
