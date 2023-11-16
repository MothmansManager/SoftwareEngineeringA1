import tkinter as tk
from tkinter import *
from tkinter import ttk

import gui, todoScreen, taskBar, settings

settings.widgetList = []

#C - The Screen to be displayed when the app is first opened
def greetingWindow():

    #C - Greeting for when the app is opened
    greeting = tk.Label( text="Welcome to QuestIt!",
                        fg = "black",
                        bg = "pink",
                        font = ("bubblegum",25))
    greeting.place(relx=.5, rely=.05,anchor= CENTER)
    settings.widgetList.append(greeting)

    #C- Button to continue to profile set up
    contButton = tk.Button(text="Create Account",
                            fg = "black",
                            bg = "pink",
                            command = lambda: [gui.clearScreen(settings.widgetList), createAccScreen()])
    contButton.place(x=250, y=200)
    settings.widgetList.append(contButton)

#C- Screen to display upon first launch of the program to create a user account with associated names and "generative"(used to create recommended tasks) tags
def createAccScreen():

    tagList = ["Student", "Professor", "Pet Owner", "Dentist"]

    accountCreateHeader = tk.Label(text="Create Account",
                    fg = "black",
                    bg = "pink",
                    font = ("BubbleGum",24))
    accountCreateHeader.place(relx=.5, rely=.05,anchor= CENTER)
    settings.widgetList.append(accountCreateHeader)
    
    name = tk.Label(text="First Name:",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI",12))
    name.place(relx=.30, rely=.2,anchor= CENTER)
    settings.widgetList.append(name)

    #C- Entry box for user to input their name for later use
    nameEntry = tk.Entry()
    settings.widgetList.append(nameEntry)
    nameEntry.place(relx=.50, rely=.2,anchor= CENTER)

    #C- Displays tag text and 3 dropdown selections for user to chose applicable tags from
    tagTitle = tk.Label(text="User Tags:",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI",12))
    tagTitle.place(relx=.5, rely=.3,anchor= CENTER)
    settings.widgetList.append(tagTitle)

    tag1 = ttk.Combobox(values = tagList)
    tag1.set("Select a Tag")
    tag1.place(relx=.50, rely=.35,anchor= CENTER)
    settings.widgetList.append(tag1)

    tag2 = ttk.Combobox(values = tagList)
    tag2.set("Select a Tag")
    tag2.place(relx=.50, rely=.4,anchor= CENTER)
    settings.widgetList.append(tag2)

    tag3 = ttk.Combobox(values = tagList)
    tag3.set("Select a Tag")
    tag3.place(relx=.50, rely=.45,anchor= CENTER)
    settings.widgetList.append(tag3)

    contButton = tk.Button(text="Submit",
                            fg = "black",
                            bg = "pink",
                            font = ("Segoe UI",10),
                            command = lambda: [gui.clearScreen(settings.widgetList), todoScreen.questScreen(), taskBar.taskbar()])
    contButton.place(relx=.50, rely=.5,anchor= CENTER)
    settings.widgetList.append(contButton)
