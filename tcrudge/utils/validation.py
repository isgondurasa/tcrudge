"""
Module for common validation tools.
"""


def validate_integer(val, min_value=None, max_value=None, default=None):
    """
    Validates the input val parameter.

    If it is can not be converted to integer, returns default_value.
    If it is less than min_value, returns min_value.
    If it is greater than max_value, returns max_value.

    :param val: number to validate
    :type val: int, float, digital string

    :param min_value: int
    :type min_value: int

    :param max_value: int
    :type max_value: int

    :param default: int
    :type default: int

    :return: In case of exception None, otherwise - given min, max, default
    or result - int.
    :rtype: NoneType, int
    """
    try:
        result = int(val)  # TODO - check for non int in values
    except (TypeError, ValueError):
        return default
    if min_value is not None and result < min_value:
        result = min_value
    if max_value is not None and result > max_value:
        result = max_value
    return result
