import tkinter as tk
from tkinter import *
from tkinter import ttk

import gui, todoScreen, taskBar, settings, builder

def completedQuests():

    #----INSERT FUNCTION TO PULL CURRENCY AMOUNT FROM DB----
    cashCounter = tk.Label( text = "$25",
                           fg = "black",
                           bg = settings.bgColor,
                           font= ("Segoe UI Black", 25))
    cashCounter.place(relx=.9, rely=.05,anchor= CENTER)
    settings.widgetList.append(cashCounter)

    completedTitle = tk.Label( text="Completed Quests!",
                        fg = "black",
                        bg = settings.bgColor,
                        font = ("Segoe UI Black", 25))
    completedTitle.place(relx=.5, rely=.05,anchor= CENTER)
    settings.widgetList.append(completedTitle)

    builder.taskBuilder(settings.completedTaskList)

    