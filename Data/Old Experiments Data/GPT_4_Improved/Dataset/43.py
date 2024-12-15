def pairs_sum_to_zero(l):
    s = set()
    for i in l:
        if -i in s:
            return True
        s.add(i)
    return False
