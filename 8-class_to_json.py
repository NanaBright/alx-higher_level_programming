#!/usr/bin/python3
"""Contains the "class_to_json" function"""


def class_to_json(obj):
    """Return the dictionary display of a data structure."""
    return obj.__dict__
