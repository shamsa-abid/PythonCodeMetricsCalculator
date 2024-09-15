from typing import List, Tuple
from operator import mul
from functools import reduce


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    try:
        sum_value = sum(numbers)
        prod_value = reduce(mul, numbers, 1)
        return sum_value, prod_value
    except TypeError:
        return 'Input data type is not correct'
