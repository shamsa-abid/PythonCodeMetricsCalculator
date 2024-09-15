def compare_one(a, b):
    a_val = float(a.replace(',', '.')) if isinstance(a, str) else float(a)
    b_val = float(b.replace(',', '.')) if isinstance(b, str) else float(b)

    if a_val == b_val:
        return None
    return a_val if a_val > b_val else b_val
