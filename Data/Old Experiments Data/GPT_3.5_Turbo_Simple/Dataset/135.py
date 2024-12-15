def can_arrange(arr):
    if not arr:
        return -1

    largest_index = -1
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            largest_index = i - 1

    return largest_index
