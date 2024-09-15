def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i]) - 1, -1, -1):
            if lst[i][j] == x:
                result.append((i, j))
    result.sort(key=lambda tup: (-tup[0], tup[1]))
    return result
