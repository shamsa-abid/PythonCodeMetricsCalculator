def is_simple_power(x, n):
    if x == 1:
        return True
    elif n == 1:
        return False
    else:
        temp = x
        while temp >= n:
            if temp == n:
                return True
            temp = temp / n
        return False
