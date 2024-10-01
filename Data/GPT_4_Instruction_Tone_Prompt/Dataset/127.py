import math


def intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    length = max(0, end - start)
    if length <= 1:
        return "NO"
    if length > 2 and length % 2 == 0:
        return "NO"
    for i in range(3, int(math.sqrt(length)) + 1, 2):
        if length % i == 0:
            return "NO"
    return "YES"
