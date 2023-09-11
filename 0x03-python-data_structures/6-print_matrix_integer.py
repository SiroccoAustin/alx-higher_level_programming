#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
i = 0
while i < len(matrix):
    j = 0
    for j in matrix[i]:
        print(j, end=" ")
        j+= 1
    print("\n")
    i += 1
