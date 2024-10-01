from typing import List, Tuple
from functools import reduce
import operator


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if len(numbers) == 0:
        return (0, 1)
    else:
        sum_num = sum(numbers)
        prod_num = reduce(operator.mul, numbers, 1)
        return (sum_num, prod_num)
