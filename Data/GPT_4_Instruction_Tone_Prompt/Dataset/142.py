def sum_squares(lst):
    total = 0
    for index in range(len(lst)):
        if index % 3 == 0 and index % 4 != 0:
            total += lst[index] ** 2
        elif index % 4 == 0:
            total += lst[index] ** 3
        else:
            total += lst[index]
    return total
