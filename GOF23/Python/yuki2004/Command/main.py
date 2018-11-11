
from command.classes import *
from drawer.classes import *

import tkinter as tk

class Main(tk.Frame):

    def __init__(self, title, master=None):
        super().__init__(master, width=60)

        self._history = MacroCommand()

        self.master.title(title)
        self.pack()

        self.buttonClear = tk.Button(text="Cancel", command=self.clear)
        self.buttonUndo = tk.Button(text="Undo", command=self.undo)
        self.buttonClear.pack(side="top")
        self.buttonUndo.pack(side="top")
        self._canvas = DrawCanvas(400, 400, self._history)
        self._canvas.bind("<ButtonPress-1>", self.StartMove)
        self._canvas.bind("<ButtonRelease-1>", self.StopMove)
        self._canvas.bind("<B1-Motion>", self.OnMotion)
        self._canvas.pack(side="top")
    
    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        cmd = DrawCommand(self._canvas, Point(event.x,event.y))
        self._history.append(cmd)
        cmd.execute()

    def undo(self):
        item = self._history.undo()
        self._canvas.delete(item)

    def clear(self):
        self._history.clear()
        self._canvas.delete("all")


if __name__ == '__main__':
    root = tk.Tk()
    app = Main("Command Pattern Sample", root)
    app.mainloop()