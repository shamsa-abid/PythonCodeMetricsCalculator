from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    rescaled_numbers = [(num - min_num) / (max_num - min_num)
                        for num in numbers]
    return rescaled_numbers
