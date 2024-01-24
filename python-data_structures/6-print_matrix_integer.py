#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for number in matrix[i]:
            print("{:d}".format(number), end="")
        print()
