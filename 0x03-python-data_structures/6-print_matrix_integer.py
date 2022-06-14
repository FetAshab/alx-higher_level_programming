#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        print(" ".join("{:d}".format(b) for b in a))
