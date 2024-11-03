def add_elements(arr, k):
    total = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            total += arr[i]
    return total
