
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    sorted_numbers = sorted(numbers)
    min_number = sorted_numbers[0]
    max_number = sorted_numbers[-1]
    return [(x - min_number) / (max_number - min_number) for x in numbers]
