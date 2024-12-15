def pairs_sum_to_zero(l):
    s = set(l)
    for i in s:
        if -i in s:
            return True
    return False
