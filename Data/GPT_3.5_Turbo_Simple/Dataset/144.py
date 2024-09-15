def simplify(x, n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify_fraction(num, denom):
        common = gcd(num, denom)
        return num // common, denom // common

    def is_whole_number(num, denom):
        return num % denom == 0

    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    result_num = x_num * n_num
    result_denom = x_denom * n_denom

    simplified_num, simplified_denom = simplify_fraction(
        result_num, result_denom)

    return is_whole_number(simplified_num, simplified_denom)
