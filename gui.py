"""
This file contains the code relating to the graphical user interface of the application.
This includes things like window, window size, buttons, text, images, etc.
"""
import settings, accountScreens
import tkinter as tk
from tkinter import *
from tkinter import ttk



root = tk.Tk()

#C - Function for displaying the app window on the screen and any GUI
def windowOut():

    #C - This gives the window a title, size and does not allow for its dimensions to be changed.
    root.title("Questing App")
    root.geometry("600x900+50+50")
    root.configure(bg=settings.windowColor)
    root.resizable(False,False)

    #C- Calls Greeting Screen to display
    accountScreens.greetingWindow()
    

    #C- The main loop for the window application
    root.mainloop()


    







