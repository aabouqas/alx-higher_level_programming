#!/usr/bin/python3
""" Defining read file function """


def read_file(filename=""):
    """ call open functions to open the file"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
