from itertools import accumulate
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    return list(accumulate(numbers, max))
