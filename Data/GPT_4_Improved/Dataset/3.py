from typing import List
from itertools import accumulate


def below_zero(operations: List[int]) -> bool:
    return any(balance < 0 for balance in accumulate(operations))
