#coding:utf-8

import random
import enum
import configparser
from typing import Final, Tuple, List
from abc import ABCMeta, abstractmethod


INITIAL_CHIP: Final[int] = 100
BLACK_JACK: Final[int] = 21
MIN_ACE: Final[int] = 1
MAX_ACE: Final[int] = 11
MIN_RATE: Final[int] = 10
MAX_RATE: Final[int] = 100

class InitialCard(enum.IntEnum):
    A = 11
    J = 10
    Q = 10
    K = 10


class Suit(enum.Enum):
    club = enum.auto()
    diamond = enum.auto()
    heart = enum.auto()
    spade = enum.auto()


class Card:
    def __init__(self, number: int, suit: int):
        self.__number = number
        self.__suit = suit

    @property
    def get_number(self):
        return self.__number
    
    @property
    def get_suit(self):
        return self.__suit


class Deck:
    CARD_NUMBER: Tuple = (InitialCard.A, 2, 3, 4, 5, 6, 7, 8, 9, 10, InitialCard.J, InitialCard.Q, InitialCard.K)
    CLUB_CARD: Tuple = (Card(number, Suit.club) for number in CARD_NUMBER)
    DIAMOND_CARD: Tuple = (Card(number, Suit.diamond) for number in CARD_NUMBER)
    HEART_CARD: Tuple = (Card(number, Suit.heart) for number in CARD_NUMBER)
    SPADE_CARD: Tuple = (Card(number, Suit.spade) for number in CARD_NUMBER)

    def __init__(self):
        self.deck = list(Deck.CLUB_CARD) +list(Deck.DIAMOND_CARD) +list(Deck.HEART_CARD) +list(Deck.SPADE_CARD)

    def shuffle_deck(self) -> None:
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
        self.__isBlackJack = False

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
    
    def stand(self) -> None:
        self.__isStand = True

    def burst(self) -> None:
        if BLACK_JACK < self.__total:
            self.__isBurst = True

    def BlackJack(self) -> None:
        if BLACK_JACK == self.__total:
            self.__isBlackJack = True

    def Calculate_total(self) -> None:
        total = 0
        Ace_cards = []
        for hand in self.__hand:
            if hand.get_number != InitialCard.A:
                total += hand.get_number
            elif hand.get_number == InitialCard.A:
                Ace_cards.append(hand)
        if len(Ace_cards) != 0:
            for hand in Ace_cards:
                if BLACK_JACK < (self.__total + MAX_ACE):
                    total += MIN_ACE
                else:
                    total += MAX_ACE
        self.__total = total



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

deck = Deck()
print(deck.deck)