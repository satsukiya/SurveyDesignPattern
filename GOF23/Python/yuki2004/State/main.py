from classes import *
import tkinter as tk
import time
import concurrent.futures

def daytime(frame):
    while True:
        for hour in range(24):
            frame.setClock(hour)
            time.sleep(1)
    

if __name__ == '__main__':
    root = tk.Tk()
    app = SafeFrame(master=root)
    executor = concurrent.futures.ThreadPoolExecutor()
    executor.submit(daytime, app)
    app.mainloop()
