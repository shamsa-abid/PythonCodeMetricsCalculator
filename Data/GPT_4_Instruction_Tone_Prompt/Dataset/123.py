def get_odd_collatz(n):
    sequence = []
    while n != 1:
        if n % 2:
            sequence.append(n)
        n = n / 2 if n % 2 == 0 else n * 3 + 1
    sequence.append(1)
    return sorted(sequence)
