#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_my_list = my_list[:]
    if idx < 0 or idx > (len(new_my_list) - 1):
        return(new_my_list)
    else:
        new_my_list[idx] = element
        return(new_my_list)
    return(my_list)
