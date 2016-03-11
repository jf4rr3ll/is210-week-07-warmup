#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 Module"""

from decimal import Decimal


def lexicographics(to_analyze):
    """ Defines a function that determines the maximum, minimum, and
    average number of words per line.

    Args:
    to_analyze (mixed): Text to be analyzed

    Returns:
        max (int): The maximum number of words per line
        min (int): The minimum number of words per line
        average (decimal): The average number of words per line, as a decimal

    Examples:
        >>> import task_03
        >>> task_03.lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal(4.0))
    """

    text = []

    for line in to_analyze.split("\n"):
        text.append(len(line.split()))

    return (max(text), min(text), Decimal(sum(text))/Decimal(len(text)))
