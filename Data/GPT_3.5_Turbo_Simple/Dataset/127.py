def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)

    if intersection_end < intersection_start:
        return "NO"

    intersection_length = intersection_end - intersection_start

    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"
