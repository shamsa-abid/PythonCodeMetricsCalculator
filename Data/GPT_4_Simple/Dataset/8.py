from typing import List, Tuple
from functools import reduce
import operator


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    return sum(numbers), reduce(operator.mul, numbers, 1)
