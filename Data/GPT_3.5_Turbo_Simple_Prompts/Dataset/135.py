def can_arrange(arr):
    max_index = -1

    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            max_index = i - 1

    return max_index


# Test cases
print(can_arrange([1, 2, 4, 3, 5]))  # Output should be 3
print(can_arrange([1, 2, 3]))  # Output should be -1
