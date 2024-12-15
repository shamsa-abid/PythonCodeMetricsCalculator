def derivative(xs: list):
    new_xs = []
    for i in range(1, len(xs)):
        new_xs.append(i*xs[i])
    return new_xs
