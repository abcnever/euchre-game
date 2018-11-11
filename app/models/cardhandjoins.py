from . import db

class CardHandJoin(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)

    card_id = db.Column(db.Integer, db.ForeignKey('cards.id', ondelete='CASCADE'), nullable=False)
    hand_id = db.Column(db.Integer, db.ForeignKey('hands.id', ondelete='CASCADE'), nullable=False)
