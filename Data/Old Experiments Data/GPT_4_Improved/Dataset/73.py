def smallest_change(arr):
    return sum(el1 != el2 for el1, el2 in zip(arr, arr[::-1])) // 2
