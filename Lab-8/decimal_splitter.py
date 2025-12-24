from decimal import Decimal

class DecimalSplitter:
    """
    Method to get the whole number from a double
    """
    def get_whole(number):
        d=Decimal(str(number)) #preserves all the decimals 
        return int(d)

    """
    Method to get the fractional part of a double number
    """
    def get_fraction(number):
        d=Decimal(str(number))
        return d-int(d)

    """
    Method to check if a given number is odd or even
    """
    def is_odd(number):
        if number&1==0:
            return True
        else:
            return False
