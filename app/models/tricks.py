from . import db
from .db.Columns.suit import Suit

class Trick(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)

    dealer_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id', ondelete='CASCADE'), nullable=False)
    trump_suit = db.Column(Suit)
