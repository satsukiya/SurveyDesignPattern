from abc import ABCMeta, abstractmethod

import tkinter as tk

class Mediator(metaclass=ABCMeta):
    @abstractmethod
    def createColleagues(self):
        pass

    @abstractmethod
    def colleagueChanged(self):
        pass

class Colleague(metaclass=ABCMeta):
    @abstractmethod
    def setMediator(self, mediator):
        pass

    @abstractmethod
    def setColleagueEnabled(self, enabled):
        pass

class ColleagueButton(tk.Button, Colleague):

    def __init__(self, caption:str, master=None):
        super().__init__(master)
        self["text"] = caption
        self._mediator = None

    def setMediator(self, mediator):
        self._mediator = mediator

    def setColleagueEnabled(self, enabled):
        if enabled:
            self["state"] = tk.NORMAL
        else :
            self["state"] = tk.DISABLED

class ColleagueCheckbox(tk.Radiobutton, Colleague):

    def __init__(self, caption:str, group, val, master=None, v=0):
        super().__init__(master)
        self.configure(background="#d3d3d3", variable=val, command=self.itemStateChanged, val=v)
        self["text"] = caption
        self._mediator = None

    def setMediator(self, mediator):
        self._mediator = mediator

    def setColleagueEnabled(self, enabled):
        self._boolvar.set(enabled)

    def itemStateChanged(self):
        self._mediator.colleagueChanged()


class ColleagueTextField(tk.Entry, Colleague):

    def __init__(self, text:str, columns:int, master=None):
        super().__init__(master)
        self._mediator = None
        self.configure(text=text, width=columns)
        self.bind("<Key>", self.textValueChanged)

    def setMediator(self, mediator):
        self._mediator = mediator

    def setColleagueEnabled(self, enabled:bool):
        if enabled:
            self["state"] = tk.NORMAL
        else :
            self["state"] = tk.DISABLED
        self["disabledbackground"] = "#ffffff" if enabled else "#d3d3d3"

    def textValueChanged(self, event):
        self._mediator.colleagueChanged(event)


class Parameter:
    def __init__(self, val, key):
        self.__val = val
        self.__key = key

    @property
    def val(self):
        return self.__val

    @property
    def key(self):
        dst = ""
        if self.__key is not None:
            dst = self.__key
        return dst

class Condition(metaclass=ABCMeta):

    def __init__(self, param):
        self._param = param

    @abstractmethod
    def condition(self):
        pass

    def __str__(self):
        return self._param.val + ":" + self._param.key

class InitCondition(Condition):

    def __init__(self, param):
        super().__init__(param)

    def condition(self):
        dst = False
        if self._param.key is None:
                dst = True
        return dst

class GeneralCondition(Condition):

    def __init__(self, param):
        super().__init__(param)

    def condition(self):
        dst = False
        if 0 < len(self._param.val):
            dst = True
        return dst

class ComfirmList:

    def __init__(self):
        self._condList = []

    def addConditon(self, item):
        self._condList.append(item)

    def result(self):
        dst = False
        for item in self._condList:
            if item.condition():
                dst = True
                break
        return dst

class LoginFrame(tk.Frame, Mediator):
    def __init__(self, title:str, master=None):
        super().__init__(master, width=60)
        self.master.title(title)
        self.configure(background="#d3d3d3", width=500,height=500)
        self.pack()
        self.val = tk.IntVar()
        self.createColleagues()
        self.colleagueChanged()

    def createColleagues(self):
        checkboxArea = tk.Frame(self, background="#d3d3d3")
        userNameArea = tk.Frame(self, background="#d3d3d3")
        passwordArea = tk.Frame(self, background="#d3d3d3")
        buttonArea = tk.Frame(self, background="#d3d3d3")

        self.val.set(0)
        self.checkGuest = ColleagueCheckbox("Guest", self.master, self.val, checkboxArea, 0)
        self.checkLogin = ColleagueCheckbox("Login", self.master, self.val, checkboxArea, 1)

        ulabel = tk.Label(userNameArea, text="Username:", background="#d3d3d3")
        self.textUser = ColleagueTextField("", 20, userNameArea)
        
        plabel = tk.Label(passwordArea, text="Password:", background="#d3d3d3")
        self.textPass = ColleagueTextField("", 20, passwordArea)
        self.textPass.configure(show="*")

        self.buttonOk = ColleagueButton("OK", buttonArea)
        self.buttonCancel = ColleagueButton("Cancel", buttonArea)

        self.checkGuest.setMediator(self)
        self.checkLogin.setMediator(self)
        self.textUser.setMediator(self)
        self.textPass.setMediator(self)
        self.buttonOk.setMediator(self)
        self.buttonCancel.setMediator(self)

        checkboxArea.pack()
        userNameArea.pack()
        passwordArea.pack()
        buttonArea.pack()

        self.checkGuest.pack(side="left")
        self.checkLogin.pack(side="left")
        
        ulabel.pack(side="left")
        self.textUser.pack(side="left")

        plabel.pack(side="left")
        self.textPass.pack(side="left")
        
        self.buttonOk.pack(side="left")
        self.buttonCancel.pack(side="left")

    def colleagueChanged(self, event=None):
        if self.val.get() == 0:
            self.textUser.setColleagueEnabled(False)
            self.textPass.setColleagueEnabled(False)
            self.buttonOk.setColleagueEnabled(True)
        else:
            self.textUser.setColleagueEnabled(True)
            self.userpassChanged(event)

    def userpassChanged(self, event=None):

        key = None
        if event is not None:
            key = event.keysym

        if self.distributor(self.textUser.get(), key).result():
            self.textPass.setColleagueEnabled(True)
            if self.distributor(self.textPass.get(), key).result():
                self.buttonOk.setColleagueEnabled(True)
            else :
                self.buttonOk.setColleagueEnabled(False)
        else :
            self.textPass.setColleagueEnabled(False)
            self.buttonOk.setColleagueEnabled(False)

    def distributor(self, val, key):
        p = Parameter(val, key)
        cl = ComfirmList()
        cl.addConditon(InitCondition(p))
        cl.addConditon(GeneralCondition(p))
        return cl