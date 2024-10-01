import itertools
def triples_sum_to_zero(l: list) -> bool:
    possible_combinations = list(itertools.combinations(l, 3))
    for tup in possible_combinations:
        if sum(tup) == 0:
            return True
    return False
