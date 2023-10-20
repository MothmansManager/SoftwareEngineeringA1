import tkinter as tk
from tkinter import ttk

"""
This file contains the code relating to the graphical user interface of the application.
This includes things like window, window size, buttons, text, images, etc.
"""

def windowOut():
    root = tk.Tk()


    root.title("Questing App")
    root.geometry("600x900+50+50")
    root.resizable(False,False)

    root.mainloop()