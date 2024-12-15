
def f(n):
    res = []
    for i in range(n):
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            res.append(factorial)
        else:
            summation = 0
            for j in range(1, i+1):
                summation += j
            res.append(summation)
    return res
