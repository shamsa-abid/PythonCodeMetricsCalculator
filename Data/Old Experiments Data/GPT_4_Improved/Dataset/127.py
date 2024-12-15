def intersection(interval1, interval2):
    max_start = max(interval1[0], interval2[0])
    min_end = min(interval1[1], interval2[1])

    length = max(0, min_end - max_start)
    if length < 2:
        return "NO"
    else:
        for i in range(2, int(length ** 0.5) + 1):
            if length % i == 0:
                return "NO"
        return "YES"
