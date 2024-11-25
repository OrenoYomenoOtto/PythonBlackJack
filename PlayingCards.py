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
        self.rank: Final[int] = rank
        self.suit: Final[Suit] = suit
    
class Deck:
    RANKS: Tuple = (FaceCard.ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, FaceCard.JACK, FaceCard.QUEEN, FaceCard.KING)
    SUITS: Tuple = (Suit.SPADE, Suit.CLUB, Suit.HEART, Suit.DIAMOND)
    def __init__(self) -> None:
        self.__deck = [Card(rank, suit) for rank in Deck.RANKS for suit in Deck.SUITS] 
        self.__has_stack = True

    @property
    def get_deck(self) -> list:
        return self.__deck
    
    @property
    def get_has_stack(self) -> bool:
        return self.__has_stack

    def shuffle_deck(self) -> None:
        random.shuffle(self.__deck)

    def draw_card(self) -> Card:
        card = self.__deck.pop()
        return card
    
    def check_stack(self) -> None:
        if self.count_card_quantity() is 0:
            self.__has_stack = False

    def count_card_quantity(self) -> int:
        return len(self.__deck)