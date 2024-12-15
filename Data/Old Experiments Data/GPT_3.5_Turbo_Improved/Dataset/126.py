def is_sorted(lst):
    count_digit = {}
    for i in lst:
        if i in count_digit:
            count_digit[i] += 1
        else:
            count_digit[i] = 1

    if any(count > 1 for count in count_digit.values()):
        return False

    return lst == sorted(set(lst))

