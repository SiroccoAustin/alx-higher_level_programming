#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    while i < len(matrix):
        j = 0
        for j in matrix[i]:
            print("{:d}".format(j), end=" ")
            j+= 1
        print("\n")
        i += 1
