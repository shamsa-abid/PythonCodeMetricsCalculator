
def can_arrange(arr):
    largest_idx = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            largest_idx = i - 1
    return largest_idx
