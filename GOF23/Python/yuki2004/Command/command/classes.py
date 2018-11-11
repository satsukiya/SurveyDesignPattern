from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class MacroCommand(Command):

    def __init__(self):
        self._commands = []
        self._index = 1

    def execute(self):
        for item in self._commands:
            item.execute()

    def append(self, cmd):
        if cmd != self:
            self._commands.append((cmd,self._index))
            self._index += 1

    def undo(self):
        dst = None
        if 0 < len(self._commands):
            item = self._commands.pop()
            dst = item[1]
        return dst

    def clear(self):
        self._commands.clear()

