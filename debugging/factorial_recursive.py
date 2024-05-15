#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number.

    Function Description:
    ----------------------
    This function calculates the factorial of a non-negative integer. The factorial of a number n, denoted by n!, 
    is the product of all positive integers less than or equal to n.

    Parameters:
    -----------
    n : int
        The number for which the factorial is to be calculated. It must be a non-negative integer.

    Returns:
    --------
    int
        The factorial of the given number. If the input is 0, the function returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
