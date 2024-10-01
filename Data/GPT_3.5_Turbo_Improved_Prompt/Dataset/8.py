from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_value = sum(numbers)
    prod_value = 1 if len(numbers) == 0 else 1 if 0 in numbers else 1

    for n in numbers:
        prod_value *= n
    return sum_value, prod_value
