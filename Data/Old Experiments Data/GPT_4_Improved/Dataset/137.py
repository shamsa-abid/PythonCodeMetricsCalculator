def compare_one(a, b):
    def convert_to_number(n):
        return float(str(n).replace(',', '.'))

    number_a = convert_to_number(a)
    number_b = convert_to_number(b)

    if number_a == number_b:
        return None
    return a if number_a > number_b else b
