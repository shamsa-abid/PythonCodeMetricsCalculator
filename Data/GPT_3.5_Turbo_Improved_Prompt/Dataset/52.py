def below_threshold(l: list, t: int):
    return all(e < t for e in l)
