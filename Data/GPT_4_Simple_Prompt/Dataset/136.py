def largest_smallest_integers(lst):

    if not lst:
        return (None, None)

    negative_nums = [num for num in lst if num < 0]
    positive_nums = [num for num in lst if num > 0]

    largest_negative = max(negative_nums) if negative_nums else None
    smallest_positive = min(positive_nums) if positive_nums else None

    return (largest_negative, smallest_positive)
