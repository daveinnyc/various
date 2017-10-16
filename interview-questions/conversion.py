'''

Task: Convert a non-negative integer to a hex value for printing


Copyright 2017, Dave Cuthbert. License MIT
'''


def int_to_hex(number):
    """
    Check 0 
    >>> int_to_hex(0)
    '0'

    Value less than 10
    >>> int_to_hex(9)
    '9'

    Value requiring letter digits
    >>> int_to_hex(15)
    'F'

    Boundary (Uses 10s place)
    >>> int_to_hex(16)
    '10'

    Boundary (Uses 10s, and 1s places)
    >>> int_to_hex(17)
    '11'

    Multiple 16ths
    >>> int_to_hex(129)
    '81'

    Boundary (Uses 100s, 10s, and 1s places)
    >>> int_to_hex(301)
    '12D'
    """
    hex_string = ''
    hex_digits = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    
    if number == 0:
        hex_string += str(0)
    else:
        while number > 0:
            digit = number % 16
            hex_string += str(hex_digits[digit])
            number = int(number / 16)

    return hex_string[::-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    


