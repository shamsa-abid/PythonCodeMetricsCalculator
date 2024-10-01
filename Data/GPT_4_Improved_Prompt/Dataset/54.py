def same_chars(s0: str, s1: str) -> bool:
    return sorted(list(set(s0))) == sorted(list(set(s1)))
