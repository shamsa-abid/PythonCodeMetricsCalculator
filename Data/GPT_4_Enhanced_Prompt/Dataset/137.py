def compare_one(a, b):
    def num_format(n):
        return float(str(n).replace(",", "."))

    if num_format(a) == num_format(b):
        return None

    return a if num_format(a) > num_format(b) else b
