def triangle_area(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        # calculate the area
        area = (s*(s - a)*(s - b)*(s - c)) ** 0.5
        return round(area, 2)

    return -1
