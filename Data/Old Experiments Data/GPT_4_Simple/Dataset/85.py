def add(lst):
    return sum(el for idx, el in enumerate(lst) if idx % 2 != 0 and el % 2 == 0)
