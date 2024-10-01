def f(n):
    ret = []
    factorial = 1
    running_sum = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            factorial *= i
            ret.append(factorial)
        else:
            running_sum += i
            ret.append(running_sum)

    return ret
