from abc import ABCMeta, abstractmethod

class Factory(metaclass=ABCMeta):

    @staticmethod
    def getFactory(classname:str):
        factory = None
        try :
            factory = Factory.get_class(classname)
        except Exception as e:
            print(e)
        return factory

    @abstractmethod
    def createLink(caption:str, url:str):
        pass

    @abstractmethod
    def createTrya(caption:str):
        pass

    @abstractmethod
    def createPage(title:str, author:str):
        pass

    def get_class( kls ):
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m

class Item(metaclass=ABCMeta):
    def __init__(self, caption:str):
        self._caption = caption

    @abstractmethod
    def makeHTML(self):
        pass

class Link(Item, metaclass=ABCMeta):
    def __init__(self, caption:str, url:str):
        super().__init__(caption)
        self._url = url

class Tray(Item, metaclass=ABCMeta):
    def __init__(self, caption:str):
        super().__init__(caption)
        self._tray = []

    def add(self, item):
        self._tray.append(item)

class Page(metaclass=ABCMeta):

    def __init__(self, title:str, author:str):
        self._title = title
        self._author = author
        self._content = []

    def add(self, item):
        self._content.append(item)

    def output(self):
        filename = self._title + ".html"
        try:
            fout = open(filename, "w")
            fout.write(self.makeHTML())
            fout.close
        except IOError as e:
            print(e)

    @abstractmethod
    def makeHTML(self):
        pass