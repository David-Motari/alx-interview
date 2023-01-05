#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    a function to establish if all the boxes can be opened
    """
    if not boxes:
        return False

    tracker = {}
    counter = 0

    for box in boxes:
        if len(box) == 0 or counter == 0:
            tracker[counter] = -1
        for key in box:
            if key < len(boxes) and key != counter:
                tracker[key] = key
        if len(tracker) == len(boxes):
            return True
        counter += 1
    return False
