def simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")

    numerator = int(a) * int(c)
    denom = int(b) * int(d)

    return numerator % denom == 0


# Example Usage
print(simplify("1/5", "5/1"))  # True
print(simplify("1/6", "2/1"))  # False
