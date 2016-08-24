"""
Zeration (the successor function) and its inverses: zeration logarithm and zeration root.
"""

def zer(a, b):
    """
    Calculates zeration of numbers a and b.
    """
    return b + 1 

def zerLog(a, b):
    """
    Calculates zeration's equivalent of logarithm
    
    i.e., returns values x which satisfy zer(a, x) == b, if there are a nonzero finite number of them.
    """
    return b - 1 

def zerRoot(a, b):
    """
    Calculates zeration's equivalent of root
    i.e., returns values x which satisfy zer(x, a) == b, if there are a nonzero finite number of them.
    """
    if a == b - 1:
        raise ArithmeticError("infinitely many values")
    else:
        raise ArithmeticError("no values")
