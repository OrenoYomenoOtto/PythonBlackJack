#coding:utf-8

import random
import enum
import configparser
from abc import ABCMeta, abstractmethod


class Card:
    def __init__(self):
        pass


class Deck:
    def __init__(self):
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
