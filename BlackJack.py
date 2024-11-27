#coding:utf-8

import random
import enum
import configparser
from typing import Final, Tuple, List
from abc import ABCMeta, abstractmethod

import PlayingCards as Cards


INITIAL_CHIP: Final[int] = 100
BLACK_JACK_NUMBER: Final[int] = 21
MIN_RATE: Final[int] = 10
MAX_RATE: Final[int] = 100


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
    def get_isStand(self) -> bool:
        return self.__isStand

    @property
    def get_isBurst(self) -> bool:
        return self.__isBurst
    
    @property
    def get_isBlackJack(self) -> bool:
        return self.__isBlackJack

    def hit(self, deck: Cards.Deck) -> None:
        card = deck.draw_card()
        self.__hand.append(card)

    def stand(self) -> None:
        self.__isStand = True

    def burst(self) -> None:
        if BLACK_JACK_NUMBER < self.__total:
            self.__isBurst = True

    def BlackJack(self) -> None:
        if BLACK_JACK_NUMBER == self.__total:
            self.__isBlackJack = True
            
    def hands_total_point(self) -> None:
        total_point = 0
        ace_lst = []
        for card in self.__hand:
            if card.rank == Cards.FaceCard.ACE:
                self.__hasAce = True
                ace_lst.append(card)
                pass
            elif card.rank == Cards.FaceCard.JACK or card.rank == Cards.FaceCard.QUEEN or card.rank == Cards.FaceCard.KING:
                total_point += 10
            else:
                total_point += card.rank
        if self.__hasAce is True:
            for card in ace_lst:
                if total_point < 11:
                    total_point += 10
                else:
                    total_point += 1
        self.__total = total_point


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


def main():
    Deck = Cards.Deck()


if __name__ == "__main__":
    main()