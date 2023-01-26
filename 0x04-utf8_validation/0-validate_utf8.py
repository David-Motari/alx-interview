#!/usr/bin/python3
"""
A method that checks if a given data set represents a valid UTF-8
"""


def toBinary(integer):
    """
    A function that: converts an integer to its binary representation.
     """
    binary = bin(integer)[2:]
    add = '0' * (8 - len(binary))
    return add + binary

def validUTF8(data):
    """
    function that checks if a given data set represents a valid UTF-8
    and returns an boolean
    """
    i = 0
    while i < len(data):
        if toBinary(data[i])[0] == '0':
            i += 1
        elif (toBinary(data[i])[:3] == '110' and i + 1 < len(data) and
                toBinary(data[i + 1])[:2] == '10'):
            i += 2
        elif (toBinary(data[i])[:4] == '1110' and i + 2 < len(data) and
                toBinary(data[i + 1])[:2] == '10' and
                toBinary(data[i + 1])[:2] == '10'):
            i += 3
        elif (toBinary(data[i])[:5] == '11110' and i + 3 < len(data) and
                toBinary(data[i + 1])[:2] == '10' and
                toBinary(data[i + 2])[:2] == '10' and
                toBinary(data[i + 3])[:2] == '10'):
            i += 4
        else:
            return False
    return True