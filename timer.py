from tkinter import *
import tkinter as tk
import time, settings, gui

#Code heavily referenced from the following site:
#https://www.tutorialspoint.com/how-to-create-a-timer-using-tkinter

def taskTimer(hours):
    times = int(hours)*3600
    while times> -1:
        minute, second = (times//60, times%60)
        hour = 0

        if minute>60:
            hour, minute = (minute//60, minute%60)
        
        hrs = tk.Label( text=hour,
                            fg = "black",
                            bg = settings.bgColor,
                            font = ("Segoe UI", 9))
        hrs.place(relx=.5, rely=.7,anchor= CENTER)
        settings.widgetList.append(hrs)

        mins = tk.Label( text=minute,
                            fg = "black",
                            bg = settings.bgColor,
                            font = ("Segoe UI", 9))
        mins.place(relx=.6, rely=.7,anchor= CENTER)
        settings.widgetList.append(mins)

        secs = tk.Label( text=second,
                            fg = "black",
                            bg = settings.bgColor,
                            font = ("Segoe UI", 9))
        secs.place(relx=.7, rely=.7,anchor= CENTER)
        settings.widgetList.append(secs)

        gui.root.update()
        time.sleep(1)

        times -=1