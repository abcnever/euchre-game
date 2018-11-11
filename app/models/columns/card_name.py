from attr import attrs, attrib
import enum

from .enum import EnumColumn

class CardName(EnumColumn):
    class Enum(enum.Enum):
        @attrs(frozen=True)
        class _CardName():
            card_name = attrib()

        nine = _CardName("9")
        ten = _CardName("10")
        jack = _CardName("Jack")
        queen = _CardName("Queen")
        king = _CardName("King")
        ace = _CardName("Ace")
