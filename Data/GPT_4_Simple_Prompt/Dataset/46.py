def fib4(n: int):
    fib = [0, 0, 2, 0]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2] + fib[-3] + fib[-4])
    return fib[n]
