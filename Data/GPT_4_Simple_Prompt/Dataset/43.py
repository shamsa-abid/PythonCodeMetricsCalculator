def pairs_sum_to_zero(l):
    d = set()
    for i in l:
        if -i in d:
            return True
        d.add(i)
    return False
