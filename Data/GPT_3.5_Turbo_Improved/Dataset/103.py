def rounded_avg(n, m):
    if m < n:
        return -1

    total = (n + m) * (m - n + 1) // 2
    return bin(total // (m - n + 1))
