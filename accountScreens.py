import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3, settings
#import mysql.connector #must be installed "pip install mysql-connector-python"

import todoScreen, taskBar, settings

conn = sqlite3.connect("userDetails.db")
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY NOT NULL,
        password INTEGER NOT NULL,
        name TEXT,
        tag1 TEXT,
        tag2 TEXT,
        tag3 TEXT,
        currency INTEGER
)''')

conn.commit()
conn.close()

#C - The Screen to be displayed when the app is first opened
def greetingWindow():
    def display_usernames():
            # Connect to the database
            conn = sqlite3.connect("userDetails.db")
            cursor = conn.cursor()

            # Retrieve all users
            cursor.execute("SELECT user_id FROM users")
            users = cursor.fetchall()

            # Display usernames using labels
            yPixel = 280
            usersArray = []
            for i, user_id in enumerate(users):
                existingUser = tk.Button(text=f"User {i+1}: {user_id[0]}",
                                        fg = "black",
                                        bg = "pink",
                                        font = ("Segoe UI", 9),
                                        command = lambda user_id = user_id: [settings.clearScreen(settings.widgetList), login(user_id)])
                existingUser.place(relx=0.5, y=yPixel, anchor=CENTER)
                settings.widgetList.append(existingUser)
                yPixel += 35

    #C - Greeting for when the app is opened
    greeting = tk.Label( text="Welcome to QuestIt!",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI Black",25))
    greeting.place(relx=0.5, rely=.05, anchor=CENTER)
    settings.widgetList.append(greeting)

    #C- Button to continue to profile set up
    contButton = tk.Button(text="Create Account",
                            fg = "black",
                            bg = "pink",
                            command = lambda: [settings.clearScreen(settings.widgetList), createAccScreen()])
    contButton.place(x=250, y=200)
    settings.widgetList.append(contButton)

    #TESTING BUTTON REMOVE FOR FULL RELEASE
    skipButton = tk.Button(text="SKIP",
                            fg = "black",
                            bg = "pink",
                            command = lambda: [settings.clearScreen(settings.widgetList), todoScreen.questScreen(0), taskBar.taskbar()])
    skipButton.place(relx=.5, rely=.9, anchor = CENTER)
    settings.widgetList.append(skipButton)

    display_usernames()

    conn.close()
#C- Screen to display upon first launch of the program to create a user account with associated names and "generative"(used to create recommended tasks) tags
def createAccScreen():

    account_created=False

    tagList = ["Student", "Professor", "Pet Owner", "Dentist"]

    accountCreateHeader = tk.Label(text="Create Account",
                    fg = "black",
                    bg = "pink",
                    font = ("Segoe UI Black",24))
    accountCreateHeader.place(relx=.5, rely=.05,anchor= CENTER)
    settings.widgetList.append(accountCreateHeader)

    username = tk.Label(text="Username(2-8 Characters):",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI",12))
    username.place(relx=.4, rely=.15, anchor=E)
    settings.widgetList.append(username)

    usernameEntry = tk.Entry()
    settings.widgetList.append(usernameEntry)
    usernameEntry.place(relx=.50, rely=.15,anchor= CENTER)
    
    name = tk.Label(text="First Name(3-12):",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI",12))
    name.place(relx=.4, rely=.2,anchor= E)
    settings.widgetList.append(name)

    #C- Entry box for user to input their name for later use
    nameEntry = tk.Entry()
    settings.widgetList.append(nameEntry)
    nameEntry.place(relx=.50, rely=.2,anchor= CENTER)

    password = tk.Label(text="Password(4-10):",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI",12))
    password.place(relx=.4, rely=.25, anchor=E)
    settings.widgetList.append(password)

    passwordEntry = tk.Entry(show="*")
    settings.widgetList.append(passwordEntry)
    passwordEntry.place(relx=.50, rely=.25,anchor= CENTER)

    #C- Displays tag text and 3 dropdown selections for user to chose applicable tags from
    tagTitle = tk.Label(text="User Tags:",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI",12))
    tagTitle.place(relx=.5, rely=.3,anchor= CENTER)
    settings.widgetList.append(tagTitle)

    tag1 = ttk.Combobox(values = tagList)
    tag1.set("Select a Tag")
    tag1.place(relx=.50, rely=.35,anchor= CENTER)
    settings.widgetList.append(tag1)
    tag1["state"] = "readonly"

    tag2 = ttk.Combobox(values = tagList)
    tag2.set("Select a Tag")
    tag2.place(relx=.50, rely=.4,anchor= CENTER)
    settings.widgetList.append(tag2)
    tag2["state"] = "readonly"

    tag3 = ttk.Combobox(values = tagList)
    tag3.set("Select a Tag")
    tag3.place(relx=.50, rely=.45,anchor= CENTER)
    settings.widgetList.append(tag3)
    tag3["state"] = "readonly"

    contButton = tk.Button(text="Submit",
                            fg = "black",
                            bg = "pink",
                            font = ("Segoe UI",10),
                            command = lambda: submitAccount(usernameEntry.get(), passwordEntry.get(), nameEntry.get()))
    contButton.place(relx=.50, rely=.5,anchor= CENTER)
    settings.widgetList.append(contButton)

    username = usernameEntry.get()
    password = passwordEntry.get()
    name = nameEntry.get()

    return account_created

def validate_entry(entry):
    return len(entry) > 0

def validate_name_len(entry):
    return (12>=len(entry) >=3)

def validate_username_len(entry):
    return (8>=len(entry)>=2)

def validate_password_len(entry):
    return (10>=len(entry)>=4)

def submitAccount(username, password, name):
    global conn

    # Connect to the database
    conn = sqlite3.connect("userDetails.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE user_id=?", (username,))
    existing_user = cursor.fetchone()
    if not (validate_entry(username) and validate_entry(password) and validate_entry(name)):
    # Display an error message if any of the required fields are empty
        error_label = tk.Label(text="Please fill in all required fields",
                            fg="red",
                            bg="pink",
                            font=("Segoe UI", 12))
        error_label.place(relx=.5, rely=.55, anchor=CENTER)
        settings.widgetList.append(error_label)
    else:    
        # Connect to the database
        conn = sqlite3.connect("userDetails.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE user_id=?", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            existing = tk.Label(text="                      This username already exists. Please choose another one or login                      ",
                            fg="red",
                            bg="pink",
                            font=("Segoe UI", 12))
            existing.place(relx=.5, rely=.6, anchor=CENTER)
            settings.widgetList.append(existing)

        elif not validate_name_len(name):
            namelen = tk.Label(text="                      Name must be between 3 and 12 characters.                      ",
                fg="red",
                bg="pink",
                font=("Segoe UI", 12))
            namelen.place(relx=.5, rely=.6, anchor=CENTER)
            settings.widgetList.append(namelen)
            
        elif not validate_username_len(username):
            userlength = tk.Label(text="                      Username must be between 2 and 8 characters.                      ",
                fg="red",
                bg="pink",
                font=("Segoe UI", 12))
            userlength.place(relx=.5, rely=.6, anchor=CENTER)
            settings.widgetList.append(userlength)

        elif not validate_password_len(password):
            plength = tk.Label(text="                      Password must be between 4 and 10 characters.                      ",
                fg="red",
                bg="pink",
                font=("Segoe UI", 12))
            plength.place(relx=.5, rely=.6, anchor=CENTER)
            settings.widgetList.append(plength)
        else:
            # Insert the new user into the database
            cursor.execute("INSERT INTO users (user_id, password, currency, name) VALUES (?, ?, ?, ?)", (username, password, 0, name))
            conn.commit()
            cursor.execute('SELECT currency FROM users WHERE user_id=?', (username,))
            settings.currency = cursor.fetchone()

            # Set the account_created variable to True
            account_created = True
    
            if account_created == True:    
                settings.clearScreen(settings.widgetList)
                todoScreen.questScreen(settings.currency)
                taskBar.taskbar(settings.currency)
            # Close the database connection
    conn.close()

def loginToAccount(password, username):

    logged_in = False

    global conn

    # Connect to the database
    conn = sqlite3.connect("userDetails.db")
    cursor = conn.cursor()

    if not (validate_entry(password)):
    # Display an error message if any of the required fields are empty
        error_label = tk.Label(text="Please fill the required field",
                            fg="red",
                            bg="pink",
                            font=("Segoe UI", 12))
        error_label.place(relx=.5, rely=.55, anchor=CENTER)
        settings.widgetList.append(error_label)
    else:    
        # Connect to the database
        conn = sqlite3.connect("userDetails.db")
        cursor = conn.cursor()

        cursor.execute('SELECT password FROM users WHERE user_id=?', (username))
        correctPass = cursor.fetchone()

        if correctPass and correctPass[0] == password:
            # Set the account_created variable to True
            logged_in = True
            cursor.execute('SELECT currency FROM users WHERE user_id=?', (username))
            settings.currency = cursor.fetchone()

            cursor.execute('SELECT name from users WHERE user_id=?', (username))
            name = cursor.fetchone()

            if logged_in == True:    
                settings.clearScreen(settings.widgetList)
                todoScreen.questScreen(settings.currency)
                taskBar.taskbar(settings.currency)
        else:
            incorrect = tk.Label(text="This password is incorrect",
                            fg="red",
                            bg="pink",
                            font=("Segoe UI", 12))
            incorrect.place(relx=.5, rely=.55, anchor=CENTER)
            settings.widgetList.append(incorrect)
            # Close the database connection
    conn.close()

            
def login(user_id):

    conn = sqlite3.connect("userDetails.db")
    cursor = conn.cursor()

    cursor.execute('SELECT name FROM users WHERE user_id=?', (user_id))
    name = cursor.fetchone()    

    name = str(name).replace('(', '').replace("'", '').replace(',', '').replace(')', '')

    displayName = tk.Label(text=f"Welcome back, {name}!",
                           fg="black",
                           bg="pink",
                           font=("Segoe UI Black", 25))
    displayName.place(relx=.5, rely=0.3,anchor=CENTER)
    settings.widgetList.append(displayName)

    loginHeader = tk.Label(text="Login",
                fg = "black",
                bg = "pink",
                font = ("BubbleGum",24))
    loginHeader.place(relx=.5, rely=.05,anchor= CENTER)
    settings.widgetList.append(loginHeader)

    username = tk.Label(text=user_id,
                    fg = "black",
                    bg = "pink",
                    font = ("Segoe UI",12))
    username.place(relx=.30, rely=.15, anchor=CENTER)
    settings.widgetList.append(username)

    password = tk.Label(text="Password:",
                    fg = "black",
                    bg = "pink",
                    font = ("Segoe UI",12))
    password.place(relx=.30, rely=.2, anchor=CENTER)
    settings.widgetList.append(password)

    passwordEntry = tk.Entry(show="*")
    settings.widgetList.append(passwordEntry)
    passwordEntry.place(relx=.50, rely=.2,anchor= CENTER)

    contButton = tk.Button(text="Submit",
                        fg = "black",
                        bg = "pink",
                        font = ("Segoe UI",10),
                        command = lambda: loginToAccount(passwordEntry.get(), user_id))
    contButton.place(relx=.50, rely=.5,anchor= CENTER)
    settings.widgetList.append(contButton)

    conn.close()

