from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:

    numbers.sort()
    closest_index = min(range(1, len(numbers)),
                        key=lambda index: numbers[index]-numbers[index-1])

    return numbers[closest_index-1], numbers[closest_index]
