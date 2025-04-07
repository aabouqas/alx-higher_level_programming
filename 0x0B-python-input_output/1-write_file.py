#!/usr/bin/python3
""" Defining write file function """


def write_file(filename="", text=""):
    """ call open functions to open the file"""
    with open(filename, "w", encoding="utf-8") as file:
        count = file.write(text)
        return count
