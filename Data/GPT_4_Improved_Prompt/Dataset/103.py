def rounded_avg(n, m):
    if m < n:
        return -1
    summation = (m*(m+1)/2) - (n*(n-1)/2)
    return bin(round(summation / (m-n+1)))
