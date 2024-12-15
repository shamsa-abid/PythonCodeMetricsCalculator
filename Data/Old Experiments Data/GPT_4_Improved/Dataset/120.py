from heapq import nlargest


def maximum(arr, k):
    return sorted(nlargest(k, arr))
