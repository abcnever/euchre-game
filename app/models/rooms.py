from app import db

class Room(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)

    def __repr__(self):
        return "<Room(id={})>".format(self.id)
