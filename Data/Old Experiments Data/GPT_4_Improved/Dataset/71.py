def triangle_area(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return -1
    s = sum(sides) / 2
    return round((s * (s - sides[0]) * (s - sides[1]) * (s - sides[2])) ** 0.5, 2)
