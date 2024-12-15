def sort_third(l: list):
    divisible_by_three = sorted([l[i] for i in range(len(l)) if i % 3 == 0])
    result = l.copy()
    result[::3] = divisible_by_three
    return result
