import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
import accountScreens, settings, timerRun, gui, builder

conn = sqlite3.connect("userDetails.db")
cursor = conn.cursor()
#cursor.execute("SELECT currency FROM users WHERE user_id=?", (accountScreens.username,))
result = cursor.fetchone()

def questScreen(currency):
    modified_currency = str(currency).replace('(', '$').replace(',', '').replace(')', '')
    #Displays current credit amount at top right
    cashCounter = tk.Label( text = f'{modified_currency}',
                           fg = "black",
                           bg = settings.bgColor,
                           font= ("Segoe UI Black", 25))
    cashCounter.place(relx=.9, rely=.05,anchor= CENTER)
    settings.widgetList.append(cashCounter)


    #Page header
    greeting = tk.Label( text="Todays Quests!",
                        fg = "black",
                        bg = settings.bgColor,
                        font = ("Segoe UI Black",25))
    greeting.place(relx=.5, rely=.05,anchor= CENTER)
    settings.widgetList.append(greeting)

    builder.taskBuilder(settings.taskList)

    # #Lists quests available
    # questOne = tk.Label(text = "This is quest 1!",
    #                     fg = "black",
    #                     bg = settings.bgColor,
    #                     font = ("Segoe UI",14))
    # questOne.place(relx=.5, rely=.10,anchor= CENTER)
    # settings.widgetList.append(questOne)

    # acceptOne = tk.Button(text="Accept",
    #                         fg = "black",
    #                         bg = settings.bgColor,
    #                         font = ("Segoe UI",10),
    #                         command = lambda : [])
    # acceptOne.place(relx=.5, rely=.15,anchor= CENTER)
    # settings.widgetList.append(acceptOne)
    

    # questTwo = tk.Label(text = "This is quest 2!",
    #                     fg = "black",
    #                     bg = settings.bgColor,
    #                     font = ("Segoe UI",14))
    # questTwo.place(relx=.5, rely=.20,anchor= CENTER)
    # settings.widgetList.append(questTwo)

    # acceptTwo = tk.Button(text="Accept",
    #                         fg = "black",
    #                         bg = settings.bgColor,
    #                         font=("Segoe UI",10))
    # acceptTwo.place(relx=.5, rely=.25,anchor= CENTER)
    # settings.widgetList.append(acceptTwo)
