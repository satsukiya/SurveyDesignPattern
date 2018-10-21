from abc import ABCMeta, abstractmethod

class Builder(metaclass=ABCMeta):
    @abstractmethod
    def makeTitle(self, title:str):
        pass

    @abstractmethod
    def makeString(self, src:str):
        pass

    @abstractmethod
    def makeItems(self, items):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def getResult(self) -> str:
        pass

class Director:

    def __init__(self, bulider:Builder):
        self.__builder = bulider

    def construct(self):
        self.__builder.makeTitle("Greeting")
        self.__builder.makeString("朝から昼にかけて")
        self.__builder.makeItems(["おはようございます","こんにちは"])
        self.__builder.makeString("夜に")
        self.__builder.makeItems(["こんばんは。","おやすみなさい。","さようなら"])
        self.__builder.close()

class TextBuilder(Builder):

    def __init__(self):
        self.__buffer = ""

    def makeTitle(self, title:str):
        self.__buffer += "==============================\n"
        self.__buffer += "『" + title + "』\n"
        self.__buffer += "\n"

    def makeString(self, src:str):
        self.__buffer += "■" + src + "\n"
        self.__buffer += "\n"

    def makeItems(self, items):
        for item in items:
            self.__buffer += "　・" + item + "\n"
        self.__buffer += "\n"

    def close(self):
        self.__buffer += "==============================\n"

    def getResult(self) -> str:
        return self.__buffer

class HTMLBuilder(Builder):

    def __init__(self):
        self.__filename = ""
        self.__fout = ""

    def makeTitle(self, title:str):
        self.__filename = title + ".html"
        self.__fout = open(self.__filename, "w")
        self.__fout.write("<html><head><title>" + title + "</title></head><body>")
        self.__fout.write("<h1>" + title + "</h1>")

    def makeString(self, src:str):
        self.__fout.write("<p>" + src + "</p>")

    def makeItems(self, items):
        self.__fout.write("<ul>")
        for item in items:
            self.__fout.write("<li>" + item + "</li>")

        self.__fout.write("</ul>")

    def close(self):
        self.__fout.write("</body></html>")
        self.__fout.close()

    def getResult(self):
        return self.__filename