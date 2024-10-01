def triangle_area(a, b, c):
    if a+b > c and a+c > b and b+c > a:
        # calculate semi-perimeter
        s = (a + b + c) / 2
        # calculate area
        area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
        return round(area, 2)
    else:
        return -1
