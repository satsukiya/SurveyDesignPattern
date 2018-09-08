from abc import ABCMeta, abstractmethod

class Print(metaclass=ABCMeta):
    @abstractmethod
    def printWeak(self):
        pass

    @abstractmethod
    def printStrong(self):
        pass

class Banner:

    def __init__(self, string:str):
        self.__string = string

    def showWithParen(self):
        dst = "(" + self.__string + ")"
        print(dst)

    def showWithAster(self):
        dst = "*" + self.__string + "*"
        print(dst)

class PrintBanner(Banner, Print):

    def __init__(self, string:str):
        super().__init__(string)

    def printWeak(self):
        super().showWithParen()

    def printStrong(self):
        super().showWithAster()

