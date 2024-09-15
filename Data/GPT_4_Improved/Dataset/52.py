def below_threshold(l: list, t: int) -> bool:
    return all(e < t for e in l)
