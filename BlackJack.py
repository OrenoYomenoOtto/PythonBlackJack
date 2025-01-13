#coding:utf-8

import configparser
from enum import Enum, auto
from typing import Final, Tuple, List

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

class Result_condition(Enum):
    WIN: Final[int] = auto()
    LOSE: Final[int] = auto()
    DRAW: Final[int] = auto()


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
        super().__init__()
        self.__chip = INITIAL_CHIP
        self.__result_condition = None

    @property
    def get_chip(self) -> int:
        return self.__chip
    
    @property
    def get_result_condition(self) -> None:
        pass

    def bet(self):
        pass


class Dealer(Rule):
    def __init__(self):
        pass


def judgement(dealer: Dealer, player: Player):
    DEALERS_POINT: Final[int] = dealer.get_total
    PLAYERS_POINT: Final[int] = player.get_total
    DEALERS_BURST_CONDITION: Final[bool] = dealer.get_isBurst
    PLAYERS_BURST_CONDITION: Final[bool] = player.get_isBurst
    judge_condition = None

    if PLAYERS_BURST_CONDITION is True or DEALERS_POINT > PLAYERS_POINT:
        judge_condition = Result_condition().LOSE
    elif DEALERS_BURST_CONDITION is True or DEALERS_POINT< PLAYERS_POINT: 
        judge_condition = Result_condition().WIN
    elif DEALERS_POINT == PLAYERS_POINT:
        judge_condition = Result_condition().DRAW
    return judge_condition


# def main():
#     #各クラスのインスタンス化
#     Deck = Cards.Deck()
#     Deck.shuffle_deck()
#     Dealer = Dealer()
#     Players: List = [Player() for i in range(PLAYER_NUM)]

#     #初手のカードをplayerとdealer配る
#     for i in range(2):
#         Dealer.hit(Deck)
#         for Player in Players:
#             Player.hit(Deck)
    
#     for Player in Players:
#         while True:
#             #playerがstandもしくはburstしていたらターンを終わる
#             if Player.get_isStand is True or Player.get_isBurst is True:
#                 break
#             # playerがBlackJackした場合はスタンドする
#             elif Player.get_isBlackJack is True:
#                 Player.stand()
#                 break
#             #TODO次の行動を決める
#             #TODO hitした場合
#             Player.hit(Deck)
#             Player.hands_total_point()
#             Player.BlackJack()
#             Player.burst()
#             #TODO standした場合
#             Player.stand()

#     #ディーラーの行動
#     while True:
#         pass


# if __name__ == "__main__":
#     main()

#テスト
deck = Cards.Deck()
deck.shuffle_deck()
player = Player()
print(player.get_hand)
print(deck.get_deck_rest)
player.hit(deck)
print(player.get_hand)
print(deck.get_deck_rest)