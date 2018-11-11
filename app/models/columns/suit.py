from attr import attrs, attrib
import enum

from .enum import EnumColumn

class Suit(EnumColumn):
    class Enum(enum.Enum):

        @attrs(frozen=True)
        class _Suit():
            suit_name = attrib()
            ascii_icon = attrib()

        spades = _Suit(
            suit_name="Spades",
            ascii_icon="♠"
        )
        clubs = _Suit(
            suit_name="Clubs",
            ascii_icon="♣"
        )
        diamonds = _Suit(
            suit_name="Diamonds",
            ascii_icon="\033[91m♦\0330m"
        )
        hearts = _Suit(
            "Hearts",
            ascii_icon="\033[91m♥\0330m"
        )
