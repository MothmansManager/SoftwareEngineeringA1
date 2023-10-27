"""
This file contains the code relating to the graphical user interface of the application.
This includes things like window, window size, buttons, text, images, etc.
"""

import tkinter as tk
import time
from tkinter import *
from tkinter import ttk


#C - Function for displaying the app window on the screen and any GUI
def windowOut():
    root = tk.Tk()
    frame = Frame(root)

    #C - This gives the window a title, size and does not allow for its dimensions to be changed.
    root.title("Questing App")
    root.geometry("600x900+50+50")
    root.resizable(False,False)

    #C- Calls Greeting Screen to display
    greetingWindow()

    #C- The main loop for the window application
    root.mainloop()




#C - The Screen to be displayed when the app is first opened
def greetingWindow():

    """
    CLean up nextScreenLogin() code!!!
    """
    def nextScreenLogin():
        greeting.destroy()
        contButton.destroy()
        createAccScreen()
        
    
    #C - Greeting for when the app is opened
    greeting = tk.Label( text="Welcome to QuestIt!",
                        fg = "black",
                        font = ("Arial",25))
    greeting.place(x=138, y=100)

    #C- Button to continue to profile set up
    contButton = tk.Button(text="Create Account",
                            fg = "black",
                            command = nextScreenLogin)
    contButton.place(x=250, y=200)

#C- Screen to display upon first launch of the program to create a user account with associated names and "generative"(used to create recommended tasks) tags
def createAccScreen():

    tagList = ["Student", "Professor", "Pet Owner", "Dentist"]

    accountCreateHeader = tk.Label(text="Create Account",
                    fg = "black",
                    font = ("Arial",24)).grid(row=0, columnspan=2)
    
    name = tk.Label(text="First Name:",
                        fg = "black",
                        font = ("Arial",12)).grid(row=1)

    #C- Entry box for user to input their name for later use
    nameEntry = tk.Entry()
    nameEntry.grid(row=1, column=1)

    #C- Displays tag text and 3 dropdown selections for user to chose applicable tags from
    tagTitle = tk.Label(text="User Tags:",
                        fg = "black",
                        font = ("Arial",12)).grid(row=2)
    tag1 = ttk.Combobox(values = tagList)
    tag1.set("Select a Tag")
    tag1.grid(row=2, column=1)

    tag2 = ttk.Combobox(values = tagList)
    tag2.set("Select a Tag")
    tag2.grid(row=3, column=1)

    tag3 = ttk.Combobox(values = tagList)
    tag3.set("Select a Tag")
    tag3.grid(row=4, column=1)

    contButton = tk.Button(text="Submit",
                            fg = "black").grid(row=5)

#hello