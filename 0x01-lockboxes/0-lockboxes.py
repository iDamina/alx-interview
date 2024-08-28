#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    """
    n = len(boxes)
    unlocked = {0}  # Start with box 0 unlocked
    keys = list(boxes[0])  # Start with the keys from box 0

    while keys:
        key = keys.pop()  # Explore the latest key
        if key < n and key not in unlocked:  # If it's valid key for unlocked
            unlocked.add(key)  # Unlock the box
            keys.extend(boxes[key])  # Add the keys found in box to explore

    # If all boxes from 0 to n-1 are unlocked
    return len(unlocked) == n
