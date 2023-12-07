#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """This method determines if allboxes can be opened"""

    bunch_of_keys = list(range(1, len(boxes)))

    for key in bunch_of_keys:
        found = False

        for idx, box in enumerate(boxes):
            if idx == key:
                continue
            if key in box:
                found = True
                break
            if not found:
                return False

    return True
