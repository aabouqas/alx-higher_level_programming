#!/usr/bin/python3
""" Defining append file function """


def append_write(filename="", text=""):
    """ call open functions to open the file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
