from app import db

class Round(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)

    trick_id = db.Column(db.Integer, db.ForeignKey('trick.id', ondelete='CASCADE'), nullable=False)
