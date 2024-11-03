def right_angle_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()  # Sorting the sides to find the hypotenuse easily
    # Checking if it forms a right-angled triangle
    return sides[0]**2 + sides[1]**2 == sides[2]**2
