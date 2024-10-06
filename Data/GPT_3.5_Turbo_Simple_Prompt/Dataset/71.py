def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1


# Test the function with the given examples
print(triangle_area(3, 4, 5))  # Output: 6.0
print(triangle_area(1, 2, 10))  # Output: -1
