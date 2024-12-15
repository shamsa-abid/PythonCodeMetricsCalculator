def sort_even(l: list):
    evens = sorted(l[::2])
    odds = l[1::2]
    return [val for pair in zip(evens, odds + [0]) for val in pair] if len(evens) > len(odds) else [val for pair in zip(evens + [0], odds) for val in pair][:-1]
