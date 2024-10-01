
def rounded_avg(n, m):
    if m < n:
        return -1

    total_numbers = m - n + 1
    average = (n + m) * total_numbers // 2
    return bin(average)
