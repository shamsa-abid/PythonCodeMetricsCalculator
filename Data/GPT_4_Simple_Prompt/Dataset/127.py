def intersection(interval1, interval2):
    # identifying the intersection
    n = max(min(interval1[1], interval2[1]) -
            max(interval1[0], interval2[0]), 0)

    # determine if n is prime
    if n < 2:
        return "NO"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "NO"
    return "YES"
