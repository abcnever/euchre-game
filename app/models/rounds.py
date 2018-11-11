from sqlalchemy import Column, ForeignKey, Integer

from . import Base


class Round(Base):
    __tablename__ = 'rounds'

    id = Column(Integer, nullable=False, primary_key=True)

    trick_id = Column(Integer, ForeignKey('tricks.id', ondelete='CASCADE'), nullable=False)
