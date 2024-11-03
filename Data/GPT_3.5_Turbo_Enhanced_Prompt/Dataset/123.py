
def get_odd_collatz(n):
    odd_collatz = []

    while n != 1:
        if n % 2 == 1:
            odd_collatz.append(n)
        n = n // 2 if n % 2 == 0 else n * 3 + 1

    odd_collatz.append(1)

    return sorted(odd_collatz)
