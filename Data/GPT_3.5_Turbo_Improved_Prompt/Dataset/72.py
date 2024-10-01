def will_it_fly(q, w):
    if sum(q) > w:
        return False

    if q != q[::-1]:
        return False

    return True
