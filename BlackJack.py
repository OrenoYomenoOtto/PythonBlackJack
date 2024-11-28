#coding:utf-8

import configparser
from enum import Enum, auto
from typing import Final, Tuple, List
from abc import ABCMeta, abstractmethod

import PlayingCards as Cards


INITIAL_CHIP: Final[int] = 100
DEALER_STAND_NUMBER: Final[int] = 17
BLACK_JACK_NUMBER: Final[int] = 21
MIN_RATE: Final[int] = 10
MAX_RATE: Final[int] = 100
PLAYER_NUM: Final[int] = 2

class Action_selection(Enum):
    HIT: Final[int] = auto()
    STAND: Final[int] = auto()


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
        self.__result = False

    @property
    def get_chip(self) -> int:
        return self.__chip
    
    def won_game(self) -> None:
        self.__result = True

    def bet(self, card):
        pass


class Dealer(Rule):
    def __init__(self):
        pass

#TODO 勝利判定
def judgement(dealer: Dealer, Players: list):
    DEALERS_POINT: Final[int] = dealer.get_total
    #TODO 引き分けの時の処理を書いていない
    if dealer.get_isBurst:
        for Player in Players:
            if Player.get_stand is True:
                Player.won_game()
    else:
        for Player in Players:
            if DEALERS_POINT  < Player.get_total:
                Player.won_game()

def main():
    #各クラスのインスタンス化
    Deck = Cards.Deck()
    Deck.shuffle_deck()
    Dealer = Dealer()
    Players: List = [Player() for i in range(PLAYER_NUM)]

    #初手のカードをplayerとdealer配る
    for i in range(2):
        Dealer.hit(Deck)
        for Player in Players:
            Player.hit(Deck)
    
    for Player in Players:
        while True:
            #playerがstandもしくはburstしていたらターンを終わる
            if Player.get_isStand is True or Player.get_isBurst is True:
                break
            # playerがBlackJackした場合はスタンドする
            elif Player.get_isBlackJack is True:
                Player.stand()
                break
            #TODO次の行動を決める
            #TODO hitした場合
            Player.hit(Deck)
            Player.hands_total_point()
            Player.BlackJack()
            Player.burst()
            #TODO standした場合
            Player.stand()

    #ディーラーの行動
    while True:
        pass


if __name__ == "__main__":
    main()