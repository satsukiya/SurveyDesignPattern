from abc import ABCMeta, abstractmethod

class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for i in range(5):
            self.print()
        self.close()

class CharDisplay(AbstractDisplay):

    def __init__(self, ch):
        self.__ch = ch

    def open(self):
        print("<<", end="")

    def print(self):
        print(self.__ch, end="")

    def close(self):
        print(">>")

class StringDisplay(AbstractDisplay):

    def __init__(self, string):
        self.__string = string

    def open(self):
        self.printLine()

    def print(self):
        print("|" +  self.__string + "|")

    def close(self):
        self.printLine()

    def printLine(self):
        print("+", end="")
        for i in range(len(self.__string.encode('utf-8'))):
            print("-", end="")
        print("+")