def largest_smallest_integers(lst):
    largest = max(filter(lambda x: x < 0, lst), default=None)
    smallest = min(filter(lambda x: x > 0, lst), default=None)
    return (largest, smallest)
