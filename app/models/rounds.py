from sqlalchemy import Column, ForeignKey, Integer

from .. import db


class Round(db.Model):
    id = Column(Integer, nullable=False, primary_key=True)

    trick_id = Column(Integer, ForeignKey('tricks.id', ondelete='CASCADE'), nullable=False)
