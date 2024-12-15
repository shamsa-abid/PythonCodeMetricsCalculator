def count_distinct_characters(string: str) -> int:
    return len({char.lower() for char in string if char.isalpha()})
