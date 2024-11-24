# coding:utf-8

from typing import Final, Tuple
from enum import Enum, IntEnum, auto
import random

class Suit(Enum):
    SPADE: Final[int] = auto()
    CLUB: Final[int] = auto()
    HEART: Final[int] = auto()
    DIAMOND: Final[int] = auto()

class FaceCard(IntEnum):
    ACE: Final[int] = 1
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
    
class Deck:
    Ranks: Tuple = (FaceCard.ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, FaceCard.JACK, FaceCard.QUEEN, FaceCard.KING)
    Suits: Tuple = (Suit.SPADE, Suit.CLUB, Suit.HEART, Suit.DIAMOND)
    Deck: Tuple = ((Card(rank, suit) for rank in Deck.Ranks) for suit in Deck.Suits)
    def __init__(self, has_joker: bool) -> None:
        self.__deck = Deck.Deck 

    def shuffle_deck(self) -> None:
        self.__deck = random.shuffle(self.__deck)