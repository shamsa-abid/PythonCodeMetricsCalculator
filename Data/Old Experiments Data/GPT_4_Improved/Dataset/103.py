def rounded_avg(n, m):
    if m < n:
        return -1
    avg = (m + n) // 2
    avg = round(avg)
    return bin(avg)
