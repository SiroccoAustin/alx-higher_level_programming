#!/usr/bin/python3

def matrix_divided(matrix, div):
    outerArray = []
    firstrow = len(matrix[0])
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if len(i) != firstrow:
            raise TypeError("Each row of the matrix must have the same size")
        innerArray = []
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            result = round(j / div, 2)
            innerArray.append(result)
        outerArray.append(innerArray)
    return outerArray
