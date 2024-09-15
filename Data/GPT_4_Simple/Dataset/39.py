
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n):
    fib = fibonacci()
    count = 0
    while True:
        candidate = next(fib)
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate
