def fib4(n: int):
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    sequence = [0, 0, 2, 0]

    for i in range(4, n+1):
        sequence.append(sum(sequence[-4:]))

    return sequence[-1]
