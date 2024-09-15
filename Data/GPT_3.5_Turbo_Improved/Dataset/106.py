def f(n):
    ret = []
    fact = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            fact *= i
            ret.append(fact)
        else:
            total = sum(range(1, i + 1))
            ret.append(total)
    return ret
