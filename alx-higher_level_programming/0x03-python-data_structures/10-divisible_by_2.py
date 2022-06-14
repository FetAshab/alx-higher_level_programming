#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiples_of_two = my_list[:]
    for i in range(len(multiples_of_two)):
        if multiples_of_two[i] % 2 == 0:
            multiples_of_two[i] = True
        else:
            multiples_of_two[i] = False
    return multiples_of_two
