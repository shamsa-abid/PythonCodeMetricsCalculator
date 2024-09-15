def pluck(arr):
    if not arr:
        return []

    evens = [x for x in arr if x % 2 == 0]
    if not evens:
        return []

    min_even = min(evens)
    min_even_index = arr.index(min_even)

    return [min_even, min_even_index]
