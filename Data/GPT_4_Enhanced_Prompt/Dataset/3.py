from itertools import accumulate
from typing import List


def below_zero(operations: List[int]) -> bool:
    return any(balance < 0 for balance in accumulate(operations))
