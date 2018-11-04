
import random
import gc
import time


class Memento:

    def __init__(self, money):
        self._money = money
        self._fruits = []

    def getMoney(self):
        return self._money

    def addFruit(self, fruit):
        self._fruits.append(fruit)

    def getFruits(self):
        return self._fruits

class Gamer:

    fruitsname = ["リンゴ", "ぶどう", "バナナ", "みかん"]

    def __init__(self, money):
        self._money = money
        self._fruitsList = []

    def getMoney(self):
        return self._money

    def bet(self):
        dice = random.randrange(6) + 1
        if dice == 1:
            self._money += 100
            print("所持金が増えました。")
        elif dice == 2:
            self._money /= 2
            print("所持金が半分になりました。")
        elif dice == 6:
            f = self.getFruit()
            print("フルーツ(" + f + ")をもらいました。")
            self._fruitsList.append(f)
        else:
            print("何も起こりませんでした。")

    def createMemento(self):
        m = Memento(self._money)
        is_sweet = lambda item : "おいしい" in item  
        sweetlist = list(filter(is_sweet, self._fruitsList))
        for item in sweetlist:
            m.addFruit(item)
        return m

    def restoreMemento(self, memento):
        self._money = memento.getMoney()
        self._fruitsList = memento.getFruits()

    def getFruit(self):
        dst = ""
        fruits_type = len(self.fruitsname)
        choice = random.randrange(fruits_type)
        if random.choice([True, False]):
            dst = "おいしい"
        return dst + self.fruitsname[choice]

    def __str__(self):
        dst = "[money = "
        dst += str(self._money)
        dst += ", fruits = " 
        dst += str(self._fruitsList)
        dst += "]"
        return dst
