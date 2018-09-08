from abc import ABCMeta, abstractmethod

class DisplayImpl(metaclass=ABCMeta):
    @abstractmethod
    def rawOpen(self):
        pass

    @abstractmethod
    def rawPrint(self):
        pass

    @abstractmethod
    def rawClose(self):
        pass

class Display:

    def __init__(self, impl:DisplayImpl):
        self.__impl = impl

    def open(self):
        self.__impl.rawOpen()

    def print(self):
        self.__impl.rawPrint()

    def close(self):
        self.__impl.rawClose()

    def display(self):
        self.open()
        self.print()
        self.close()

class StringDisplayImpl(DisplayImpl):

    def __init__(self, string:str):
        self.__string = string
        self.__width = len(self.__string)

    def rawOpen(self):
        self.printLine()

    def rawPrint(self):
        dst = "|" + self.__string + "|"
        print(dst)

    def rawClose(self):
        self.printLine()

    def printLine(self):
        print("+", end="")
        for i in range(self.__width):
            print("-", end="")
        print("+")

class CountDisplay(Display):
    def __init__(self, impl:DisplayImpl):
        super(CountDisplay, self).__init__(impl)

    def multiDisplay(self, times:int):
        self.open()
        for i in range(times):
            self.print()
        self.close()
