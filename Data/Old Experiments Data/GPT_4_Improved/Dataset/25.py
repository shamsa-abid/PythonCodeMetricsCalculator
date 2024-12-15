from typing import List


def factorize(n: int) -> List[int]:
    factors = []
    p = 2
    while n >= p * p:
        if n % p:
            p += 1
        else:
            n //= p
            factors.append(p)
    if n > 1:
        factors.append(n)
    return factors
