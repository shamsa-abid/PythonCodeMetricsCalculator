def sort_array(arr):
    return sorted(arr, key=lambda n: (bin(n).count('1'), n))
