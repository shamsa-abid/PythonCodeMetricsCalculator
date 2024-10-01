def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            fact = 1
            for num in range(1, i+1):
                fact *= num
            result.append(fact)
        else:
            sum_ = sum(range(1, i+1))
            result.append(sum_)
    return result
