from sqlalchemy import Column, Integer

class Room(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Room(id={})>".format(self.id)
