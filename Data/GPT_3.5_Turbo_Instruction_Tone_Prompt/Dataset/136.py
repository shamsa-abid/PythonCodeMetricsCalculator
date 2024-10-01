def largest_smallest_integers(lst):
    negatives = [num for num in lst if num < 0]
    positives = [num for num in lst if num > 0]

    if negatives:
        largest_negative = max(negatives)
    else:
        largest_negative = None

    if positives:
        smallest_positive = min(positives)
    else:
        smallest_positive = None

    return (largest_negative, smallest_positive)
