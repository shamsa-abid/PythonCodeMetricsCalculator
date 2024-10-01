def prod_signs(arr):
    if not arr:
        return None
    else:
        prod = 1
        for a in arr:
            prod *= 1 if a > 0 else -1 if a < 0 else 0
        return sum([abs(x) for x in arr]) * prod
