
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    range_num = max_num - min_num
    if range_num == 0:  # Handle case when all numbers are the same
        return [0.0] * len(numbers)
    return [(num - min_num) / range_num for num in numbers]
