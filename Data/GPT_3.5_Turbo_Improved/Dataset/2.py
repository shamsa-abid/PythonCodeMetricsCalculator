def truncate_number(number: float) -> float:
    return number - int(number) if number > 0 else 0.0
