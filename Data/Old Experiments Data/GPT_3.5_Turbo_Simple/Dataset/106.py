def f(n):
    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    def calculate_sum(num):
        return sum(range(1, num + 1))

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(calculate_sum(i))

    return result
