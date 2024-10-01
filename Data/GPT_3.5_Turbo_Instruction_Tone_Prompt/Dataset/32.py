
def find_zero(xs):
    import math

    def poly(xs, x):
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

    def f(x):
        return poly(xs, x)

    def newton_method(f, df, x0, eps=1e-9, max_iter=1000):
        x = x0
        for _ in range(max_iter):
            fx = f(x)
            if math.fabs(fx) < eps:
                return x
            dfx = df(x)
            if dfx == 0:
                return None
            x = x - fx / dfx
        return None

    n = len(xs) - 1

    def df(x): return sum([i * xs[i] * math.pow(x, i-1)
                           for i in range(1, n+1)])
    solution = newton_method(f, df, 0)
    return solution
