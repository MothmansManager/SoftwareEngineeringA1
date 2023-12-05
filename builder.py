import settings, timerRun, threading
import tkinter as tk
from tkinter import *
import random, settings, sqlite3
from tagsAndTasks import tagsArray

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

def compareTags():
    from accountScreens import checkTags
    common = []
    tags = checkTags()
    array = tagsArray()
    for tag in tags:
        if tag in array:
            common.append(tag)
    return common

def recommendedTasks():
    recommendation = []
    common = compareTags()
    conn = sqlite3.connect("tags.db")
    cursor = conn.cursor()
    for tag in common:
        cursor.execute("SELECT task1, task2, task3 from tags WHERE tagName=?", tag)
        recommendations = cursor.fetchall()
    for i in recommendations:
        recommendation.append[i]
    
    task = random.choice(recommendation)
    task1 = tk.Label(text = task,
                        fg = "black",
                        bg = settings.bgColor,
                        font = ("Segoe UI",14))
    task1.place(relx=.5, rely=.5,anchor=CENTER)
    settings.widgetList.append(task1)
    accept1 = tk.Button(text="Accept",
                        fg = "black",
                        bg = settings.bgColor,
                        font = ("Segoe UI",10),
                        command = lambda taskText = task: [threading.Thread(target = timerRun.taskTimer(task), daemon = True).start()])
    accept1.place(relx=.5, rely=.55,anchor= CENTER)
    settings.widgetList.append(accept1)


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
                            command = lambda: [changeColor("#99b3ff", "#99ffe6"), settings.clearScreen(taskBar.tbWidgets), settings.clearScreen(settings.widgetList), shopScreen(settings.currency), taskBar.taskbar()])
    optionOne.place(relx=.25, rely=.3,anchor= CENTER)
    settings.widgetList.append(optionOne)
    return