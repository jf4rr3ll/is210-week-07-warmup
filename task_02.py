#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 Module"""


def bool_to_str(bval):
    """Determines if a value is truthy or falsy

    Args:
        bval (bool): A true or false value

    Returns:
        string: Either 'Yes' or 'No'

    Examples:
        >>> import task_02
        >>> task_02.bool_to_str(True)
        'Yes'

        >>> import task_02
        >>> task_02.bool_to_str('')
        'No'
    """

    if bval:
        answer = 'Yes'
    else:
        answer = 'No'

    return answer
