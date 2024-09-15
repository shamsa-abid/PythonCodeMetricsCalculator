def closest_integer(value):
    original_value = float(value)
    if original_value >= 0:
        return int(original_value) if original_value - int(original_value) < 0.5 else int(original_value) + 1
    else:
        return int(original_value) if int(original_value) - original_value < 0.5 else int(original_value) - 1
