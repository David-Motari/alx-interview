#!/usr/bin/python3
"""
0-nqueen
"""
from sys import argv


class NQueen:
    """Class Queens"""

    def __init__(self, n):
        """
        Initialization of class properties
        """
        self.n = n
        self.x = [0 for i in range(n + 1)]
        self.point = []

    def is_secure(self, k, i):
        """Check if a secure place"""

        for j in range(1, k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return 0
        return 1

    def nQueen(self, k):
        """
        Solution for placing n queens in chess board
        """
        for i in range(1, self.n + 1):
            if self.is_secure(k, i):
                self.x[k] = i
                if k == self.n:
                    solution = []
                    for i in range(1, self.n + 1):
                        solution.append([i - 1, self.x[i] - 1])
                    self.point.append(solution)
                else:
                    self.nQueen(k + 1)
        return self.point


def validate():
    """
    validation for N
    """
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    N = argv[1]

    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)


if __name__ == "__main__":
    """
    program call
    """
    validate()
    queen = NQueen(int(argv[1]))
    board = queen.nQueen(1)

    for i in board:
        print(i)
