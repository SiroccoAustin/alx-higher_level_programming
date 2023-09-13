#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    i = 0
    while len(matrix) > i:
        sub_array = []
        j = 0
        for j in matrix[i]:
            power = j ** 2
            sub_array.append(power)
            j += 1
        new_matrix.append(sub_array)
        i += 1
    return new_matrix
