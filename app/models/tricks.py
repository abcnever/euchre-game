from app import db
from .columns.suit import Suit

class Trick(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)

    dealer_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id', ondelete='CASCADE'), nullable=False)
    trump_suit = db.Column(Suit)
