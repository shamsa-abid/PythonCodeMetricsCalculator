def tri(n):
    res = [0] * (n + 2)
    res[1] = 3

    for i in range(2, n + 2):
        if i % 2 == 0:
            res[i] = 1 + i / 2
        else:
            res[i] = res[i - 1] + res[i - 2] + res[i + 1]

    return res[1: n + 2]
