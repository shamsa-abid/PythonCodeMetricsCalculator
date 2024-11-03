from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []

    result = [numbers[0]]
    for n in numbers[1:]:
        result.extend([delimeter, n])

    return result
