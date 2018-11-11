from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .. import db

class CardHandJoin(db.Model):
    id = Column(Integer, nullable=False, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id', ondelete='CASCADE'), nullable=False)
