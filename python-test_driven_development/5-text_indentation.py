#!/usr/bin/python3
""" This prints a text with 2 new lines after each of these characters: ., ?
and : """


def text_indentation(text):
    """

    Prints a text with 2 new lines after each of the characters: ., ?, and :.

    Args:
        text (str): The text to be printed with the specified indentation.

    Raises:
        TypeError: If the provided text is not a string.
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    delimiters = ".?:"
    temp = ""

    for char in text:
        temp += char
        if char in delimiters:
            print(temp.strip())
            print()
            temp = ""

    if temp:
        print(temp.strip(), end="")
