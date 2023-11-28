import tkinter as tk
from tkinter import *
from tkinter import ttk

import gui, todoScreen, taskBar, settings

"""
Display page for the shop screen. Here, users can spend earned currency on app customizations such as a different background color or font.
"""
def changeColor(background, taskbar):
    settings.bgColor = background
    gui.root.configure(bg = background)
    settings.taskbarColor = taskbar


def shopScreen():

    #----INSERT FUNCTION TO PULL CURRENCY AMOUNT FROM DB----
    cashCounter = tk.Label( text = "$25",
                           fg = "black",
                           bg = settings.bgColor,
                           font= ("Segoe UI Black", 25))
    cashCounter.place(relx=.9, rely=.05,anchor= CENTER)
    settings.widgetList.append(cashCounter)

    shopTitle = tk.Label( text="The Shop",
                        fg = "black",
                        bg = settings.bgColor,
                        font = ("Segoe UI", 25))
    shopTitle.place(relx=.5, rely=.05,anchor= CENTER)
    settings.widgetList.append(shopTitle)

    colourHeader = tk.Label( text="Available Colours!",
                        fg = "black",
                        bg = settings.bgColor,
                        font = ("Segoe UI", 20))
    colourHeader.place(relx=.5, rely=.15,anchor= CENTER)
    settings.widgetList.append(colourHeader)

    optionOnetxt = tk.Label( text="Baby Blue Theme",
                        fg = "black",
                        bg = settings.bgColor,
                        font = ("Segoe UI", 25))
    optionOnetxt.place(relx=.25, rely=.2,anchor= CENTER)
    settings.widgetList.append(optionOnetxt)

    optionOne =tk.Button(text="Buy",
                            fg = "black",
                            bg = settings.bgColor,
                            command = lambda: [changeColor("#99b3ff", "#99ffe6"), gui.clearScreen(taskBar.tbWidgets), gui.clearScreen(settings.widgetList), shopScreen(), taskBar.taskbar()])
    optionOne.place(relx=.25, rely=.25,anchor= CENTER)
    settings.widgetList.append(optionOne)

    optionTwotxt = tk.Label( text="Forest Walk Theme",
                        fg = "black",
                        bg = settings.bgColor,
                        font = ("Segoe UI", 25))
    optionTwotxt.place(relx=.25, rely=.2,anchor= CENTER)
    settings.widgetList.append(optionOnetxt)

    optionTwo =tk.Button(text="Buy",
                            fg = "black",
                            bg = settings.bgColor,
                            command = lambda: [changeColor("#4a6741", "#3f5a36"), gui.clearScreen(taskBar.tbWidgets), gui.clearScreen(settings.widgetList), shopScreen(), taskBar.taskbar()])
    optionTwo.place(relx=.75, rely=.2,anchor= CENTER)
    settings.widgetList.append(optionTwo)

    optionThree =tk.Button(text="Buy",
                            fg = "black",
                            bg = settings.bgColor,
                            command = lambda: [changeColor("green", "red"), gui.clearScreen(taskBar.tbWidgets), gui.clearScreen(settings.widgetList), shopScreen(), taskBar.taskbar()])
    optionThree.place(relx=.25, rely=.4,anchor= CENTER)
    settings.widgetList.append(optionThree)

    optionFour =tk.Button(text="Buy",
                            fg = "black",
                            bg = settings.bgColor,
                            command = lambda: [changeColor("green", "red"), gui.clearScreen(taskBar.tbWidgets), gui.clearScreen(settings.widgetList), shopScreen(), taskBar.taskbar()])
    optionFour.place(relx=.75, rely=.4,anchor= CENTER)

    resetColor =tk.Button(text="Reset Colours",
                            fg = "black",
                            bg = settings.bgColor,
                            command = lambda: [changeColor("pink", "#ffe2e6"), gui.clearScreen(taskBar.tbWidgets), gui.clearScreen(settings.widgetList), shopScreen(), taskBar.taskbar()])
    resetColor.place(relx=.5, rely=.8,anchor= CENTER)
    settings.widgetList.append(optionFour)
