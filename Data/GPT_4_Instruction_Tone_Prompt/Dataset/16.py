def count_distinct_characters(string: str) -> int:
    return len(set(string.lower())) if string else 0
