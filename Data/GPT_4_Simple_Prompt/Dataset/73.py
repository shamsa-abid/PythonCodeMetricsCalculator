def smallest_change(arr):
    n = len(arr)
    l = 0
    r = n - 1
    changes = 0

    # Checking for the palindromic property
    while l <= r:
        if arr[l] != arr[r]:
            changes += 1
        l += 1
        r -= 1
    return changes
