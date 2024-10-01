def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    def poly(xs: list, x: float):
        """
        Evaluates polynomial with coefficients xs at point x.
        return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
        """
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

    if len(xs) % 2 != 0:
        return "Number of coefficients should be even."

    if xs[-1] == 0:
        return "Largest non zero coefficient should not be 0."

    if len(xs) == 2:
        return -1 * xs[0] / xs[1]

    result = None
    max_coeff = max([abs(coeff) for coeff in xs[:-1]])
    for guess in range(-1000, 1001):
        if poly(xs, guess) == 0:
            result = guess
            break
    return result
