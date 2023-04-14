#!/usr/bin/python3
""" Contains a function write_file """


def number_of_lines(filename=""):
    """ Function that reads from a file and prints its number of lines nod"""
    nod = 0
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            nod += 1
    return nod
