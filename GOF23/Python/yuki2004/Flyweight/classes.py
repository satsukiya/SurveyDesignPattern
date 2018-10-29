

class BigChar:
    _charname = ""
    _fontdata = ""

    def __init__(self, charname):
        self._charname = charname
        filename = "big" + charname + ".txt"
        buf = ""
        with open(filename) as fin:
            buf = fin.read()
        self._fontdata = buf

    def fprint(self):
        print(self._fontdata)


class BigCharFactory:

    _pool = {}
    _unique_instance = None

    @classmethod 
    def getInstance(cls):
        if not cls._unique_instance:
            cls._unique_instance = cls()
        return cls._unique_instance

    def __new__(cls):
        message = "[Singleton!]\n"
        message += "if you get a instance,\n"
        message += "you should call the get instance method."
        try :
            raise Exception
        except Exception as e:
            print(message)

    def getBigChar(self, charname):
        key = "" + charname
        bc = None
        if key in self._pool:
            bc = self._pool[key]
        else :
            bc = BigChar(charname)
            self._pool[key] = bc
        return bc

class BigString:

    _bigchars = []

    def __init__(self, string):
        factory = BigCharFactory.getInstance()
        for item in string:
            self._bigchars.append(factory.getBigChar(item))

    def fprint(self):
        for item in self._bigchars:
            item.fprint()