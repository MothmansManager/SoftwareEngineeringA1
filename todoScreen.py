import tkinter as tk
from tkinter import *
import sqlite3
import settings, builder

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
