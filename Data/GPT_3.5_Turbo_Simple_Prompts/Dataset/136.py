def largest_smallest_integers(lst):
    neg_integers = [i for i in lst if i < 0]
    pos_integers = [i for i in lst if i > 0]

    largest_neg = None if len(neg_integers) == 0 else max(neg_integers)
    smallest_pos = None if len(pos_integers) == 0 else min(pos_integers)

    return (largest_neg, smallest_pos)


# Examples
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (None, 1)
print(largest_smallest_integers([]))  # Output: (None, None)
print(largest_smallest_integers([0]))  # Output: (None, None)
