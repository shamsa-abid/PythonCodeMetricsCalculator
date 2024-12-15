from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number, max_number = min(numbers), max(numbers)
    denominator = max_number - min_number
    if denominator == 0:
        return [0.0] * len(numbers)
    return [(x - min_number) / denominator for x in numbers]
