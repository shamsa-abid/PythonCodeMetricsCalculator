
import math


def triangle_area(a, b, c):
    # Check if the three sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculating the semi-perimeter of the triangle
        s = (a + b + c) / 2
        # Calculating the area using Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return round(area, 2)
    else:
        return -1
