def compare_one(a, b):
    a_val = float(str(a).replace(",", "."))
    b_val = float(str(b).replace(",", "."))

    if a_val > b_val:
        return a
    elif a_val < b_val:
        return b
    else:
        return None
