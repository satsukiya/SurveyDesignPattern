
from framework.classes import *
import copy

class MessageBox(Product):

    def __init__(self, decochar):
        self._decochar = decochar

    def use(self, s:str):
        message = ""
        for i in range(len(s)):
            message += self._decochar
        message += "\n"
        message += self._decochar + " " + s + " " + self._decochar
        message += "\n"
        for i in range(len(s)):
            message += self._decochar
        print(message)

    def createClone(self):
        return copy.deepcopy(self)

class UnderlinePen:

    def __init__(self, ulchar):
        self._ulchar = ulchar

    def use(self, s:str):
        message = ""
        message += "\"" + s +"\"\n"
        message += " "
        for i in range(len(s)):
            message += self._ulchar
        print(message)

    def createClone(self):
        return copy.deepcopy(self)