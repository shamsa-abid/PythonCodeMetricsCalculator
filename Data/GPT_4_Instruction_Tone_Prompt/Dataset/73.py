def smallest_change(arr):
    # calculate the number of changes required
    changes = sum(arr[i] != arr[-i-1] for i in range(len(arr) // 2))

    return changes
