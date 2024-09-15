def search(lst):
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1

    return max([i for i in range(1, len(frq)) if frq[i] >= i] + [-1])
