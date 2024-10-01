def f(n):
    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x-1)

    def sum_upto(x):
        return x * (x + 1) // 2

    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum_upto(i))

    return result
