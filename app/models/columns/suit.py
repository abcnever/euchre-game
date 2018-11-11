from attr import attrs, attrib
import enum

from .enum import EnumColumn

from collections import namedtuple

class Suit(EnumColumn):
    class Enum(enum.Enum):

        @attrs(frozen=True)
        class _Suit():
            suit_name = attrib()

        spades = _Suit("Spades")
        clubs = _Suit("Clubs")
        diamonds = _Suit("Diamonds")
        hearts = _Suit("Hearts")
