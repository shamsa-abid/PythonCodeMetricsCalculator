from math import factorial


def f(n):
    return [i*(i+1)//2 if i % 2 else factorial(i) for i in range(1, n+1)]
