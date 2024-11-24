# coding:utf-8

from typing import Final
from enum import Enum, IntEnum, auto

class Suit(Enum):
    SPADE: Final[int] = auto()
    CLUB: Final[int] = auto()
    HEART: Final[int] = auto()
    DIAMOND: Final[int] = auto()

class FaceCard(IntEnum):
    ACE = 1
    JACK: Final[int] = 11
    QUEEN: Final[int] = 12
    KING: Final[int] = 13

class Joker:
    JOKER = None

class Card:
    def __init__(self, rank: int, suit: Suit) -> None:
        self.__rank = rank
        self.__suit = suit

    @property
    def get_rank(self) -> int:
        return self.__rank
    
    @property
    def get_suit(self) -> Suit:
        return self.__suit