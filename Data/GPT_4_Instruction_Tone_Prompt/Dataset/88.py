def sort_array(array):
    if not array:
        return array
    else:
        sum_ends = array[0] + array[-1]
        if sum_ends % 2 == 0:
            array = sorted(array, reverse=True)
        else:
            array = sorted(array)
        return array
