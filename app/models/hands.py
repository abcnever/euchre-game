from . import db

class Hand(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    trick_id = db.Column(db.Integer, db.ForeignKey('trick.id', ondelete='CASCADE'), nullable=False)
