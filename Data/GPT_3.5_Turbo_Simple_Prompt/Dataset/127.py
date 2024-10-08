def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2

    intersect_start = max(start1, start2)
    intersect_end = min(end1, end2)

    if intersect_start > intersect_end:
        return "NO"

    length = intersect_end - intersect_start + 1

    if is_prime(length):
        return "YES"
    else:
        return "NO"


# Test Cases
print(intersection((1, 2), (2, 3)))  # Output: "NO"
print(intersection((-1, 1), (0, 4)))  # Output: "NO"
print(intersection((-3, -1), (-5, 5)))  # Output: "YES"
