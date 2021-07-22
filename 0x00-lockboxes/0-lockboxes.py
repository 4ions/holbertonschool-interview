#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def addKeys(keyInBox, keys):
    """ add keys to list """
    if 0 not in keys:
        keys.append(0)
    for box in keyInBox:
        if box not in keys:
            keys.append(box)
    keys.sort()
    return keys


def _canUnlockAll(boxes, keys, index):
    """ check each box to find keys """
    if index not in keys:
        return keys
    count = 0
    count2 = 0
    no_in_key = []
    for box in range(0, len(boxes)):
        if box in keys:
            keys = addKeys(boxes[box], keys)
        if box not in keys:
            no_in_key.append(box)
    for no in no_in_key:
        if no in keys:
            _canUnlockAll(boxes, keys, box)
    return keys


def canUnlockAll(boxes):
    """ function to unlock boxes with keys """
    if len(boxes) == 0:
        return False
    keys = []
    keys = addKeys(boxes[0], keys)
    count = _canUnlockAll(boxes, keys, 0)
    if len(keys) == len(boxes):
        return True
    else:
        return False
