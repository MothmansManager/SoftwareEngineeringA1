from tkinter import *
import tkinter as tk
import time, settings, gui

#UNUSED TIMER CODE - MAY IMPLEMENT LATER

#Code heavily referenced from the following site:
#https://www.tutorialspoint.com/how-to-create-a-timer-using-tkinter

def taskTimer(running):
    hours = 1
    times = int(hours)*3600
    
    while times> -1:
        if running:
            minute, second = (times//60, times%60)
            hour = 0

            if minute>60:
                hour, minute = (minute//60, minute%60)
            
            hrs = tk.Label( text=(str(hour) + ":"+ str(minute) + ":" + str(second)),
                                fg = "black",
                                bg = settings.bgColor,
                                font = ("Segoe UI", 9))
            hrs.place(relx=.5, rely=.7,anchor= CENTER)
            settings.widgetList.append(hrs)

            if times <= -1:
                hrs = tk.Label( text=(str(00) + ":"+ str(00) + ":" + str(00)),
                                    fg = "black",
                                    bg = settings.bgColor,
                                    font = ("Segoe UI", 9))
                hrs.place(relx=.5, rely=.7,anchor= CENTER)
                settings.widgetList.append(hrs)
            gui.root.update()
            time.sleep(1)        

            times -=1
        else:
            return

    return