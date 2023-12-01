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


def shopScreen(currency):
    modified_currency = str(currency).replace('(', '$').replace(',', '').replace(')', '')
    #----INSERT FUNCTION TO PULL CURRENCY AMOUNT FROM DB----
    cashCounter = tk.Label( text = f"{modified_currency}",
                           fg = "black",
                           bg = settings.bgColor,
                           font= ("Segoe UI Black", 25))
    cashCounter.place(relx=.9, rely=.05,anchor= CENTER)
    settings.widgetList.append(cashCounter)

    shopTitle = tk.Label( text="The Shop",
                        fg = "Black",
                        bg = settings.bgColor,
                        font = ("Segoe UI Black", 25))
    shopTitle.place(relx=.5, rely=.05,anchor= CENTER)
    settings.widgetList.append(shopTitle)

    colourHeader = tk.Label( text="Available Colours!",
                        fg = "black",
                        bg = settings.bgColor,
                        font = ("Segoe UI", 20))
    colourHeader.place(relx=.5, rely=.15,anchor= CENTER)
    settings.widgetList.append(colourHeader)

    optionOnetxt = tk.Label( text="Ice King",
                        fg = "black",
                        bg = settings.bgColor,
                        font = ("Segoe UI", 13))
    optionOnetxt.place(relx=.25, rely=.2,anchor= CENTER)
    settings.widgetList.append(optionOnetxt)

    option1Color1 = tk.Label( text="      ",
                        bg = "#99b3ff",
                        font = ("segoue ui", 30))
    option1Color1.place(relx=.20, rely=.25,anchor= CENTER)
    settings.widgetList.append(option1Color1)

    option1Color2 = tk.Label( text="      ",
                        bg = "#99ffe6",
                        font = ("segoue ui", 30))
    option1Color2.place(relx=.32, rely=.25,anchor= CENTER)
    settings.widgetList.append(option1Color2)

    optionOne =tk.Button(text="Buy",
                            fg = "black",
                            bg = settings.bgColor,
                            command = lambda: [changeColor("#99b3ff", "#99ffe6"), gui.clearScreen(taskBar.tbWidgets), gui.clearScreen(settings.widgetList), shopScreen(settings.currency), taskBar.taskbar()])
    optionOne.place(relx=.25, rely=.3,anchor= CENTER)
    settings.widgetList.append(optionOne)

    optionTwotxt = tk.Label( text="Forest Walk Theme",
                        fg = "black",
                        bg = settings.bgColor,
                        font = ("Segoe UI", 13))
    optionTwotxt.place(relx=.75, rely=.2,anchor= CENTER)
    settings.widgetList.append(optionTwotxt)

    option2Color1 = tk.Label( text="      ",
                        bg = "#4a6741",
                        font = ("segoue ui", 30))
    option2Color1.place(relx=.68, rely=.25,anchor= CENTER)
    settings.widgetList.append(option2Color1)

    option2Color2 = tk.Label( text="      ",
                        bg = "#3f5a36",
                        font = ("segoue ui", 30))
    option2Color2.place(relx=.80, rely=.25,anchor= CENTER)
    settings.widgetList.append(option2Color2)

    optionTwo =tk.Button(text="Buy",
                            fg = "black",
                            bg = settings.bgColor,
                            command = lambda: [changeColor("#4a6741", "#3f5a36"), gui.clearScreen(taskBar.tbWidgets), gui.clearScreen(settings.widgetList), shopScreen(settings.currency), taskBar.taskbar()])
    optionTwo.place(relx=.75, rely=.3,anchor= CENTER)
    settings.widgetList.append(optionTwo)

    optionThreetxt = tk.Label( text="Yellow Meadows",
                        fg = "black",
                        bg = settings.bgColor,
                        font = ("Segoe UI", 13))
    optionThreetxt.place(relx=.25, rely=.45,anchor= CENTER)
    settings.widgetList.append(optionThreetxt)

    option3Color1 = tk.Label( text="      ",
                        bg = "#ffd800",
                        font = ("segoue ui", 30))
    option3Color1.place(relx=.2, rely=.50,anchor= CENTER)
    settings.widgetList.append(option3Color1)

    option3Color2 = tk.Label( text="      ",
                        bg = "#ffbf00",
                        font = ("segoue ui", 30))
    option3Color2.place(relx=.32, rely=.50,anchor= CENTER)
    settings.widgetList.append(option3Color2)

    optionThree =tk.Button(text="Buy",
                            fg = "black",
                            bg = settings.bgColor,
                            command = lambda: [changeColor("#ffd800", "#ffbf00"), gui.clearScreen(taskBar.tbWidgets), gui.clearScreen(settings.widgetList), shopScreen(settings.currency), taskBar.taskbar()])
    optionThree.place(relx=.25, rely=.55,anchor= CENTER)
    settings.widgetList.append(optionThree)

    optionFourtxt = tk.Label( text="50 Shades of Beige",
                        fg = "black",
                        bg = settings.bgColor,
                        font = ("Segoe UI", 13))
    optionFourtxt.place(relx=.75, rely=.45,anchor= CENTER)
    settings.widgetList.append(optionFourtxt)

    option4Color1 = tk.Label( text="      ",
                        bg = "#969286",
                        font = ("segoue ui", 30))
    option4Color1.place(relx=.68, rely=.50,anchor= CENTER)
    settings.widgetList.append(option4Color1)

    option4Color2 = tk.Label( text="      ",
                        bg = "#e3ded1",
                        font = ("segoue ui", 30))
    option4Color2.place(relx=.80, rely=.50,anchor= CENTER)
    settings.widgetList.append(option4Color2)
    

    optionFour =tk.Button(text="Buy",
                            fg = "black",
                            bg = settings.bgColor,
                            command = lambda: [changeColor("#969286", "#e3ded1"), gui.clearScreen(taskBar.tbWidgets), gui.clearScreen(settings.widgetList), shopScreen(settings.currency), taskBar.taskbar()])
    optionFour.place(relx=.75, rely=.55,anchor= CENTER)
    settings.widgetList.append(optionFour)


    resetColor =tk.Button(text="Reset Colours",
                            fg = "black",
                            bg = settings.bgColor,
                            command = lambda: [changeColor("pink", "#ffe2e6"), gui.clearScreen(taskBar.tbWidgets), gui.clearScreen(settings.widgetList), shopScreen(settings.currency), taskBar.taskbar()])
    resetColor.place(relx=.5, rely=.85,anchor= CENTER)
    settings.widgetList.append(resetColor)
