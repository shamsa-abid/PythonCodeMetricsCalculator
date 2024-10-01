def fruit_distribution(s, n):
    total_fruits = n
    fruits = s.split()
    for f in fruits:
        if f.isdigit():
            total_fruits -= int(f)
    return total_fruits
