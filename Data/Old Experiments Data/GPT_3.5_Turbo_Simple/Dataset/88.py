def sort_array(array):
    temp_array = array.copy()
    if (temp_array[0] + temp_array[-1]) % 2 == 0:
        return sorted(temp_array, reverse=True)
    else:
        return sorted(temp_array)
