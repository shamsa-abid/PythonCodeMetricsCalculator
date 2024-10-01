from typing import List
from itertools import accumulate


def rolling_max(numbers: List[int]) -> List[int]:
    return list(accumulate(numbers, max))
