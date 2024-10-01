def can_arrange(arr):
    previous_element = arr[0]
    largest_index = -1

    for i in range(1, len(arr)):
        if arr[i] < previous_element:
            largest_index = i
        previous_element = max(previous_element, arr[i])

    return largest_index
