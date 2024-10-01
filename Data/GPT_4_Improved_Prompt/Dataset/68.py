def pluck(arr):
    even_min_index = -1
    even_min_value = float('inf')
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < even_min_value:
            even_min_value = arr[i]
            even_min_index = i
    return [even_min_value, even_min_index] if even_min_index != -1 else []
