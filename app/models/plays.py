from sqlalchemy import Column, ForeignKey, Integer

from . import Base


class Play(Base):
    __tablename__ = 'plays'

    id = Column(Integer, nullable=False, primary_key=True)

    round_id = Column(Integer, ForeignKey('tricks.id', ondelete='CASCADE'), nullable=False)
    cardhandjoin_id = Column(Integer, ForeignKey('cardhandjoins.id', ondelete='CASCADE'), nullable=False)
