def largest_smallest_integers(lst):
    smallest, largest = None, None

    # Find the smallest positive and largest negative number in one loop
    for i in lst:
        if i < 0:
            if smallest is None or smallest < i:
                smallest = i

        elif i > 0:
            if largest is None or largest > i:
                largest = i

    return smallest, largest
