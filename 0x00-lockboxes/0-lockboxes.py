#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def _canUnlockAll(boxes, keys):
    """ check each box to find keys """
    no_in_key = []
    for box in range(0, len(boxes)):
        if box in keys:
            for key in boxes[box]:
                if key not in keys and key < len(boxes):
                    keys.append(key)
        if box not in keys:
            no_in_key.append(box)
    for no in no_in_key:
        if no in keys:
            keys = _canUnlockAll(boxes, keys)
    return keys


def canUnlockAll(boxes):
    """ function to unlock boxes with keys """
    if len(boxes) == 0:
        return False
    if type(boxes) is not list:
        return False
    keys = [0]
    keys = addKeys(boxes[0], keys)
    keys = _canUnlockAll(boxes, keys)
    if len(keys) - 1 == len(boxes) - 1:
        return True
    else:
        return False
