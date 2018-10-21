from abc import ABCMeta, abstractmethod

class Entry(metaclass=ABCMeta):

    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def getSize(self) -> int:
        pass

    def add(self, entry):
        pass

    @abstractmethod
    def printList(self, prefix:str):
        pass

    def printAllList(self):
        self.printList("")

    def __str__(self):
        dst = self.getName()
        dst += "("
        dst += str(self.getSize())
        dst += ")"
        return dst

class Directory(Entry):

    def __init__(self, name):
        self.__name = name
        self.__directory = []

    def getName(self) -> str:
        return self.__name

    def getSize(self) -> int:
        size = 0
        it = iter(self.__directory)
        try :
            while(it):
                item = next(it)
                size += item.getSize()
        except StopIteration:
            pass
        return size

    def add(self, entry:Entry):
        self.__directory.append(entry)
        return self

    def printList(self, prefix:str):
        print(prefix + "/" + str(self))
        it = iter(self.__directory)
        try :
            while(it):
                item = next(it)
                item.printList(prefix + "/" + self.__name)
        except StopIteration:
            pass  

class File(Entry):

    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def getName(self) -> str:
        return self.__name

    def getSize(self) -> int:
        return self.__size

    def printList(self, prefix:str):
        print(prefix + "/" + str(self))