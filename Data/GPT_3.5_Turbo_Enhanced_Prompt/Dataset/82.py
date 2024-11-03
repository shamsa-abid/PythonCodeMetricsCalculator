
import math


def prime_length(string):
    l = len(string)

    if l < 2:
        return False

    if l == 2:
        return True

    if l % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(l)) + 1, 2):
        if l % i == 0:
            return False

    return True
