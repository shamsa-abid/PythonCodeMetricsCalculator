def get_odd_collatz(n):
    odd_collatz = [n] if n % 2 != 0 else []
    while n > 1:
        n = n / 2 if n % 2 == 0 else n * 3 + 1
        if n % 2 != 0:
            odd_collatz.append(n)

    return sorted(map(int, odd_collatz))
