def is_happy(s: str) -> bool:
    if len(s) < 3:
        return False
    return all(s[i] != s[i+1] != s[i+2] != s[i] for i in range(len(s) - 2))
