#coding:utf-8

import random
import enum
import configparser
from typing import Final, Tuple, List
from abc import ABCMeta, abstractmethod


INITIAL_CHIP: Final[int] = 100
MIN_RATE: Final[int] = 10
MAX_RATE: Final[int] = 100


class InitialCard(enum.IntEnum):
    A = 1
    J = 11
    Q = 12
    K = 13


class Suit(enum.Enum):
    club = enum.auto()
    diamond = enum.auto()
    heart = enum.auto()
    spade = enum.auto()


class Card:
    def __init__(self, number: int, suit: int):
        self.number = number
        self.suit = suit


class Deck:
    CARD_NUMBER: Tuple = (InitialCard.A, 2, 3, 4, 5, 6, 7, 8, 9, 10, InitialCard.J, InitialCard.Q, InitialCard.K)
    CLUB_CARD: Tuple = (Card(number, Suit.club) for number in CARD_NUMBER)
    DIAMOND_CARD: Tuple = (Card(number, Suit.diamond) for number in CARD_NUMBER)
    HEART_CARD: Tuple = (Card(number, Suit.heart) for number in CARD_NUMBER)
    SPADE_CARD: Tuple = (Card(number, Suit.spade) for number in CARD_NUMBER)
    def __init__(self):
        self.deck = list(Card.club) +list(Card.diamond) +list(Card.heart) +list(Card.spade)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def pull_card(self) -> int:
        pulled_card = self.deck.pop(0)
        return pulled_card


class Rule():
    def __init__(self):
        self.__hand: List = []
        self.__total = 0
        self.__hasAce = False
        self.__isStand = False
        self.__isBurst = False

    @property
    def get_hand(self) -> list:
        return self.__hand
    
    @property
    def get_total(self) -> int:
        return self.__total
    
    @property
    def get_isStand(self) -> bool:
        return self.__isStand
    
    @property
    def get_isBurst(self) -> bool:
        return self.__isBurst

    def hit(self):
        pass
    
    def stand(self):
        self.__isStand = True

    def Calculate_total(self):
        total = sum(self.__hand)
        have_ace_num = self.__hand.count(InitialCard.A)
        if self.__hasAce == True:
            while True:
                if total > 21 and have_ace_num != 0:
                    total -= 10
                    have_ace_num -= 1
                else:
                    break
        self.__total = total

    def burst(self):
        pass

    def BlackJack(self):
        pass


class Player(Rule):
    def __init__(self):
        self.__chip = INITIAL_CHIP

    @property
    def get_chip(self) -> int:
        return self.__chip
    
    def bet(self, card):
        pass


class Dealer(Rule):
    def __init__(self):
        pass

    def deal(self):
        pass
