import unittest

import tkinter as tk

from accountScreens import validate_name_len, validate_password_len, validate_username_len
from tkinter import *
from tkinter import ttk

#Tests for account creation validation

class testAccountCreation(unittest.TestCase):
    #2 pass test for name right length, name with alphanumerics
    def test_ValidateNameLenPass(self):
        name = "Barry"

        result = validate_name_len(name)
        self.assertEqual(result, True)

    def test_ValidateNameLenPassAlphanumeric(self):
        name = "Bliss 12"

        result = validate_name_len(name)
        self.assertEqual(result, True)

    #3 fail cases for name too short, too long, and empty
    def test_ValidateNameLenFailShort(self):
        name = "Fi"

        result = validate_name_len(name)
        self.assertEqual(result, True)

    def test_ValidateNameLenFailBlank(self):

        name = ""

        result = validate_name_len(name)
        self.assertEqual(result, True)

    def test_ValidateNameLenFailLong(self):
        name = "This is a reallllly long name."

        result = validate_name_len(name)
        self.assertEqual(result, True)

###############################################################
    #1 pass test for user name right lenght and alphanumeric
    def test_ValidateUsernameLenPass(self):
        name = "CianB23"

        result = validate_username_len(name)
        self.assertEqual(result, True)

    #3Fail test for username entry too short, too long, empty
    def test_ValidateUsernameLenFailShort(self):
        name = "B"

        result = validate_username_len(name)
        self.assertEqual(result, True)

    def test_ValidateUsernameLenFailBlank(self):
        name = ""

        result = validate_username_len(name)
        self.assertEqual(result, True)

    def test_ValidateUsernameLenFailLong(self):
        name = "Bodyodyodyodyodyodyodyoydy"

        result = validate_username_len(name)
        self.assertEqual(result, True)

##############################################################
    #1 pass test for password
    def test_ValidatePasswordLenPass(self):
        password = "SafeS0und"

        result = validate_username_len(password)
        self.assertEqual(result, True)

    #3 fail test for password
    def test_ValidatePasswordLenFailLong(self):
        password = "SafeS0undlySleeping"

        result = validate_username_len(password)
        self.assertEqual(result, True)

    def test_ValidatePasswordLenFailBlank(self):
        password = ""

        result = validate_username_len(password)
        self.assertEqual(result, True)

    def test_ValidatePasswordLenFailShort(self):
        password = "Tomb"

        result = validate_username_len(password)
        self.assertEqual(result, True)

    pass