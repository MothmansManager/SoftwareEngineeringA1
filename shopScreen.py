import tkinter as tk
from tkinter import *
from tkinter import ttk

import gui, todoScreen, taskBar, settings

"""
Display page for the shop screen. Here, users can spend earned currency on app customizations such as a different background color or font.
"""

def shopScreen():

    #----INSERT FUNCTION TO PULL CURRENCY AMOUNT FROM DB----
    cashCounter = tk.Label( text = "$25",
                           fg = "black",
                           bg = "pink",
                           font= ("Segoe UI Black", 25))
    cashCounter.place(relx=.9, rely=.05,anchor= CENTER)
    settings.widgetList.append(cashCounter)

    shopTitle = tk.Label( text="The Shop",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI", 25))
    shopTitle.place(relx=.5, rely=.05,anchor= CENTER)
    settings.widgetList.append(shopTitle)

    colourHeader = tk.Label( text="Available Colours!",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI", 20))
    colourHeader.place(relx=.5, rely=.15,anchor= CENTER)
    settings.widgetList.append(colourHeader)

    optionOne =tk.Button(text="Buy",
                            fg = "black",
                            bg = "pink",
                            command = "")
    optionOne.place(relx=.25, rely=.2,anchor= CENTER)
    settings.widgetList.append(optionOne)

    optionTwo =tk.Button(text="Buy",
                            fg = "black",
                            bg = "pink",
                            command = "")
    optionTwo.place(relx=.75, rely=.2,anchor= CENTER)
    settings.widgetList.append(optionTwo)

    optionThree =tk.Button(text="Buy",
                            fg = "black",
                            bg = "pink",
                            command = "")
    optionThree.place(relx=.25, rely=.4,anchor= CENTER)
    settings.widgetList.append(optionThree)

    optionFour =tk.Button(text="Buy",
                            fg = "black",
                            bg = "pink",
                            command = "")
    optionFour.place(relx=.75, rely=.4,anchor= CENTER)
    settings.widgetList.append(optionFour)


