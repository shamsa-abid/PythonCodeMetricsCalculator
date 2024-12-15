from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    return list(filter(lambda num: isinstance(num, int), values))
