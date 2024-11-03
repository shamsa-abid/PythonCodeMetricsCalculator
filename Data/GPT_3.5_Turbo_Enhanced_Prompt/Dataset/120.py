def maximum(arr, k):
    if k == 0:
        return []

    ans = sorted(arr)[-k:]
    return ans
