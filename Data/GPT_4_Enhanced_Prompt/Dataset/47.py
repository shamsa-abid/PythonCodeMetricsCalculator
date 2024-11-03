from typing import Union


def median(l: list) -> Union[int, float]:
    l.sort()
    half, odd = divmod(len(l), 2)
    return l[half] if odd else (l[half - 1] + l[half]) / 2.0
