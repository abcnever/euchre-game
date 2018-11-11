from . import db

class Play(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)

    round_id = db.Column(db.Integer, db.ForeignKey('tricks.id', ondelete='CASCADE'), nullable=False)
    cardhandjoin_id = db.Column(db.Integer, db.ForeignKey('cardhandjoins.id', ondelete='CASCADE'), nullable=False)
