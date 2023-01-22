#!/usr/bin/python3
"""
0-minoperations
"""


def minOperations(n: int) -> int:
    """
    finds minimum  number of copy all and paste print n Hs in a file
    """
    ops = 0
    if not isinstance(n, int) or n <= 1:
        return 0
    for i in range(2, n + 1):
        """ """
        while n % i == 0:
            n = n / i
            ops += i
    return ops
