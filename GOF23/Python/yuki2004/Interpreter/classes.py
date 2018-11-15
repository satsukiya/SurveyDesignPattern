from abc import ABCMeta, abstractmethod

class ParseException(Exception):

    def __init__(self, msg=""):
        super().__init__()
        self._msg = msg

    @property
    def msg(self):
        return self._msg

class Node(metaclass=ABCMeta):
    @abstractmethod
    def parse(self, context):
        pass

class Context:

    def __init__(self, text):
        self._tokenizer = iter(text.split(" "))
        self._currentToken = None

    def currentToken(self) -> str:
        return self._currentToken

    def currentNumber(self) -> int:
        number = 0
        try :
            number = int(self._currentToken)
        except NameError:
            pass
        return number

    def nextToken(self):
        try :
            self._currentToken = next(self._tokenizer)
        except StopIteration:
            self._currentToken = None
        return self._currentToken

    def skipToken(self, token):
        if token == self._currentToken:
            pass
            #try:
            #    raise
            #except Exception :
            #    print("[WARNING]:" + token + " is expected, but " + self._currentToken + " is found.")
        self.nextToken()

class ProgramNode(Node):

    def __init__(self):
        self._commandListNode = None

    def parse(self, context):
        context.skipToken("program")
        self._commandListNode = CommandListNode()
        self._commandListNode.parse(context)

    def __str__(self):
        dst = "[program "
        dst += str(self._commandListNode)
        dst += "]"
        return dst

class RepeatCommandNode(Node):

    def __init__(self):
        self._number = 0
        self._commandListNode = None

    def parse(self, context):
        context.skipToken("repeat")
        self._number = context.currentNumber()
        context.nextToken()
        self._commandListNode = CommandListNode()
        self._commandListNode.parse(context) 

    def __str__(self):
        dst = "[repeat "
        dst += str(self._number)
        dst += " "
        dst += str(self._commandListNode)
        dst += "]"
        return  dst

class PrimitiveCommandNode(Node):
    
    def __init__(self):
        self._name = ""

    def parse(self, context):
        self._name = context.currentToken()
        context.skipToken(self._name)
        if not self._name == "go" and \
            not self._name == "right" and \
            not self._name == "left":
            pass
            #try :
            #    raise
            #except Exception:
            #    message = "[WARNING]:"
            #    message += self._name
            #    message += " is undefined"
            #    print(message)


    def __str__(self):
        return self._name


class CommandNode(Node):

    def __init__(self):
        self._node = None

    def parse(self, context):
        if context.currentToken() == "repeat":
            self._node = RepeatCommandNode()
            self._node.parse(context)
        else :
            self._node = PrimitiveCommandNode()
            self._node.parse(context)
        
    def __str__(self):
        return str(self._node)


class CommandListNode(Node):

    def __init__(self):
        self._list = []

    def parse(self, context):
        while True:
            if context.currentToken() is None:
                try :
                    raise
                except Exception :
                    print("Missing 'end'")
            elif context.currentToken() == "end":
                context.skipToken("end")
                break
            else :
                commandNode = CommandNode()
                commandNode.parse(context)
                if str(commandNode) != "program":
                    self._list.append(commandNode)

    def __str__(self):
        dst = "["
        for i,item in enumerate(self._list):
            if i != 0:
                dst += ","
            dst += str(item)
        dst += "]"
        return dst