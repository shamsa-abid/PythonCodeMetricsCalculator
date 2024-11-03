def prime_length(string):
    from math import sqrt
    l = len(string)
    if l < 2:
        return False
    for i in range(2, int(sqrt(l)) + 1):
        if l % i == 0:
            return False
    return True
