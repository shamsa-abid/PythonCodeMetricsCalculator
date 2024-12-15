def cycpattern_check(a, b):
    import re

    # Make a pattern to match with 'b' and its cyclic rotations joined the result with '|'
    # This '|' acts as 'OR' condition in regular expressions
    pattern = '|'.join([b[i:] + b[:i] for i in range(len(b))])

    # Check if 'pattern' is a substring of 'a'
    if re.search(pattern, a):
        return True

    # When 'pattern' is not a substring of 'a'
    return False
