from abc import ABCMeta, abstractmethod

import random
import time

class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, generator):
        pass

class NumberGenerator(metaclass=ABCMeta):

    def __init__(self):
        self._observers = []

    def addObserver(self, observer):
        self._observers.append(observer)

    def deleteObserver(self, observer):
        try :
            self._observer.remove(observer)
        except ValueError as e:
            print(e)

    def notifyObservers(self):
        oit = iter(self._observers)
        try:
            while True:
                item = next(oit)
                item.update(self)
        except StopIteration as e:
            pass

    @abstractmethod
    def getNumber(self) -> int:
        pass

    @abstractmethod
    def execute(self):
        pass

class RandomNumberGenerator(NumberGenerator):

    def __init__(self):
        super().__init__()
        self._number = 0

    def getNumber(self) -> int:
        return self._number

    def execute(self):
        for i in range(20):
            self._number = random.randrange(50)
            self.notifyObservers()

class DigitObserver(Observer):

    def update(self, generator):
        message = "DigitObserver:" + str(generator.getNumber())
        print(message)
        time.sleep(0.1)

class GraphObserver(Observer):
    def update(self, generator):
        message = "GraphObserver:" + str(generator.getNumber())
        print(message)
        count = generator.getNumber()
        
        src = ""
        for i in range(count):
            src += "*"
        print(src)

        time.sleep(0.1)