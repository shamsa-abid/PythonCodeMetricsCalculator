def sort_array(array):
    if len(array) == 0:
        return []
    else:
        is_even = (array[0] + array[-1]) % 2 == 0
        return sorted(array, reverse=is_even)
