#coding:utf-8

import random
import enum
import configparser
from typing import Final, Tuple, List
from abc import ABCMeta, abstractmethod


class InitialCard(enum.IntEnum):
    A = 1
    J = 11
    Q = 12
    K = 13


class Card:
    club: Tuple = (InitialCard.A, 2, 3, 4, 5, 6, 7, 8, 9, 10, InitialCard.J, InitialCard.Q, InitialCard.K)
    diamond: Tuple = (InitialCard.A, 2, 3, 4, 5, 6, 7, 8, 9, 10, InitialCard.J, InitialCard.Q, InitialCard.K)
    heart: Tuple = (InitialCard.A, 2, 3, 4, 5, 6, 7, 8, 9, 10, InitialCard.J, InitialCard.Q, InitialCard.K)
    spade: Tuple = (InitialCard.A, 2, 3, 4, 5, 6, 7, 8, 9, 10, InitialCard.J, InitialCard.Q, InitialCard.K)


class Deck:
    def __init__(self):
        self.deck = list(Card.club) +list(Card.diamond) +list(Card.heart) +list(Card.spade)

    def shuffle_deck(self):
        pass

    def draw_card(self):
        pass

    

class Rule(metaclass = ABCMeta):
    @abstractmethod
    def hit(self):
        pass
    
    @abstractmethod
    def stand(self):
        pass

    @abstractmethod
    def burst(self):
        pass


class Player(Rule):
    def __init__(self):
        pass


class Dealer(Rule):
    def __init__(self):
        pass

    def deal(self):
        pass

