def get_row(lst, x):
    coordinates = []

    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                coordinates.append((i, j))

    coordinates.sort(key=lambda tup: (tup[0], -tup[1]))

    return coordinates
