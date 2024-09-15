from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_number, max_number = min(numbers), max(numbers)
    scale = max_number - min_number

    if scale == 0:
        raise ValueError("All elements in the input list are the same")

    return [(x - min_number) / scale for x in numbers]
