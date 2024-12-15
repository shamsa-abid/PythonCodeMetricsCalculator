from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    numbers.sort()
    return any(abs(numbers[i+1]-numbers[i]) < threshold for i in range(len(numbers)-1))
