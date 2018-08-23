from abc import ABCMeta, abstractmethod

class Trouble:

    def __init__(self, number:int):
        self.__number = number

    def getNumber(self) -> int:
        return self.__number

    def __str__(self):
        return "[Trouble %d]" % self.__number        

class Support(metaclass=ABCMeta):

    def __init__(self, name):
        self.__name = name
        self.__next = None

    def setNext(self, snext):
        self.__next = snext
        return self.__next

    def support(self, trouble:Trouble):
        if self.resolve(trouble):
            self.done(trouble)
        elif self.__next is not None:
            self.__next.support(trouble)
        else :
            self.fail(trouble)

    def __str__(self):
        return "[%s]" % self.__name

    @abstractmethod
    def resolve(self, trouble:Trouble) -> bool:
        pass

    def done(self, trouble:Trouble):
        message = str(trouble) + "is resolved by" + str(self.__str__()) + "."
        print(message)

    def fail(self, trouble:Trouble):
        message = "%s cannot be resolved." % str(trouble)
        print(message)

class NoSupport(Support):

    def __init__(self, name:str):
        super(NoSupport, self).__init__(name)

    def resolve(self, trouble:Trouble):
        return False

class LimitSupport(Support):
    def __init__(self, name:str, limit:int):
        super(LimitSupport, self).__init__(name)
        self.__limit = limit

    def resolve(self, trouble:Trouble):
        if trouble.getNumber() < self.__limit:
            return True
        else :
            return False

class SpecialSupport(Support):
    def __init__(self, name:str, number:int):
        super(SpecialSupport, self).__init__(name)
        self.__number = number

    def resolve(self, trouble:Trouble):
        if trouble.getNumber() == self.__number:
            return True
        else :
            return False

class OddSupport(Support):
    def __init__(self, name:str):
        super(OddSupport, self).__init__(name)

    def resolve(self, trouble:Trouble):
        if trouble.getNumber() % 2 == 1:
            return True
        else :
            return False
