#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return(None)

    Biggest = my_list[0]
    for the_num in range(len(my_list)):
        if my_list[the_num] > Biggest:
            Biggest = my_list[the_num]
    return(Biggest)
