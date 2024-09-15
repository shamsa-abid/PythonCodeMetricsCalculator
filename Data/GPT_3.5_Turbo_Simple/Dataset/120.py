def maximum(arr, k):
    arr.sort()
    return arr[-k:] if k > 0 else []
