#!/usr/bin/python3
'''
Module: '0-lockboxes'
'''


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    allKeys = [0]
    for key in allKeys:
        for newKey in boxes[key]:
            if newKey not in allKeys and newKey < len(boxes):
                allKeys.append(newKey)

    return len(allKeys) == len(boxes)
