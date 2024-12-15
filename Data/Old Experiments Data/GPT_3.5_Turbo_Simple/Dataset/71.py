def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
        return area
    else:
        return -1
