def add_elements(arr, k):
    return sum(elem for elem in arr[:k] if 9 < elem < 100)
