from abc import ABCMeta, abstractmethod
import tkinter as tk

class Context(metaclass=ABCMeta):
    @abstractmethod
    def setClock(self, hour:int):
        pass

    @abstractmethod
    def changeState(self, state):
        pass

    @abstractmethod
    def callSecurityCenter(self, msg:str):
        pass

    @abstractmethod
    def recordLog(self, msg:str):
        pass

class State(metaclass=ABCMeta):
    @abstractmethod
    def doClock(self, context:Context, hour:int):
        pass

    @abstractmethod
    def doUse(self, context:Context):
        pass

    @abstractmethod
    def doAlarm(self, context:Context):
        pass

    @abstractmethod
    def doPhone(self, context:Context):
        pass

class DayState(State):
    _unique_instance = None

    def __init__(self):
        pass

    def doClock(self, context, hour:int):
        if hour < 9 or 17 <= hour:
            context.changeState(NightState.get_instance())

    def doUse(self, context:Context):
        context.recordLog("金庫使用(昼間)")

    def doAlarm(self, context:Context):
        context.callSecurityCenter("非常ベル(昼間)")

    def doPhone(self, context:Context):
        context.callSecurityCenter("通常の通話(昼間)")

    def __str__(self):
        return "[昼間]"

    @classmethod
    def get_instance(cls):
        if not cls._unique_instance:
            cls._unique_instance = cls()
        return cls._unique_instance

class NightState(State):
    _unique_instance = None

    def __init__(self):
        pass

    def doClock(self, context, hour:int):
        if 9 <= hour and hour < 16:
            context.changeState(DayState.get_instance())

    def doUse(self, context:Context):
        context.recordLog("非常：夜間の金庫使用！")

    def doAlarm(self, context:Context):
        context.callSecurityCenter("非常ベル(夜間)")

    def doPhone(self, context:Context):
        context.callSecurityCenter("夜間の通話録音")

    def __str__(self):
        return "[夜間]"

    @classmethod
    def get_instance(cls):
        if not cls._unique_instance:
            cls._unique_instance = cls()
        return cls._unique_instance

class SafeFrame(tk.Frame, Context):

    def __init__(self, master=None):
        super().__init__(master)
        self.__state = DayState.get_instance()
        self.master = master
        self.configure(background = "#d3d3d3")
        self.pack()
        self.create_widgets()

    def __del__(self):
        del self.__state

    def create_widgets(self):
        self.textClock = tk.Entry(self, width=60)
        self.textScreen = tk.Text(self, width=60, height=10)

        self.operateFrame = tk.LabelFrame(self, width=10, height=10)
        self.buttonUse = tk.Button(self.operateFrame, text="金庫使用")
        self.buttonAlarm = tk.Button(self.operateFrame, text="非常ベル")
        self.buttonPhone = tk.Button(self.operateFrame, text="通常通話")
        self.buttonExit = tk.Button(self.operateFrame, text="終了",command=self.master.destroy)

        self.textClock.pack(side="top")
        self.textScreen.pack(side="top")
        self.operateFrame.pack(side="top")
        self.buttonUse.pack(side="left")
        self.buttonAlarm.pack(side="left")
        self.buttonPhone.pack(side="left")
        self.buttonExit.pack(side="left")
        self.buttonUse.bind("<ButtonPress>", self.callback)
        self.buttonAlarm.bind("<ButtonPress>", self.callback)
        self.buttonPhone.bind("<ButtonPress>", self.callback)

    def callback(self,event):
        if event.widget is self.buttonUse:
            self.__state.doUse(self)
        elif event.widget is self.buttonAlarm:
            self.__state.doAlarm(self)
        elif event.widget is self.buttonPhone:
            self.__state.doPhone(self)
        else :
            print("?")

    def setClock(self, hour:int):
        clock_message = "現在時刻は%02d:00" % hour
        self.textClock.delete(0,tk.END)
        self.textClock.insert(tk.END, clock_message)
        self.__state.doClock(self, hour)

    def changeState(self, state):
        message = str(self.__state)
        message += "から"
        message = str(state)
        message += "へ状態が変化しました。"
        print(message)
        self.__state = state

    def printing(self):
        print(self)

    def callSecurityCenter(self, msg:str):
        self.textScreen.insert(tk.END, "call! " + msg + "\n")

    def recordLog(self, msg:str):
        self.textScreen.insert(tk.END, "record ... " + msg + "\n")
