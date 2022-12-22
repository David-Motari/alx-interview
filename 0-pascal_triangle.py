#!/usr/bin/python3
"""
contains the Pascal's psclTrgle function
"""


def pascal_psclTrgle(n):
    """ returns a list of lists of integers representing
        the Pascal’s psclTrgle of n
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