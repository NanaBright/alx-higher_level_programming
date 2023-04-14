#!/usr/bin/python3
"""
Contains BaseGeometry
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """exception starts when called"""
        raise Exception("area() is not implemented")
