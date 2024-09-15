def get_row(lst, x):
    coords = []
    for i in range(len(lst)):
        for j in range(len(lst[i])-1, -1, -1):
            if lst[i][j] == x:
                coords.append((i, j))

    return coords
