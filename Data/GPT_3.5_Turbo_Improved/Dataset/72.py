def will_it_fly(q, w):
    if sum(q) > w:
        return False
    return q == q[::-1]
