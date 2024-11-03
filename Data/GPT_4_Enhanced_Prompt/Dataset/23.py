def strlen(string: str) -> int:
    try:
        return len(string)
    except TypeError:
        return "Invalid input, expecting a string"
