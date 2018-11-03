from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, nullable=False, primary_key=True)
    room_id = Column(Integer, ForeignKey('room.id', ondelete='CASCADE'), nullable=False)
    wins = Column(Integer, nullable=False)
    losses = Column(Integer, nullable=False)
