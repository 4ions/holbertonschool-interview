#!/usr/bin/python3
""" Module of lock boxes """


def addKeys(keyInBox, keys):
    """ add keys to list """
    if 0 not in keys:
        keys.append(0)
    for box in keyInBox:
        if box not in keys:
            keys.append(box)
    keys.sort()
    return keys


def canUnlockAll(boxes):
    """
    unlock boxes
    """
    keys = []
    keys = addKeys(boxes[0], keys)
    count = 0
    for box in range(0, len(boxes)):
        if box in keys:
            keys = addKeys(boxes[box], keys)
            count = count + 1
    if count == len(boxes):
        return True
    else:
        return False
