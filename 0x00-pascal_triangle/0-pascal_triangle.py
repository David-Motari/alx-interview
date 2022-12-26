#!/usr/bin/python3
"""
contains the Pascal's triangle function
"""


def pascal_triangle(n):
    """
    returns pascal triangle
    """
    psclTrgle = []
    for i in range(1, n+1):
        row = []
        for j in range(i):
            if j == 0 or j == i-1:
                n = 1
                row.append(n)
            else:
                n = psclTrgle[i-2][j-1] + psclTrgle[i-2][j]
                row.append(n)
        psclTrgle.append(row)

    return psclTrgle
