def sort_array(array):
    return [] if not array else sorted(array, reverse=(array[0]+array[-1]) % 2 == 0)
