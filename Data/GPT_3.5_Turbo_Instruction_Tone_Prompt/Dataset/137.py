def compare_one(a, b):
    if isinstance(a, str):
        a = a.replace(",", ".")

    if isinstance(b, str):
        b = b.replace(",", ".")

    if a == b:
        return None
    elif type(a) == float or type(b) == float:
        return max(float(a), float(b))
    else:
        return max(a, b)
