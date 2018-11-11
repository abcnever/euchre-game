from . import db

class Team(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    room_id = db.Column(db.Integer, db.ForeignKey("room.id", ondelete="CASCADE"), nullable=False)
    wins = db.Column(db.Integer, nullable=False)
    losses = db.Column(db.Integer, nullable=False)
