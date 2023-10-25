import tkinter as tk
import time
from tkinter import *

"""
This file contains the code relating to the graphical user interface of the application.
This includes things like window, window size, buttons, text, images, etc.
"""

#C- Function for displaying the app window on the screen and any GUI
def windowOut():
    root = tk.Tk()

    #C - This gives the window a title, size and does not allow for its dimensions to be changed.
    root.title("Questing App")
    root.geometry("600x900+50+50")
    root.resizable(False,False)

    greetingWindow()
    contScreen()

    #C- The main loop for the window application
    root.mainloop()


#C - The Screen to be displayed when the app is first opened
def greetingWindow():
    #C - Greeting for when the app is opened
    greeting = tk.Label(text="Welcome to QuestIt!",
                        fg = "green",
                        bg = "black",
                        width = 600,
                        height = 900)
    greeting.pack()

def contScreen():
    contButton = tk.Button(text="Continue",
                        fg = "green",
                        bg = "black",
                        width = 300,
                        height = 600)
    contButton.pack()