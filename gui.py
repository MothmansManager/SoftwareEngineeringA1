"""
This file contains the code relating to the graphical user interface of the application.
This includes things like window, window size, buttons, text, images, etc.
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk

from accountScreens import *


#C - Function for displaying the app window on the screen and any GUI
def windowOut():
    root = tk.Tk()
    frame = Frame(root)

    #C - This gives the window a title, size and does not allow for its dimensions to be changed.
    root.title("Questing App")
    root.geometry("600x900+50+50")
    root.configure(bg='pink')
    root.resizable(False,False)

    #C- Calls Greeting Screen to display
    greetingWindow()
    

    #C- The main loop for the window application
    root.mainloop()

def clearScreen(widgets):
    for widget in widgets:
        widget.destroy()
    
    widgets = []
    







