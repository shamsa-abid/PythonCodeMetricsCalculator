def truncate_number(number: float) -> float:
    int_part = int(number)
    decimal_part = number - int_part
    return decimal_part
