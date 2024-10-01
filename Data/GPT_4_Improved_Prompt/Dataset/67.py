def fruit_distribution(s, n):
    fruit_count = sum([int(num) for num in s.split(' ') if num.isdigit()])
    return n - fruit_count
