def fib4(n: int):
    results = [0, 0, 2, 0]

    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        next_val = sum(results)
        results.pop(0)
        results.append(next_val)

    return results[-1]
