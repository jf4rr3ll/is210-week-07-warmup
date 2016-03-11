#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 Module"""


def fibonacci(maxint):
    """A function that returns a fibonacci sequence

    Args:
        maxint (int): the integer serving as the upper bound of the loop

    Returns:
        list: fibonacci sequence

    Examples:
        >>> import task_01
        >>> task_01.fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
    """

    fib_sequence = [0]
    lastnum, curnum = 0, 1
    while curnum < maxint:
        fib_sequence.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum

    return fib_sequence
