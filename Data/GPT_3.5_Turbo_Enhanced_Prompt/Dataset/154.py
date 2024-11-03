def cycpattern_check(a, b):
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        if a[i:i+l] in pat:
            return True
    return False
