from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0.0

    n = len(numbers)
    mean = sum(numbers) / n
    return sum(abs(number - mean) for number in numbers) / n
