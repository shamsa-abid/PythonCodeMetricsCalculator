def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int):
    fib = [0, 1]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])

    prime_count = 0
    i = 2
    while prime_count < n:
        if is_prime(fib[i]):
            prime_count += 1
        i += 1

    return fib[i-1]
