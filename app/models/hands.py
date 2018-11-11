from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from . import Base

class Hand(Base):
    __tablename__ = 'hands'

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    trick_id = Column(Integer, ForeignKey('tricks.id', ondelete='CASCADE'), nullable=False)
