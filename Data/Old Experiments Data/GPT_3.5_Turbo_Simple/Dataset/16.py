def count_distinct_characters(string: str) -> int:
    string = string.lower()
    distinct_chars = set(string)
    distinct_chars.discard(' ')  # Remove spaces
    return len(distinct_chars)
