def decimal_to_binary(decimal):
    if isinstance(decimal, int) and decimal >= 0:
        return f"db{bin(decimal)[2:]}db"
    else:
        raise ValueError("Input must be a non-negative integer")
