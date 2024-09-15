def sort_array(array):
    if not array:
        return []
    return sorted(array, reverse=not ((array[0]+array[-1]) % 2))
