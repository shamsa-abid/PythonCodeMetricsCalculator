def tri(n):
    if n == 0:
        return [1]

    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(1 + i / 2)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (1 + (i + 1) / 2))

    return my_tri
