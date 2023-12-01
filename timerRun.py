from tkinter import *
import tkinter as tk
import time, settings, gui
#UNUSED TIMER CODE - MAY IMPLEMENT LATER

#Code heavily referenced from the following site:
#https://www.tutorialspoint.com/how-to-create-a-timer-using-tkinter



def taskTimer():

    hours = 1
    global times
    times = int(hours)*3600

    def stoppingFunc():
        global times
        times = int(-1)
    
    while times > -1:
        minute, second = (times//60, times%60)
        hour = 0

        if minute>60:
            hour, minute = (minute//60, minute%60)

        if second == 0:
            hrs = tk.Label( text=("0" + str(hour) + ":"+ str(minute) + ":00"),
                    fg = "black",
                    bg = settings.bgColor,
                    font = ("Segoe UI", 12))
            hrs.place(relx=.5, rely=.7,anchor= CENTER)
            settings.widgetList.append(hrs)
        else:
        
            hrs = tk.Label( text=("0" + str(hour) + ":"+ str(minute) + ":" + str(second) ),
                                fg = "black",
                                bg = settings.bgColor,
                                font = ("Segoe UI", 12))
            hrs.place(relx=.5, rely=.7,anchor= CENTER)
            settings.widgetList.append(hrs)
            
        stopTimer = tk.Button( text = "Stop Timer",
                            fg = "Black",
                            bg = settings.bgColor,
                            font = ("Segoe UI", 12),
                            command = lambda : [stoppingFunc()] )
        stopTimer.place(relx=.5, rely=.75,anchor= CENTER)
        settings.widgetList.append(stopTimer)

        gui.root.update()
        time.sleep(1)        

        times -=1
    else:
        hrs = tk.Label( text=("00:00:00"),
                            fg = "black",
                            bg = settings.bgColor,
                            font = ("Segoe UI", 12))
        hrs.place(relx=.5, rely=.7,anchor= CENTER)
        settings.widgetList.append(hrs)
        return