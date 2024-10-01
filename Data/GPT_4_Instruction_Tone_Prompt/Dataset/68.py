def pluck(arr):
    even_numbers = [(x, i) for i, x in enumerate(arr) if x % 2 == 0]
    if even_numbers:
        return min(even_numbers, key=lambda x: (x[0], x[1]))
    else:
        return []
