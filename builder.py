import settings, gui, timerRun, threading
import tkinter as tk
from tkinter import *

#Used to display all the generated tasks on the todoScreen page
def taskBuilder(taskList):
    xpos = .5
    ypos = .1
    for task in taskList:
        #Lists quests available
        taskLabel = tk.Label(text = task,
                            fg = "black",
                            bg = settings.bgColor,
                            font = ("Segoe UI",14))
        taskLabel.place(relx=xpos, rely=ypos,anchor= CENTER)
        settings.widgetList.append(taskLabel)

        ypos +=.05

        accept = tk.Button(text="Accept",
                                fg = "black",
                                bg = settings.bgColor,
                                font = ("Segoe UI",10),
                                command = lambda taskText = task: [threading.Thread(target = timerRun.taskTimer, daemon = True).start(),settings.completedTaskList.append(taskText)])
        accept.place(relx=xpos, rely=ypos,anchor= CENTER)
        settings.widgetList.append(accept)

        ypos += .05

    return

#modified version of above to do similar for the completed tasks page
def completedBuilder(completedTaskList):

    xpos = .5
    ypos = .1
    for task in completedTaskList:
        #Lists quests available
        task = tk.Label(text = task,
                            fg = "black",
                            bg = settings.bgColor,
                            font = ("Segoe UI",14))
        task.place(relx=xpos, rely=ypos,anchor= CENTER)
        settings.widgetList.append(task)

        ypos +=.05

    return

def shopBuilder(shopDict):

    
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
    return