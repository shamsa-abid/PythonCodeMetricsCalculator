from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    else:
        return [element for sublist in [(n, delimeter) for n in numbers[:-1]] + [numbers[-1:]] for element in sublist]
