#!/usr/bin/python3

"""This is the test for the console"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """this is class test console"""

    def create(self):
        """this create the intance"""
        return HBNBCommand()

    def test_quit(self):
        """ this is the test for the method quit
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """this is the test for the method EOF
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
