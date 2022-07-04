#!/usr/bin/python3
""" class MyList """


class MyList(list):
    """ class MyList that inherits from list """

    def __init__(self):
        """ initialize a Rectangle """
        super().__init__()

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        sort_list = self.copy()
        sort_list.sort()
        print(sort_list)
