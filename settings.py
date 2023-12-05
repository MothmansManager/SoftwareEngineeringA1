import sqlite3
from accountScreens import *

#Global variable where widgets are stored, allows screen to be cleared/appended to.
widgetList = []

#color of taskbar background, change this to edit it (hex) - NOT WORKING AS GLOBAL VAR
bgColor = "pink"

#variable for storing the background color
taskbarColor = "#ffe2e6"

#variable for storing background window color
windowColor = "pink"

#stores the current users currency
conn = sqlite3.connect("userDetails.db")
cursor = conn.cursor()
cursor.execute("SELECT currency FROM users WHERE user_id=?", (str(user.get_username),))
currency = cursor.fetchone()


#test variable for making a task list
taskList = ["Clean the Bathroom", "Do my Homework", "Walk the Dog", "YAdaYAda"]

#appends completed tasks from to do to this array for easy viewing and use by builder
completedTaskList = []

def clearScreen(widgets):
    for widget in widgets:
        widget.destroy()
    
    widgets = []