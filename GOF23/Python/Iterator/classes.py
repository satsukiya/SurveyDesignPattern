from abc import ABCMeta, abstractmethod

class Book:
    def __init__(self, name:str):
        self.__name = name
    
    def __str__(self):
        return self.__name

class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def next(self):
        pass

class Aggregate():
    @abstractmethod
    def iterator(self):
        pass

class BookShelf(Aggregate):
    def __init__(self):
        self.__books = []
        self.__last = 0

    def getBookAt(self,index):
        return self.__books[index]

    def appendBook(self, book:Book):
        self.__books.append(book)

    def getLength(self):
        return len(self.__books)

    def iterator(self):
        return BookShelfIterator(self)

class BookShelfIterator(Iterator):
    def __init__(self, bookShelf:BookShelf):
        self.__index = 0
        self.__bookShelf = bookShelf

    def hasNext(self):
        dst = True
        if self.__index < self.__bookShelf.getLength():
            dst = True
        else :
            dst = False
        return dst

    def next(self):
        book = self.__bookShelf.getBookAt(self.__index)
        self.__index += 1
        return book

