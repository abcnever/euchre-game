from . import db

class Hand(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    trick_id = db.Column(db.Integer, db.ForeignKey('tricks.id', ondelete='CASCADE'), nullable=False)
