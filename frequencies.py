"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    dict = {}
    for i in range(len(items)):
        dict[str(items[i])] = dict.get(str(items[i]),0) + 1
    return frequencies