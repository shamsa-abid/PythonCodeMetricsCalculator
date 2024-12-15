def median(l: list):
    l.sort()
    n = len(l)
    mid = n // 2
    return (l[mid] + l[~mid]) / 2.0 if n % 2 == 0 else l[mid]


# Test Cases
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 8.0
print(median([5]))  # Output: 5
print(median([6, 5]))  # Output: 5.5
print(median([8, 1, 3, 9, 9, 2, 7]))  # Output: 7
