def largest_smallest_integers(lst):
    pos_int = [i for i in lst if i > 0]
    neg_int = [i for i in lst if i < 0]

    largest_neg = max(neg_int) if neg_int else None
    smallest_pos = min(pos_int) if pos_int else None

    return (largest_neg, smallest_pos)
