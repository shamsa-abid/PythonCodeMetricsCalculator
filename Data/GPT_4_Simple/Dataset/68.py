def pluck(arr):
    lowest_even = -1
    lowest_index = -1
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and (lowest_even == -1 or arr[i] < lowest_even):
            lowest_even = arr[i]
            lowest_index = i
    if lowest_even == -1:
        return []
    else:
        return [lowest_even, lowest_index]
