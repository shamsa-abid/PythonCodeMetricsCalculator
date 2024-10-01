def largest_smallest_integers(lst):
    smallest = min((x for x in lst if x > 0), default=None)
    largest = max((x for x in lst if x < 0), default=None)
    return (largest, smallest)
