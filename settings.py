#Global variable where widgets are stored, allows screen to be cleared/appended to.
widgetList = []

#color of taskbar background, change this to edit it (hex) - NOT WORKING AS GLOBAL VAR
bgColor = "pink"

#variable for storing the background color
taskbarColor = "#ffe2e6"

#variable for storing background window color
windowColor = "pink"

#stores the current users currency
currency = 0

#test variable for making a task list
taskList = ["Do something you enjoy", "Hang out with your friends!", "Have some time to yourself", "Watch your favourite show!"]

#appends completed tasks from to do to this array for easy viewing and use by builder
completedTaskList = []

def clearScreen(widgets):
    for widget in widgets:
        widget.destroy()
    
    widgets = []