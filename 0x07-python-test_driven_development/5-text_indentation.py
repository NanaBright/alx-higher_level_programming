#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")  
    """ Raise an exception if text is not a string """

    """ Define the punctuation characters that trigger indentation """
    punctuation_chars = [".", "?", ":"]

    """ Loop through each character in the text """
    for char in text:
        """ Print the character, followed by two new lines if it's a punctuation character """
        if char in punctuation_chars:
            print(char + "\n\n")
        else:
            print(char, end="")  
            """ Print the character without a newline character """
