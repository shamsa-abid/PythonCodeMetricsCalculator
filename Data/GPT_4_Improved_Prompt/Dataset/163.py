def generate_integers(a, b):
    lower, upper = sorted([a, b])
    result = [i for i in range(lower + lower % 2, upper + 1, 2)]
    return result if all(2 <= digit <= 8 for digit in result) else []
