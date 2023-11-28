import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
import mysql.connector

conn = sqlite3.connect("userDetails.db")
cursor = conn.cursor()
#cursor.execute("SELECT currency FROM users WHERE user_id=?", (username,))
result = cursor.fetchone()

"""
This creates a nav bar at the bottom of each page outside of account creation/set-up
"""
def taskbar():

    #color of taskbar background, change this to edit it (hex)
    bgColor = "#ffe2e6"

    #creating the taskbar background as a blank label with color bg
    bgBorder = tk.Label(text = "                                                                                                            ",
                        bg = bgColor,
                        font=("Segoe UI", 60))
    bgBorder.place(relx=.0, rely=.94,anchor= CENTER)
    
    #importing photo for completed button in taskbar
    check = PhotoImage(file = "Images/check.png")
    checkButton = tk.Button(image = check, 
                         bg=bgColor,
                         bd = 0,
                         command = "")
    checkButton.image = check
    checkButton.place(relx=.15, rely=.92,anchor= CENTER)
    completed = tk.Label( text="Completed",
                        fg = "black",
                        bg = bgColor,
                        font = ("Segoe UI",12))
    completed.place(relx=.15, rely=.97,anchor= CENTER)

    #importing photo for home button in taskbar
    home = PhotoImage(file = "Images/home.png")
    homeButton = tk.Button(image = home, 
                         bg=bgColor,
                         bd = 0,
                         command = "")
    homeButton.image = home
    homeButton.place(relx=.5, rely=.92,anchor= CENTER)
    quests = tk.Label( text="Quests",
                        fg = "black",
                        bg = bgColor,
                        font = ("Segoe UI",12))
    quests.place(relx=.5, rely=.97,anchor= CENTER)

    #importing photo for shop button in taskbar
    shop = PhotoImage(file = "Images/shop.png")
    shopButton = tk.Button(image = shop, 
                         bg=bgColor,
                         bd = 0,
                         command = "")
    shopButton.image = shop
    shopButton.place(relx=.85, rely=.92,anchor= CENTER)
    store = tk.Label( text="Shop",
                        fg = "black",
                        bg = bgColor,
                        font = ("Segoe UI",12))
    store.place(relx=.85, rely=.97,anchor= CENTER)