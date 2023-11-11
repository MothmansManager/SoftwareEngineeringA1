import tkinter as tk
from tkinter import *
from tkinter import ttk


import accountScreens

def questScreen():

    cashCounter = tk.Label( text = "$25",
                           fg = "black",
                           bg = "pink",
                           font= ("Segoe UI Black", 25))
    cashCounter.place(relx=.9, rely=.05,anchor= CENTER)

    greeting = tk.Label( text="Todays Quests!",
                        fg = "black",
                        bg = "pink",
                        font = ("BubbleGum",25))
    greeting.place(relx=.5, rely=.05,anchor= CENTER)
    accountScreens.widgetList.append(greeting)


    questOne = tk.Label(text = "This is quest 1!",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI",14))
    questOne.place(relx=.5, rely=.10,anchor= CENTER)
    accountScreens.widgetList.append(questOne)

    acceptOne = tk.Button(text="Accept",
                            fg = "black",
                            bg = "pink",
                            font = ("Segoe UI",10))
    acceptOne.place(relx=.5, rely=.15,anchor= CENTER)
    accountScreens.widgetList.append(acceptOne)
    

    questTwo = tk.Label(text = "This is quest 2!",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI",14))
    questTwo.place(relx=.5, rely=.20,anchor= CENTER)
    accountScreens.widgetList.append(questTwo)

    acceptTwo = tk.Button(text="Accept",
                            fg = "black",
                            bg = "pink",
                            font=("Segoe UI",10))
    acceptTwo.place(relx=.5, rely=.25,anchor= CENTER)
    accountScreens.widgetList.append(acceptTwo)
