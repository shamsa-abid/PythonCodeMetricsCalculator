def fruit_distribution(s, n):
    apples, oranges = [int(i) for i in s.split() if i.isdigit()]
    return n - apples - oranges