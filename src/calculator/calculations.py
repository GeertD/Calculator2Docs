# calculator/calculations.py

"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0
"""

def add(a, b=5.0):
    """Compute and return the sum of two numbers, Hidy.
    
    Args:
        a (float): A number to be added first.
        b (float): A number to be added second.
    
    Returns:
        (float): A number representing the sum of `a` and `b`.
        
    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0
        
    Notes:
        Some extra explanation here about this method.
    """
    return float(a + b)

def subtract(a, b):
    """Compute and return the difference between two numbers.
    
    Args:
        a (float): A number to subtract from.
        b (float): A number that will be subtracted.
    
    Returns:
        (float): A number representing the difference of `a` and `b`.
        
    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(16, 5)
        11.0
    """
    return float(a - b)

def multiply(a, b):
    """Compute and return the product of two numbers.
    
    Args:
        a (float): The first factor.
        b (float): The second factor.
    
    Returns:
        (float): A number representing the product of `a` and `b`.
        
    Examples:  
        >>> multiply(10.0, 5.0)
        50.0
        >>> multiply(2, 3)
        6.0
    """
    return float(a * b)

def divide(a, b):
    """Compute and return the division of two numbers.
    
    Args:
        a (float): The thing that will be divided.
        b (float): The divisor.
    
    Returns:
        (float): A number representing the quotient of `a` and `b`.
    
    Raises:
        (ZeroDivisionError): If b is zero.
        
    Examples:
        >>> divide(10.0, 2.0)
        5.0
        >>> divide(10, 0)
        ZeroDivisionError    
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)

def _internal_stuff():
    """Some internal function.
    No need to make this public.
    """