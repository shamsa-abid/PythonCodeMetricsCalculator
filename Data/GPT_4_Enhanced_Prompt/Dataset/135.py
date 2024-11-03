def can_arrange(arr):
    return next((i for i in range(1, len(arr)) if arr[i] < arr[i-1]), -1)
