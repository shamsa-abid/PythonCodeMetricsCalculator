def pluck(arr):
    if len(arr) == 0:
        return []

    evens = [x for x in arr if x % 2 == 0]
    if not evens:
        return []

    min_even = min(evens)
    index = arr.index(min_even)

    return [min_even, index]
