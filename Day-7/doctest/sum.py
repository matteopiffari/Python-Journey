import doctest
def sum(a, b):
    """
    Some desc

    :param a: int: First number
    :param b: int: Second number
    :return: int: Sum of a and b

    >>> sum(1, 2)
    3
    >>> sum(-1, 1)
    0
    """
   
    return a + b

print(doctest.testmod())