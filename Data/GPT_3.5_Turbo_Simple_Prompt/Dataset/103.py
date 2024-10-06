def rounded_avg(n, m):
    if n > m:
        return -1

    avg = round(sum(range(n, m+1)) / (m - n + 1))
    return bin(avg)


# Test cases
print(rounded_avg(1, 5))  # Output: 0b11
print(rounded_avg(7, 5))  # Output: -1
print(rounded_avg(10, 20))  # Output: 0b1111
print(rounded_avg(20, 33))  # Output: 0b11010
