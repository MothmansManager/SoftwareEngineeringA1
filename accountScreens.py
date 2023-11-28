import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
#import mysql.connector #must be installed "pip install mysql-connector-python"

import gui, todoScreen, taskBar

widgetList = []

conn = sqlite3.connect("userDetails.db")
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY NOT NULL,
        password INTEGER NOT NULL,
        name TEXT,
        tag1 TEXT,
        tag2 TEXT,
        tag3 TEXT,
        currency INTEGER
)''')

conn.commit()
conn.close()

#C - The Screen to be displayed when the app is first opened
def greetingWindow():

    #C - Greeting for when the app is opened
    greeting = tk.Label( text="Welcome to QuestIt!",
                        fg = "black",
                        bg = "pink",
                        font = ("bubblegum",25))
    greeting.place(x=138, y=100)
    widgetList.append(greeting)

    #C- Button to continue to profile set up
    contButton = tk.Button(text="Create Account",
                            fg = "black",
                            bg = "pink",
                            command = lambda: [gui.clearScreen(widgetList), createAccScreen()])
    contButton.place(x=250, y=200)
    widgetList.append(contButton)

#C- Screen to display upon first launch of the program to create a user account with associated names and "generative"(used to create recommended tasks) tags
def createAccScreen():

    account_created=False

    tagList = ["Student", "Professor", "Pet Owner", "Dentist"]

    accountCreateHeader = tk.Label(text="Create Account",
                    fg = "black",
                    bg = "pink",
                    font = ("BubbleGum",24))
    accountCreateHeader.place(relx=.5, rely=.05,anchor= CENTER)
    widgetList.append(accountCreateHeader)

    username = tk.Label(text="Username:",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI",12))
    username.place(relx=.30, rely=.15, anchor=CENTER)
    widgetList.append(username)

    usernameEntry = tk.Entry()
    widgetList.append(usernameEntry)
    usernameEntry.place(relx=.50, rely=.15,anchor= CENTER)
    
    name = tk.Label(text="First Name:",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI",12))
    name.place(relx=.30, rely=.2,anchor= CENTER)
    widgetList.append(name)

    #C- Entry box for user to input their name for later use
    nameEntry = tk.Entry()
    widgetList.append(nameEntry)
    nameEntry.place(relx=.50, rely=.2,anchor= CENTER)

    password = tk.Label(text="Password:",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI",12))
    password.place(relx=.30, rely=.25, anchor=CENTER)
    widgetList.append(password)

    passwordEntry = tk.Entry(show="*")
    widgetList.append(passwordEntry)
    passwordEntry.place(relx=.50, rely=.25,anchor= CENTER)

    #C- Displays tag text and 3 dropdown selections for user to chose applicable tags from
    tagTitle = tk.Label(text="User Tags:",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI",12))
    tagTitle.place(relx=.5, rely=.3,anchor= CENTER)
    widgetList.append(tagTitle)

    tag1 = ttk.Combobox(values = tagList)
    tag1.set("Select a Tag")
    tag1.place(relx=.50, rely=.35,anchor= CENTER)
    widgetList.append(tag1)

    tag2 = ttk.Combobox(values = tagList)
    tag2.set("Select a Tag")
    tag2.place(relx=.50, rely=.4,anchor= CENTER)
    widgetList.append(tag2)

    tag3 = ttk.Combobox(values = tagList)
    tag3.set("Select a Tag")
    tag3.place(relx=.50, rely=.45,anchor= CENTER)
    widgetList.append(tag3)

    contButton = tk.Button(text="Submit",
                            fg = "black",
                            bg = "pink",
                            font = ("Segoe UI",10),
                            command = lambda: submitAccount(usernameEntry.get(), passwordEntry.get()))
    contButton.place(relx=.50, rely=.5,anchor= CENTER)
    widgetList.append(contButton)

    username = usernameEntry.get()
    password = passwordEntry.get()

    return account_created


def submitAccount(username, password):
    global widgetList
    global conn

    # Connect to the database
    conn = sqlite3.connect("userDetails.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE user_id=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        existing = tk.Label(text="This username already exists. Please choose another one or login",
                           fg="red",
                           bg="pink",
                           font=("Segoe UI", 12))
        existing.place(relx=.6, rely=.3, anchor=CENTER)
        widgetList.append(existing)
    else:
        # Insert the new user into the database
        cursor.execute("INSERT INTO users (user_id, password, currency) VALUES (?, ?, 0)", (username, password))
        conn.commit()
        account_created_label = tk.Label(text="You have successfully signed up!! Please login",
                                         fg="black",
                                         bg="pink",
                                         font=("Segoe UI", 12))
        account_created_label.place(relx=.6, rely=.3, anchor=CENTER)
        widgetList.append(account_created_label)

        # Set the account_created variable to True
        account_created = True
    
    if account_created == True:          
        gui.clearScreen(widgetList)
        todoScreen.questScreen()
        taskBar.taskbar()
    # Close the database connection
    conn.close()

            


