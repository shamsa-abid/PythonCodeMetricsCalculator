def count_distinct_characters(string: str) -> int:
    if not isinstance(string, str):
        raise TypeError("Expected string but received "+type(string).__name__)
    return len(set(string.casefold()))
