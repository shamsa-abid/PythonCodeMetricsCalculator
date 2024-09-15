def derivative(xs: list):
    return [i * xs[i] for i in range(1, len(xs))]


# Testing the function
print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))
print(derivative([3, 2, 1]))
print(derivative([3, 2, 1, 0, 4]))
print(derivative([1]))
