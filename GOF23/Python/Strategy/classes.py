
from abc import ABCMeta, abstractmethod
from collections import namedtuple
import random
import datetime

_hand_pattern_ = {0:"グー", 1:"チョキ", 2:"パー"}


def fight(p1:int, p2:int):
    dst = 0
    if p1 == p2:
        dst = 0
    elif (p1 + 1) % 3 == p2:
        dst = 1
    else :
        dst = -1
    return dst


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def nextHand(self):
        pass

    @abstractmethod
    def study(self, win:bool):
        pass

class WinnerStrategy(Strategy):

    def __init__(self):
        self.__won = True
        self.__prevHand = None

    def nextHand(self):
        random.seed(datetime.datetime.now().microsecond)
        if self.__won:
            self.__prevHand = random.randrange(3)
        return self.__prevHand

    def study(self, win:bool):
        self.__won = win

    def __str__(self):
        return str(self.__won)

class ProbStrategy(Strategy):
    def __init__(self):
        self.__history = [[1,1,1],[1,1,1],[1,1,1]]
        self.__prevHandValue = 0
        self.__currentHandValue = 0

    def nextHand(self):
        betrange = self.getSum(self.__currentHandValue)
        random.seed(datetime.datetime.now().microsecond)
        bet = random.randrange(betrange) if 0 < betrange else 0
        handvalue = 0
        condition_gu = lambda v : v < self.__history[self.__currentHandValue][0]
        condition_choki = lambda v : v < self.__history[self.__currentHandValue][0] + self.__history[self.__currentHandValue][1]

        if condition_gu(bet):
            handvalue = 0
        elif condition_choki(bet):
            handvalue = 1
        else :
            handvalue = 2
        self.__prevHandValue = self.__currentHandValue
        self.__currentHandValue = handvalue
        print(self.__history)
        return handvalue

    def getSum(self, hv):
        return sum(self.__history[hv])

    def study(self, win:bool):
        if win:
            self.__history[self.__prevHandValue][self.__currentHandValue] += 1
        else :
            self.__history[self.__prevHandValue][(self.__currentHandValue + 1) % 3] += 1
            self.__history[self.__prevHandValue][(self.__currentHandValue + 2) % 3] += 1


class Player:
    def __init__(self, name, strategy:Strategy):
        self.name = name
        self.__strategy = strategy
        self.__gamecount = 0
        self.__wincount = 0
        self.__losecount = 0

    def win(self):
        self.__strategy.study(True)
        self.__gamecount += 1
        self.__wincount += 1

    def lose(self):
        self.__strategy.study(False)
        self.__gamecount += 1
        self.__losecount += 1

    def even(self):
        self.__gamecount += 1

    def nextHand(self):
        return self.__strategy.nextHand()

    def __str__(self):
        dst = "name:" + self.name
        dst += " game:" + str(self.__gamecount)
        dst += " win:" + str(self.__wincount)
        dst += " lose:" + str(self.__losecount)
        return dst

