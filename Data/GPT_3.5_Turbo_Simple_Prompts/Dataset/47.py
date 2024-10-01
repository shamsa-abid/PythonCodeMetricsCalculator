def median(l: list):
    l.sort()
    n = len(l)

    if n % 2 == 0:
        mid1 = l[n//2]
        mid2 = l[n//2 - 1]
        median = (mid1 + mid2) / 2
    else:
        median = l[n//2]

    return median


# Test cases
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
