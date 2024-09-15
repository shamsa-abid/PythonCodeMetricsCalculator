def tri(n):
    res = [1]
    a, b, c = 1, 3, 2.0
    for i in range(1, n):
        res.append(b if i % 2 == 0 else a + b + c)
        a, b, c = b, c, res[-1]
    return res
