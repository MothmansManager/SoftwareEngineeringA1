import settings, timerRun, threading
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
                                command = lambda taskText = task: [threading.Thread(target = timerRun.taskTimer(task), daemon = True).start()])
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
