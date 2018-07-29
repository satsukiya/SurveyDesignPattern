from abc import ABCMeta, abstractmethod


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def createProduct(self, owner):
        pass

    @abstractmethod
    def registerProduct(self, product):
        pass

    def create(self, owner):
        p = self.createProduct(owner)
        self.registerProduct(p)
        return p

class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass

class IDCard(Product):
    def __init__(self, owner):
        print(owner + "のカードを作ります。")
        self.__owner = owner

    def use(self):
        print(self.__owner + "のカードを使います。")

    def getOwner(self):
        return self.__owner

class IDCardFactory(Factory):

    def __init__(self):
        self.__owners = []

    def createProduct(self, owner):
        return IDCard(owner)

    def registerProduct(self, product):
        self.__owners.append(product.getOwner())

    def getOwners(self):
        return self.__owners
