from typing import List
from statistics import mean


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean_value = mean(numbers)
    return sum(abs(x - mean_value) for x in numbers) / len(numbers)
