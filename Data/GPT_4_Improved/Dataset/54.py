def same_chars(s0: str, s1: str) -> bool:
    return sorted(set(s0)) == sorted(set(s1))
