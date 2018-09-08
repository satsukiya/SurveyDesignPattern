from abc import ABCMeta, abstractmethod

class Display(metaclass=ABCMeta):
    @abstractmethod
    def getColumns(self) -> int:
        pass

    @abstractmethod
    def getRows(self) -> int:
        pass

    @abstractmethod
    def getRowText(self, row:int) -> str:
        pass

    def show(self):
        for i in range(self.getRows()):
            print(self.getRowText(i))

class Border(Display,metaclass=ABCMeta):
    def __init__(self, display:Display):
        self._display = display

class StringDisplay(Display):

    def __init__(self, string:str):
        self.__string = string

    def getColumns(self) -> int:
        return len(self.__string)

    def getRows(self) -> int:
        return 1

    def getRowText(self, row:int) -> str:
        if row == 0:
            return self.__string
        else :
            return None

class SideBorder(Border):

    def __init__(self, display, ch:str):
        super().__init__(display)
        self.__borderChar = ch

    def getColumns(self) -> int:
        return 1 + self._display.getColumns() + 1

    def getRows(self) -> int:
        return self._display.getRows()

    def getRowText(self, row:int) -> str:
        dst = ""
        dst += self.__borderChar
        dst += self._display.getRowText(row)
        dst += self.__borderChar
        return dst

class FullBorder(Border):
    def __init__(self, display:Display):
        super().__init__(display)

    def getColumns(self):
        return 1 + self._display.getColumns() + 1

    def getRows(self):
        return 1 + self._display.getRows() + 1

    def getRowText(self, row:int) -> str:
        dst = ""
        if row == 0:
            dst = "+" + self.makeLine("-", self._display.getColumns()) + "+"
        elif row ==  self._display.getRows() + 1:
            dst = "+" + self.makeLine("-", self._display.getColumns()) + "+"
        else :
            dst = "|" + self._display.getRowText(row - 1) + "|"
        
        return dst

    def makeLine(self, ch:str, count:int) -> str:
        dst = ""
        for i in range(count):
            dst += ch
        return dst
