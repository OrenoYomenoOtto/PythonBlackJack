#coding:utf-8

import enum
import configparser
from typing import Final, Tuple, List
from abc import ABCMeta, abstractmethod

import PlayingCards as Cards


INITIAL_CHIP: Final[int] = 100
DEALER_STAND_NUMBER: Final[int] = 17
BLACK_JACK_NUMBER: Final[int] = 21
MIN_RATE: Final[int] = 10
MAX_RATE: Final[int] = 100
PLAYER_NUM: Final[int] = 2


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

    def hit(self):
        pass

    def stand(self) -> None:
        self.__isStand = True

    def burst(self) -> None:
        if BLACK_JACK_NUMBER < self.__total:
            self.__isBurst = True

    def BlackJack(self) -> None:
        if BLACK_JACK_NUMBER == self.__total:
            self.__isBlackJack = True


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
    #各クラスのインスタンス化
    Deck = Cards.Deck()
    Dealer = Dealer()
    Players = [Player() for i in range(PLAYER_NUM)]

    #カードを配る
    for i in range(2):
        Dealer.hit()
        for Player in Players:
            Player.hit()
    #プレイヤーの行動
    while True:
        for Player in Players:
            #TODO次の行動を決める
            pass
        #player全員がstandもしくはburstしてるか確認する
        counter = 0
        for Player in Players:
            if Player.get_isStand is True or Player.get_isBurst is True:
                counter += 1
        if counter == PLAYER_NUM:
            break
    #ディーラーの行動
    while True:
        pass


if __name__ == "__main__":
    main()