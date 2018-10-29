import threading

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
        new_instance = None
        try :
            assert cls._unique_instance is None, message
            new_instance = super().__new__(cls)
        except Exception as e:
            print(message)

        return new_instance


    def getBigChar(self, charname):

        _lock = threading.Lock()

        # LOCK
        _lock.acquire()
        key = "" + charname
        bc = None
        if key in self._pool:
            bc = self._pool[key]
        else :
            bc = BigChar(charname)
            self._pool[key] = bc

        # RELEASE
        _lock.release()

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