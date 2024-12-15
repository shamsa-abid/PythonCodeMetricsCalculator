def fib(n: int):
    if n < 0:
        raise ValueError(
            "Invalid input! Input should be a non-negative integer.")
    seq = [0, 1]
    for i in range(2, n + 1):
        seq.append(seq[-1] + seq[-2])
    return seq[n]
