def sort_third(l: list):
    indexes_divisible_by_three = [idx for idx in range(len(l)) if idx % 3 == 0]
    values_at_indexes_divisible_by_three = sorted(
        [l[idx] for idx in indexes_divisible_by_three])
    for i, idx in enumerate(indexes_divisible_by_three):
        l[idx] = values_at_indexes_divisible_by_three[i]
    return l
