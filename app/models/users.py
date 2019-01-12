from . import db

class User(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)

    username = db.Column(db.String, nullable=False)
    wins = db.Column(db.Integer, nullable=False, default=0)
    losses = db.Column(db.Integer, nullable=False, default=0)
