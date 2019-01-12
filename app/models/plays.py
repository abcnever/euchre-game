from . import db

class Play(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)

    round_id = db.Column(db.Integer, db.ForeignKey('trick.id', ondelete='CASCADE'), nullable=False)
    card_hand_join_id = db.Column(db.Integer, db.ForeignKey('card_hand_join.id', ondelete='CASCADE'), nullable=False)
