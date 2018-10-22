from abc import ABCMeta, abstractmethod

class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, file):
        pass

class Element(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, v:Visitor):
        pass

class Entry(Element, metaclass=ABCMeta):
    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def getSize(self) -> int:
        pass

    def add(self, entry):
        pass

    def iterator(self):
        pass

    def __str__(self):
        dst = self.getName()
        dst += "("
        dst += str(self.getSize())
        dst += ")"
        return dst

class Directory(Entry):

    def __init__(self, name):
        self._name = name
        self._dir = []

    def getName(self):
        return self._name

    def getSize(self):
        size = 0
        it = iter(self._dir)

        try :
            while(it is not None):
                item = next(it)
                size += item.getSize()
        except StopIteration:
            pass

        return size

    def add(self ,entry):
        self._dir.append(entry)
        return self

    def __iter__(self):
        return iter(self._dir)

    def accept(self, v:Visitor):
        v.visit(self)

class File(Entry):

    def __init__(self, name, size):
        self._name = name
        self._size = size

    def getName(self):
        return self._name

    def getSize(self):
        return self._size

    def accept(self, v:Visitor):
        v.visit(self)

class ListVisitor(Visitor):
    currentdir = ""
    def visit(self, src):
        message = self.currentdir
        message += "/"
        message += str(src)
        print(message)
        if isinstance(src, Directory):
            savedir = self.currentdir
            self.currentdir = self.currentdir + "/" + src.getName()

            ditr = iter(src)
            try:
                while True:
                    entry = next(ditr)
                    entry.accept(self)
            except StopIteration:
                pass
            self.currentdir = savedir
