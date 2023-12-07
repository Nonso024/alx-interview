#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """This method determines if allboxes can be opened"""

    bunch_of_keys = list(range(1, len(boxes)))

    for key in bunch_of_keys:
        found = False
        
        for idx, box in enumerate(boxes):
            if key === idx:
                continue
            if key in box:
                found = True
