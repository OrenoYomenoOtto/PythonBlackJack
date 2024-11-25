# coding:utf-8

from typing import Final, Tuple, Dict
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
    FACE_CARD_NAMES: Dict = {face.value: face.name.capitalize() for face in FaceCard}
    def __init__(self, rank: int, suit: Suit) -> None:
        self.rank: Final[int] = rank
        self.suit: Final[Suit] = suit
        self.rank_name: Final[str] =  Card.FACE_CARD_NAMES.get(self.rank, str(self.rank))
    
    def __str__(self) -> str:
        return f"{self.rank_name} of {self.suit.name.capitalize()}"
    
class Deck:
    RANKS: Tuple = (FaceCard.ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, FaceCard.JACK, FaceCard.QUEEN, FaceCard.KING)
    SUITS: Tuple = (Suit.SPADE, Suit.CLUB, Suit.HEART, Suit.DIAMOND)
    def __init__(self) -> None:
        self.__deck = [Card(rank, suit) for rank in Deck.RANKS for suit in Deck.SUITS]
        self.__deck_rest = len(self.__deck) 
        self.__has_stack = True

    @property
    def get_deck(self) -> list:
        return self.__deck
    
    @property
    def get_deck_rest(self) -> int:
        return self.__deck_rest
    
    @property
    def get_has_stack(self) -> bool:
        return self.__has_stack

    def shuffle_deck(self) -> None:
        random.shuffle(self.__deck)

    def draw_card(self) -> Card:
        if self.__has_stack == False:
            raise IndexError("No more card in the deck.")
        card = self.__deck.pop()
        self.count_card_quantity()
        self.check_stack()
        return card
    
    def count_card_quantity(self) -> int:
        self.__deck_rest = len(self.__deck)
    
    def check_stack(self) -> None:
        if self.__deck_rest == 0:
            self.__has_stack = False
    
# #テスト
# tramp = Deck()
# tramp.shuffle_deck()
# while tramp.get_has_stack == True:
#     card = tramp.draw_card()
#     print(f"[残り {tramp.get_deck_rest}]: {card}")