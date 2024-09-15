def derivative(xs):
    if len(xs) <= 1:
        return []

    result = []
    for i in range(1, len(xs)):
        result.append(xs[i] * i)

    return result
