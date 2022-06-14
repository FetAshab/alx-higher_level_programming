#!/usr/bin/python3
def no_c(my_string):
    a = ""
    for string in my_string:
        if string != "c" and string != "C":
            a += string
    return (a)
