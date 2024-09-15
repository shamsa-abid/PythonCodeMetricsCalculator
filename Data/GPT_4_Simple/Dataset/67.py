def fruit_distribution(s, n):
    split_str = s.split()
    apples = split_str[0]
    oranges = split_str[3]
    mango = n - int(apples) - int(oranges)
    return mango
