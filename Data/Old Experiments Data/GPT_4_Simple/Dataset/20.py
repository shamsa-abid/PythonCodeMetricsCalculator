from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    closest = min(zip(numbers, numbers[1:]), key=lambda x: x[1] - x[0])
    return closest
