
def compare_one(a, b):
    if isinstance(a, str):
        a = a.replace(',', '.')
    if isinstance(b, str):
        b = b.replace(',', '.')

    if float(a) == float(b):
        return None
    return a if float(a) > float(b) else b
