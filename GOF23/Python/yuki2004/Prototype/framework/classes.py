
from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):

    @abstractmethod
    def use(self, s:str):
        pass

    @abstractmethod
    def createClone(self):
        pass

class Manager:

    _showcase = {}
    def register(self, name:str, proto:str):
        self._showcase[name] = proto

    def create(self, protoname:str):
        p = self._showcase[protoname]
        return p.createClone()