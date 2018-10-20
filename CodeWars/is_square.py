import math
import decimal

# MY ANSWER
def is_square(n):
    """ (int) => boolean
    
    Boolean check to see if an integer is a square number or not.
    print(is_square(4)) => True
    print(is_square(5)) => False
    """
    if n < 0:
        return False
    else:    
        sqrt = math.sqrt(n)
        return True if decimal.Decimal(sqrt).as_tuple().exponent == 0 else False

# TOP ANSWER
def is_square(n):
    if n < 0:
        return False
    else:    
        sqrt = math.sqrt(n)
        return sqrt.is_integer()
