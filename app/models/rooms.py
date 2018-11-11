from . import db

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return "<Room(id={})>".format(self.id)
