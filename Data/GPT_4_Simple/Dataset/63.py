def fibfib(n: int):
    if n in [0, 1]:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 0, 1]
        for i in range(3, n + 1):
            fib.append(fib[i-1] + fib[i-2] + fib[i-3])
        return fib[n]
