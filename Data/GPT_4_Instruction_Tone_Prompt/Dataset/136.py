def largest_smallest_integers(lst):
    largest_negative = max(filter(lambda n: n < 0, lst), default=None)
    smallest_positive = min(filter(lambda n: n > 0, lst), default=None)
    return largest_negative, smallest_positive
