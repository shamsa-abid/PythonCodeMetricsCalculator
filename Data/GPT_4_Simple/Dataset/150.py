def x_or_y(n, x, y):
    if n == 1 or n % 2 == 0 and n != 2:
        return y
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return y
        return x
