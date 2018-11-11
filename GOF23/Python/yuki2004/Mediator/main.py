
from classes import * 
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    app = LoginFrame("Mediator Sample", master=root)
    app.grid(column=0, row=0, sticky=(tk.N, tk.S))
    app.mainloop()