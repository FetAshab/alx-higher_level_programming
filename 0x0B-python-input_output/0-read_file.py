#!/usr/bin/python3
""" reads a text file """


def read_file(filename=""):
    """ function that reads a text file and prints it to stdout """
    with open(filename, encoding="UTF8") as myFile:
        print(myFile.read(), end="")
